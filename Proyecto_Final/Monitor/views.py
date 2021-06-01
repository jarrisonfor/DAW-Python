from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .models import Sistem, Cpu, Ram, Disk, Net

from django.shortcuts import redirect


class ApiRest(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        sistemInfo = Sistem.objects.get_or_create(nodeName=data['sistemInfo']['nodeName'], defaults=data['sistemInfo'])[0]
        """ Cpu.objects.update_or_create(data['cpuInfo'], system_id=sistemInfo.id)
        Ram.objects.update_or_create(data['ramInfo'], system_id=sistemInfo.id) """
        Cpu.objects.create(system_id=sistemInfo.id, **data['cpuInfo'])
        Ram.objects.create(system_id=sistemInfo.id, **data['ramInfo'])
        Disk.objects.update_or_create(
            data['diskInfo'], system_id=sistemInfo.id)
        Net.objects.update_or_create(data['netInfo'], system_id=sistemInfo.id)
        return Response({"interval": 10})


class Index(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login/')
        return render(request, 'monitor/index.html', {'sistems': Sistem.objects.all()})


class SistemPanel(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return redirect('login/')
        sistem = get_object_or_404(Sistem, id=id)
        cpus = Cpu.objects.filter(system_id=id).order_by('-creationDate')[:20][::-1]
        cpuLabels = []
        cpuData = []
        for cpu in cpus:
            cpuData.append(cpu.cpuTotalUsage)
            cpuLabels.append(cpu.creationDate.strftime("%H:%M:%S"))
            cpuInfo = {
                "physicalCores": cpu.physicalCores,
                "totalCores": cpu.totalCores,
                "frequencyMax": cpu.frequencyMax,
                "frequencyMin": cpu.frequencyMin,
                "frequencyCurrent": cpu.frequencyCurrent,
            }
        rams = Ram.objects.filter(system_id=id).order_by('-creationDate')[:20][::-1]
        ramLabels = []
        ramData = []
        for ram in rams:
            ramData.append(ram.percentage)
            ramLabels.append(ram.creationDate.strftime("%H:%M:%S"))
            ramInfo = {
                "total": ram.total,
                "available": ram.available,
            }
        disk = Disk.objects.get(system_id=id)
        net = Net.objects.get(system_id=id)
        return render(request, 'monitor/sistema.html', {
            'sistem': sistem,
            'cpuInfo': cpuInfo,
            'cpuUsage': {
                "cpuLabels": cpuLabels,
                "cpuData": cpuData,
            },
            'ramInfo': ramInfo,
            'ramUsage': {
                "ramLabels": ramLabels,
                "ramData": ramData,
            },
            'disk': disk,
            'net': net,
        })


class SistemDelete(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return render('login/')
        sistem = get_object_or_404(Sistem, id=id)
        sistem.delete()
        return redirect('monitor')
