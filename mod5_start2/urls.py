"""mod5_start2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from filmy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.IndexView.as_view(), name='index'),
    path("add_person/", views.CreatePersonView.as_view(), name='add_person'),
    path("add_person_by_python_form/", views.CreatePersonViewByForm.as_view(), name='add_person_form'),
    path("view_persons/", views.ListPersonView.as_view(), name='view_persons'),
    path("update_persons/<int:id>/", views.UpdatePersonView.as_view(), name='update_persons'),
    path("add_movie/", views.CreateMovieView.as_view(), name='create_movie'),
    path("add_movie_model_form/", views.CreateMovieViewByModelForm.as_view(), name='create_movie_model_form'),

]
