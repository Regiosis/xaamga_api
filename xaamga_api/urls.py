from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from django.views.generic.base import TemplateView
from drf_yasg import openapi
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView, ResendEmailVerificationView
from dj_rest_auth.views import PasswordResetConfirmView, PasswordResetView

from django.contrib.auth.forms import PasswordChangeForm
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.base import reverse_lazy

schema_view = get_schema_view(
   openapi.Info(
      title="XAAMGA API",
      default_version='v1',
      description="Xaamga backend API",
      contact=openapi.Contact(email="fdjerabe@regiosis.com"),
      license=openapi.License(name="BSD License"),
   ),
   url='http://localhost:8000',
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # path('accounts/', include('allauth.urls')), 
    # path('accounts/' , include( 'allauth.socialaccount.urls')),
    path('admin/', admin.site.urls),
    path('api/', include("accounts.urls")),
    path('api/v1/auth/', include('dj_rest_auth.urls')),

    path('api/v1/auth/registration/account-confirm-email/<str:key>/',  ConfirmEmailView.as_view(),),
    
    path("register/verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"),
    path("register/resend-email/", ResendEmailVerificationView.as_view(), name="rest_resend_email"),

    path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls')),
    
    path('reset_password/',
        auth_views.PasswordResetView.as_view(),
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(), 
        name="password_reset_done"),

    path('password/reset/confirm/<str:uidb64>/<str:token>/',
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(), 
        name="password_reset_complete"),


    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
