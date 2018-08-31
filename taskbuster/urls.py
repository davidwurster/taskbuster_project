from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from .views import home, home_files
from .views import home, home_files, logout_view 

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),
    url(r'^$', home, name='home'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'i18n/', include('django.conf.urls.i18n')),
    url(r'^accounts/logout/$', logout_view), 
]

urlpatterns += i18n_patterns(
    url(r'^$', home, name='home'),
    url(r'^admin/', (admin.site.urls)),
)