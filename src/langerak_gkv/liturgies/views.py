from django.shortcuts import render, get_object_or_404
from .models import Liturgy

def liturgy_list(request):
    context = {
        'liturgies': Liturgy.objects.all()
    }
    return render (request, 'liturgies/list.html', context)

def liturgy_detail(request, liturgy_id=None):
    context = {
        'liturgy': get_object_or_404(Liturgy, id=liturgy_id)
    }
    return render (request, 'liturgies/detail.html', context)