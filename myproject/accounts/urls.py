from django.urls import path
from .forms import SignIn

urlpatterns = [
    path('signup/', SignIn.as_view(),name='sign')
]