from django.urls import path
from .import views
app_name="app_main"
urlpatterns = [
    path('',views.index,name="index"),
]
