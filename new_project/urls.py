from django.contrib import admin
from django.urls import path
from blog.views import about_view, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.auth import views
from users.views import register, profile, user_update
from django.conf import settings
from django.conf.urls.static import static
from blog.views import invoice, test_func

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/new/', PostCreateView.as_view(), name='create_post'),
    path('home/', PostListView.as_view(), name='home'),
    path('', PostListView.as_view()),
    path('post/<int:pk>', PostDetailView.as_view(), name='detail_view'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='delete_post'),
    path('about/', about_view, name='about'),
    path('register/', register, name='register'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('update/', user_update, name='update'),
    path('invoice1/', invoice),
    path('test/', test_func)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
