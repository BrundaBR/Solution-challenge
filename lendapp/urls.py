from django.urls import path,include
from lendapp import views


urlpatterns = [
    path('',views.signUp,name="signuppage"),
    path('signin/',views.signIn,name="signinpage"),
 
]
