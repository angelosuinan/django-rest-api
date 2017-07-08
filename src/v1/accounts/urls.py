from django.conf.urls import url
from django.contrib import admin
from .views.user import Index

urlpatterns = [
    url(r'^$', Index.as_view()),
    ]
