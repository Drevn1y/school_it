from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from . import forms
from django.shortcuts import render, redirect
from .models import Category, Courses
# Create your views here.


def home(request):
    # Поисковая строка
    search_bar = forms.Search()
    courses = Courses.objects.all()
    category = Category.objects.all()
    context = {
        'search_bar': search_bar,
        'courses': courses,
        'category': category,
    }
    return render(request, 'index.html', context=context)


# Вывод информации о конкретном продукте
def get_full_courses(request):
    courses = Courses.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses.html', context)


def get_exact(request, pk):
    course = Courses.objects.get(id=pk)
    context = {
        'course': course
    }
    return render(request, 'exact_course.html', context)


# Вывод товаров по категории
def get_full_category(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'category.html', context)


def get_exact_category(request, pk):
    category = Category.objects.get(id=pk)
    course = Courses.objects.filter(category_name=category)
    context = {
        'courses': course
    }

    return render(request, 'get_category_courses.html', context)


def ratings(request):
    return render(request, 'ratings.html')


def profile(request):
    return render(request, 'registration/profile.html')


def contacts(request):
    return render(request, 'contacts.html')


def information(request):
    return render(request, 'information.html')


# Поиск курсов
def search_courses(request):
    if request.method == 'POST':
        get_courses = request.POST.get('search_courses')
        try:
            get_exact = Courses.objects.get(name__icontains=get_courses)

            return redirect(f'courses/{get_exact.id}')
        except:
            return redirect('/not-found')


# Если курс не был найден
def not_found(request):
    return render(request, 'not_found.html')


class Register(View):
    template_name = 'registration/register.html'

    # Отправка формы регистрации
    def get(self, request):
        context = {'form': UserCreationForm}
        return render(request, self.template_name, context)

    # Добавление в БД
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        context = {'form': UserCreationForm}
        return render(request, self.template_name, context)


# Функция для logout
def logout_view(request):
    logout(request)
    return redirect('/')


