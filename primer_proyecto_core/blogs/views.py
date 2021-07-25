
from django.shortcuts import HttpResponse, redirect


def root(request):
    return redirect("/blogs")


def index(request):
    documento = """
        <html>
            <head>
            </head>
            <body>
                <h1>Lista de Blogs</h1>
                <h2>Blog 1</h2>
                <h2>Blog 2</h2>
                <h2>Blog 3</h2>
                <h2>Blog 4</h2>
            </body>
        </html>
    """
    return HttpResponse(documento)


def new(request):
    documento = """
    <html>
        <head>
        </head>
        <body>
            <h1>Formulario</h1>
            <FORM action="http://algunsitio.com/" method="post">
                <P>
                <LABEL for="nombre">Nombre: </LABEL>
                    <INPUT type="text" id="nombre"><BR>
                <LABEL for="apellido">Apellido: </LABEL>
                    <INPUT type="text" id="apellido"><BR>
                <LABEL for="email">email: </LABEL>
                    <INPUT type="text" id="email"><BR>
                <INPUT type="radio" name="sexo" value="Varón"> Varón<BR>
                <INPUT type="radio" name="sexo" value="Mujer"> Mujer<BR>
                <INPUT type="submit" value="Enviar"> <INPUT type="reset">
                </P>
            </FORM>
        </body>
    </html>
    """
    return HttpResponse(documento)


def show(request, numero):
    num = numero
    documento = """
    <html>
        <head>
        </head>
        <body>
            <h1>Este es el Blog número %s</h1>
        </body>
    </html>
    """ % (num)
    return HttpResponse(documento)


def edit(request, numero):
    num = numero
    documento = """
    <html>
        <head>
        </head>
        <body>
            <h1>Editando el blog número %s</h1>
        </body>
    </html>
    """ % (num)
    return HttpResponse(documento)


def create(request):
    return redirect("/")


def destroy(request, numero):
    return redirect("/blogs")
