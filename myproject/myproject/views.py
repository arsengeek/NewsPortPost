from django.views.generic import View

from django.http import HttpResponse


class IndexView(View):
    def get(self, request):
        hello.delay()
        return HttpResponse('hello')