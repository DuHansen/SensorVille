from django.db import models

class FormularioModel(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=False)  # Permite que a data seja definida manualmente
    file = models.FileField(upload_to='uploads/', null=True, blank=True)  # Campo de arquivo opcional

    def __str__(self):
        return self.name
