import string
import random
from django.utils import timezone
from django.db import models
from django.db.models.signals import pre_save

class PromoCodeManager(models.Manager):

    def get_valid(self, code):
        now = timezone.now() 
        return self.filter(code=code).filter(used=False).filter(valid_from__lte=now).filter(valid_to__gte=now).first()

class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Codigo")
    discount = models.FloatField(default=0.0, verbose_name="Descuento")
    valid_from = models.DateTimeField(verbose_name="Valido desde")
    valid_to = models.DateTimeField(verbose_name="Valido para")
    used = models.BooleanField(default=False, verbose_name="Usado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el:")

    objects = PromoCodeManager()

    def __str__(self) -> str:
        return self.code
    
    def use(self):
        self.used = True
        self.save()

    class Meta:
        verbose_name = 'Codigo Promocional'
        verbose_name_plural = 'Codigos Promocionales'
        ordering = ['id']

def set_code(sender, instance, *args, **kwargs):
    if instance.code:
        return
    chars = string.ascii_uppercase + string.digits
    instance.code = ''.join( random.choice(chars) for _ in range(10) )

pre_save.connect(set_code, sender=PromoCode)

