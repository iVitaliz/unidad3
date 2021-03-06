"""misperris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf.urls import include, url
from rest_framework import routers
from perris.quickstart import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'groups',views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('perris.urls')),
    path('', include('pwa.urls')),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
    path('accounts/', include('django.contrib.auth.urls')),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset.html'
         ),
         name='password_reset'), 
    path('password-reset/done',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_don.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirmar.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_completo.html'
         ),
         name='password_reset_complete'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))    
         
]   

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)