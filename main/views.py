from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306228472',
        'name': 'Rakabima Ghaniendra Rusdianto',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
