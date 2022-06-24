from django.urls import path, re_path
from . import views
from django.conf.urls import url
from quiz.api import MyTestListAPI, TestListAPI, TestDetailAPI, SaveUsersAnswer, SubmitTestAPI, UploadAudioFileAPI

urlpatterns = [
    path("tests/", TestListAPI.as_view()),
    path("my-tests/", MyTestListAPI.as_view()),
    path("save-answer/", SaveUsersAnswer.as_view()),
    path("upload/", UploadAudioFileAPI.as_view()),
    re_path(r"tests/(?P<slug>[\w\-]+)/$", TestDetailAPI.as_view()),
    re_path(r"tests/(?P<slug>[\w\-]+)/submit/$", SubmitTestAPI.as_view()),
]