from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from usuarios import views


#api versioning
router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioView, 'usuarios')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='usuarios api'))
]