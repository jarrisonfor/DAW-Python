from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import redirect


# Create your views here.

class ApiRest(APIView):
    def post(self, request):
        return Response({"interval": 10})


class Index(View):
    def get(self, request):
        """ category_list = Category.objects.all()
        context = {'object_list': category_list} """
        if not request.user.is_authenticated:
            return redirect('login/')
        return render(request, 'monitor/index.html')

