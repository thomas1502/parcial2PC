from django.urls import path
from .views import ProductoView, VentaView, DetalleVentaView, SolicitudesView, OrdenesView, ProveedorView, ClienteView, BancoView, TarjetaView,mostrar_clientes,mostrar_bancos,mostrar_proveedores,obtener_tarjetas_cliente,obtener_tarjetas_banco, obtener_tarjetas_proveedor
urlpatterns=[
    #URL Productos
    path('productos/', ProductoView.as_view(), name='productos_list'),
    path('productos/<int:id>', ProductoView.as_view(), name='productos_process'),

    #URL Ventas
    path('ventas/', VentaView.as_view(), name='ventas_list'),
    path('ventas/<int:id>', VentaView.as_view(), name='ventas_proccess'),

    #URL Detalles
    path('detalles/', DetalleVentaView.as_view(), name='detalles_list'),
    path('detalles/<int:id>', DetalleVentaView.as_view(), name='detalles_proccess'),

    #URL Solicitudes
    path('solicitud/', SolicitudesView.as_view(), name='solicitudes_list'),

    #Ruta para Ordenes
    path('ordenes/listado/', OrdenesView.as_view(), name='listar_ordenes'),
    path('ordenes/listado/<int:id>', OrdenesView.as_view(), name='listar_orden'),
    path('ordenes/crear/', OrdenesView.as_view(), name='nueva_orden'),
    path('ordenes/editar/<int:id>/', OrdenesView.as_view(), name='editar_orden'),
    path('ordenes/eliminar/<int:id>/', OrdenesView.as_view(), name='eliminar_orden'),

    #Rutas ejercicio
    path('proveedor/listado/', ProveedorView.as_view(), name='listar_proveedores'),
    path('proveedor/listado/<int:id>', ProveedorView.as_view(), name='listar_proveedor'),

    path('cliente/listado/', ClienteView.as_view(), name='listar_clientes'),
    path('cliente/listado/<int:id>', ClienteView.as_view(), name='listar_cliente'),

    path('banco/listado/', BancoView.as_view(), name='listar_bancos'),
    path('banco/listado/<int:id>', BancoView.as_view(), name='listar_banco'),

    path('tarjeta/listado/', TarjetaView.as_view(), name='listar_tarjetas'),
    path('tarjeta/listado/<int:id>', TarjetaView.as_view(), name='listar_tarjeta'),
    path('tarjeta/listado/<str:texto>', TarjetaView.as_view(), name='listar_tarjeta_cliente'),

    path('clientes_mayores/', mostrar_clientes, name='mostrar_clientes'),
    path('mostrar_bancos/', mostrar_bancos, name='mostrar_bancos'),
    path('mostrar_proveedores/', mostrar_proveedores, name='mostrar_proveedores'),
    path('cliente/<int:cliente_id>/tarjetas/', obtener_tarjetas_cliente, name='obtener_tarjetas_cliente'),

    path('banco/<int:id_banco>/tarjetas/', obtener_tarjetas_banco, name='obtener_tarjetas_banco'),
    path('proveedor/<int:id_proveedor>/tarjetas/', obtener_tarjetas_proveedor, name='obtener_tarjetas_proveedor'),
]