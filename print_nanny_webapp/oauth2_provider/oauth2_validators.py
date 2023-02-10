from oauth2_provider.oauth2_validators import OAuth2Validator
from django.apps import apps

from print_nanny_webapp.devices.api.serializers import PiSerializer

PiModel = apps.get_model("devices", "Pi")


class CustomOAuth2Validator(OAuth2Validator):
    # Set `oidc_claim_scope = None` to ignore scopes that limit which claims to return,
    # otherwise the OIDC standard scopes are used.
    oidc_claim_scope = OAuth2Validator.oidc_claim_scope
    oidc_claim_scope.update({"permissions": "permissions"})

    def get_additional_claims(self, request):
        name = (
            None
            if request.user.first_name is None or request.user.last_name is None
            else " ".join([request.user.first_name, request.user.last_name])
        )
        return {
            "given_name": request.user.first_name,
            "family_name": request.user.last_name,
            "name": name,
            "email": request.user.email,
            "username": request.user.email,
            "permissions": list(request.user.get_group_permissions()),
        }

    def get_userinfo_claims(self, request):
        claims = super().get_userinfo_claims(request)
        pis = PiModel.objects.filter(user=request.user).all()
        claims["pis"] = PiSerializer(pis, many=True).data
        return claims
