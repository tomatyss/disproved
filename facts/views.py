from multiprocessing import context
from django.shortcuts import render, get_object_or_404

from facts.models import Fact


def index(request):
    year = request.GET.get('year', None)
    if year:
        facts_list = Fact.objects.filter(year__gte=year).order_by('year')
        context = {'facts_list': facts_list}
        return render(request, 'facts/index.html', context)
    return render(request, 'facts/index.html')


def detail(request, question_id):
    fact = get_object_or_404(Fact, pk=question_id)
    return render(request, 'facts/detail.html', {'fact': fact})

def random(request):
    fact = Fact.objects.order_by('?').first()
    return render(request, 'facts/detail.html', {'fact': fact})

def about(request):
    return render(request, 'facts/about.html')


