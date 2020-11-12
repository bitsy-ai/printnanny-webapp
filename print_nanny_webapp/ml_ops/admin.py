from django.contrib import admin


from .models import TFLiteModel

@admin.register(TFLiteModel)
class TFLiteAdmin(admin.ModelAdmin):
    fields = ('labels', 'model', 'metadata')
