from django.contrib import admin

# Register your models here.

from .models import *

# agrega tus modelos al admin

admin.site.register(ModeloTareas)