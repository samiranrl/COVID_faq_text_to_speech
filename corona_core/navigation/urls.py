from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.open_landing_page, name='landing'),
    path('/?l=<str:language>', views.open_landing_page, name='language_home'),
    path('/about/', views.open_about_page, name='about'),

]


