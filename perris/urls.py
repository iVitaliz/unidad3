from django.conf.urls import include, url
from django.urls import path, include
from .views import register
from . import views



urlpatterns = [

    url(r'^$', views.inicio),
    url('perris/login', views.login , name="login"),
    url(r'^register/', views.register, name= "register"),
    url('perris/disponibles', views.perros_disponibles , name="perros_disponibles"),
    url('administrador',views.administrador_inicio, name="adm.inicio" ),
    path('agregar', views.new_post_perro, name='new_post_perro'),
    path('perro/<int:pk>/editar/', views.edit_post_perro, name='edit_post_perro'),
    url(r'^perro/(?P<pk>[0-9]+)/$', views.detail_post_perro,name='detail_post_perro'),
    path('eliminar/<int:pk>', views.delete_post_perro, name='delete_post_perro'),
    
]

