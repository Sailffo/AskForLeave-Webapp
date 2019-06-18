from django.urls import path
from . import views

app_name = 'myApp'

urlpatterns = [
    path('',views.user_login,name = 'user_login'),#登陆页和主页
    path('logout/',views.user_logout,name = 'user_logout'),#退出
    path('stuHome/',views.stu_home,name = 'stu_home'),#学生主页
    path('teaHome/',views.tea_home,name = 'tea_home'),#老师主页
    path('teaHome/tea_self_center/',views.tea_self_center,name = 'tea_self_center'),#老师个人中心
    path('stuHome/stu_self_center/',views.stu_self_center,name = 'stu_self_center'),#学生个人中心
    #path('stuHome/stu_self_center/stu_edit_profile',views.stu_edit_profile,name = 'stu_edit_profile'),#学生信息编辑
    #path('stuHome/tea_self_center/tea_edit_profile',views.tea_edit_profile,name = 'tea_edit_profile'),#老师信息编辑
    path('stuHome/stu_grade',views.stu_grade,name = 'stu_grade'),#学生所属班级
    path('teaHome/tea_grade',views.tea_grade,name = 'tea_grade'),#老师教学班级
    path('stuHome/leave',views.leave,name = 'leave'),#请假信息
    path('teaHome/leave_manage',views.leave_manage,name = 'leave_manage'),#请假管理
    path('stuHome/leave_history',views.leave_history,name = 'leave_history')#请假记录

]