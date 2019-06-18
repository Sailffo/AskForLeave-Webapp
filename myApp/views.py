from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.decorators import login_required
from .models import*
from comment.models import*
from .forms import*



#登陆和主页
def user_login(request):
    if request.method == 'POST':
        user = authenticate(request,username = request.POST['user_name'],
                            password = request.POST['pwd'])
        if user is not None:
            login(request, user)
            if request.POST['type'] == '0':
                name = request.user.teacher.tname  # 查询当前用户的老师名
                tea = Teacher.objects.filter(tname=name).first()  # 查询出该老师
                gender = tea.tgender
                return render(request, 'myApp/老师个人中心.html', {"name": name, 'gender': gender})
            elif request.POST['type'] == '1':
                name = request.user.student.sname  # 查询当前用户的学生名
                stu = Student.objects.filter(sname=name).first()  # 查询出该学生
                gender = stu.sgender
                return render(request, 'myApp/学生个人中心.html', {"name": name, 'gender': gender})
            elif request.POST['type'] == False:
                return render(request, 'myApp/首页登陆.html', {'error': '尚未选择学生或老师'})
        else:
            return render(request, 'myApp/首页登陆.html', {'error': '用户名或密码错误'})

    else:
        return render(request,'myApp/首页登陆.html')

#登出
def user_logout(request):
    if request.method == 'POST':
        user = authenticate(request,username = request.POST['user_name'],
                            password = request.POST['pwd'])
        if user is not None:
            login(request, user)
            if request.POST['type'] == '0':
                name = request.user.teacher.tname  # 查询当前用户的老师名
                tea = Teacher.objects.filter(tname=name).first()  # 查询出该老师
                gender = tea.tgender
                return render(request, 'myApp/老师个人中心.html', {"name": name, 'gender': gender})
            elif request.POST['type'] == '1':
                name = request.user.student.sname  # 查询当前用户的学生名
                stu = Student.objects.filter(sname=name).first()  # 查询出该学生
                gender = stu.sgender
                return render(request, 'myApp/学生个人中心.html', {"name": name, 'gender': gender})
        else:
            return render(request, 'myApp/首页登陆.html', {'error': "用户名或密码错误"})
    return render(request,'myApp/首页登陆.html')

#老师主页
@login_required(login_url = "myApp:login")
def tea_home(request):
    return render(request, 'myApp/老师主页.html')

#老师个人中心
@login_required(login_url = "myApp:login")
def tea_self_center(request):
    name = request.user.teacher.tname  # 查询当前用户的老师名
    tea = Teacher.objects.filter(tname=name).first()  # 查询出该老师
    gender = tea.tgender
    return render(request, 'myApp/老师个人中心.html', {"name": name, 'gender': gender})

#学生个人中心
@login_required(login_url = "myApp:login")
def stu_self_center(request):
    name = request.user.student.sname  # 查询当前用户的学生名
    stu = Student.objects.filter(sname=name).first()  # 查询出该学生
    gender = stu.sgender
    return render(request, 'myApp/学生个人中心.html',{"name":name,'gender':gender})


#学生主页
@login_required(login_url = "myApp:login")
def stu_home(request):
    name = request.user.student.sname  # 查询当前用户的学生名
    return render(request, 'myApp/学生个人中心.html', {"name":name,})


#老师信息编辑
'''
@login_required(login_url = "myApp:login")
def tea_edit_profile(request):
    if request.method == 'POST':
        edit_form = Stu_edit_form(request.POST)
        if edit_form.is_valid():
            edit_form.save()
            user = authenticate(username=edit_form.cleaned_data['username'],password=edit_form.cleaned_data['password1'])
            login(request,user)
            return redirect('myApp:学生主页')
    else:
        edit_form = Stu_edit_form(instance = request.user)

    content = {'edit_form':edit_form}
    #if request.method == 'POST':
    return render(request, 'myApp/老师信息编辑.html',content)
'''

#学生的班级
@login_required(login_url = "myApp:login")
def stu_grade(request):
    name = request.user.student.sname#查询当前用户的学生名
    stu = Student.objects.filter(sname = name).first()#查询出该学生
    my_grades = stu.sgrade.all()#查询出该学生关联的所有班级
    return render(request,'myApp/学生的班级.html',{'name':name,'grades':my_grades})

#老师的班级
@login_required(login_url = "myApp:login")
def tea_grade(request):
    name = request.user.teacher.tname#查询当前用户的老师名
    tea = Teacher.objects.filter(tname = name).first()#查询出该老师
    tea_grades = tea.teacher_grade.all()#查询出该老师关联的所有班级
    return render(request,'myApp/老师的班级.html',{'grades':tea_grades,'name':name})

#请假信息
@login_required(login_url = "myApp:login")
def leave(request):
    stu_name = request.user.student.sname
    obj = Student.objects.filter(sname = stu_name).first()
    stu_grades = obj.sgrade.all()
    if request.method == 'POST':
        grade_name = request.POST['grade']
        text = request.POST['text']
        grade = Grade.objects.get(gname=grade_name)  # 找到数据库中对应的班级
        jiatiao = Comment(grade=grade, stu=stu_name, body=text, created='',is_agree='')
        jiatiao.save()
    return render(request,'myApp/请假信息.html',{'grades':stu_grades,'name':stu_name})

#请假管理
@login_required(login_url = "myApp:login")
def leave_manage(request):
    name = request.user.teacher.tname  # 查询当前用户的老师名
    tea = Teacher.objects.filter(tname=name).first()  # 查询出该老师
    tea_grades = tea.teacher_grade.all()  # 查询出该老师关联的所有班级
    comments = []
    for grade in tea_grades:#每个班级的请假条
        comments = grade.grade_comment.all()
    if request.method == 'POST':
        if request.POST['is_agree'] == '0':
            jiatiao = Comment.objects.filter(body = request.POST['jiatiao']).first()
            jiatiao.is_agree = False
            jiatiao.save()
        elif request.POST['is_agree'] == '1':
            print(1)
            jiatiao = Comment.objects.filter(body=request.POST['jiatiao']).first()
            jiatiao.is_agree = True
            jiatiao.save()
    return render(request, 'myApp/请假管理.html',{'comments':comments,'name':name})

@login_required(login_url = "myApp:login")
def leave_history(request):
    name = request.user.student.sname  # 获取当前用户的学生姓名
    jiatiao = Comment.objects.filter(stu = name).all()
    return render(request, 'myApp/请假记录.html', {"comment": jiatiao, 'name': name})
