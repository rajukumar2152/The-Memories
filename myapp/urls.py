from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_home_page, name='index'),
    path("category/<int:cid>/" , views.showcat, name='catview')
    # path("category/" , views.showcat, name='catview')

    # path("blogpost/<int:id>", views.blogpost, name="blogHome")
]