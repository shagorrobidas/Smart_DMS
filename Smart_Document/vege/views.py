from django.shortcuts import render, redirect
from .models import Receipe
# Create your views here.


def receipes(request):
    if request.method == "POST":

        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        Receipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
            )

        return redirect('/recipes/')
    queryset = Receipe.objects.all()
    context = {'receipes': queryset}
    return render(request, "receipes.html", context)


def delete_receipes(request,id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')