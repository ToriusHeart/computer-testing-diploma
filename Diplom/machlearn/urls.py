from django.urls import path, re_path
from . import views
from django.conf.urls import url
from .api import PredictAnswerAPI

urlpatterns = [
    path("predict/", PredictAnswerAPI.as_view())
]