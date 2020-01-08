from django.db import models

# Create your models here.
class user(models.Model):
    cust_name=models.CharField(max_length=50)
    cust_email=models.EmailField(default='na')

    class Meta:
        db_table="user"
