from django.urls import path
from facts import views

app_name = 'facts'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('random/', views.random, name='random'),
    path('facts/<int:question_id>/', views.detail, name='detail'),
]