# add device forms here
from django.forms import ModelForm

from .models import License

class LicenseGenerateForm(ModelForm):
    class Meta:
        model = License
        exclude = ("user",)

    def save(self, *args, **kwargs):
        request = kwargs.pop('request')
        if request.user.is_anonymous:
            raise Exception("Authentication is required")
        
        self.instance.user = request.user
        return super(LicenseGenerateForm).save(*args, **kwargs)
