from django.contrib import admin
from django.utils.html import format_html
from print_nanny_webapp.shop.models import InventoryItem, Product, Order

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
        url = obj.djstripe_product.get_stripe_dashboard_url()
        return format_html("<a href='{url}'>{url}</a>", url=url)

    class Meta:
        model = Product


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "created_dt",
        "status",
        "last_status_dt",
        "user",
        "djstripe_customer",
        "stripe_dashboard_url",
        "product_names",
    )

    def status(self, obj):
        if obj.last_status:
            return obj.last_status.status

    def last_status_dt(self, obj):
        if obj.last_status:
            return obj.last_status.created_dt

    def product_names(self, obj):
        return [product.name for product in obj.products.all()]

    def stripe_dashboard_url(self, obj):
        url = "unknown"
        if obj.djstripe_checkout_session.mode == "payment":
            url = (
                obj.djstripe_checkout_session.payment_intent.get_stripe_dashboard_url()
            )
        elif obj.djstripe_checkout_session.mode == "subscription":
            url = obj.djstripe_checkout_session.get_stripe_dashboard_url()

        return format_html("<a href='{url}'>{url}</a>", url=url)

    class Meta:
        model = Order


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "order",
        "created_dt",
        "updated_dt",
    )

    class Meta:
        model = InventoryItem
