from django.urls import path
from .views import helloworldfunc

urlpatterns = [
    path('helloworldapp2/', helloworldfunc),
]
