from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

class TextExtractor:
    def __init__(self, image_path):
        # Carrega e pré-processa a imagem
        image = Image.open(image_path).convert('L')
        image = ImageEnhance.Contrast(image).enhance(2.0)
        image = image.filter(ImageFilter.SHARPEN)

        # Extrai o texto japonês da imagem
        self.texto_extraido = pytesseract.image_to_string(image, lang='jpn')
        if self.texto_extraido == "":
            self.texto_extraido = pytesseract.image_to_string(image, lang='jpn', config="--psm 8")

        # Remove espaços e quebras de linha
        self.palavra = ''.join(c for c in self.texto_extraido if c not in [' ', '\n'])

    def imprimir_texto_extraido(self):
        print("Texto extraído (completo):")
        print(self.texto_extraido)
        print("Texto limpo (usado para busca):")
        print(self.palavra)
