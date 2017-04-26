from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response


def test(request,  *args, **kwargs):
    try:
        id = request.GET.get('id')
        obj = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        raise Http404
    return HttpResponse(obj.text, content_type='text/plain')