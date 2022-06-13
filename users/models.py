from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    city_address = models.CharField(max_length=100)
    state_address = models.CharField(max_length=100)
    zip_code = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.first_name + " " + self.last_name + " "

class User_child(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    # parent = models.OneToOneField(User, on_delete=models.CASCADE)
    child_first_name = models.CharField(max_length=50)
    child_last_name = models.CharField(max_length=50)