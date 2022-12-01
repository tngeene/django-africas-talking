"""django_africas_talking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from users.views.auth_redirect import AuthRedirect, LoginUserView, PasswordUpdateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # auth redirection
    path('accounts/logout/', AuthRedirect.logout_user, name='logout'),
    path('', LoginUserView.as_view(), name='login'),
    path(
        'accounts/login-redirect/',
        AuthRedirect.login_redirect,
        name='login_redirect',
    ),
    path(
        'accounts/password-update/',
        PasswordUpdateView.as_view(),
        name='password_update',
    ),
]

urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
