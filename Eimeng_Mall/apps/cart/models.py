

from django.db import models

# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True, null=False, unique=True, verbose_name='id')
    sku_id = models.CharField(max_length=255, null=False, verbose_name='商品id', unique=True)
    nums = models.IntegerField()
    is_delete = models.IntegerField()

    class Meta:
        db_table = 'shopping_cart'