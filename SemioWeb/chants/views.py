from django.shortcuts import render
from .models import Chants


def krug_glas(request, num_glas=1):
    krugs_data = Chants.objects.filter(glas=num_glas).select_related('sign')
    context = {'krugs_data': krugs_data}
    return render(request, 'chants/krug.html', context)
