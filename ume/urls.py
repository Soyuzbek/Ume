from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import LanguageView, IndexView, LessonsView, LessonItemView
from users.views import SignUpView, StudentSignUpView, TeacherSignUpView, LogoutView, LoginView, StudentsView, \
    StudentItemView, TeachersView, TeacherItemView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include(('users.urls', 'users'), 'users')),
    path('lang/<str:lang>', LanguageView.as_view(), name='lang'),
    path('translate/', include('rosetta.urls')),
    path('', IndexView.as_view(), name='home'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('account/signup/', SignUpView.as_view(), name='signup'),
    path('account/signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('account/signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
    path('account/logout/', LogoutView.as_view(), name='logout'),
    path('account/login/', LoginView.as_view(), name='login'),
    path('students/', StudentsView.as_view(), name='students'),
    path('students/<str:pk>/', StudentItemView.as_view(), name='stud_item'),
    path('lessons/', LessonsView.as_view(), name='lessons'),
    path('lessons/<str:pk>', LessonItemView.as_view(), name='lesson'),
    path('teachers/', TeachersView.as_view(), name='teachers'),
    path('teachers/<str:pk>/', TeacherItemView.as_view(), name='teach_item'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ]