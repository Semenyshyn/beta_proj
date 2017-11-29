from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from .models import Messages


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

# TEST GIT 1