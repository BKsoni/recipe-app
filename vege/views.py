from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def add_recipe(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        recipe_name = data.get('recipe-name')
        recipe_description = data.get('recipe-desc')
        recipe_img = request.FILES.get('recipe-img')

        print(recipe_name, recipe_description, recipe_img)
        Recipe.objects.create( name=recipe_name, description=recipe_description, image=recipe_img)
        return redirect('/')

    return render(request, 'add_recipe.html',{"title": 'Add Recipe'})

@login_required(login_url='/login/')
def manage_recipe(request):
    recipes = Recipe.objects.all()
    if request.GET.get('search'):
        recipes = Recipe.objects.filter(name__icontains=request.GET.get('search'))
        
    return render(request, 'manage_recipe.html', {"title": 'Manage Recipe', 'recipes': recipes})

@login_required(login_url='/login/')
def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect('/manage-recipe/')

@login_required(login_url='/login/')
def update_recipe(request, id):
    recipe = Recipe.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        id = data.get('recipe-id')
        recipe.name = data.get('recipe-name')
        recipe.description = data.get('recipe-desc')
        recipe_img = request.FILES.get('recipe-img')

        if recipe_img:
            recipe.image = recipe_img

        recipe.save()
        return redirect('/manage-recipe/')
    
    return render(request, 'update_recipe.html', {"title": 'Update Recipe', 'recipe': recipe})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username does not exist")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
    
    return render(request, 'login.html', {"title": 'Login'})

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('/register/')
        user = User.objects.create(first_name=first_name, last_name=last_name, username=username)
        user.set_password(password)
        user.save()
        messages.success(request, "Registration Successful. Please Login")
        return redirect('/login/')

    return render(request, 'register.html', {"title": 'Register'})

def logout_page(request):
    logout(request)
    return redirect('/login/')