# Gestor de Tareas — Proyecto Django Web App

Aplicación web desarrollada en Django que permite a los usuarios registrarse, autenticarse, y gestionar proyectos y tareas de forma segura y dinámica.

## Características

- Registro y autenticación de usuarios (`django.contrib.auth`)
- Gestión de proyectos y tareas asociados a cada usuario
- Formularios con validaciones (`ModelForm`)
- Templates con herencia (`base.html`)
- Sitio administrativo personalizado
- Restricciones de acceso mediante `LoginRequiredMixin`
- Protección CSRF en todos los formularios
- Pruebas unitarias para modelos y vistas
- Interfaz completamente en español, con diseño propio (paleta de azules)

## Requisitos previos

- Python 3.10 o superior
- pip

## Instalación

1. Clona este repositorio y entra a la carpeta del proyecto:
```bash
   git clone <url-del-repositorio>
   cd Django-WebApp
```

2. Crea y activa un entorno virtual:
```bash
   python3 -m venv venv
   source venv/bin/activate   # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```bash
   pip install django
```

4. Aplica las migraciones para crear la base de datos:
```bash
   python manage.py migrate
```

5. Crea un superusuario para acceder al panel administrativo:
```bash
   python manage.py createsuperuser
```

6. Levanta el servidor de desarrollo:
```bash
   python manage.py runserver
```

7. Abre tu navegador en `http://127.0.0.1:8000/`

## Uso

- **Registro**: `http://127.0.0.1:8000/registro/`
- **Inicio de sesión**: `http://127.0.0.1:8000/accounts/login/`
- **Mis proyectos**: `http://127.0.0.1:8000/` (requiere sesión iniciada)
- **Panel administrativo**: `http://127.0.0.1:8000/admin/` (requiere superusuario)

Una vez logeado, el usuario puede:
1. Crear un nuevo proyecto desde "Mis proyectos".
2. Entrar al detalle de un proyecto para agregarle tareas.
3. Editar o eliminar tanto proyectos como tareas.
4. Cerrar sesión desde el menú superior.

## Ejecutar las pruebas unitarias

```bash
python manage.py test tareas
```

## Estructura del proyecto

Django-WebApp/
├── config/ # Configuración global del proyecto (settings, urls)
├── tareas/ # App principal
│ ├── models.py # Modelos Proyecto y Tarea
│ ├── views.py # Vistas basadas en clases (CRUD)
│ ├── forms.py # ModelForms de Proyecto y Tarea
│ ├── urls.py # Rutas de la app
│ ├── admin.py # Registro y personalización del panel admin
│ ├── tests.py # Pruebas unitarias
│ └── templates/tareas/ # Templates propios de la app
├── templates/ # Templates globales (base.html, registration/)
├── manage.py
└── requirements.txt (opcional)


## Modelo de datos

- **Usuario** (`django.contrib.auth.models.User`): usuario del sistema.
- **Proyecto**: pertenece a un usuario (`ForeignKey`). Atributos: nombre, descripción, fecha de creación.
- **Tarea**: pertenece a un proyecto (`ForeignKey`). Atributos: título, descripción, estado (pendiente/en progreso/completada), fecha límite.

## Retos enfrentados durante el desarrollo

- Configuración correcta de la carpeta `templates/` a nivel de proyecto vs. a nivel de app (`app/templates/app/`), necesaria para que Django encuentre las plantillas de `registration/` y de `tareas/` por separado.
- Implementación de restricciones de acceso a nivel de consulta (`get_queryset` filtrando por `usuario`), para evitar que un usuario autenticado pueda ver o modificar datos de otro usuario cambiando el ID en la URL.
- Redirecciones post-login/logout configuradas en `settings.py` (`LOGIN_REDIRECT_URL`, `LOGOUT_REDIRECT_URL`, `LOGIN_URL`).
- Localización de la interfaz al español mediante `LANGUAGE_CODE = 'es'` en `settings.py`.

## Autor

Proyecto desarrollado como evaluación del Módulo 6 — Django, Desarrollo Web con Python (bootcamp de programación).
