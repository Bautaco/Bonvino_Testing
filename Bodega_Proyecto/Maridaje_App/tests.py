from django.test import TestCase
from .models import Maridaje, Vino, Comida
from django.core.exceptions import ValidationError

# Clase de prueba para el modelo Vino
class VinoModelTest(TestCase):

    # Prueba que el campo 'nombre' no puede estar vacío
    def test_vino_nombre_vacio(self):
        vino = Vino(nombre='', añada=2020, region='Argentina')  # Crea una instancia de Vino con nombre vacío
        with self.assertRaises(ValidationError) as context:  # Espera que se lance un ValidationError
            vino.clean()  # Llama al método clean para validar
        # Verifica que el mensaje de error sea el esperado
        self.assertEqual(str(context.exception), '["El campo \\"nombre\\" no puede estar vacío."]')

    # Prueba que el campo 'region' no puede estar vacío
    def test_vino_region_vacio(self):
        vino = Vino(nombre='Malbec', añada=2020, region='')  # Crea una instancia de Vino con region vacío
        with self.assertRaises(ValidationError) as context:
            vino.clean()  # Llama al método clean
        # Verifica que el mensaje de error sea el esperado
        self.assertEqual(str(context.exception), '["El campo \\"region\\" no puede estar vacío."]')

    # Prueba que un vino válido no lance errores de validación
    def test_vino_correcto(self):
        vino = Vino(nombre='Malbec', añada=2020, region='Argentina')  # Crea una instancia válida
        try:
            vino.clean()  # Debe pasar sin errores
        except ValidationError:
            self.fail('ValidationError was raised unexpectedly!')  # Falla si se lanza un ValidationError

# Clase de prueba para el modelo Maridaje
class MaridajeModelTest(TestCase):
    
    # Método que se ejecuta antes de cada prueba para configurar el entorno
    def setUp(self):
        # Crea instancias de Vino y Comida para las pruebas
        self.vino = Vino.objects.create(
            nombre='Cabernet Sauvignon',
            añada=2020,
            region='Cafayate'
        )
        self.comida = Comida.objects.create(
            nombre='Queso Azul',
            descripcion='Queso fuerte y salado.'
        )
        # Crea una instancia de Maridaje utilizando los objetos creados
        self.maridaje = Maridaje.objects.create(
            nombre='Maridaje de Queso Azul y Cabernet',
            descripcion='Maridaje ideal para cenas.',
            vino=self.vino,
            comida=self.comida
        )

    # Prueba que el maridaje se crea correctamente
    def test_maridaje_creation(self):
        self.assertIsInstance(self.maridaje, Maridaje)  # Verifica que maridaje sea una instancia de Maridaje
        self.assertEqual(self.maridaje.nombre, 'Maridaje de Queso Azul y Cabernet')  # Verifica el nombre

    # Prueba que el método __str__ del modelo Maridaje funcione correctamente
    def test_maridaje_str_method(self):
        self.assertEqual(str(self.maridaje), 'Maridaje de Queso Azul y Cabernet')  # Verifica la representación en cadena
        
        
    # Prueba que las relaciones entre Maridaje, Vino y Comida se establezcan correctamente
    def test_maridaje_relationships(self):
        self.assertEqual(self.maridaje.vino.nombre, 'Cabernet Sauvignon')  # Verifica el vino relacionado
        self.assertEqual(self.maridaje.comida.nombre, 'Queso Azul')  # Verifica la comida relacionada
    
    
    # Prueba que el campo 'nombre' del maridaje no puede estar vacío
    def test_maridaje_nombre_vacio(self):
        maridaje = Maridaje(nombre='', descripcion='Maridaje ideal.', vino=self.vino, comida=self.comida)  # Crea una instancia con nombre vacío
        with self.assertRaises(ValidationError) as context:
            maridaje.clean()  # Llama al método clean
        # Verifica que el mensaje de error sea el esperado
        self.assertEqual(str(context.exception), '["El campo \\"nombre\\" no puede estar vacío."]')
    
    
    # Prueba que el campo 'descripcion' del maridaje no puede estar vacío
    def test_maridaje_descripcion_vacia(self):
        maridaje = Maridaje(nombre='Maridaje de Queso y Vino', descripcion='', vino=self.vino, comida=self.comida)  # Crea una instancia con descripcion vacía
        with self.assertRaises(ValidationError) as context:
            maridaje.clean()  # Llama al método clean
        # Verifica que el mensaje de error sea el esperado
        self.assertEqual(str(context.exception), '["El campo \\"descripcion\\" no puede estar vacío."]')
        