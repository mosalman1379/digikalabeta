from django.db import models

class phoneInfo(models.Model):
    phoneUrl=models.URLField(verbose_name='phone link')
    phoneName=models.CharField(max_length=40,verbose_name='phone name')
    phonePrice=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    phoneBeforeDiscount=models.DecimalField(null=True,max_digits=10,decimal_places=2)
    phonePicLink=models.URLField(verbose_name='phone picture link')
    rateQuality=models.FloatField(max_length=5.0,default=0.0)
    rateBuy=models.FloatField(max_length=5.0,default=0.0)
    rateCreativeness=models.FloatField(max_length=5.0,default=0.0)
    rateFeature=models.FloatField(max_length=5.0,default=0.0)
    rateSimplicity=models.FloatField(max_length=5.0,default=0.0)
    rateDesign=models.FloatField(max_length=5.0,default=0.0)
    linkHistory=models.ForeignKey(to='phones.phoneHistory',on_delete=models.PROTECT,default=None)

    def __str__(self):
        return f'phone name is {self.phoneName} with price {self.phonePrice}'

class phoneHistory(models.Model):
    name=models.CharField(verbose_name='phone name used for category',max_length=40)