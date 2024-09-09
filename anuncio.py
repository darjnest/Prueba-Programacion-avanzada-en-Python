from error import SubTipoInvalidoError


class Anuncio:
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        """
        Constructor de la clase Anuncio.
        Inicializa las dimensiones, las URLs y el subtipo del anuncio.
        Valida que las dimensiones sean correctas y que el subtipo sea válido.

        :param ancho: Ancho del anuncio.
        :param alto: Alto del anuncio.
        :param url_archivo: URL del archivo del anuncio (imagen/video).
        :param url_clic: URL donde se redirige cuando se hace clic en el anuncio.
        :param sub_tipo: Subtipo del anuncio (definido por las clases derivadas).
        """
        self.ancho = self._validar_dimension(ancho)
        self.alto = self._validar_dimension(alto)
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo

    def _validar_dimension(self, valor):
        """
        Valida que el valor de la dimensión sea mayor que 0. Si no lo es, lo establece en 1.
        
        :param valor: El valor de la dimensión (ancho o alto).
        :return: El valor validado de la dimensión.
        """
        return valor if valor > 0 else 1

    @property
    def sub_tipo(self):
        """
        Getter para el subtipo del anuncio.
        :return: El subtipo actual del anuncio.
        """
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, valor):
        """
        Setter para el subtipo del anuncio. Valida que el subtipo esté dentro de los permitidos.
        
        :param valor: El subtipo que se quiere establecer.
        :raises SubTipoInvalidoError: Si el subtipo no es válido para el tipo de anuncio.
        """
        if valor not in self.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Subtipo {valor} no es válido.")
        self._sub_tipo = valor

    @staticmethod
    def mostrar_formatos():
        """
        Método estático que muestra los formatos y subtipos permitidos para cada tipo de anuncio.
        """
        for formato in [Video, Display, Social]:
            print(f"FORMATO {formato.FORMATO}:")
            print("="*10)
            for subtipo in formato.SUB_TIPOS:
                print(f"- {subtipo}")
            print("")

    def comprimir_anuncio(self):
        """
        Método abstracto para la compresión del anuncio.
        Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Este método debe ser implementado por subclases.")

    def redimensionar_anuncio(self):
        """
        Método abstracto para la redimensión del anuncio.
        Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Este método debe ser implementado por subclases.")


class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo, duracion):
        """
        Constructor de la clase Video. Inicializa el anuncio de tipo video con una duración.
        
        :param ancho: Ancho del anuncio de video.
        :param alto: Alto del anuncio de video.
        :param url_archivo: URL del archivo de video.
        :param url_clic: URL donde se redirige cuando se hace clic en el video.
        :param sub_tipo: Subtipo del video (instream, outstream).
        :param duracion: Duración del video.
        """
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
        self.duracion = duracion

    def comprimir_anuncio(self):
        """
        Método para comprimir el video. Imprime un mensaje indicando que se ha comprimido el video.
        """
        print(f"Compresión de video {self.sub_tipo}")

    def redimensionar_anuncio(self):
        """
        Método para redimensionar el video. Imprime un mensaje indicando que se ha redimensionado el video.
        """
        print(f"Redimensionamiento de video {self.sub_tipo}")


class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio(self):
        """
        Método para comprimir el anuncio de tipo Display.
        Imprime un mensaje indicando que se ha comprimido el anuncio de Display.
        """
        print(f"Compresión de anuncio Display {self.sub_tipo}")

    def redimensionar_anuncio(self):
        """
        Método para redimensionar el anuncio de tipo Display.
        Imprime un mensaje indicando que se ha redimensionado el anuncio de Display.
        """
        print(f"Redimensionamiento de anuncio Display {self.sub_tipo}")


class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self):
        """
        Método para comprimir el anuncio de tipo Social.
        Imprime un mensaje indicando que se ha comprimido el anuncio de Social.
        """
        print(f"Compresión de anuncio Social {self.sub_tipo}")

    def redimensionar_anuncio(self):
        """
        Método para redimensionar el anuncio de tipo Social.
        Imprime un mensaje indicando que se ha redimensionado el anuncio de Social.
        """
        print(f"Redimensionamiento de anuncio Social {self.sub_tipo}")
