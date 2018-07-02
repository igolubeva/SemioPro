from django.shortcuts import render

# Create your views here.

def z_list(request):
    
    return render(request, 'StatisticModule\z_list.html', {})