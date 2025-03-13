from django.shortcuts import render
from Application.models import Personne

def index(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        address = request.POST.get('address')

        Personne.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            address=address
        )

    context = {}
    context['Personnes'] = Personne.objects.all()
    return render(request, 'index.html', context=context)