from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # fields
    
    def __str__(self):
        return self.username
