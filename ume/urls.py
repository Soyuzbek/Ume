from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import LanguageView, IndexView, StudentSignUpView, TeacherSignUpView, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include(('users.urls', 'users'), 'users')),
    path('lang/<str:lang>', LanguageView.as_view(), name='lang'),
    path('translate/', include('rosetta.urls')),
    path('', IndexView.as_view(), name='home'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
