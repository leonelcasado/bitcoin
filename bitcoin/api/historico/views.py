# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN
from rest_framework.viewsets import ViewSet

from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from bitcoin.backend.historico.models import Historico
from bitcoin.backend.core.templates import utils
from bitcoin.api.historico.models import HistoricoSerializer
from bitcoin.backend.historico.cotacao_fox_bit import consultar_indicadores_bitcoin
import time
#==============================================================
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data,renderer_context={'indent':4})
        kwargs['content_type'] = 'application/json;charset=UTF-8'
        super(JSONResponse, self).__init__(content, **kwargs)
#==============================================================
class HistoricoViewSet(ViewSet):
    #permission_classes = (IsAuthenticated,EmpresaPermission,)
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (JSONWebTokenAuthentication,)
    #==========================================================
    #http://127.0.0.1:8000/bitcoin/api/historico/listar/
    def list_historico(self,request):
        try:
            #print request.META['REMOTE_ADDR']
            if request.method == 'GET':
                obj = Historico.objects.all()
                if obj:
                    serializer = HistoricoSerializer(obj, many=True)
                    return JSONResponse({'code':HTTP_200_OK,'message':utils.MSG_SUCCESS,'results':serializer.data})
                else:
                    return JSONResponse({'code':HTTP_404_NOT_FOUND,'message':utils.MSG_NOT_FOUND,'results':'[]'})
            else:
                return JSONResponse({'code':HTTP_403_FORBIDDEN,'message':utils.MSG_FORBIDDEN,'results':'[]'})
            
        except Exception:
            return JSONResponse({'code':HTTP_500_INTERNAL_SERVER_ERROR,'message':utils.MSG_FAILURE,'results':'[]'})
    #==========================================================
    #http://127.0.0.1:8000/bitcoin/api/historico/iniciar/
    def iniciar_historico(self,request):
        while(True):
            consultar_indicadores_bitcoin()
            time.sleep(5)
    #==========================================================
#==============================================================
