from email.policy import default
from django.db import models

class Congregacion(models.Model):
    code = models.CharField(max_length=25, null=False)
    primer_nombre = models.CharField(max_length=35, null=False)
    segundo_nombre = models.CharField(max_length=25, null=False)
    primer_apellido = models.CharField(max_length=25, null=False)
    segundo_apellido = models.CharField(max_length=25, null=True, default='NA')
    apellido_casada = models.CharField(max_length=25, null=True, default='NA')
    nombre_completo= models.CharField(max_length=25, null=False)
    anios_congregados = models.IntegerField(null=True)
    anios = models.IntegerField(null=True)
    direccion = models.TextField(blank=True, null=True, max_length=100)
    municipio = models.CharField(null=True, max_length=30)
    #departamento = models.CharField(blank=True, null=True, max_length=15)
    departamento = models.ForeignKey('Departamentos', models.DO_NOTHING, blank=True, null=True)
    ministerio = models.ForeignKey('Ministerios', models.DO_NOTHING, blank=True, null=True)
    fecha_bautizado = models.DateField(blank=True, null=True)
    img_bautizado = models.FileField(upload_to='images/bautizado/')
    activo = models.BooleanField(default=True)
    fecha_ingreso_bd = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = True
        db_table = 'sicar_congregacion'
        verbose_name = "sicar_congregacion"
        verbose_name_plural = "sicar_congregacion"
        ordering = ['id']
        
    def __str__(self):
        return self.nombre_completo    
        
class Departamentos(models.Model):
    nombre = models.CharField(null=True, max_length=30)
    pais = models.ForeignKey('Paises', models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'departamentos'
        verbose_name = "departamentos"
        verbose_name_plural = "departamentos"
        ordering = ['id']

    def __str__(self):
        return self.nombre   
    
class Paises(models.Model):
    nombre = models.CharField(null=True, max_length=30)
    continente =  models.ForeignKey('Continentes', models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'paises'
        verbose_name = "paises"
        verbose_name_plural = "paises"
        ordering = ['id']
    
    def __str__(self):
        return self.nombre 
    
class Continentes(models.Model):
    nombre = models.CharField(null=True, max_length=30)
    
    class Meta:
        managed = True
        db_table = 'continentes'
        verbose_name = "continentes"
        verbose_name_plural = "continentes"
        ordering = ['id']
    
    def __str__(self):
        return self.nombre 
    
class Gastos(models.Model):
    monto = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    periodo = models.DateField(blank=True, null=True)
    ministerio = models.ForeignKey('Ministerios', models.DO_NOTHING, blank=True, null=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'gastos'
        verbose_name = "gastos"
        verbose_name_plural = "gastos"
        ordering = ['id']
    def __str__(self):
        return self.ministerio 
    
    
class Ministerios(models.Model):
    nombre = models.CharField(max_length=30, null=True)
    lider = models.ForeignKey('Congregacion', models.DO_NOTHING, blank=True, null=True)
    disponible_presupuesto = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    
    class Meta:
        managed = True
        db_table = 'ministerios'
        verbose_name = "ministerios"
        verbose_name_plural = "ministerios"
        ordering = ['id']
    def __str__(self):
        return self.nombre 
        
class VotacionesAdmin(models.Model):
    nombre = models.CharField(max_length=30, null=True)
    periodo = models.DateField(blank=True, null=True)
    ministerio = models.ForeignKey('Ministerios', models.DO_NOTHING, blank=True, null=True)
    candidatos = models.JSONField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'votacionesadmin'
        verbose_name = "votacionesadmin"
        verbose_name_plural = "votacionesadmin"
        ordering = ['id']
    def __str__(self):
        return self.nombre 
        
class Lideres(models.Model):
    code_name = models.ForeignKey('Congregacion', models.DO_NOTHING, blank=True, null=True)
    Ministerio = models.ForeignKey('Ministerios', models.DO_NOTHING, blank=True, null=True)
    anio = models.DateField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'lideres'
        verbose_name = "lideres"
        verbose_name_plural = "lideres"
        ordering = ['id']
    def __str__(self):
        return self.code_name 
        
class Votaciones(models.Model):
    code_hermano = models.ForeignKey('Congregacion', models.DO_NOTHING, blank=True, null=True)
    code_votacion = models.ForeignKey('Votacionesadmin', models.DO_NOTHING, blank=True, null=True)
    votacion_response = models.JSONField(blank=True, null=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = True
        db_table = 'votaciones'
        verbose_name = "votaciones"
        verbose_name_plural = "votaciones"
        ordering = ['id']
        
    def __str__(self):
        return self.code_hermano 
    
    
