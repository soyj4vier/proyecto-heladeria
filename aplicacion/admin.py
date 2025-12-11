from django.contrib import admin
from aplicacion.models import Cliente, MovimientoPuntos

# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display = ['run', 'nombre', 'apellido_paterno', 'apellido_materno', 'puntos']

class MovimientoPuntosAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'puntos', 'descripcion', 'fecha']

admin.site.register(Cliente, ClientesAdmin)
admin.site.register(MovimientoPuntos, MovimientoPuntosAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Configura los campos que deseas mostrar en el panel de administración
    model = CustomUser
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'role')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('email', 'role')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)