from django.db import models


class Editora(models.Model):
    site = models.URLField(blank=True, null=True)
    nome = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nome} - {self.site}"
