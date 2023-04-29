from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


from django.contrib.admin import site


urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + [

    path('', include('example.urls')),
    path('admin/', site.urls),
    path('', include('django.contrib.auth.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
