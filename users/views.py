from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import CustomUser
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

# Страница регистрации
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    # В случае успеха перенаправление на страницу авторизации
    success_url = reverse_lazy('login')
    # Сама страница регистрации
    template_name = 'signup.html'


# Список пользователей
class UserView(LoginRequiredMixin, generic.View):
    login_url = reverse_lazy('login')
    model = CustomUser

    def get(self, request):
        try:
            users = self.model.objects.all()
        except self.model.DoesNotExist:
            return HttpResponse(status=404)
        return render(request, 'users/list.html', {'users': users})


# Личная страница пользователя
class UserProfile(LoginRequiredMixin, generic.View):
    login_url = reverse_lazy('login')
    model = CustomUser

    def get(self, *args, **kwargs):
        try:
            owner = self.model.objects.get(id=self.kwargs['user_id'])
        except self.model.DoesNotExist:
            return HttpResponse(status=404)
        return render(self.request, 'home.html', {'owner': owner})


# Страница редактирования профиля
class UserEditProfile(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    form_class = CustomUserChangeForm
    # Сама страница с редактированием
    template_name = 'edit.html'
    model = CustomUser

    def test_func(self):
        try:
            return self.model.objects.get(id=self.kwargs['pk']).id == self.request.user.id
        except self.model.DoesNotExist:
            return HttpResponse(status=404)

    # В случае успеха перенаправление на страницу профиля пользователя
    def get_success_url(self):
        return reverse('users:user_profile', kwargs={'user_id': self.request.user.id})


# Удаление профиля
class UserDeleteProfile(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = CustomUser
    success_url = "/"

    def test_func(self):
        try:
            return self.model.objects.get(id=self.kwargs['pk']).id == self.request.user.id
        except self.model.DoesNotExist:
            return HttpResponse(status=404)

    def delete(self, request, *args, **kwargs):
        del_user = self.model.objects.get(id=self.kwargs['pk'])
        del_user.delete()
        return redirect('users:signup')
