from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic

# Create your views here.
# import aiml
from . import aiml3

kernel = aiml3.Kernel()
kernel.learn('Emily/templates/Emily/AIML/std-startup.xml')
kernel.respond("load aiml b")


def index(request):
    return render(request, 'Emily/index.html')


def json(request):
    if request.is_ajax():
        command = request.GET['Command']
        answer = kernel.respond(command)

        if not answer:
            answer = 'Nie rozumiem Cie. Pamietaj ze jestem polka i porozumiewam sie tylko poprawna polszczyzna!'

    context = {'Answer': answer}
    return JsonResponse(context)
