from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Div, Field, Submit
from crispy_forms.bootstrap import PrependedText, FieldWithButtons, StrictButton

from print_nanny_webapp.common.fields import CustomCheckbox, CustomRadio, CustomSwitch


class SampleForm(forms.Form):
    text = forms.CharField(label="Text", required=False)
    email = forms.EmailField(label="Email", required=False, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label="Password", required=False,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))
    placeholder = forms.CharField(label="Placeholder", required=False,
                                  widget=forms.TextInput(attrs={'placeholder': 'Your placeholder'}))
    text_area = forms.CharField(label="Text area", required=False, widget=forms.Textarea(attrs={'rows': 5}))

    read_only = forms.CharField(label="Readonly", required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Readonly value', 'readonly': 'readonly'}))

    disabled = forms.CharField(label="Disabled", required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Disabled value', 'disabled': 'disabled'}))

    static = forms.CharField(label="Static control", required=False,
                             widget=forms.EmailInput(attrs={'value': 'email@example.com', 'readonly': 'readonly',
                                                            'class': 'form-control-plaintext'}))

    help_text = forms.CharField(label="Help Text", required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'help text'}),
                                help_text="A block of help text that breaks onto a new line and may extend beyond one line.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'


class SampleForm2(forms.Form):
    select = forms.ChoiceField(label='Select Input', required=False, choices=[(i, i) for i in range(1, 6)])
    multiple_select = forms.MultipleChoiceField(label='Multiple Select Input', required=False,
                                                choices=[(i, i) for i in range(1, 6)])
    default_file = forms.FileField(label="Default file input", required=False)
    date = forms.CharField(label="Date", required=False,
                           widget=forms.DateInput(attrs={'type': 'date'}))
    month = forms.CharField(label="Month", required=False,
                            widget=forms.TextInput(attrs={'type': 'month'}))
    time = forms.CharField(label="Time", required=False,
                           widget=forms.TextInput(attrs={'type': 'time'}))
    week = forms.CharField(label="Week", required=False,
                           widget=forms.TextInput(attrs={'type': 'week'}))
    number = forms.IntegerField(label="Number", required=False)
    color = forms.CharField(label="Color", required=False,
                            widget=forms.TextInput(attrs={'type': 'color', 'value': '#727cf5'}))
    range = forms.CharField(label="Range", required=False,
                            widget=forms.TextInput(attrs={'type': 'range', 'class': 'custom-range'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'


class SampleForm3(forms.Form):
    small = forms.CharField(label="Small", required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control-sm', 'placeholder': '.input-sm'}))
    normal = forms.CharField(label="Normal", required=False,
                             widget=forms.TextInput(attrs={'placeholder': 'normal'}))
    large = forms.CharField(label="Large", required=False,
                            widget=forms.TextInput(attrs={'placeholder': 'large', 'class': 'form-control-lg'}))
    grid_size = forms.CharField(label="Grid Size", required=False,
                                widget=forms.TextInput(attrs={'placeholder': '.col-sm-4', 'class': 'col-sm-4'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'


class SampleForm4(forms.Form):
    small2 = forms.CharField(label="Small", required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control-sm', 'placeholder': '.input-sm'}))
    static2 = forms.CharField(label="Static", required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    button = forms.CharField(label="Button", required=False,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': 'Recipient\'s username'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'small2',
            PrependedText('static2', '@'),
            FieldWithButtons('button', StrictButton('Button', css_class='btn btn-dark')),
        )


class SampleForm5(forms.Form):
    email2 = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
                              help_text="We'll never share your email with anyone else.")
    password2 = forms.CharField(label="Password", required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))
    checkbox = forms.BooleanField(label='Check me out', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': ''}

        self.helper.layout = Layout(
            'email2',
            'password2',
            Div(CustomCheckbox('checkbox'), css_class='form-group'),
            Submit('submit', 'Submit')
        )


class SampleForm6(forms.Form):
    email3 = forms.EmailField(label="Email", required=False, widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
                              help_text="We'll never share your email with anyone else.")
    password3 = forms.CharField(label="Password", required=False,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))
    checkbox3 = forms.BooleanField(label='Check me out', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'email3',
            'password3',
            Div(CustomCheckbox('checkbox3'), css_class='form-group'),
            Submit('submit2', 'Submit')
        )
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-3'
        self.helper.field_class = 'col-9'


class SampleForm7(forms.Form):
    checkbox4 = forms.BooleanField(label='Check this custom checkbox', required=False)
    checkbox5 = forms.BooleanField(label='Check this custom checkbox2', required=False)

    radio1 = forms.BooleanField(label='Toggle this custom radio', required=False, widget=forms.RadioSelect())
    radio2 = forms.BooleanField(label='Or toggle this custom radio', required=False, widget=forms.RadioSelect())

    switch1 = forms.BooleanField(label='Toggle this switch element', required=False)
    switch2 = forms.BooleanField(label='Disabled switch element', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Div(CustomCheckbox('checkbox4'), CustomCheckbox('checkbox5'), css_class='form-group'),
            Div(CustomRadio('radio1'), CustomRadio('radio2'), css_class='form-group'),
            Div(CustomSwitch('switch1'), CustomSwitch('switch2'), css_class='form-group'),
        )


class SampleForm8(forms.Form):
    email5 = forms.EmailField(label="Email", required=False, widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
                              help_text="We'll never share your email with anyone else.")
    password5 = forms.CharField(label="Password", required=False,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Div(
                Div('email5', css_class="col-auto"),
                Div('password5', css_class="col-auto"),
                Div(Submit('submit3', 'Submit'), css_class="col-auto"),
                css_class='row')
            )

        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap4/layout/inline_field.html'