from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)


    def __str__(self):
        return f'User {self.username}'


class PDFUpload(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to='files')
