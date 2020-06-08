from django.conf.urls import url
from . import views
from .views import ImageView,ImageDetail,CreateDetail,UpdateDetail,CreateComment,CommentView,ImageDelete,imagepreference,ProfileApi
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .models import Image,Profile
from django.urls import path,include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('profile',views.ProfileList)
router.register('profie-details', views.ImageList)



urlpatterns = [ 
    path('api/merch/merch-id/(?P<pk>[0-9]+)/',views.MerchDescription.as_view()),
    path('apis/', views.ProfileApi.as_view()),
    path('image/<int:imageid>/preference/<int:userpreference>', views.imagepreference, name='imagepreference'),
    path('', ImageView.as_view(), name = 'blog-home'),
    path('api-token-auth/', obtain_auth_token),
    path('api/',include(router.urls)),
    path('image/<int:pk>/', ImageDetail.as_view(), name = 'image-detail'),
    path('apiz/', views.apiz, name = 'comment-detail'),
    path('image/<int:pk>/update', UpdateDetail.as_view(), name = 'image-update'),
    path('image/<int:pk>/delete',ImageDelete.as_view(), name = 'image-delete'),
    path('image/new/', CreateDetail.as_view(), name = 'image-create'),
    path('register/', views.register, name = 'blog-register'),
    path('profile/', views.profile, name = 'blog-profile'),
    path('login', auth_views.LoginView.as_view(template_name = 'blog/login.html'), name = 'blog-login'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'blog/logout.html'), name = 'blog-logout'),
    path('search/', views.search_results, name='search_results'),
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)