from django.db import models
class beneficio(models.Model):
    nome = models.CharField(max_length=100,null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    imagem_beneficio = models.ImageField(null=False, blank=False)
    tipo_beneficio = models.IntegerField(null=False, blank=False)
    def __str__(self):
        return self.nome
# Create your models here.
