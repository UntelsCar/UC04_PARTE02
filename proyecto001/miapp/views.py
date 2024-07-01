from django.shortcuts import render

# Create your views here.
def layout(request):
    return render(request,'layout.html',{
    })

def saludo(request):
    return render(request,'saludo.html',{
        'titulo':'Saludo',
        'autor_saludo':'TPB'
    })

def integrantes(request):
    estudiantes = [ 'Torres Guzman, Henry Fabian', 
                    'Peña Chirinos, Carlos Joel',
                    'Bravo Veintemilla, Jorge Alberto',
                    ]
    return render(request,'integrantes.html', {
        'titulo':'Integrantes',
        'estudiantes': estudiantes
    })    
