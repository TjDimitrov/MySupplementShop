from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model, logout
from ExamProject.accounts.forms import RegisterUserForm, LoginUserForm, EditUserForm

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('homepage')


class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('homepage')


class EditUserView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    form_class = EditUserForm
    model = UserModel

    def get_success_url(self):
        return reverse_lazy(
            'profile edit',
            kwargs={'pk': self.object.pk}
        )


class DeleteUserView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel

    def post(self, request, *args, **kwargs):
        self.request.user.delete()
        return redirect('homepage')
