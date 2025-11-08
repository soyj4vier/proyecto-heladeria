from django.contrib import admin
from django.urls import include, path
from aplicacion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('aplicacion2/', include('aplicacion2.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('inicio/', views.inicio, name='inicio'),
    path('clienteadd/', views.crear_cliente, name='crearcliente'),
    path('clientes/', views.listar_clientes, name='listarclientes'),
    path('clientecargar/<int:run>', views.cargar_cliente, name='cargarcliente'),
    path('clientemodificado/<int:run>', views.modificar_cliente, name='modificarcliente'),
    path('clienteeliminar/<int:run>/', views.eliminar_cliente, name='eliminarcliente'),
    path('promocionesadd/', views.crear_promocion, name='crearpromocion'),
    path('promocioneslist/', views.listar_promociones, name='listarpromociones'),
    path('promocionesmodificado/<int:id>', views.modificar_promocion, name='modificarpromocion'),
    path('promocionescargar/<int:id>', views.cargar_promocion, name='cargarpromocion'),
    path('promocioneseliminar/<int:id>/', views.eliminar_promocion, name='eliminarpromocion'),
    path('movimientoadd/', views.crear_movimiento, name='crearmovimiento'),
]
