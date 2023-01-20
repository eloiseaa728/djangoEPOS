from django.db import models
from django.db import connection

class vat(models.Model):
    vatCode = models.BigIntegerField(blank=False)
    vat = models.FloatField(blank=False)
class product(models.Model):
    EAN = models.BigIntegerField(blank=False)
    vatCode = models.ForeignKey(vat,on_delete=models.PROTECT,blank=False)
    description = models.CharField(max_length=500,blank=False)
    stock = models.IntegerField(blank=False)
class priceHistory(models.Model):
    EAN = models.ForeignKey(product,on_delete=models.PROTECT,blank=False)
    startDate = models.DateTimeField(blank=False)
    endDate = models.DateTimeField(blank=True,null=True)
    net = models.FloatField(blank=False)
    gross = models.FloatField(blank=False)
    # i.e why has the price change, for example VAT code has been updated
    description = models.CharField(max_length=500,blank=False)
    '''def save(self, *args, **kwargs):
        if not self.gross:
            cursor = connection.cursor()
            print(self.EAN)
            tmp = cursor.execute("SELECT epos_vat.vat FROM epos_vat JOIN epos_product ON epos_vat.id=epos_product.vatCode_id WHERE epos_product.id={};".format(self.EAN))
            print(str(tmp))
            self.gross = (float(self.net) * float(tmp))
        super(Subject, self).save(*args, **kwargs)'''

class order(models.Model):
    orderID = models.BigIntegerField(blank=False)
    isSettled = models.BooleanField(blank=False)
    isSale = models.BooleanField(blank=False)
    orderTime = models.DateTimeField(auto_now=True,blank=False)
class transaction(models.Model):
    orderID = models.ForeignKey(order,on_delete=models.PROTECT,blank=False)
    EAN = models.ForeignKey(product,on_delete=models.PROTECT,blank=False)
    quantity = models.IntegerField(blank=False)
    percentageModifier = models.FloatField(blank=False)
