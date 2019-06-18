from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Teacher(models.Model):
    #db_column为数据库表头名，verbose_name为后台页面列表中显示的字段名
    teacher = models.OneToOneField(User,default="",on_delete=models.CASCADE,verbose_name='用户')
    tname = models.CharField(max_length=20,db_column='名字',verbose_name='名字')
    tgender = models.BooleanField(default=True,db_column='性别',verbose_name='性别')
    tid = models.CharField(max_length=20,db_column='职工号',verbose_name='职工号')
    isDelete = models.BooleanField(db_column='是否删除',default=False)

    def __str__(self):
        return "%s-%s"%(self.tname,self.tid)
    #元选项
    class Meta:
        db_table = 'teachers'
        ordering = ['id']

class Grade(models.Model):
    gname = models.CharField(max_length=20,db_column='班级名',verbose_name='班级名')
    gdate = models.DateTimeField(db_column='创建时间',verbose_name='创建时间')
    gnum = models.IntegerField(db_column='班级人数',verbose_name='班级人数')
    ggirlnum = models.IntegerField(db_column='女生人数',verbose_name='女生人数')
    gboynum = models.IntegerField(db_column='男生人数',verbose_name='男生人数')
    isDelete = models.BooleanField(db_column='是否删除',default=False)
    gteacher = models.ForeignKey(Teacher,related_name='teacher_grade',on_delete=models.CASCADE,verbose_name='老师')

    def __str__(self):
        return "%s"%(self.gname)
    lastTime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'grades'
        ordering = ['id']

class Student(models.Model):
    student = models.OneToOneField(User,default='',on_delete=models.CASCADE)
    verbose_name = '学生'
    sname = models.CharField(max_length=20,db_column='名字',verbose_name='名字')
    sgender = models.BooleanField(default=True,db_column='性别',verbose_name='性别')
    sid = models.CharField(max_length=20,db_column='学号',verbose_name='学号')
    smajor = models.CharField(default='',max_length=20,db_column='专业',verbose_name='专业')
    sgrade = models.ManyToManyField("Grade",verbose_name='班级')
    isDelete = models.BooleanField(db_column='是否删除',default=False)

    def __str__(self):
        return "%s-%s"%(self.sname,self.sid)

    class Meta:
        db_table = 'students'
        ordering = ['id']
