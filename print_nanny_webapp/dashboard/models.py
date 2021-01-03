from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField

User = get_user_model()

class AppCategoryChoices(models.TextChoices):
    NOTIFICATIONS = "Notifcations", "Notifications"
    ECOMMERCE = "Ecommerce", "Ecommerce"
    AUTOMATION = "Automation", "Automation"

class AppCard(models.Model):

    '''
        Dummy app integration card used to measure interest from users via "notification" feature
    '''

    static_image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    service_url = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=AppCategoryChoices.choices)



class AppNotification(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    app = models.ForeignKey(AppCard, on_delete=models.CASCADE, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)


    

