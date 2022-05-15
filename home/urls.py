from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('me', views.testhtml),
    path('detail/<int:id>', views.detailview, name="detail"),
    path('create', views.viewcreate),
    path('delete/<int:id>', views.viewdelete, name="delete"),
    path('update/<int:id>', views.viewupdate, name="update"),
    path('list', views.viewlist, name="list")
]