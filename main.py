
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import argparse

class EditorDeImagen:
    ''''Clase para editar imágenes utilizando la biblioteca PIL (Pillow).'''
    def __init__(self, ruta_imagen):
        '''Inicializa la clase con la ruta de la imagen a editar.'''
        self.imagen = Image.open(ruta_imagen)


editor = EditorDeImagen(r'C:\Users\Windows Microsoft\Desktop\trabajo py\Bart_Simpson_200px.png')
editor.imagen.show()