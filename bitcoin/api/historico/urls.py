from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^iniciar/$', views.HistoricoViewSet.as_view({'get':'iniciar_historico'})),
    url(r'^listar/$', views.HistoricoViewSet.as_view({'get':'list_historico'})),
    
]