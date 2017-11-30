from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .models import Messages
from .forms import DataForm


@csrf_exempt
@require_POST
def stream_data(request):
    Messages.objects.create(
        method=request.method,
        body=request.body,
        encoding=request.encoding,
        content_type=request.content_type,
    )
    return HttpResponse('OK')


def message_list(request):
    elements = Messages.objects.all()
    return render(request, 'messages_list.html', {
        'elements': elements
    })


@csrf_exempt
def post_request(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = DataForm()
    return render(request, 'display_http.html', {'form': form})


def send_post(request):
    data = str(request.body).split('&')[1]
    return render(request, 'test_post_sending.html', {'res': data})
