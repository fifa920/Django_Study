from django.shortcuts import render

# Create your views here.

def ping(request):
    return render(request, 'boards/ping.html')

def pong(request):
    message = request.GET.get('message')
    context = {
        'message': message
    }
    return render(request,'boards/pong.html', context)