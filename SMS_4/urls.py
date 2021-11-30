from django.contrib import admin
from django.urls import path,include
from user import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/",include('django.contrib.auth.urls')),
    path('register/',views.registerUser,name="user_register"),
    path('add_post/',views.add_post,name="user_add_post"),
    path('show_post/',views.show_post,name="user_post_list"),
    path('delete_post/<str:postname>',views.delete_post,name="deletepost"),
    path('update_post/<int:id>',views.update_post,name="updatepost"),
    path('registration/emailVerification/<uidb64>/<token>', views.activate, name='emailActivate'),
    path('user_profile/',views.view_profile,name="user_profile"),
    path('',views.home,name="home"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)