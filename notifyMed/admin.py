from django.contrib import admin

from .models import Persona
from .models import Usuario
from .models import Sexo
from .models import Dia
from .models import Hora  
from .models import TipoToma
from .models import PrincipioActivo
from .models import Medicamento
from .models import Toma
from .models import Recetas


admin.site.register(Persona)
admin.site.register(Usuario)
admin.site.register(Sexo)
admin.site.register(Dia)
admin.site.register(Hora)
admin.site.register(TipoToma)
admin.site.register(PrincipioActivo)
admin.site.register(Medicamento)
admin.site.register(Toma)
admin.site.register(Recetas)