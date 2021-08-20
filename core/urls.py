from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('store/', include('apps.store.urls')),
    path('carts/', include('apps.carts.urls')),
    # path('accounts/', include('apps.accounts.urls')),
    # path('orders/', include('apps.orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
