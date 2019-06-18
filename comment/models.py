from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from myApp.models import Grade

# Create your models here.
class Comment(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='grade_comment',default='',verbose_name='班级')
    stu = models.CharField(max_length=90,default='',db_column='请假学生',verbose_name='请假学生')
    body = models.TextField(verbose_name='内容',db_column="内容")
    created = models.DateTimeField(auto_now=True,verbose_name='创建时间')
    is_agree = models.NullBooleanField(default=None,db_column="状态",verbose_name='状态')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "%s-%s-%s"%(self.grade,self.stu,self.body)