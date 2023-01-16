from django.db import models
from django.contrib.auth.models import AbstractUser
import service


class User(AbstractUser):
    patronymic = models.CharField(max_length=20)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_driver = models.BooleanField(default=False)

    def get_status(self):
        statuses = service.models.StatusType.objects.filter(profile=self).values('raiting')
        result = {}
        num = 0
        ser = 0
        for i in statuses:
            num = num + i['raiting']
            print(i)
            ser = ser + 1
        if num != 0:
            result['оценка'] = num / ser
            return result
        result['оценка'] = num
        return result

    def __str__(self):
        return f'{self.user.username} - {self.is_driver}'