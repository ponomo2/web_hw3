from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="mainQP"),
    path('hot', views.hot, name="hotQP"),
    path('tag/blablabla', views.tag, name="tagQP"),
# cтраница одного вопроса со списком ответов (URL = /question/35/)
    path('question/<num>', views.question, name="oneQP"),
    path('login', views.login, name="loginP"),
    path('signup', views.signup, name="signupP"),
    path('ask', views.ask, name="newQP"),
    path('profile', views.settings, name="settingsP")
]