from django.db import models

YES_NO = ((False, "否"),
          (True, "是"))

MARKET_CHOICES = ((0, "深市"), (1, "沪市"))


class Stockcode(models.Model):
    code = models.CharField(verbose_name='代码', max_length=10, unique=True)
    name = models.CharField(verbose_name='名称', max_length=8)
    usedName = models.CharField(verbose_name='曾用名', max_length=255, default='')
    market = models.IntegerField('市场', default=0, choices=MARKET_CHOICES)
    update = models.DateField(verbose_name='上市日期')
    isindex = models.SmallIntegerField("是否指数", default=0, choices=YES_NO)
    isdelisted = models.SmallIntegerField("是否退市", default=0, choices=YES_NO)

    def __str__(self):
        return '{0} {1}'.format(self.code, self.name)