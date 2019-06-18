from django.contrib import admin
from .models import Grade,Teacher,Student
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


#关联属性,方便创建班级时添加学生
class StudentInline(admin.TabularInline):
    model = Student
    can_delete = False
    verbose_name_plural = "学生"

class TeacherInline(admin.TabularInline):
    model = Teacher
    can_delete = False
    verbose_name_plural = "老师"

class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline,TeacherInline)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)

class StudentInfo(admin.TabularInline):
    model = Student
    extra = 3

class GradeInfo(admin.TabularInline):
    model = Grade
    extra = 0


# 装饰器完成注册
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def show_sgrade(self,obj):
        return [i.gname for i in obj.sgrade.all()]

    #列表页属性
    list_display = ['pk','sname','sgender','sid','smajor','show_sgrade']
    list_filter = ['sname']
    search_fields = ['sname']
    list_per_page = 5
    #属性分类
    fieldsets = [
        ("基本信息",{'fields':['sname','sgender','sid','smajor','sgrade']})
    ]

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    #列表页属性
    list_display = ['pk','gname','gdate','gnum','gboynum','ggirlnum','gteacher']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5
    #添加、修改页属性
    #fields = ['gnum','gboynum','ggirlnum','gdate','gname']
    #属性分类
    fieldsets = [
        ("人数信息",{'fields':['gnum','gboynum','ggirlnum']}),
        ("基本信息",{'fields':['gname','gdate','gteacher']})
    ]

@admin.register(Teacher)
class TeachearAdmin(admin.ModelAdmin):
    inlines = [GradeInfo]
    #列表页属性
    list_display = ['pk','tname','tgender','tid']
    list_filter = ['tname']
    search_fields = ['tname']
    list_per_page = 5
    #属性分类
    fieldsets = [
        ("基本信息",{'fields':['tname','tgender','tid','teacher']})
    ]






