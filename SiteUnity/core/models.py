from django.db import models

class SiteUnity(models.Model):
    titulo = models.CharField('Titulo', max_length="100")
