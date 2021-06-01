from django.db import models


class Sistem(models.Model):
    system = models.CharField(max_length=200)
    nodeName = models.CharField(max_length=200)
    release = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    machine = models.CharField(max_length=200)
    processor = models.CharField(max_length=200)
    bootTime = models.DateTimeField()
    creationDate = models.DateTimeField(auto_now_add=True)



class Cpu(models.Model):
    system = models.ForeignKey(Sistem, on_delete=models.CASCADE)
    physicalCores = models.BigIntegerField()
    totalCores = models.BigIntegerField()
    frequencyMax = models.FloatField()
    frequencyMin = models.FloatField()
    frequencyCurrent = models.FloatField()
    cpuTotalUsage = models.FloatField()
    creationDate = models.DateTimeField(auto_now_add=True)


class Ram(models.Model):
    system = models.ForeignKey(Sistem, on_delete=models.CASCADE)
    total = models.BigIntegerField()
    available = models.BigIntegerField()
    used = models.BigIntegerField()
    percentage = models.FloatField()
    creationDate = models.DateTimeField(auto_now_add=True)



class Disk(models.Model):
    system = models.ForeignKey(Sistem, on_delete=models.CASCADE)
    readBytesFromBoot = models.BigIntegerField()
    writeBytesFromBoot = models.BigIntegerField()
    creationDate = models.DateTimeField(auto_now_add=True)


class Net(models.Model):
    system = models.ForeignKey(Sistem, on_delete=models.CASCADE)
    sentBytesFromBoot = models.BigIntegerField()
    receivedBytesFromBoot = models.BigIntegerField()
    creationDate = models.DateTimeField(auto_now_add=True)
