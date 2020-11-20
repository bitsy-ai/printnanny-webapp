from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView, FormView, View

from .forms import SampleForm, SampleForm2, SampleForm3, SampleForm4, SampleForm5, SampleForm6, SampleForm7, SampleForm8


# Create your views here.

User = get_user_model()

class DemoFormView(LoginRequiredMixin, TemplateView):
    def get_context_data(self, **kwargs):
        context = super(DemoFormView, self).get_context_data(**kwargs)
        context['sample_form1'] = SampleForm()
        context['sample_form2'] = SampleForm2()
        context['sample_form3'] = SampleForm3()
        context['sample_form4'] = SampleForm4()
        context['sample_form5'] = SampleForm5()
        context['sample_form6'] = SampleForm6()
        context['sample_form7'] = SampleForm7()
        context['sample_form8'] = SampleForm8()
        return context


class DemoFormValidationView(LoginRequiredMixin, FormView):
    form_class = SampleForm5
    success_url = '/ui/form/validation'

    def form_valid(self, form):
        return super().form_valid(form)


class DemoFormUploadView(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


form_basic_view = DemoFormView.as_view(template_name='form/basic.html')
form_validation_view = DemoFormValidationView.as_view(template_name='form/validation.html')

form_advanced_view = TemplateView.as_view(template_name='form/advanced.html')
form_editors_view = TemplateView.as_view(template_name='form/editors.html')
form_elements_view = TemplateView.as_view(template_name='form/elements.html')
form_wizard_view = TemplateView.as_view(template_name='form/wizard.html')

form_fileuploads_view = DemoFormUploadView.as_view(template_name='form/fileuploads.html')