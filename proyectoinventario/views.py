from xml.dom import INVALID_STATE_ERR
from django.http import HttpRequest
from django.shortcuts import redirect, render
from proyectoinventario.forms import FormAssets, FormIp, FormSalidas, FormUpdateIp
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from proyectoinventario.models import Assets, Clientes, Ip


def logi(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.error(request, "Informacion incorrecta")
    form = AuthenticationForm()
    return render(request, "proyectowebapp/index.html", {"form": form})


def home(request):
    bode = Assets.objects.all().filter(accion=0)
    return render(request, "proyectowebapp/home.html", {'bode': bode})

def regresarBodega(request, id_asset):
    Assets.objects.filter(id_asset=id_asset).update(accion=1)
    messages.error(request, "¡El asset se regreso a Bodega!")
    bode = Assets.objects.all().filter(accion=0)
    return render(request, "proyectowebapp/home.html", {'bode': bode, "mensaje": 'OK'})

def historial(request, id_asset):
    bodega = Assets.objects.get(id_asset=id_asset)
    cli = Clientes.objects.all().filter(asset=bodega)
    return render(request, "proyectowebapp/historial.html", {'cli': cli})

# Filtra en bodega todas las entradas.


def bodega(request):
    bode = Assets.objects.all().filter(accion=1)
    return render(request, "proyectowebapp/bodega.html", {'bode': bode})

def equipo(request):
    bode = Ip.objects.all()
    return render(request, "proyectowebapp/equipos.html", {'bode': bode, })

def cerrar_sesion(request):
    logout(request)
    return redirect('Login')


def eliminarAsset(request, id_asset):
    bodes = Assets.objects.get(id_asset=id_asset)
    bodes.delete()
    bode = Assets.objects.all().filter(accion=1)
    messages.error(request, "¡Asset eliminado correctamente!")
    return render(request, "proyectowebapp/bodega.html", {'bode': bode, "mensa": 'OK'})


def editarAsset(request, id_asset):
    bodes = Assets.objects.filter(id_asset=id_asset).first()
    form = FormAssets(instance=bodes)
    return render(request, "proyectowebapp/editarAsset.html", {"form": form, 'bodes': bodes})


def actualizarAsset(request, id_asset):
    bodes = Assets.objects.get(id_asset=id_asset)
    form = FormAssets(request.POST, instance=bodes)
    if form.is_valid():
        form.save()
        messages.error(request, "¡Asset actualizado correctamente!")
    else:
        messages.error(request, "¡ERROR!")
        return render(request, "proyectowebapp/assetsindex.html", {"form": form, "mensa": 'OK'})
    bode = Assets.objects.all().filter(accion=1)
    return render(request, "proyectowebapp/bodega.html", {"bode": bode, "mensa": 'OK'})


class FormAssetsView(HttpRequest):

    def inde(request):
        assets = FormAssets()
        return render(request, "proyectowebapp/assetsindex.html", {"form": assets})
# Guardar el formulario

    def procesar_formulario(request):
        assets = FormAssets(request.POST)
        if assets.is_valid():
            assets.save()
            messages.error(request, "¡Asset registrado correctamente!")
        else:
            messages.error(request, "¡ERROR!")
            return render(request, "proyectowebapp/assetsindex.html", {"form": assets, "mensa": 'OK'})
        bode = Assets.objects.all().filter(accion=1)
        return render(request, "proyectowebapp/bodega.html", {"bode": bode, "mensa": 'OK'})


class FormAssetsSalidas(HttpRequest):
    # Metodo para registrar lo del formulario

    def registrarSalida(request, id_asset):
        # PASAMOS POR METODO POST EL ID PARA ALMACENARLO EN UNA VARIABLE
        dispo = Assets.objects.get(id_asset=id_asset) 
        form = FormSalidas(instance=dispo)
        return render(request, "proyectowebapp/assetSalidaForm.html", {"form": form, 'dispo': dispo})
    # Guardar el formulario

    def procesarSalida(request, id_asset):
        # ALMACENAMONS EL ID QUE SE OBTIENE DEL POST EN UNA VARIABLE PARA QUE CREE EN LA BASE DE DATOS
        dispo = Assets.objects.get(id_asset=id_asset)
        nombre = request.POST['nombre']
        email = request.POST['email']
        departamento = request.POST['departamento']
        hotel = request.POST['hotel']
        estado = request.POST['estado']
        descripcion = request.POST['descripcion']
        clientes = Clientes.objects.create(asset=dispo, nombre=nombre, email=email,
                                           departamento=departamento, hotel=hotel, estado=estado, descripcion=descripcion)
        Assets.objects.filter(id_asset=id_asset).update(accion=0)
        clientes.save()
        messages.error(request, "¡Usuario asignado correctamente!")
        bode = Assets.objects.all().filter(accion=0)
        return render(request, "proyectowebapp/home.html", {"bode": bode, "mensaje": 'OK'})

def editarUsuario(request, id_asset):
    dispo = Clientes.objects.filter(id=id_asset).first()
    form = FormSalidas(instance=dispo)
    return render(request, "proyectowebapp/editarUsuario.html", {"form": form, 'dispo': dispo})


def actualizarUsuario(request, id_asset):
    dispo = Clientes.objects.get(id=id_asset)
    form = FormSalidas(request.POST, instance=dispo)
    if form.is_valid():
        form.save()
        messages.error(request, "¡Usuario actualizado correctamente!")
    bode = Assets.objects.all().filter(accion=0)
    return render(request, "proyectowebapp/home.html", {'bode': bode, 'mensaje': "OK"})

class FormAssetsIp(HttpRequest):

    def registroip(request):
        equipos = FormIp()
        return render(request, "proyectowebapp/form_ip.html", {"form": equipos})
# Guardar el formulario

    def guardarip(request):
        equipos = FormIp(request.POST)
        if equipos.is_valid():
            equipos.save()
            messages.error(request, "¡IP registrada!")
        else:
            messages.error(request, "¡ERROR!")
            return render(request, "proyectowebapp/form_ip.html", {"form": equipos, "mensa": 'OK'})
        bode = Ip.objects.all()
        return render(request, "proyectowebapp/equipos.html", {"bode": bode, "mensa": 'OK'})


def editarEquipo(request, id):
    bodes = Ip.objects.filter(id=id).first()
    form = FormUpdateIp(instance=bodes)
    return render(request, "proyectowebapp/asignarEquipo.html", {"form": form, 'bodes': bodes})


def asignarEquipo(request, id):
    bodes = Ip.objects.get(id=id)
    form = FormUpdateIp(request.POST, instance=bodes)
    if form.is_valid():
        form.save()
        messages.error(request, "¡Nombre de Equipo Asignado!")
    else:
        messages.error(request, "¡ERROR!")
        return render(request, "proyectowebapp/asignarEquipo.html", {"form": form, "mensa": 'OK'})
    bode = Ip.objects.all()
    return render(request, "proyectowebapp/equipos.html", {"bode": bode, "mensa": 'OK'})

