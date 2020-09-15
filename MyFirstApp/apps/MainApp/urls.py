from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:item_id>', views.item, name = 'item'),
    path('<int:item_id>/leave_comment', views.leave_comment, name = 'leave_comment'),
]
