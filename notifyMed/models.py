from django.db import models
class Usuario(models.Model):
    nombre_text = models.CharField(max_length=100)
    apellidos_text = models.CharField(max_length=100)
    fechaNac_datetime = models.DateTimeField('fecha nacimiento')
    mail_text = models.EmailField(max_length=200)
    usuario_text = models.CharField(max_length=200)
    password_text = models.CharField(max_length=200)
    SIP_text = models.CharField(max_length=200)
    def __str__(self):
        return self.usuario_text

class Sexo(models.Model):
    descripcion_text = models.CharField(max_length=1)
    def __str__(self):
        return self.descripcion_text

class Persona(models.Model):
    SIP_text = models.CharField(max_length=200,default='')
    nombre_text = models.CharField(max_length=200)
    apellidos_text = models.CharField(max_length=200,default='')
    sexo_text = models.ForeignKey(Sexo,default='', on_delete=models.CASCADE)
    fechaNac_datetime = models.DateTimeField('fecha nacimiento')
    usuario_text = models.ForeignKey(Usuario,default='', on_delete=models.CASCADE)
    def __str__(self):
        return self.apellidos_text + ", " + self.nombre_text

class Dia(models.Model):
    descripcion_text = models.CharField(max_length=20)
    def __str__(self):
        return self.descripcion_text

class Hora(models.Model):
    descripcion_text = models.CharField(max_length=200)
    def __str__(self):
        return self.descripcion_text

class TipoToma(models.Model):
    descripcion_text = models.CharField(max_length=200)
    def __str__(self):
        return self.descripcion_text

class PrincipioActivo(models.Model):
    nombre_text = models.CharField (max_length=200)
    def __str__(self):
        return self.nombre_text

class Medicamento(models.Model):
    nombre_text = models.CharField(max_length=200)
    TipoToma = models.ForeignKey(TipoToma, on_delete=models.CASCADE)
    cantidad_text = models.CharField(max_length=10)
    PrincipiosActivos_text = models.ManyToManyField(PrincipioActivo)
    def __str__(self):
        return self.nombre_text

class Toma(models.Model):
    persona_text = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now=True)
    descripcion_text = models.CharField(max_length=200)
    activa = models.IntegerField(default=0)
    dias_text = models.ManyToManyField(Dia)
    horas_text = models.ManyToManyField(Hora)
    medicamento_text = models.ManyToManyField(Medicamento)
    def __str__(self):
        return self.persona_text.apellidos_text + ", " + self.persona_text.nombre_text + " - " + self.descripcion_text


class Recetas(models.Model):
    persona_text = models.ForeignKey(Persona, on_delete=models.CASCADE)
    medicamento_text = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad_text = models.CharField(max_length=10)
    cantidadPorToma_text = models.CharField(max_length=10)
    FechaInicio_datetime = models.DateTimeField('Fecha de inicio')
    Fechafin_datetime = models.DateTimeField('Fecha de Finalización')
    def __str__(self):
        return self.persona_text.apellidos_text + ", " + self.persona_text.nombre_text + " - " + self.medicamento_text.nombre_text
