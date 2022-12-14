from django.urls import path
from . import views

app_name = 'MainApp'

urlpatterns = [
    path('',views.index, name='index'),
    path('pizzas',views.pizzas,name='pizzas'),
    path('pizzas/<int:pizza_id>/',views.pizza,name='pizza'),
    path('new_review/<int:pizza_id>/',views.new_review,name='new_review'),
]