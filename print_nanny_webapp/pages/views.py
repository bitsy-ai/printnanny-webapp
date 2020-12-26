from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView

User = get_user_model()


class CustomView(LoginRequiredMixin, TemplateView):
    pass


# pages
custom_pages_faq_view = CustomView.as_view(template_name="extra/faq.html")
custom_pages_invoice_view = CustomView.as_view(template_name="extra/invoice.html")
custom_pages_maintenance_view = CustomView.as_view(
    template_name="extra/maintenance.html"
)
custom_pages_preloader_view = CustomView.as_view(template_name="extra/preloader.html")
custom_pages_pricing_view = CustomView.as_view(template_name="extra/pricing.html")
custom_pages_profile_view = CustomView.as_view(template_name="extra/profile.html")
custom_pages_profile2_view = CustomView.as_view(template_name="extra/profile2.html")
custom_pages_starter_view = CustomView.as_view(template_name="extra/starter.html")
custom_pages_time_line_view = CustomView.as_view(template_name="extra/time-line.html")
custom_pages_login_2_view = CustomView.as_view(template_name="extra/login-2.html")
custom_pages_register_2_view = CustomView.as_view(template_name="extra/register-2.html")
custom_pages_404_alt_view = CustomView.as_view(template_name="extra/404-alt.html")
custom_pages_404_view = CustomView.as_view(template_name="404.html")
custom_pages_500_view = CustomView.as_view(template_name="500.html")
custom_pages_confirm_mail_2_view = CustomView.as_view(
    template_name="extra/confirm-mail-2.html"
)
custom_pages_confirm_mail_view = CustomView.as_view(
    template_name="extra/confirm-mail.html"
)
custom_pages_recoverpw_2_view = CustomView.as_view(
    template_name="extra/recoverpw-2.html"
)
custom_pages_logout_view = CustomView.as_view(template_name="extra/logout.html")
custom_pages_logout_2_view = CustomView.as_view(template_name="extra/logout-2.html")
custom_pages_logout_view = CustomView.as_view(template_name="extra/logout.html")
custom_pages_lock_screen_2_view = CustomView.as_view(
    template_name="extra/lock-screen-2.html"
)
custom_pages_lock_screen_view = CustomView.as_view(
    template_name="extra/lock-screen.html"
)

# landing
custom_landing_landing_view = CustomView.as_view(template_name="landing/landing.html")

# layouts
custom_email_read_view = CustomView.as_view(template_name="custom/email/read.html")
custom_email_read_view = CustomView.as_view(template_name="custom/email/read.html")
