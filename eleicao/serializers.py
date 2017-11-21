from rest_framework import routers, serializers, viewsets
from eleicao.models import *

class EleicaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eleicao
        fields = ('local','dataInicio','dataFim')

class CandidatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidato
        fields = ('nome','rg','cpf','idade')

class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = ('codigo',)

class VagaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vaga
        fields = ('cargo','candidato')

class EleitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eleitor
        fields = ('nome','cpf','token')

class VotacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Votacao
        fields = ('eleitor','candidato','votoBranco','dataHora')