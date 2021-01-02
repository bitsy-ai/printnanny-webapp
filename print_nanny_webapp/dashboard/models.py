from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField

User = get_user_model()

class IntegrationCard(models.Model):

    '''
        Dummy integration card used to measure interest from users via "notification" feature
    '''

    static_image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    features = models.ArrayField(
        models.CharField(max_length=255)
    )
    service_url = models.CharField(max_length=255)




class IntegrationNotification(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    integration = ForeignKey(IntegrationCard, on_delete=models.CASCADE, db_index=True)
    user = ForeignKey(User, on_delete=models.CASCADE, db_index=True)


    

