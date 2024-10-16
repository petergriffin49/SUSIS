from django.contrib import admin
from django.contrib.auth import views as auth_views 
from django.urls import path, include
from inventory import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', user_views.logout_view, name='logout'),

    path("inventory/", include("inventory.urls")),
    path('admin/', admin.site.urls),
]
