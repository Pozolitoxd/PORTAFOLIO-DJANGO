from django.shortcuts import render

def inicio(request):
    return render(request, 'content/inicio.html')
def proyecto(request):
    return render(request, 'content/proyecto.html')
def contacto(request):
    return render(request,'content/contacto.html')