from django.urls import path
from . import views
urlpatterns = [
    path('list_todo/',views.ListGenerics.as_view()),
    path('details_list_todo/<str:pk>/',views.DetailsListGenerics.as_view()),
]    