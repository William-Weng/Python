
# = mysite.urls  = #
from django.conf.urls import url, include
from django.contrib import admin
import myApp.myClass import run

urlpatterns = [
    url(r'^run/$', run), 
	# localhost:8000/run/ ==> 執行 myApp/myClass 內的 run()
    
	url(r'^help/', include('myApp.urls')), # == 好處就是…只要找到(help/)就好了，剩下的交給學弟處理>.< ==
	# localhost:8000/help/add/  ==> 找到了help/..... ==>
	# 把剩下的add/ 丟到 myApp.urls 去處理 ==>
	# myApp.urls ==> 找到了add/..... ==>
	# 執行 myApp 內的 add()
]


# ==================== 我是分隔線 ===================== #


# = myApp.urls  = #
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^add/$', add),
    url(r'^plus/', plus),
]

def add():
	print('add')
	
def plus():
	print('plus')