from django.contrib import admin

from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','target_calorie_intake','total_calorie_intake','achived_calorie_intake','target_calorie_burn','total_calorie_burn','achived_calorie_burn']
    