from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306202315',
        'name': 'Muhammad Falah Marzuq',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
