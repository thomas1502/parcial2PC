from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Producto, Venta, Detalle, Solicitud, Ordenes
import json
from django.http.response import JsonResponse
from decimal import Decimal, InvalidOperation

# Create your views here.
class ProductoView(View):
    #Metodo que se ejecuta cada vez que se realiza una peticion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # Views para productos
    def get(self, request, id=0):
        if(id > 0):
            productos = list(Producto.objects.filter(id=id).values())
            if len(productos) > 0:
                producto = productos[0]
                datos = {'message': "Success", 'producto': producto}
            else:
                datos = {'message': "Producto no encontrado"}
            return JsonResponse(datos)
        else:
            productos = list(Producto.objects.values())
            if len(productos) > 0:
                datos = {'message': "Success", 'productos': productos}
            else:
                datos = {'message': "Productos no encontrados"}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Producto.objects.create(nombre=jd['nombre'], descripcion=jd['descripcion'], precio=jd['precio'], stock=jd['stock'])
        datos = { 'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id=0):
        jd = json.loads(request.body)
        productos = list(Producto.objects.filter(id=id).values())
        if len(productos) > 0:
            producto = Producto.objects.get(id=id)
            producto.nombre = jd['nombre']
            producto.descripcion = jd['descripcion']
            producto.precio = jd['precio']
            producto.stock = jd['stock']
            producto.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Producto no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        productos = list(Producto.objects.filter(id=id).values())
        if len(productos) > 0:
            Producto.objects.filter(id=id).delete()
            datos = { 'message': "Success"}
        else:
            datos = {'message': "Producto no encontrado"}
        return JsonResponse(datos)
    
class VentaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) 
    
    #Views para ventas
    def get(self, request, id=0):
        if(id > 0):
            ventas = list(Venta.objects.filter(id=id).values())
            if len(ventas) > 0:
                venta = ventas[0]
                datos = {'message': "Success", 'venta': venta}
            else:
                datos = {'message': "Venta no encontrada"}
            return JsonResponse(datos)
        else:
            ventas = list(Venta.objects.values())
            if len(ventas) > 0:
                datos = {'message': "Success", 'ventas': ventas}
            else:
                datos = {'message': "Ventas no encontradas"}
            return JsonResponse(datos)
        
    def post(self, request):
        jd = json.loads(request.body)
        Venta.objects.create(nombre_cliente=jd['nombre_cliente'], fecha_venta=jd['fecha_venta'], total=jd['total'])
        datos = { 'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id=0):
        jd = json.loads(request.body)
        ventas = list(Venta.objects.filter(id=id).values())
        if len(ventas) > 0:
            venta = Venta.objects.get(id=id)
            venta.nombre_cliente = jd['nombre_cliente']
            venta.fecha_venta = jd['fecha_venta']
            venta.total = jd['total']
            venta.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Venta no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        ventas = list(Venta.objects.filter(id=id).values())
        if len(ventas) > 0:
            Venta.objects.filter(id=id).delete()
            datos = { 'message': "Success"}
        else:
            datos = {'message': "Venta no encontrado"}
        return JsonResponse(datos)
    
class DetalleVentaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) 
    
    def get(self, request, id=0):
        if(id > 0):
            detalles = list(Detalle.objects.filter(id=id).values())
            if len(detalles) > 0:
                detalle = detalles[0]
                datos = {'message': "Success", 'detalle': detalle}
            else:
                datos = {'message': "Detalle de venta no encontrado"}
            return JsonResponse(datos)
        else:
            detalles = list(Detalle.objects.values())
            if len(detalles) > 0:
                datos = {'message': "Success", 'detalles': detalles}
            else:
                datos = {'message': "Detalles de ventas no encontradas"}
            return JsonResponse(datos)
        
    def post(self, request):
        #Guardamos el id del producto que se quiere comprar
        jd = json.loads(request.body)
        idProducto = jd['producto_id']

        #Buscamos la cantidad existente del producto
        productoCantidad = Producto.objects.filter(id=idProducto).values_list('stock', flat=True).first()

        #Condicion de cantidad
        if(jd['cantidad'] <= productoCantidad):
            Detalle.objects.create(cantidad=jd['cantidad'], subtotal=jd['subtotal'], producto_id=jd['producto_id'], venta_id=jd['venta_id'])
            #Actualizacion de stock de producto
            nuevaCantidad = productoCantidad - jd['cantidad']
            
            producto = Producto.objects.get(id=idProducto)
            producto.stock = nuevaCantidad
            producto.save()

            datos = { 'message': "Success"}
            return JsonResponse(datos)
        else:
            datos = { 'message': "No hay suficiente existencia de producto para vender."}
            return JsonResponse(datos)

    def put(self, request, id=0):
        jd = json.loads(request.body)
        detalles = list(Detalle.objects.filter(id=id).values())
        if len(detalles) > 0:
            detalle = Detalle.objects.get(id=id)
            detalle.cantidad = jd['cantidad']
            detalle.subtotal = jd['subtotal']
            detalle.producto_id = jd['producto_id']
            detalle.venta_id = jd['venta_id']
            detalle.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Detalle de venta no encontrado"}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        detalles = list(Detalle.objects.filter(id=id).values())
        if len(detalles) > 0:
            #Buscamos la cantidad del detalle a vender
            cantidadProductoAgregar = Detalle.objects.filter(id=id).values_list('cantidad', flat=True).first()
            idProducto = Detalle.objects.filter(id=id).values_list('producto_id', flat=True).first()
            cantidadProductoAntes = Producto.objects.filter(id=idProducto).values_list('stock', flat=True).first()
            nuevaCantidad = cantidadProductoAgregar + cantidadProductoAntes

            #Eliminamos el detalle
            Detalle.objects.filter(id=id).delete()

            #Devolvemos la cantidad
            producto = Producto.objects.get(id=idProducto)
            producto.stock = nuevaCantidad
            producto.save()

            datos = { 'message': "Success"}
        else:
            datos = {'message': "Detalle de venta no encontrado"}
        return JsonResponse(datos)
    
class SolicitudesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) 
    
    def post(self, request):
        bandera = 0
        #Buscamos la cantidad de codigos existentes
        jd = json.loads(request.body)
        if(jd['tipo_solicitud'] == 'solicitud de estudiante permanente'):
            cantidad = Solicitud.objects.filter(codigo_solicitud__icontains='PERMANENTE').count() + 1
            bandera = 1
        elif (jd['tipo_solicitud'] == 'solicitud de oyente'):
            cantidad = Solicitud.objects.filter(codigo_solicitud__icontains='OYENTE').count() + 1
            bandera = 2
        
        #Concatenamos
        if(bandera == 1):
            concatenado = 'PERMANENTE-' + str(cantidad)
        elif(bandera == 2):
            concatenado = 'OYENTE-' + str(cantidad)

        #Almacenamos y mostramos mensaje
        if(bandera > 0):
            Solicitud.objects.create(tipo_solicitud=jd['tipo_solicitud'], codigo_solicitud=concatenado)
            if(bandera == 1):
                mensaje = "su solicitud como oyente ha sido procesada, su número de boleta es " + concatenado
                datos = { 'message': mensaje}
            elif(bandera == 2):
                mensaje = "su solicitud como estudiante permanente ha sido procesada, su número de boleta es " + concatenado
                datos = { 'message': mensaje}
            return JsonResponse(datos)
        else:
            datos = { 'message': 'No existe la solicitud'}
            return JsonResponse(datos)

class OrdenesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            ordenes = list(Ordenes.objects.filter(id=id).values('id', 'nombreCliente'))
            if len(ordenes) > 0:
                orden = ordenes[0]
                datos = {'message': "CORRECTO", "Orden": orden}
            else:
                datos = {'message': 'Orden no encontrada...'}
        else:
            ordenes = list(Ordenes.objects.values('id', 'nombreCliente'))
            if len(ordenes) > 0:
                datos = {"Ordenes": ordenes}
            else:
                datos = {'message': 'No se encontraron órdenes...'}
        return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        try:
            total = Decimal(jd['total'])
        except InvalidOperation:
            return JsonResponse({'message': 'Error en el servidor'}, status=500)
        Ordenes.objects.create(nombreCliente=jd['nombreCliente'], total=total)
        datos = {'message': 'Success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        total = Decimal(jd.get('total', 0))

        ordenes = list(Ordenes.objects.filter(id=id).values())

        if len(ordenes) > 0:
            orden = Ordenes.objects.get(id=id)
            orden.nombreCliente = jd['nombreCliente']
            orden.total = total
            orden.save()
            datos = {"message": "Exito, se editó la orden"}
        else:
            datos = {"message": "ERROR, no se encontró la orden"}
        return JsonResponse(datos)

    def delete(self, request, id):
        ordenes = list(Ordenes.objects.filter(id=id).values())

        if len(ordenes) > 0:
            Ordenes.objects.filter(id=id).delete()
            datos = {"message": "Exito, se eliminó la orden"}
        else:
            datos = {"message": "ERROR, no se encontró la orden"}
        return JsonResponse(datos)
