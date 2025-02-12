from django.contrib import admin
from django.urls import path
from eaddapp import views  # Replace 'your_app' with your app name
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', lambda request: redirect('login')),  # Redirect root URL to login
#     path('login/', views.custom_login, name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('send-email/', views.send_email_view, name='send_email'),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.custom_login, name='login'),
    path('login/', views.custom_login, name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', views.custom_logout, name='logout'),  
    path('register/', views.register, name='register'),
    path('send-email/', views.send_email_view, name='send_email'),
]

