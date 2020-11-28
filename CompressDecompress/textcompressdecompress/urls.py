from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Home, text_file_upload

urlpatterns = [
    # path('', Home.as_view(), name='index'),
    path('', text_file_upload, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)