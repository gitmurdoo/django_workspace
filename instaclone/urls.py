from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView
from .pydenticon_views import image as pydenticon_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', login_required(TemplateView.as_view(
        template_name='root.html')), name='root'),
    path('accounts/', include('accounts.urls')),
    path('identicon/image/<path:data>/',
         pydenticon_image, name='pydenticon_image'),
    path('', include('instagram.urls')),
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
