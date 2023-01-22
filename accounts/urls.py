from django.urls import path

from accounts.views import AccountsSignUpView, AccountsLoginView


urlpatterns = [
    path('signup/', AccountsSignUpView.as_view(), name='signup'),
    path('login/', AccountsLoginView.as_view(), name='login'),
]