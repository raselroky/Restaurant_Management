
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('user_management.urls')),
    path('rolesandpermission/',include('roles_permission.urls')),
    path('restaurant_menu/',include('restaurant_menu.urls')),
    path('ordering_payments/',include('ordering_payments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)