from django.conf.urls import url
from . import main
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', main.index, name='index'),        
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
