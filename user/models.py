from django.db import models

# Create your models here.
class User(models.Model):
    # date = models.DateField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)
    target_calorie_intake = models.IntegerField()
    total_calorie_intake = models.IntegerField()
    achived_calorie_intake = models.BooleanField()
    target_calorie_burn = models.IntegerField()
    total_calorie_burn = models.IntegerField()
    achived_calorie_burn = models.BooleanField()



    def __str__(self):
        return self.name
