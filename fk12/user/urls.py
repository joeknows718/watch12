from django.conf.urls import urls
from django.contrib import admin

from views import (
	UserCreateAPIView,
	AccountCreateAPIView
	)

url_pattern = [
	url(r'^register/$', UserCreateAPIView.as_view(), name='register')
]