from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main-view'),
    #path('questions',views.questions, name='questions-view'),
    #path('questions/tagged/<slug:tag_name>',views.questions, name='questions-view'),
    #path('questions/<int:question_id>', views.question, name='question-view'),
    #path('users', views.users, name='users-view'),
    #path('users/<int:user_id>', views.user, name='user-view'),
    #path('tags', ),
    #path('singup',),
    #path('login',),
]