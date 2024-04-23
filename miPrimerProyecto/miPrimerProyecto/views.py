from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context
import datetime


def games(request):
    agno=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%X")
    
    fecha="%s/%s/%s a las %s"%(dia,mes,agno,hora)
    
    doc_externo=loader.get_template("games.html")
    documento=doc_externo.render({"fecha":fecha})
    return HttpResponse(documento)

def musica(request):
    agno=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%X")
    
    fecha="%s/%s/%s a las %s"%(dia,mes,agno,hora)
    
    doc_externo=loader.get_template("musica.html")
    documento=doc_externo.render({"fecha":fecha})
    return HttpResponse(documento)


def tecnologia(request):
    agno=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%X")
    
    fecha="%s/%s/%s a las %s"%(dia,mes,agno,hora)
    
    doc_externo=loader.get_template("tecnologia.html")
    documento=doc_externo.render({"fecha":fecha})
    return HttpResponse(documento)


def saludar(request):
    cantar=["Don omar","Romeo santos","Justin quiles"]
    doc_externo=loader.get_template("primera_plantilla.html")
    documento=doc_externo.render({"lista":cantar})
    return HttpResponse(documento)


def fecha(request):
    fechaActual=datetime.datetime.now()
    documento="""<HTML>
                        <HEAD>
                            <TITLE>Esta es una prueba HTML</TITLE>
            
                        </HEAD>
                        <BODY>
                            <h1>Usted ingreso o actualizo esta vista en la fecha %s</h1>
                        </BODY>
                    </HTML>""" %fechaActual
    return HttpResponse(documento)

def tareasEnlistadas(request):
    Tareas=["Aprender sobre la internet","Aprender HTML","Aprender CSS","Practicar python","Aprender Django","Construir mi propia WEB"]
    doc_externo=loader.get_template("SegundaPlantilla.html")
    documento=doc_externo.render({"listado":Tareas})
    return HttpResponse(documento)