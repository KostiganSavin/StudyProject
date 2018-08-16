from django.urls import path
from courses.views import BaseView

urlpatterns = [
    path("", BaseView.as_view())
]