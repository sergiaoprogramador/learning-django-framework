from django.http import JsonResponse

def index(request):
    teste = {
        "id": 1,
        "name": "Sergio Ramos"
    }
    return JsonResponse(teste)