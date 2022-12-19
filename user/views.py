import os
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.views.generic.edit import UpdateView

from .models import User
import json

# Create your views here.
# print(os.listdir())

class DataList:
    def __init__(self):
        path = {
            'food_list':'/home/rakesh/django/calorie_calc/user/data/food_list.json',
            'activity_list':'/home/rakesh/django/calorie_calc/user/data/activity_list.json'
        }
        with open(path['food_list'],'r') as f:
            self.food_list = json.load(f)

        with open(path['activity_list'],'r') as f:
            self.activity_list = json.load(f)

        self.foods = []
        self.activities = []
        for food in self.food_list:
            self.foods.append(food['food'])
        for activity in self.activity_list:
            self.activities.append(activity['activity'])

class HomeView(View):
    def get(self, request):
        users = User.objects.all().values()
        # print(users) 
        return render(request, 'home.html',{"users":users})

class HomeView_AscOrder(View):
    def get(self, request):
        users = User.objects.all().order_by('date').values()
        # print(users) 
        return render(request, 'home.html',{"users":users})

class HomeView_DesOrder(View):
    def get(self, request):
        users = User.objects.all().order_by('-date').values()
        # print(users) 
        return render(request, 'home.html',{"users":users})

class CreateView(View):
    def __init__(self):
        data = DataList()
        self.foods = data.foods
        self.activities = data.activities
        self.food_list = data.food_list
        self.activity_list = data.activity_list

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
        # print(data)
        date = data['date']
        time = data['time']
        name = data['name']
        target_calorie_intake = int(data['target_calorie_intake'])
        food_in= data['food']
        quantity = data['quantity']
        target_calorie_burn = int(data['target_calorie_burn'])
        activity_in = data['activity']
        step = data['step']
        
        total_calorie_intake = 0
        total_calorie_burn = 0
        for food in self.food_list:
            if food_in == food['food']:
                total_calorie_intake = food['calories'] * int(quantity)
                break

        for activity in self.activity_list:
            if activity_in == activity['activity']:
                total_calorie_burn = activity['calorire-burned'] * int(step)
                break

        if total_calorie_intake >= target_calorie_intake:
            achived_calorie_intake = True
        else:
            achived_calorie_intake = False

        if total_calorie_burn >= target_calorie_burn:
            achived_calorie_burn = True
        else:
            achived_calorie_burn = False

        user = User(
            date = date,
            time = time,
            name = name,
            target_calorie_intake = target_calorie_intake,
            total_calorie_intake = total_calorie_intake,
            achived_calorie_intake = achived_calorie_intake,
            target_calorie_burn = target_calorie_burn,
            total_calorie_burn = total_calorie_burn,
            achived_calorie_burn = achived_calorie_burn
        )
        user.save()
        
        # print(date, name,target_calorie_intake,quantity,target_calorie_burn,step)
        # print(total_calorie_intake)
        return redirect('home')   

 ## User existing Data Update       

class UserUpdateView(View):
    def __init__(self):
        data = DataList()
        self.foods = data.foods
        self.activities = data.activities
        self.food_list = data.food_list
        self.activity_list = data.activity_list
        
    def get(self,request,id):
        data = User.objects.get(pk=id)
        print(data)
        return render(request, 'user/update.html',
        {"data":data,
        "foodList":self.foods,
        "activityList":self.activities
        })

    # Update your data
    def post(self, request,id):
        data = User.objects.get(pk=id)
        new_data = request.POST
        print(new_data['target_calorie_intake'])
        print(new_data['target_calorie_burn'])
        
        TC_intake = int(new_data['target_calorie_intake'])
        TC_burn = int(new_data['target_calorie_burn'])
        

        food_in= new_data['food']
        quantity = new_data['quantity']
        activity_in = new_data['activity']
        step = new_data['step']

        total_calorie_intake = 0
        total_calorie_burn = 0
        for food in self.food_list:
            if food_in == food['food']:
                total_calorie_intake = food['calories'] * int(quantity)
                break

        for activity in self.activity_list:
            if activity_in == activity['activity']:
                total_calorie_burn = activity['calorire-burned'] * int(step)
                break
        # TC_intake --> Target Calorie Intake
        # burn --> Target Calorie burn
        if total_calorie_intake >= TC_intake:
            achived_calorie_intake = True
        else:
            achived_calorie_intake = False

        if total_calorie_burn >= TC_burn:
            achived_calorie_burn = True
        else:
            achived_calorie_burn = False

        data.date = new_data['date']
        data.name = new_data['name']
        data.target_calorie_intake = new_data['target_calorie_intake']
        data.total_calorie_intake = total_calorie_intake
        data.achived_calorie_intake = achived_calorie_intake
        data.target_calorie_burn = new_data['target_calorie_burn']
        data.total_calorie_burn = total_calorie_burn
        data.achived_calorie_burn = achived_calorie_burn
        # Save the updated data
        data.save()
        return redirect('home')
        
   

class NutrientsView(View):
    def __init__(self):
        data = DataList()
        self.foods = data.foods
        # self.activities = data.activities
        self.food_list = data.food_list
        self.activity_list = data.activity_list

    def get(self, request):
        return render(request, 'nutrients.html',
            {
                'foodList':self.foods,
                # 'activityList':self.activities
            }
        )
    def post(self, request):
        input_data = request.POST
        labels = []
        data = []
        for i in self.food_list:
            if input_data['food'] == i['food']:
                labels = list(i.keys())
                data = list(i.values())
                break
        labels = labels[-3:]  
        data = data[-3:]  
        # print(labels)
        # print(data)    
        return render(request, 'nutrients.html',
            {
                "data":data,
                "labels":labels,
                "foodList":self.foods,
                "selected_food":input_data['food']
            }
        )
                
        # return redirect('home')    



# Delete the user records
class DeleteView(View):
    def post(self, request,id):
        data = User.objects.get(pk=id)
        print(data)
        data.delete()
        return redirect('home')    