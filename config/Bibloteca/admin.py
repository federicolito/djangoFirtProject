from django.contrib import admin
from .models import *






class UsuarioAdmin(admin.ModelAdmin):
    #exclude = ['codigo', 'telefono']
    search_fields = ['nombre','ejemplares',]
    filter_horizontal= []
    list_filter = []
    
    def datos(self, obj):
        return ("%s %s" % (obj.codigo, obj.nombre))
    datos.short_description = 'Datos'
    def contacto(self, obj):
        return ("%s %s" % (obj.telefono, obj.direccion))
    contacto.short_description = 'Contacto'
    fieldssets = []
    list_display = ['datos', 'contacto', ]

class LibroInline(admin.StackedInline):
    model = Libro
class AutorAdmin(admin.ModelAdmin):
    inlines = [LibroInline,]

class LibroAdmin(admin.ModelAdmin):
    #exclude = ['codigo', 'telefono']
    
    
    list_filter =['titulo','codigo',]

    list_display = ['titulo', 'editorial', ]


# Register your models here.
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Ejemplar)
