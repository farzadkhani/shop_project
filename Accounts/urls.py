from django.urls import path
from . import views as siteview_views
from django.conf import settings
from django.conf.urls.static import static
from .views import SignUp, LogIn, LogOut, Profile
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', LogIn.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name='profile'),#jast show the profile of person login
    
]
