from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from django.http import HttpResponse
from eleicao.models import *
from eleicao.serializers import *


# Create your views here.

class EleicaoViewSet(viewsets.ModelViewSet):
    queryset = Eleicao.objects.all()
    serializer_class = EleicaoSerializer

class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer

class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer

class EleitorViewSet(viewsets.ModelViewSet):
    queryset = Eleitor.objects.all()
    serializer_class = EleitorSerializer

class VotacaoViewSet(viewsets.ModelViewSet):
    queryset = Votacao.objects.all()
    serializer_class = VotacaoSerializer