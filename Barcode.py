# módulo de código de barras
from barcode import EAN13
# ImageWriter-> para generar un archivo de imagen
from barcode.writer import ImageWriter


class Barcode():
    def __init__(self,number,filename):
        self.number =  number
        self.filename = filename
        
    def Generate_bar(self):
        # creemos un objeto de clase EAN13 y pasar el número 
        # con ImageWriter() para escribir en la imagen
        self.code_bar = EAN13(self.number, writer=ImageWriter())
        # Guardamos nuesto archivo imagen.
        self.code_bar.save(self.filename)

if __name__ == '__main__':
    # Asegúrate de pasar el número como cadena
    number = '511031461613'
    filename = 'My_bar_code'
    codebar = Barcode(number=number, filename=filename)
    codebar.Generate_bar()
     
        
    
        
        
            
        
          
        

