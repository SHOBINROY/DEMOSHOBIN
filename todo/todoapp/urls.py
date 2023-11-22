from . import views
from django.urls import path


urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
    path('updates/<int:taskid>/',views.updates,name='updates'),
    path('cbvdetail/<int:pk/',views.Taskdetailview.as_view(),name='cbvdetail'),
    path ('cbvupdate/<int:pk/', views.Taskupdateview.as_view(), name = 'cbvupdate'),
    path ('cbvdelete/<int:pk/', views.Taskdeleteview.as_view(), name = 'cbvdelete')

]
