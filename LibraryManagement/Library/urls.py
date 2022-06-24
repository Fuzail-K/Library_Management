from .import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup, name="signup"),
    path('login_page', views.login_page, name="login_page"),
    path('login_check', views.login_check, name="login_check"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.logout, name="logout"),
    path('add_book', views.add_book, name="add_book"),
    path('adding_book', views.adding_book, name="adding_book"),
    path('delete_book', views.delete_book, name="delete_book"),
    path('edit_book', views.edit_book, name="edit_book"),
    path('update_book', views.update_book, name="update_book")

]
