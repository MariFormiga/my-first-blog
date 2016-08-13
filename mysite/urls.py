import django.conf.urls
from django.contrib import admin

urlpatterns = [
    django.conf.urls.url(r'^admin/', django.conf.urls.include(admin.site.urls)),
    django.conf.urls.url(r'', django.conf.urls.include('blog.urls')),
]

