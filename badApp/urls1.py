# pathをつかえるようにするため
from django.urls import path
# 同階層にあるviews.pyを見れるようにするため
from . import views

# アプリケーション名と同じにする
# URL逆引きで使えるため
app_name = 'badApp'

urlpatterns = [
    path('', views.top, name='top'),
    path('member/', views.member, name='member'),
    path('bad/', views.bad, name='bad'),

]