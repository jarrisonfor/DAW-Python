import psutil
import platform
import requests
from datetime import datetime
import time


"""
pagina de ejemplo: https://www.thepythoncode.com/article/get-hardware-system-information-python
testing web: https://ptsv2.com/
testing point: https://ptsv2.com/t/1lmjp-1622227868/post

para compilar: pyinstaller -F exclavo.py
"""


class Exclavo():

    def __init__(self, url, interval=1):
        self.interval = interval
        self.url = url

    def getSistemInfo(self):
        uname = platform.uname()
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        return {
            "system": uname.system,
            "nodeName": uname.node,
            "release": uname.release,
            "version": uname.version,
            "machine": uname.machine,
            "processor": uname.processor,
            "bootTime": f"{bt.year}-{bt.month}-{bt.day} {bt.hour}:{bt.minute}:{bt.second}",
        }

    def getCpuInfo(self):
        cpufreq = psutil.cpu_freq()
        """ cpuCoresUsage = []
        for percentage in psutil.cpu_percent(percpu=True, interval=1):
            cpuCoresUsage.append(percentage) """
        return {
            'physicalCores': psutil.cpu_count(logical=False),
            'totalCores': psutil.cpu_count(logical=True),
            'frequencyMax': f'{cpufreq.max:.2f}',
            'frequencyMin': f'{cpufreq.min:.2f}',
            'frequencyCurrent': f'{cpufreq.current:.2f}',
            'cpuTotalUsage': psutil.cpu_percent()
        }
        """ 'cpuCoresUsage': cpuCoresUsage, """

    def getRamInfo(self):
        svmem = psutil.virtual_memory()
        return {
            "total": svmem.total,
            "available": svmem.available,
            "used": svmem.used,
            "percentage": svmem.percent,
        }

    def getDiskInfo(self):
        disk_io = psutil.disk_io_counters()
        diskInfo = {
            'readBytesFromBoot': disk_io.read_bytes,
            'writeBytesFromBoot': disk_io.write_bytes,
        }
        """ 'partitions': [] """
        """ partitions = psutil.disk_partitions()
        for partition in partitions:
            fstypes = ['exfat', 'fat', 'fat16', 'fat32', 'ntfs', 'efs',
                       'ext2', 'ext3', 'ext4', 'jfs', 'reiserfs', 'reiser4', 'xfs',
                       'hfs', 'hfs+']
            if partition.fstype.lower() in fstypes:
                p = {}
                p['device'] = partition.device
                p['mountpoint'] = partition.mountpoint
                p['fstype'] = partition.fstype
                try:
                    partition_usage = psutil.disk_usage(partition.mountpoint)
                except PermissionError:
                    diskInfo['partitions'].append(p)
                    continue
                p['totalSize'] = partition_usage.total
                p['totalUsed'] = partition_usage.used
                p['totalFree'] = partition_usage.free
                p['percentage'] = partition_usage.percent
                diskInfo['partitions'].append(p) """
        return diskInfo

    def getNetInfo(self):
        net_io = psutil.net_io_counters()
        netInfo = {
            'sentBytesFromBoot': net_io.bytes_sent,
            'receivedBytesFromBoot': net_io.bytes_recv,
        }
        """ 'interfaces': [] """
        """ if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            interface = {
                'name': interface_name,
            }
            for address in interface_addresses:
                if str(address.family) == 'AddressFamily.AF_INET':
                    interface['ipAddress'] = address.address
                    interface['ipNetmask'] = address.netmask
                    interface['ipBroadcast'] = address.broadcast
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    interface['macAddress'] = address.address
                    interface['macNetmask'] = address.netmask
                    interface['macBroadcast'] = address.broadcast
            netInfo['interfaces'].append(interface) """
        return netInfo

    def getData(self):
        return {
            'sistemInfo': self.getSistemInfo(),
            'cpuInfo': self.getCpuInfo(),
            'ramInfo': self.getRamInfo(),
            'diskInfo': self.getDiskInfo(),
            'netInfo': self.getNetInfo(),
        }

    def sendInfo(self):
        requests.post(self.url, json=self.getData())

    def run(self):
        while True:
            try:
                self.sendInfo()
            except Exception as e:
                print('Ha habido un error, reintentando en 15 segundos')
                print(e)
                #print(self.getData())
                self.interval = 15
            time.sleep(self.interval)


exclavo = Exclavo('http://localhost/api/postData', interval=10)
exclavo.run()
