from django.contrib import admin
from django.utils.html import format_html
from print_nanny_webapp.shop.models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sku",
        "is_active",
        "is_shippable",
        "is_preorder",
        "is_subscription",
        "djstripe_product",
        "stripe_dashboard_url",
    )

    def stripe_dashboard_url(self, obj):
        url = obj.get_stripe_dashboard_url()
        return format_html("<a href='{url}'>{url}</a>", url=url)

    class Meta:
        model = Product
