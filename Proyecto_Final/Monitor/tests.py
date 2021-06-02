from django.test import TestCase
from .models import Cpu, Sistem, Ram, Disk, Net
from django.contrib.auth.models import User
import json


class MonitorTestCase(TestCase):

    fixtures = ['pcinfo.json']

    def user_loged(self):
        user = User.objects.create_user('test', 'test@test.test', 'test')
        self.response = self.client.login(
            username='test',
            password='test'
        )

    """ Si no esta logeado no puede hacer nada """

    def test_index_no_logged(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_sistem_no_logged(self):
        response = self.client.get('/1')
        self.assertEqual(response.status_code, 302)

    def test_download_windows_no_logged(self):
        response = self.client.get('/linux/download')
        self.assertEqual(response.status_code, 302)

    def test_download_linux_no_logged(self):
        response = self.client.get('/windows/download')
        self.assertEqual(response.status_code, 302)

    def test_download_python_no_logged(self):
        response = self.client.get('/python/download')
        self.assertEqual(response.status_code, 302)

    def test_delete_sistem_no_logged(self):
        response = self.client.get('/1/delete')
        self.assertTrue(Sistem.objects.filter(pk=1).exists())
        self.assertEqual(response.status_code, 302)

    """ Si esta logeado puede hacer todo """

    def test_index_logged(self):
        self.user_loged()
        response = self.client.get('/')
        # response.context['sistem']
        # self.assertJSONEqual('')
        self.assertEqual(response.status_code, 200)

    def test_delete_sistem_logged(self):
        self.user_loged()
        response = self.client.get('/1/delete')
        self.assertFalse(Sistem.objects.filter(pk=1).exists())
        self.assertEqual(response.status_code, 302)

    def test_sistem_logged(self):
        self.user_loged()
        response = self.client.get('/1')
        self.assertEqual(response.status_code, 200)

    def test_download_windows_logged(self):
        self.user_loged()
        response = self.client.get('/linux/download')
        self.assertEqual(response.status_code, 200)

    def test_download_linux_logged(self):
        self.user_loged()
        response = self.client.get('/windows/download')
        self.assertEqual(response.status_code, 200)

    def test_download_python_logged(self):
        self.user_loged()
        response = self.client.get('/python/download')
        self.assertEqual(response.status_code, 200)

    """ Pruebas api """

    def test_api_post_data_ya_existe(self):
        postData = {
            'sistemInfo': {
                "system": "Linux",
                "nodeName": "yeray-PC",
                "release": "5.4.0-73-generic",
                "version": "#82-Ubuntu SMP Wed Apr 14 17:39:42 UTC 2021",
                "machine": "x86_64",
                "processor": "x86_64",
                "bootTime": "2021-06-01T08:51:24",
            },
            'cpuInfo': {
                "physicalCores": 8,
                "totalCores": 8,
                "frequencyMax": 4900.0,
                "frequencyMin": 800.0,
                "frequencyCurrent": 1275.2,
                "cpuTotalUsage": 28.0,
            },
            'ramInfo': {
                "total": 33604755456,
                "available": 28062294016,
                "used": 4795789312,
                "percentage": 16.5,
            },
            'diskInfo': {
                "readBytesFromBoot": 1,
                "writeBytesFromBoot": 2,
            },
            'netInfo': {
                "sentBytesFromBoot": 1,
                "receivedBytesFromBoot": 2,
            },
        }
        response = self.client.post(
            '/api/postData', json.dumps(postData), "application/json")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Cpu.objects.all().last().system_id == 1)
        self.assertTrue(Ram.objects.all().last().system_id == 1)
        self.assertTrue(
            Disk.objects.all().last().readBytesFromBoot,
            1,
        )
        self.assertTrue(
            Disk.objects.all().last().writeBytesFromBoot,
            2,
        )
        self.assertTrue(
            Net.objects.all().last().sentBytesFromBoot,
            1,
        )
        self.assertTrue(
            Net.objects.all().last().receivedBytesFromBoot,
            2,
        )
        self.assertTrue(Sistem.objects.all().count(), 1)
        self.assertEqual(Cpu.objects.all().count(), 2)
        self.assertEqual(Ram.objects.all().count(), 2)
        self.assertEqual(Disk.objects.all().count(), 1)
        self.assertEqual(Net.objects.all().count(), 1)

    def test_api_post_data_no_existe(self):
        postData = {
            'sistemInfo': {
                "system": "Linux",
                "nodeName": "otro-PC",
                "release": "5.4.0-73-generic",
                "version": "#82-Ubuntu SMP Wed Apr 14 17:39:42 UTC 2021",
                "machine": "x86_64",
                "processor": "x86_64",
                "bootTime": "2021-06-01T08:51:24",
            },
            'cpuInfo': {
                "physicalCores": 8,
                "totalCores": 8,
                "frequencyMax": 4900.0,
                "frequencyMin": 800.0,
                "frequencyCurrent": 1275.2,
                "cpuTotalUsage": 29.0,
            },
            'ramInfo': {
                "total": 33604755456,
                "available": 28062294016,
                "used": 4795789312,
                "percentage": 16.5,
            },
            'diskInfo': {
                "readBytesFromBoot": 3934242816,
                "writeBytesFromBoot": 19086054400,
            },
            'netInfo': {
                "sentBytesFromBoot": 965603367,
                "receivedBytesFromBoot": 4955165725,
            },
        }
        response = self.client.post(
            '/api/postData', json.dumps(postData), "application/json")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Sistem.objects.filter(pk=2).exists())
        self.assertTrue(Cpu.objects.filter(system_id=2).exists())
        self.assertTrue(Ram.objects.filter(system_id=2).exists())
        self.assertTrue(Disk.objects.filter(system_id=2).exists())
        self.assertTrue(Net.objects.filter(system_id=2).exists())
        self.assertTrue(Sistem.objects.all().count(), 2)
        self.assertEqual(Cpu.objects.all().count(), 2)
        self.assertEqual(Ram.objects.all().count(), 2)
        self.assertEqual(Disk.objects.all().count(), 2)
        self.assertEqual(Net.objects.all().count(), 2)
