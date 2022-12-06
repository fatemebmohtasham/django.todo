from django.urls import path
from.import views 


urlpatterns=[
  path('',views.listtodo,name='list-todo'),
  path('delete/<str:pk>/',views.deletetask,name='delete'),
  path('edit/<str:pk>/',views.edittask,name='edit'),
]