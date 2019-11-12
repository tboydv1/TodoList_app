from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name = "index"),
    path('content/<int:id>/', views.detail_page, name = "details_page"),
    path('add', views.add, name = "add")

]
