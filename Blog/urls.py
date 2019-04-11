from django.urls import path
from . import views

urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # /polls/5
    path('<int:user_id>/', views.user_info, name='user_info'),

]