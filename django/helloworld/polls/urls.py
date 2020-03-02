from django.urls import path
from . import views


##################################################################
# path(route, view, kwargs, name)
# route: 指定URL中的相对路径(去除domain和参数)
# view: 指定route对应的视图函数。
# kwargs: 参数
# name: 为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，
#       尤其是在模板中。这个有用的特性允许你只改一个文件
#       就能全局地修改某个 URL 模式。
###############################################################
app_name = "polls"
# urlpatterns = [
#     path('', views.index, name = 'index'),
#     path('<int:question_id>/', views.detail, name = 'detail'),
#     path('<int:question_id>/results/', views.results, name = 'results'),
#     path('<int:question_id>/vote', views.vote, name = 'vote'),
# ]


#通用视图
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:question_id>/', views.detail, name = 'detail'),
]