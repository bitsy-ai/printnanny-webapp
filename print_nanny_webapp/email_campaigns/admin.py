from django.contrib import admin

from print_nanny_webapp.email_campaigns.models import Campaign

# Register your models here.
@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("created_dt", "template", "subject", "send_fn")
    model = Campaign
