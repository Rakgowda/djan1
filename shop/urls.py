
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^purchase/', include('purchase.urls')),
    url(r'^sell/', include('sell.urls')),
]
