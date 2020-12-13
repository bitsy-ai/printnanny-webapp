from crispy_forms.layout import Field


class CustomCheckbox(Field):
    template = "common/checkbox-field.html"


class CustomRadio(Field):
    template = "common/radio-field.html"


class CustomSwitch(Field):
    template = "common/switch-field.html"
