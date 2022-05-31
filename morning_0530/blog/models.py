from django.db import models
#from blog.models import Article

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "my_category"

    categoryField = models.CharField(max_length=256, null=False)
    makeDesc = models.CharField(max_length=256, default='')


class Article(models.Model): # 생성한 클래스 이름
    class Meta:          # DB에 정보를 넣어주는 역할
        db_table = "my_article"

    title = models.CharField(max_length=20, null=False)
    category_field = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.CharField(max_length=256, default='')