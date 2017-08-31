from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='ENDEPOINTS API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', schema_view),
    url(r'', include('apps.themes.urls')),
    url(r'', include('apps.comments.urls')),
    url(r'', include('apps.thumbs.urls')),
    url(r'', include('apps.videos.urls')),
]
