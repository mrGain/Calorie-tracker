
from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('asc/',HomeView_AscOrder.as_view(), name='asc_home'),
    path('dec/',HomeView_DesOrder.as_view(), name='des_home'),
    path('create/',CreateView.as_view(), name='create'),
    path('update/<int:id>/',UserUpdateView.as_view(), name='update'),
    path('delete/<int:id>/',DeleteView.as_view(), name='delete'),
]