from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),

    # Proyectos
    path('', views.ListaProyectos.as_view(), name='lista_proyectos'),
    path('proyecto/nuevo/', views.CrearProyecto.as_view(), name='crear_proyecto'),
    path('proyecto/<int:pk>/', views.DetalleProyecto.as_view(), name='detalle_proyecto'),
    path('proyecto/<int:pk>/editar/', views.EditarProyecto.as_view(), name='editar_proyecto'),
    path('proyecto/<int:pk>/eliminar/', views.EliminarProyecto.as_view(), name='eliminar_proyecto'),

    # Tareas (anidadas dentro de un proyecto)
    path('proyecto/<int:proyecto_id>/tarea/nueva/', views.CrearTarea.as_view(), name='crear_tarea'),
    path('tarea/<int:pk>/editar/', views.EditarTarea.as_view(), name='editar_tarea'),
    path('tarea/<int:pk>/eliminar/', views.EliminarTarea.as_view(), name='eliminar_tarea'),
]