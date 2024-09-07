class Anuncio:
    def __init__(self,ancho,alto,url_archivo,url_clic,sub_tipo):
        self.ancho = self._validar_dim(ancho)
        self.alto = self._validar_dim(alto)
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo

        def _validar_dim(self,valor):
            return valor if valor > 0 else 1 
        
        @property
        def sub_tipo(self):
            return self._sub_tipo
        
        @sub_tipo.setter
        def sub_tipo(self,valor):
            if valor not in self.SUB_TIPOS:
                raise SubTipoInvalidoError(f"Subtipo {valor} no es valido.")
            self._sub_tipo = valor

        @staticmethod
        def mostrar_formatos():
            for formato in [Video,Display,Social]:
                print(f"FORMATO {formato.FORMATO}:")
                print("="*10)
                for subtipo in formato.SUB_TIPOS:
                    print(f"- {subtipo}")
                print("")

        def comprimit_anuncio(self):
            raise NotImplementedError("Este método debe ser implementado por subclases.")
        
        def redimensionar_anuncio(self):
            raise NotImplementedError("Este método debe ser implementado por subclases.")
        
class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream","outstream")

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo, duracion):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
        self.duracion = duracion

    def comprimir_anuncio(self):
        print(f"Compresión de video {self.sub_tipo}")

    def redimensionar_anuncio(self):
        print(f"Redimensionamiento de video {self.sub_tipo}")

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional","nativo")

    def comprimir_anuncio(self):
        print(f"Compresión de anuncio Social {self.sub_tipo}")

    def redimensionar_anuncio(self):
        print(f"Redimensionamiento de anuncio Social {self.sub_tipo}")
    
    