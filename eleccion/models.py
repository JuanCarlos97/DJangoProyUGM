# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Candidato(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombrecompleto = models.CharField(max_length=100)
    foto = models.FileField()
    sexo = models.CharField(max_length=1, blank=True, null=True)
    perfil = models.FileField()

    class Meta:
        managed = False
        db_table = 'candidato'


class Casilla(models.Model):
    id = models.BigAutoField(primary_key=True)
    ubicacion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'casilla'


class Eleccion(models.Model):
    id = models.BigAutoField(primary_key=True)
    periodo = models.CharField(max_length=100)
    fecha = models.DateField(blank=True, null=True)
    fechaapertura = models.DateField(blank=True, null=True)
    horaapertura = models.TimeField(blank=True, null=True)
    fechacierre = models.DateField(blank=True, null=True)
    horacierre = models.TimeField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eleccion'


class Eleccioncomite(models.Model):
    id = models.BigAutoField(primary_key=True)
    eleccion = models.ForeignKey(Eleccion, models.DO_NOTHING, blank=True, null=True)
    funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, blank=True, null=True)
    rol = models.ForeignKey('Rol', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eleccioncomite'
        unique_together = (('eleccion', 'funcionario'),)


class Funcionario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombrecompleto = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funcionario'


class Funcionariocasilla(models.Model):
    id = models.BigAutoField(primary_key=True)
    funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, blank=True, null=True)
    casilla = models.ForeignKey(Casilla, models.DO_NOTHING, blank=True, null=True)
    rol = models.ForeignKey('Rol', models.DO_NOTHING, blank=True, null=True)
    eleccion = models.ForeignKey(Eleccion, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funcionariocasilla'
        unique_together = (('funcionario', 'eleccion'),)


class Imeiautorizado(models.Model):
    id = models.BigAutoField(primary_key=True)
    funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, blank=True, null=True)
    eleccion = models.ForeignKey(Eleccion, models.DO_NOTHING, blank=True, null=True)
    casilla = models.ForeignKey(Casilla, models.DO_NOTHING, blank=True, null=True)
    imei = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'imeiautorizado'
        unique_together = (('funcionario', 'eleccion'),)


class Rol(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'rol'


class Voto(models.Model):
    id = models.BigAutoField(primary_key=True)
    eleccion = models.ForeignKey(Eleccion, models.DO_NOTHING, blank=True, null=True)
    casilla = models.ForeignKey(Casilla, models.DO_NOTHING, blank=True, null=True)
    evidencia = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voto'
        unique_together = (('eleccion', 'casilla'),)


class Votocandidato(models.Model):
    id = models.BigAutoField(primary_key=True)
    voto = models.ForeignKey(Voto, models.DO_NOTHING, blank=True, null=True)
    candidato = models.ForeignKey(Candidato, models.DO_NOTHING, blank=True, null=True)
    votos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'votocandidato'
        unique_together = (('voto', 'candidato'),)
