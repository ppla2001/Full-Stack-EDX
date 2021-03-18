from django.urls import path
from hello import views

urlpatterns = [
    path("", views.index, name='index'),    
    path('pedro', views.pedro, name ='pedro'),
    path('david', views.david, name ='david'),
    path('<str:name>',views.greet, name='greet')
]