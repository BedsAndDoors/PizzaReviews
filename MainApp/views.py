from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')

def pizzas(request):
    pie = Pizza.objects.order_by('pizza_name')
    context = {'pie':pie}
    return render(request,'MainApp/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    topping = pizza.topping_set.order_by('topping_name')
    new_reviews = pizza.review_set.order_by('date_added')
    context = {'pizza':pizza,'topping':topping,'new_reviews':new_reviews}
    return render(request,'MainApp/pizza.html',context)

def new_review(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = PizzaForm()
    else:
        form = PizzaForm(data=request.POST)

        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.pizza = pizza
            new_review.save()
            return redirect('MainApp:pizzas')
    context={'form':form,'pizza':pizza}
    return render(request, 'MainApp/new_review.html',context)


    