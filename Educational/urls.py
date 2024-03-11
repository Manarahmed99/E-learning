"""
URL configuration for Educational project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from TechEdu import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.BasePage,name='Base_Page'),

    path('landingPage', views.landingPage,name='landingPage'),
    path('About_us_page', views.AboutusPage,name='About_us'),
    path('Connect_With_Us_Page', views.ConnectWithUs_Page,name='Connect_With_Us_Page'),

    path('auth_logout/',views.auth_logout,name='auth_logout'),
    path('Auth_login_Page', views.Login_Page,name='Auth_login_Page'),
    path('Auth_Register_Page', views.Register_Page,name='Auth_Register_Page'),

    path('Courses/', views.course_list, name='Courses'),
    path('Details/<int:id>/', views.Details, name='Details'),

   path('cartpage/', views.show_cart, name='cartpage'), 
   path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
   path('delete/<int:item_id>/', views.delete_item, name='delete_item'),


   path('checkout/',views.checkout,name='checkout'),



]
