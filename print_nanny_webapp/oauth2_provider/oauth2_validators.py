from oauth2_provider.oauth2_validators import OAuth2Validator
from django.apps import apps

PiModel = apps.get_model("devices", "Pi")


class CustomOAuth2Validator(OAuth2Validator):
    # Set `oidc_claim_scope = None` to ignore scopes that limit which claims to return,
    # otherwise the OIDC standard scopes are used.
    oidc_claim_scope = OAuth2Validator.oidc_claim_scope

    def get_additional_claims(self, request):
        return {
            "given_name": request.user.first_name,
            "family_name": request.user.last_name,
            "name": " ".join([request.user.first_name, request.user.last_name]),
            "email": request.user.email,
        }

    def get_userinfo_claims(self, request):
        claims = super().get_userinfo_claims(request)
        claims["pis"] = PiModel.objects.get(user=request.user)
        return claims
