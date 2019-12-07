from django.urls import path
from . import views

app_name='test1'
urlpatterns = [

    path('',views.index,name='home'), #index 사이트 이름을 home 으로 지정한건가보군
    path('board',views.board,name="board"),
    path('writeboard',views.writeboard,name="writeboard"),
    path('writemanage',views.writemanage,name="writemanage"),
    path('deleteboard',views.deleteboard,name="deleteboard"),
    path('areas/<area>',views.areas),
    path('areas/<area>/results',views.results),
    path('polls/<poll_id>',views.polls),
    path('candidates/<name>',views.candidates)
]
