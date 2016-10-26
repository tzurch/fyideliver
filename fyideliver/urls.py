from django.conf.urls import url
from django.contrib import admin
from fyideliverapp import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  url(r'^business/sign-in/$', auth_views.login,
    {'template_name': 'business/sign_in.html'},
    name = 'business-sign-in'),
  url(r'^business/sign-out', auth_views.logout,
    {'next_page': '/'},
    name = 'business-sign-out'),
  url(r'^business/sign-up', views.business_sign_up,
    name = 'business-sign-up'),
  url(r'^business/$', views.business_home, name = 'business-home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
