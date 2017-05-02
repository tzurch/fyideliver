from django.conf.urls import url, include
from django.contrib import admin
from fyideliverapp import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),

  # Business
  url(r'^business/sign-in/$', auth_views.login,
    {'template_name': 'business/sign_in.html'},
    name = 'business-sign-in'),
  url(r'^business/sign-out', auth_views.logout,
    {'next_page': '/'},
    name = 'business-sign-out'),
  url(r'^business/sign-up', views.business_sign_up,
    name = 'business-sign-up'),
  url(r'^business/$', views.business_home, name = 'business-home'),

  url(r'^business/account/$',views.business_account, name = 'business-account'),
  url(r'^business/product/$',views.business_product, name = 'business-product'),
  url(r'^business/order/$',views.business_order, name = 'business-order'),
  url(r'^business/report/$',views.business_report, name = 'business-report'),

  # sign in/ Sign Up sign out
  url(r'^api/social/', include('rest_framework_social_oauth2.urls')),
  # /convert-token (sign in/ sign up)
  # /revoke-token (sign out)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
