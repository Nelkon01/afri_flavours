"""afri_flavours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from profiles.views import custom_confirm_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profiles/', include('profiles.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', custom_confirm_email,
        name='account_confirm_email'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'afri_flavours.views.custom_404'
handler500 = 'afri_flavours.views.custom_500'
