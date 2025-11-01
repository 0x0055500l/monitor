# Examen — Monitoreo del Sistema con Django y psutil 

Información del grupo: 
- Nombre(s): Josseth Bautista, Oscar Hernández
- Número(s) de cuenta: 201810020200, 200711120001

Descripción
Este proyecto implementa una aplicación Django llamada `monitor` con una app interna `sistema` que muestra en tiempo real métricas del sistema usando la librería `psutil`. La interfaz permite actualización manual (botón) y automática (JavaScript, configurada por defecto a 5s).

Contenido
- manage.py
- monitor/ (proyecto Django)
- sistema/ (app Django)
  - templates/sistema/index.html
- requirements.txt
- GROUP.txt `(archivo con identificación del grupo)`

> [!IMPORTANT]
> Requisitos
> - Linux (probado en Ubuntu/Debian)
> - Windows (probado en Windows 11 Pro/Home)
> - Python 3.11+ y virtualenv

Instalación y ejecución (local, sin Docker)
1. Clonar el repositorio o descargar los archivos.
2. Crear entorno virtual: </br>
   ``python3 -m venv venv`` </br>
   ``source venv/bin/activate`` o con Powershell usando ``.\venv\Scripts\Activate.ps1``
3. Instalar dependencias: </br>
   ``pip install -r requirements.txt``
4. Migraciones y ejecución: </br>
   ``python manage.py migrate`` </br>
   ``python manage.py runserver 0.0.0.0:8000``
5. Abrir en el navegador: http://localhost:8000/

> [!NOTE]
> Notas :
> - Si tiene fallos al instalar el psutil