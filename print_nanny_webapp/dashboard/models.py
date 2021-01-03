from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField

User = get_user_model()

class AppCard(models.Model):

    '''
        Dummy app integration card used to measure interest from users via "notification" feature
    '''

    static_image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    features = ArrayField(
        models.CharField(max_length=255)
    )
    service_url = models.CharField(max_length=255)




class AppNotification(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    app = models.ForeignKey(AppCard, on_delete=models.CASCADE, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)


    

