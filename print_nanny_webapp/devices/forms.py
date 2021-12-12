from django.forms import Select, ModelForm, ChoiceField
from .enum import CameraType
from .models import Camera


class SelectWidget(Select):
    """
    Subclass of Django's select widget that allows disabling options.
    https://stackoverflow.com/a/50109362
    """

    def __init__(self, *args, **kwargs):
        self._disabled_choices = []
        super(SelectWidget, self).__init__(*args, **kwargs)

    @property
    def disabled_choices(self):
        return self._disabled_choices

    @disabled_choices.setter
    def disabled_choices(self, other):
        self._disabled_choices = other

    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        option_dict = super(SelectWidget, self).create_option(
            name, value, label, selected, index, subindex=subindex, attrs=attrs
        )
        if value in self.disabled_choices:
            option_dict["attrs"]["disabled"] = "disabled"
        return option_dict


class CameraCreateForm(ModelForm):
    camera_type = ChoiceField(
        required=True, widget=SelectWidget, choices=CameraType.choices
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["camera_type"].widget.disabled_choices = [
            CameraType.IP.value,
            CameraType.USB.value,
        ]

    class Meta:
        model = Camera
        fields = ["name", "camera_type"]
