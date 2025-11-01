from django.shortcuts import render
from . import utils  # Importamos las funciones que creaste

def sistema_view(request):
    context = {
        'cpu': utils.get_cpu_usage(),
        'memory': utils.get_memory_usage(),
        'disk': utils.get_disk_usage(),
        'system': utils.get_system_info()
    }
    return render(request, 'sistema/index.html', context)