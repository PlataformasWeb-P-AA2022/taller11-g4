from django.db import models

# Create your models here.

class Edificio(models.Model):
    opciones_tipos = (
        ('residencial'),
        ('comercial'),
        )

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30, unique=True)
    tipo = models.CharField(max_length=30, choices=opciones_tipos)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)

    def obtener_costo_telefonos(self):
        # valor = [t.costo_plan for t in self.numeros_telefonicos.all()]
        # valor = sum(valor)  # [10.2, 20]
        valor = 0;
        for t in self.numeros_telefonicos.all(): # self.num_telefonicos -> me devuelve un listado de obj de tipo NumeroTelefonico
            valor = valor + t.costo_plan
        return valor

    def obtener_cantidad_telefonos(self):
        """
        """
        valor = len(self.numeros_telefonicos.all())
        return valor


class Departamento(models.Model):
    nombre_propietario = models.CharField(max_length=100)
    costo_departamento = models.CharField(max_length=100)
    num_cuartos = models.IntegerField('numero de cuartos')
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%s %s %d" % (self.nombre_propietario, 
        self.costo_departamento, self.num_cuartos)
