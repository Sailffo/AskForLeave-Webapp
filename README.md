# 基于Django框架
请假系统
mysql版本8.0.16
python版本3.7
django版本3.0

系统使用方法：
下载项目文件之后，配置好环境，在项目文件中打开终端
更改settings.py文件中的数据库配置，连接上mysql
执行python manage.py makemigrations生成迁移文件
执行python manage.py migrate生成数据库
执行python manage,py runserver运行应用

默认端口为127.0.0.1:8000/
127.0.0.1:8000/admin是后台管理

创建超级用户执行python manage.py createsuperuser
