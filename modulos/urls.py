from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from modulos import views


#api versioning
router = routers.DefaultRouter()
router.register(r'modulos', views.UsuarioView, 'modulos')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='usuarios api'))
]