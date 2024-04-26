from django.contrib import admin
from django.urls import path
from accounts import views
from rest_framework import routers

from allauth.socialaccount.views import signup

# router = routers.DefaultRouter()
# router.register("login",views.loginView)
# router.register("register",views.registrationView)
# router.register("logout",views.logoutView)

urlpatterns = [
    path('login/', views.login_with_email),
    path('register/', views.register_with_email),
    path('password-reset/', views.password_reset_with_email),
    path('password-change/', views.password_change),
    path('logout/', views.logout),
    path('logout/<int:pk>', views.logout),

    # path("signup/", signup, name="socialaccount_signup"),
    # path("google/", views.google_login.as_view(), name="google_login"),
]