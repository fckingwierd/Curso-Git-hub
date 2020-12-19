from django.http import HttpResponse, JsonResponse

def hi(request):
    numbers = request.GET['numbers']

    lista = [int(x) for x in numbers.split(",")]
    lista = sorted(lista)

    data = {
        "status" : "ok",
        "numbers" : lista,
        'message' : 'Integers sorted succesfully.'
    }

    return JsonResponse(data, safe = False)
    