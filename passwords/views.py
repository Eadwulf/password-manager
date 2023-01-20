from django.views.generic import ListView

from passwords.models import Password, Website


class PasswordListView(ListView):
    model = Password
    context_object_name = 'passwords'
    template_name = 'passwords/password_listview.html'
