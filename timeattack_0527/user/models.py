#user/models.py
from django.db import models


# Create your models here.
class UserModel(models.Model):  # 생성한 클래스 이름
    class Meta:                 # DB에 정보를 넣어주는 역할을 함
        db_table = "my_user"

    email = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)  # 패스워드


