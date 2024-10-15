from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from maridaje import views

#apis here
router = routers.DefaultRouter()
router.register(r"vino", views.VinoView, 'vino')
router.register(r"comida", views.ComidaView, 'comida')
router.register(r"maridaje", views.MaridajeView, 'maridaje')

urlpatterns = [
    path("bodegs_api/", include(router.urls)),
    path('docs/', include_docs_urls(title="Maridaje API"))
]


