from django.db import models

# Create your models here.

class Estudiante(models.Model):
    id=models.AutoField(primary_key=True)
    nom = models.CharField(max_length=40, verbose_name='Nombre')
    ap = models.CharField(max_length=40, verbose_name='Apellido Paterno')
    am = models.CharField(max_length=40, verbose_name='Apellido Materno')
    dir = models.TextField(null=True, verbose_name='Dirección')
    tel = models.TextField(null=True, verbose_name='Telefono')
    
    dni=models.ImageField(upload_to='imagenes/', verbose_name='foto dni',null=True)
    isa= models.FileField(upload_to='user_documents/', verbose_name='isa',null=True)
    cus= models.FileField(upload_to='imagenes/', verbose_name='cus',null=True)
    
    
    def __str__(self):
        fila="Id: "+ str(self.id)+ "-"+ "Nombre: " +self.nom + "-" "Apellido Paterno: " +self.ap
        return fila 
    
    def delete(self, using=None, Keep_parents=False):
        self.dni.storage.delete(self.dni.name)
        self.isa.storage.delete(self.cus.name)
        self.cus.storage.delete(self.isa.name)
        super().delete()