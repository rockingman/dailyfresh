from django.conf.urls import url,include

from apps.users import views

urlspattern = [
    url(r'register',views.register)
]