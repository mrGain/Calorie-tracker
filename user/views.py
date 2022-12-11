import os
from django.shortcuts import render
from django.views import View
import json

# Create your views here.
# print(os.listdir())


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class CreateView(View):
    path = {
        'food_list':'/home/rakesh/django/calorie_calc/user/data/food_list.json',
        'activity_list':'/home/rakesh/django/calorie_calc/user/data/activity_list.json'
    }
    with open(path['food_list'],'r') as f:
        food_list = json.load(f)

    with open(path['activity_list'],'r') as f:
        activity_list = json.load(f)

    foods = []
    activities = []
    for food in food_list:
        foods.append(food['food'])
    for activity in activity_list:
        activities.append(activity['activity'])

    def get(self, request):
        # print(self.food_list)
        return render(request, 'user/create.html',
            {
                'foodList':self.foods,
                'activityList':self.activities
            }
        )

    def post(self, request):
        data = request.POST
        name,target_calorie_intak,quantity = data['name'],data['target_calorie_intak'],data['quantity']
        print(type(data))
        return render(request, 'home.html',{"data":data})    
        
#'name': ['RAKESH GAIN'], 'target-calorie-intake': ['1223'], 'quantity': ['12']        