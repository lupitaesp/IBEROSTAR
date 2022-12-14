from django.urls import path
from proyectoinventario import views
from .views import actualizarAsset, cerrar_sesion
from .views import eliminarAsset
from .views import editarAsset


urlpatterns = [
    path('',views.logi,name="Login"),
    path('home',views.home,name="Home"),
    path('bodega',views.bodega,name="Bodega"),
    path('historial/<int:id_asset>',views.historial,name="Historial"),
    path('registrarIp/', views.FormAssetsIp.registroip, name='registrarIp'),
    path('guardarIp/', views.FormAssetsIp.guardarip, name='guardarIp'),
    path('Equipos', views.equipo, name='Equipo'),
    path('editarEquipo/<int:id>',  views.editarEquipo, name='editarEquipo'),
    path('asignarEquipo/<int:id>',  views.asignarEquipo, name='asignarEquipo'),

   # path('dispositivos',views.dispositivos,name="Dispositivos"),
    path('registrarAsset/', views.FormAssetsView.inde, name='registrarAsset'),
    path('guardarAsset/',  views.FormAssetsView.procesar_formulario, name='guardarAsset'),
    path('cerrar_sesion',  cerrar_sesion, name='cerrar_sesion'), 
    path('eliminarAsset/<int:id_asset>',  eliminarAsset, name='eliminarAsset'),
    path('editarAsset/<int:id_asset>',  editarAsset, name='editarAsset'),
    path('actualizarAsset/<int:id_asset>',  actualizarAsset, name='actualizarAsset'),
    path('registrarSalida/<int:id_asset>', views.FormAssetsSalidas.registrarSalida, name='registrarSalida'),
    path('guardarSalida/<int:id_asset>',  views.FormAssetsSalidas.procesarSalida, name='guardarSalida'),
    path('regresarBodega/<int:id_asset>',  views.regresarBodega, name='regresarBodega'),
    path('editarUsuario/<int:id_asset>',  views.editarUsuario, name='editarUsuario'),
    path('actualizarHistorial/<int:id_asset>',  views.actualizarUsuario, name='actualizarHistorial'),


] 
