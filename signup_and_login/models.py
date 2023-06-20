from django.db import models


class UserData(models.Model):
    
    user_id = models.AutoField
    first_name = models.CharField(max_length=50,default=None)
    last_name = models.CharField(max_length=50,default=None)
    addressLine1 = models.CharField(max_length=70,default=None)
    city = models.CharField(max_length=50,default=None)
    state = models.CharField(max_length=50,default=None)
    pincode = models.IntegerField(default=None)
    username = models.CharField(max_length=50,default=None)
    user_email = models.EmailField(default=None)
    user_password = models.CharField(max_length=8,default=None)
    user_role = models.CharField(max_length=50,default=None)
    photo = models.ImageField(upload_to="media")


    def __str__(self):
        return self.username
    



    
