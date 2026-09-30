from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Proyecto, Tarea


class ProyectoModelTest(TestCase):
    def setUp(self):
        # Se ejecuta antes de cada prueba: crea datos base
        self.usuario = User.objects.create_user(username='testuser', password='ClaveSegura123')
        self.proyecto = Proyecto.objects.create(nombre='Proyecto de prueba', usuario=self.usuario)

    def test_str_devuelve_nombre(self):
        # El __str__ del modelo debe devolver el nombre del proyecto
        self.assertEqual(str(self.proyecto), 'Proyecto de prueba')

    def test_proyecto_asociado_al_usuario_correcto(self):
        self.assertEqual(self.proyecto.usuario, self.usuario)


class TareaModelTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='testuser2', password='ClaveSegura123')
        self.proyecto = Proyecto.objects.create(nombre='Proyecto con tareas', usuario=self.usuario)
        self.tarea = Tarea.objects.create(titulo='Tarea de prueba', proyecto=self.proyecto)

    def test_estado_por_defecto_es_pendiente(self):
        # Si no se especifica, el estado debe quedar en 'pendiente' por el default del modelo
        self.assertEqual(self.tarea.estado, 'pendiente')

    def test_str_devuelve_titulo(self):
        self.assertEqual(str(self.tarea), 'Tarea de prueba')


class VistasAccesoTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='testuser3', password='ClaveSegura123')

    def test_lista_proyectos_redirige_si_no_hay_sesion(self):
        # Un usuario NO logeado debe ser redirigido al login (LoginRequiredMixin)
        response = self.client.get(reverse('lista_proyectos'))
        self.assertEqual(response.status_code, 302)  # 302 = redirección
        self.assertIn('/accounts/login/', response.url)

    def test_lista_proyectos_accesible_con_sesion(self):
        # Con sesión iniciada, la vista debe responder 200 (OK)
        self.client.login(username='testuser3', password='ClaveSegura123')
        response = self.client.get(reverse('lista_proyectos'))
        self.assertEqual(response.status_code, 200)

    def test_usuario_no_ve_proyectos_de_otro(self):
        # Un usuario no debe poder ver el detalle de un proyecto que no le pertenece
        otro_usuario = User.objects.create_user(username='otro', password='ClaveSegura123')
        proyecto_ajeno = Proyecto.objects.create(nombre='No es mío', usuario=otro_usuario)

        self.client.login(username='testuser3', password='ClaveSegura123')
        response = self.client.get(reverse('detalle_proyecto', kwargs={'pk': proyecto_ajeno.pk}))
        self.assertEqual(response.status_code, 404)  # no existe "para él"