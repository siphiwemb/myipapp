from django.db import models
# from djongo import models

# Create your models here.
class UserIp(models.Model):
    ip_addr = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_ip'