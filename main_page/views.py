from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Messages
from .forms import DataForm
import requests
import json


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


def post_request(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data['body']
            port = form.cleaned_data['port']
            url = form.cleaned_data['url']
            proxies = {'http': 'http://ivan.semenyshyn:Adidas767@sgproxy.kyivstar.ua:3128',
                       'https': 'https://ivan.semenyshyn:Adidas767@sgproxy.kyivstar.ua:3128'}
            headers = {'content-type': 'application/json'}
            r = requests.post(url + ':' + port, data=body, headers=headers, proxies=proxies)
            # return render(request, 'test_post_sending.html', {'res': r})
            return HttpResponseRedirect('/post/')
    else:
        form = DataForm()
    return render(request, 'main_page/post_fom.html', {'form': form})
