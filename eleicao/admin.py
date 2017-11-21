from django.contrib import admin

# Register your models here.


from eleicao.models import *

admin.site.register(Vaga)
admin.site.register(Eleitor)
admin.site.register(Candidato)
admin.site.register(Votacao)
admin.site.register(Eleicao)