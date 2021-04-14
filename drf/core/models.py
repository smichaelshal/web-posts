from django.db import models

# Create your models here.
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
from django.conf import settings
from django.utils.html import strip_tags

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    print('6789:', [reset_password_token.user.email])
    html_message = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="demo">{reset_password_token.key}</div>
    <script>
        document.getElementById("demo").innerHTML = "Paragraph changed!";
    </script>
</body>
</html>
    '''

    send_mail(
    'title',
    strip_tags(html_message),
    settings.EMAIL_HOST_USER,
    [reset_password_token.user.email],
    fail_silently=False,
    html_message=html_message,
    )

class UsersList(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    data = models.TextField()

    def __str__(self):
        return self.data