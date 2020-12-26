from django.urls import path

from .views import (
    custom_pages_faq_view,
    custom_pages_invoice_view,
    custom_pages_maintenance_view,
    custom_pages_preloader_view,
    custom_pages_pricing_view,
    custom_pages_profile2_view,
    custom_pages_profile_view,
    custom_pages_starter_view,
    custom_pages_time_line_view,
    custom_pages_login_2_view,
    custom_pages_register_2_view,
    custom_pages_404_alt_view,
    custom_pages_404_view,
    custom_pages_500_view,
    custom_pages_confirm_mail_2_view,
    custom_pages_confirm_mail_view,
    custom_pages_recoverpw_2_view,
    custom_pages_logout_2_view,
    custom_pages_logout_view,
    custom_pages_lock_screen_2_view,
    custom_pages_lock_screen_view,
    custom_landing_landing_view,
)

app_name = "pages"
urlpatterns = [
    # pages
    path("faq", view=custom_pages_faq_view, name="faq"),
    path("invoice", view=custom_pages_invoice_view, name="invoice"),
    path("maintenance", view=custom_pages_maintenance_view, name="maintenance"),
    path("preloader", view=custom_pages_preloader_view, name="preloader"),
    path("pricing", view=custom_pages_pricing_view, name="pricing"),
    path("profile2", view=custom_pages_profile2_view, name="profile-2"),
    path("profile", view=custom_pages_profile_view, name="profile"),
    path("starter", view=custom_pages_starter_view, name="starter"),
    path("time-line", view=custom_pages_time_line_view, name="timeline"),
    path("login-2", view=custom_pages_login_2_view, name="login-2"),
    path("register-2", view=custom_pages_register_2_view, name="register-2"),
    path("404_alt", view=custom_pages_404_alt_view, name="404-alt"),
    path("404", view=custom_pages_404_view, name="404"),
    path("500", view=custom_pages_500_view, name="500"),
    path(
        "confirm-mail-2", view=custom_pages_confirm_mail_2_view, name="confirm-mail-2"
    ),
    path("confirm-mail", view=custom_pages_confirm_mail_view, name="confirm-mail"),
    path("recoverpw-2", view=custom_pages_recoverpw_2_view, name="recoverpw-2"),
    path("logout-2", view=custom_pages_logout_2_view, name="logout-2"),
    path("logout", view=custom_pages_logout_view, name="logout"),
    path("lock-screen-2", view=custom_pages_lock_screen_2_view, name="lock-screen-2"),
    path("lock-screen", view=custom_pages_lock_screen_view, name="lock-screen"),
    # landing
    path("landing", view=custom_landing_landing_view, name="landing"),
]
