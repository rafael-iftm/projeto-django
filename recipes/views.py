from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Rafael Prado'
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Rafael Prado'
    })
