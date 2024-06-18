
from django.contrib import admin
from django.urls import path, include
from .views import helloworldfunc, HelloWorldClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('helloworldapp2.urls')),
]
