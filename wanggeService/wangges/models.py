from django.db import models
import django.utils.timezone

YES_NO = ((False, "否"),
          (True, "是"))

MARKET_CHOICES = ((0, "深市"), (1, "沪市"))

class Stockcode(models.Model):
    code = models.CharField(verbose_name='代码', max_length=10, unique=True, db_index=True)
    name = models.CharField(verbose_name='名称', max_length=8)
    usedName = models.CharField(verbose_name='曾用名', max_length=255, default='')
    market = models.IntegerField('市场', default=0, choices=MARKET_CHOICES)
    update = models.DateField(verbose_name='上市日期')
    isindex = models.SmallIntegerField("是否指数", default=False, choices=YES_NO)
    isdelisted = models.SmallIntegerField("是否退市", default=False, choices=YES_NO)

    def __str__(self):
        return '{0} {1}'.format(self.code, self.name)

class ZXG(models.Model):
    code = models.ForeignKey(Stockcode, on_delete=models.PROTECT)
    createDate = models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)
    isactived = models.BooleanField("有效", choices=YES_NO)
