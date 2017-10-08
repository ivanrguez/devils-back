"""kcfinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from articlesmanagement.views import index

from usermanagement.views import login
from usermanagement.views import auth_view
from usermanagement.views import logout
from usermanagement.views import loggedin
from usermanagement.views import invalid_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),

    url(r'^accounts/login/$', login),
    url(r'^accounts/auth/$', auth_view),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/loggedin/$', loggedin),
    url(r'^accounts/invalid/$', invalid_login),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
