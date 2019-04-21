from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('fruit', views.FruitTemplateView.as_view(), name='fruit'),
]
