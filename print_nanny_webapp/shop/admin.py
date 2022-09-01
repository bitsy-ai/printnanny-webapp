from django.contrib import admin
from django.utils.html import format_html
from djstripe.settings import djstripe_settings
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
        # use test url if STRIPE_LIVE_MODE is not in live mode
        if djstripe_settings.STRIPE_LIVE_MODE is True:
            url = f"https://dashboard.stripe.com/products/{obj.djstripe_product.id}"
        else:
            url = (
                f"https://dashboard.stripe.com/test/products/{obj.djstripe_product.id}"
            )
        return format_html("<a href='{url}'>{url}</a>", url=url)

    class Meta:
        model = Product
