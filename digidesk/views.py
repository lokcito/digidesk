from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Digimon

def index(request):
  digimons = Digimon.objects.all()

  context = {
    'digis': digimons
  }
  
  return render(request, 'index.html', context)

@csrf_exempt
def create(request):
  params = request.POST # No guarda en db
  digi = Digimon() # No guarda en db
  digi.name = params["name"] # No guarda en db
  digi.level = params["level"] # No guarda en db
  digi.img = params["img"] # No guarda en db
  digi.save() # Guarda en base de datos

  return HttpResponse(status = 200)
  
  









