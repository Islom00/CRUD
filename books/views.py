from django.shortcuts import render


def index(request):
    num1 = int(request.GET.get("num1", 0))
    op = request.GET.get("op")
    num2 = int(request.GET.get("num2", 0))

    result = 0

    if op == "+":
        result = num1 + num2

    context = {
            "result": result
        }
    return render(request, "index.html", context)
