from django.test import TestCase
from .models import Maridaje, Vino, Comida
from django.core.exceptions import ValidationError

# Clase de prueba para el modelo Vino
class IntegrationTest(TestCase):

    def setUp(self):

        # Configuracion inicial para las pruebas
        self.vino = Vino.objects.create(
            nombre='Cabernet Sauvignon',
            bodega='Sapo de Otro Pozo',
            varietal='Chardonay',
            region='Cafayate'
        )
        self.comida = Comida.objects.create(
            nombre='Queso Azul',
            descripcion='Queso fuerte y salado.'
        )

        # Prueba de cracion de vino y comida
        def test_creacion_vino(self):
            vino = Vino.objects.get(nombre='Cabernet Sauvignon')
            self.assertEqual(vino.bodega, 'Sapo de Otro Pozo')
            self.assertEqual(vino.varietal, 'Chardonay')
            self.assertEqual(vino.region, 'Cafayate')

        def test_creacion_comida(self):
            comida = Comida.objects.get(nombre='Queso Azul')
            self.assertEqual(comida.descripcion, 'Queso fuerte y salado.')

        # Crea una instancia de Maridaje utilizando los objetos creados
        def test_creacion_maridaje(self):    
            maridaje = Maridaje.objects.create(
                nombre='Maridaje de Queso Azul y Cabernet',
                descripcion='Maridaje ideal para cenas.',
                vino=self.vino,
                comida=self.comida
            )
            self.assertEqual(maridaje.vino.nombre, 'Cabernet')
            self.assertEqual(maridaje.comida.nombre, 'Queso Azul')

        # Validacion maridaje nombre vacio
        def test_vlidacion_maridaje_nombre_vacio(self):
            with self.assertRaises(ValidationError) as context:
                maridaje = Maridaje(
                    nombre='', 
                    descripcion='Descripcion valida',
                    vino=self.vino,
                    comida=self.comida
                )
                maridaje.clean() # Lanza ValidationError si el nombre está vacío

            self.assertEqual(str(context.exception), '["El campo \\"nombre\\"no puede estar vacio."]')
