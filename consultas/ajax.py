from django.http import JsonResponse
from .models import Aula

def dameAulas(request):
    id_edificio = request.GET.get('id_edificio')
    aulas = Aula.objects.none()
    opciones = '<option value="" selected="selected">--------</option>'
    if id_edificio:
        aulas = Aula.objects.filter(id_edificio=id_edificio)
    for aula in aulas:
        opciones += '<option value=%s>%s</option>' % (
            aula.id,
            aula.aula
        )
    response = {}
    response['aulas'] = opciones
    return JsonResponse(response)