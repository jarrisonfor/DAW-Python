from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .models import Sistem, Cpu, Ram, Disk, Net
from django.shortcuts import redirect
from django.http.response import FileResponse
import os


class ApiRest(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        sistemInfo = Sistem.objects.get_or_create(
            nodeName=data['sistemInfo']['nodeName'],
            defaults=data['sistemInfo']
        )[0]
        ''' Cpu.objects.update_or_create(data['cpuInfo'], system_id=sistemInfo.id)
        Ram.objects.update_or_create(data['ramInfo'], system_id=sistemInfo.id) '''
        Cpu.objects.create(system_id=sistemInfo.id, **data['cpuInfo'])
        Ram.objects.create(system_id=sistemInfo.id, **data['ramInfo'])
        Disk.objects.update_or_create(
            data['diskInfo'],
            system_id=sistemInfo.id
        )
        Net.objects.update_or_create(data['netInfo'], system_id=sistemInfo.id)
        return Response({'interval': 10})


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
        cpuData = self.getCpuData(id)
        ramData = self.getRamData(id)
        disk = Disk.objects.get(system_id=id)
        net = Net.objects.get(system_id=id)
        return render(request, 'monitor/sistema.html', {
            'sistem': sistem,
            'cpuInfo': cpuData['cpuInfo'],
            'cpuUsage': cpuData['chartInfo'],
            'ramInfo': ramData['ramInfo'],
            'ramUsage': ramData['chartInfo'],
            'disk': disk,
            'net': net,
        })

    def getCpuData(self, id):
        cpus = Cpu.objects.filter(system_id=id).order_by(
            '-creationDate')[:20][::-1]
        cpuLabels = []
        cpuData = []
        for cpu in cpus:
            cpuData.append(cpu.cpuTotalUsage)
            cpuLabels.append(cpu.creationDate.strftime('%H:%M:%S'))
            cpuInfo = {
                'physicalCores': cpu.physicalCores,
                'totalCores': cpu.totalCores,
                'frequencyMax': cpu.frequencyMax,
                'frequencyMin': cpu.frequencyMin,
                'frequencyCurrent': cpu.frequencyCurrent,
            }
        return {
            'chartInfo': {
                'cpuLabels': cpuLabels,
                'cpuData': cpuData,
            },
            'cpuInfo': cpuInfo
        }

    def getRamData(self, id):
        rams = Ram.objects.filter(system_id=id).order_by(
            '-creationDate')[:20][::-1]
        ramLabels = []
        ramData = []
        for ram in rams:
            ramData.append(ram.percentage)
            ramLabels.append(ram.creationDate.strftime('%H:%M:%S'))
            ramInfo = {
                'total': ram.total,
                'available': ram.available,
            }
        return {
            'chartInfo': {
                'ramLabels': ramLabels,
                'ramData': ramData,
            },
            'ramInfo': ramInfo
        }


class SistemDelete(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return redirect('login/')
        sistem = get_object_or_404(Sistem, id=id)
        sistem.delete()
        return redirect('monitor')


class LinuxDownload(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login/')
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + '/dist/linux'
        file = open(filepath, 'rb')
        return FileResponse(file)


class WindowsDownload(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login/')
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + '/dist/windows.zip'
        file = open(filepath, 'rb')
        return FileResponse(file)


class PythonDownload(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login/')
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + '/dist/cliente.py'
        file = open(filepath, 'rb')
        return FileResponse(file)
