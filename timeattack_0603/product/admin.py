from django.contrib import admin  # 장고에서 admin툴을 사용하겠다!
from .models import Category, Drink     # 우리가 생성한 모델 가져옴
# .models 현재 위치와 동일한 models.py에서 그 중 UserModel 모델을 가져오겠다

# Register your models here.
admin.site.register(Drink)
admin.site.register(Category)