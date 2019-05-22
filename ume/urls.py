from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import LanguageView, IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include(('users.urls', 'users'), 'users')),
    path('lang/<str:lang>', LanguageView.as_view(), name='lang'),
    path('translate/', include('rosetta.urls')),
    path('', IndexView.as_view(), name='home'),
    path('ckeditor/', include('ckeditor_uploader.urls')),

# url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
