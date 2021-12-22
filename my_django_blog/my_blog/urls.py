from django.urls import path
from .views import index, travel, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index/', index, name = "index"),
    path('', index ),
    path('travel/', PostListView.as_view() , name = "travel"),
    path('post/<int:pk>/', PostDetailView.as_view() , name = "post-detail"),
    path('post/new/', PostCreateView.as_view() , name = "post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view() , name = "post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() , name = "post-delete"),
    path('register/', user_views.register, name = "register"),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = "logout"),
    path('profile/', user_views.profile, name = "profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
