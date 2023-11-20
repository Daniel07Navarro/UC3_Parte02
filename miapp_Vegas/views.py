from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
homehtml = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Examen UC3</title>
  </head>

  <style>
    * {
      margin: 0;
      padding: 0;
    }

    body,
    html {
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
    }

    .logo {
      padding-block: 2rem;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .logo img {
      width: 400px;
    }

    nav {
      background-color: #f5b335;
      border-bottom: 1px solid #e6e6e6;
    }

    li {
      text-decoration: none;
      list-style: none;
    }

    .nav-inner {
      margin-inline: 100px;
      display: flex;
      justify-content: center;
    }

    .nav-item {
      padding: 13px 15px;
      border-left: 1px solid white;
      border-right: 1px solid white;
      font-size: 1.5rem;
    }

    a {
      text-decoration: none;
      color: #313131;
    }

    main {
      flex: auto;
			margin: 0 auto;
    }

    footer {
      background-color: #333;
      padding-block: 40px;
      display: flex;
      justify-content: center;
      align-items: center;
      color: #e6e6e6;
      font-size: 1.3rem;
    }
  </style>

  <body>
    <header>
      <div class="logo">
        <img src="https://www.untels.edu.pe/images/logo.png" alt="untels logo" />
      </div>
      <nav>
        <ul class="nav-inner">
          <li class="nav-item"><a href="/inicio">Inicio</a></li>
          <li class="nav-item"><a href="/primos/10/15">Primos[a,b]</a></li>
          <li class="nav-item"><a href="/examen">Examen</a></li>
        </ul>
      </nav>
    </header>
    <main>
		
    
"""
footer = """
</main>
<footer>
      <div class="content">UNTELS - LP3 - Vegas Navarro Ramon - 20/11/2023</div>
    </footer>
  </body>
</html>
"""

lista = ['LP3','Dinamica de Sistemas','Ingeria de Requerimientos','Legislacion informatica'
,'Algoritmos de computacion grafica','Gestion de base de datos','Teoria general de sistemas']

def home(request):
	return HttpResponse(homehtml+footer)

def mostrar_cursos(request):
	# Crear una cadena HTML con la lista de materias
	materias_html = "<h2>Lista de Materias</h2><ul>"
	for materia in lista:
		materias_html += f"<li>{materia}</li>"
	materias_html += "</ul>"
	return HttpResponse(homehtml+materias_html+footer)