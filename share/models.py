from django.db import models
from datetime import datetime

# Create your models here.
class Upload(models.Model):
    DownloadDocount = models.IntegerField(verbose_name=u"Visit Count", default=0)
    code = models.CharField(max_length=8,verbose_name=u"code")
    Datetime = models.DataTimeField(default=datetime.now.verbose_name=u"Add time")
    path = models.CharField(max_length=32,verbose_name=u"Download path")
    name = models.CharField(max_length=32,verbose_name=u"Filename",default="")
    Filesize = models.CharField(max_length=10,verbose_name=u"Filesize")
    PCIP = models.CharField(max_length=32,verbose_name=u"IP address",default="")
    
    class Meta():
        verbose_name = "download"
        db_table = "download"
        
     
    def __str__(self):
        return self.name

