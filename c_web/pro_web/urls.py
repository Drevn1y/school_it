from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('courses/<int:pk>', views.get_exact),
    path('courses', views.get_full_courses),
    path('category', views.get_full_category),
    path('profile', views.profile),
    path('information', views.information),
    path('ratings', views.ratings),
    path('contacts', views.contacts),
    path('exact-courses/<int:pk>', views.get_exact_category),
    path('search', views.search_courses),
    path('register', views.Register.as_view()),
    path('accounts/logout/', views.logout_view),

]



