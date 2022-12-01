from allauth.account.views import LoginView, PasswordChangeView
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from users.forms.users import CustomDashboardAuthenticationForm


class AuthRedirect:
    '''Handles Login and Logout Redirect'''

    @staticmethod
    def login_redirect():
        return redirect('core:index')

    @staticmethod
    def logout_user(request):
        logout(request)
        return redirect('login')


class IndexTemplateView(TemplateView):
    template_name = 'account/login.html'


class LoginUserView(LoginView):
    template_name = 'account/login.html'
    form_class = CustomDashboardAuthenticationForm

    def get_success_url(self):
        return reverse_lazy('login_redirect')


class PasswordUpdateView(PasswordChangeView):
    def get_success_url(self) -> str:
        messages.success(self.request, "Password updated successfully")
        return reverse_lazy("core:index")
