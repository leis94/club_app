from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(('club_app_backend.users.urls', 'users'), namespace='users')),
]
