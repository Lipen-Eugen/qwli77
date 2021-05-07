from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from .models import MapsPointModel
import json


def map(request):
    return render(request, 'index.html')


@csrf_exempt
def point_input(request):
    if request.method == "POST":
        json_res = json.loads(request.body.decode("utf-8"))
        print(json_res)
        a = MapsPointModel.objects.create(pointerdolgota=json_res['lat'], pointershirota=json_res['lng'])
        a.save()

    return HttpResponse(status=200)


class OutDB(ListView):
    model = MapsPointModel
    context_object_name = 'out_list'
    queryset = MapsPointModel.objects.all()
    template_name = 'out.html'


class Outmap(View):
    def get(self, request):
        point = MapsPointModel.objects.all()
        json1 = serializers.serialize('json', point)
        context = {
            'points_json': json.dumps(json1)
        }

        return render(request, 'outmap.html', context)

