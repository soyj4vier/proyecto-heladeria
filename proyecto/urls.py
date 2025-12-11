from django.contrib import admin
from django.urls import include, path
from aplicacion import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

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
    path('dashboard/promociones/', views.dashboard_promociones, name='dashboard_promociones'),
    path('buscar_clientes/', views.buscar_clientes, name='buscar_clientes'),
    path('buscar_promociones/', views.buscar_promociones, name='buscar_promociones'),
    path('generar_reporte_promocion/<int:promocion_id>/', views.generar_reporte_promocion, name='generar_reporte_promocion'),
    path('transaccion/', views.sistema_transaccional, name='sistema_transaccional'),
    #RUTAS API CLIENTES
    path('clientesapi/', views.clientesAPI, name='clientesapi'),
    path('clienteslistapi/', views.cliente_listado, name='clienteslistapi'),
    path('clienteslist/<int:pk>', views.cliente_detalle, name='clientedetalleapi'),
    # RUTAS API PROMOCIONES
    path('promocionesapi/', views.promocionesAPI, name='promocionesapi'),
    path('promocioneslistapi/', views.promocion_listado, name='promocioneslistapi'),
    path('promocioneslist/<int:pk>', views.promocion_detalle, name='promociondetalleapi'),
    # TOKENS
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

#crud clientes sprint 1
#crud promos sprint 2
#analisis promociones sprint 3