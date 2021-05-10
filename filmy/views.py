from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from filmy.forms import PersonForm, MovieForm
from filmy.models import Person, Movie


class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class CreatePersonView(View):

    def get(self, request):
        return render(request, 'form.html')

    def post(self, request):
        person = Person()
        person.first_name = request.POST.get('first_name')
        person.last_name = request.POST.get('last_name')
        person.save()
        return redirect('view_persons')

class CreatePersonViewByForm(View):

    def get(self, request):
        form = PersonForm()
        return render(request, 'form_with_python_form.html', {'form':form})

    def post(self, request):
        form = PersonForm(request.POST)
        if form.is_valid():
            person = Person()
            person.first_name = form.cleaned_data.get('first_name')
            person.last_name = form.cleaned_data.get('last_name')
            person.save()
            return redirect('view_persons')
        return render(request, 'form_with_python_form.html', {'form':form})


class ListPersonView(View):

    def get(self, request):
        return render(request, 'list_view.html', {"objects": Person.objects.all()})


class UpdatePersonView(View):

    def get(self, request, id):
        person = Person.objects.get(pk=id)
        return render(request, 'form.html', {'object': person})

    def post(self, request, id):
        person = Person.objects.get(pk=id)
        person.first_name = request.POST.get('first_name')
        person.last_name = request.POST.get('last_name')
        person.save()
        return redirect('update_persons', id)

class UpdatePersonViewAsForm(View):

    def get(self, request, id):
        person = Person.objects.get(pk=id)
        form = PersonForm(initial={'first_name':person.first_name, 'last_name':person.last_name})
        return render(request, 'form_with_python_form.html', {"form":form})

    def post(self, request, id):
        person = Person.objects.get(pk=id)
        person.first_name = request.POST.get('first_name')
        person.last_name = request.POST.get('last_name')
        person.save()
        return redirect('update_persons', id)


class CreateMovieView(View):

    def get(self, request):
        form = MovieForm()
        return render(request, 'form_with_python_form.html', {'form': form})

    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            director = form.cleaned_data['director']
            Movie.objects.create(title=title, director=director)
        return HttpResponse("udało sie dodać dziada")








