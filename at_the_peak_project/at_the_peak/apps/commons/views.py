def permission_denied_handler(request):
    from django.http import HttpResponse
    return HttpResponse('You have no permissions!')