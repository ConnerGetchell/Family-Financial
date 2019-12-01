"""ProjectThree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from finance import views
from finance import models
from django.conf import settings
from accounts import views as accounts_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('home/', views.home, name='home'),
    path('comment.html', views.comment, name='comment'),
    # path('home.html', views.home.as_view(), name='home'),
    # path('comment.html', views.post_detail(), name='post_detail'),

    path('signup/', accounts_views.signup, name="signup"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('earning/', views.earning, name='earning'),
    path('debt/', views.debt, name='debt'),
    path('spending/', views.spending, name='spending'),
    path('investment/', views.investment, name='investment'),
    path('inandout/', views.inandout, name='inandout'),
    path('memberIncome/', views.memberIncome, name='memberIncome'),
    path('memberSpending/', views.memberSpending, name='memberSpending'),
    path('new_memo', views.new_memo, name='new_memo'),
]
