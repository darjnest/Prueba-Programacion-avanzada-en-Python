from datetime import date
from anuncio import Video, Display, Social
from error import LargoExcedidoError

class Campaña:
    def __init__(self, nombre, fecha_inicio, fecha_termino, anuncios):
        """
        Constructor de la clase Campaña.
        Inicializa los atributos de la campaña como nombre, fechas de inicio y término, y los anuncios asociados.
        Valida que el nombre de la campaña no exceda los 250 caracteres.
        
        :param nombre: Nombre de la campaña publicitaria.
        :param fecha_inicio: Fecha de inicio de la campaña.
        :param fecha_termino: Fecha de término de la campaña.
        :param anuncios: Lista de anuncios a incluir en la campaña, cada uno con su tipo y detalles.
        :raises LargoExcedidoError: Si el nombre de la campaña excede los 250 caracteres.
        """
        if len(nombre) > 250:
            raise LargoExcedidoError("El nombre de la campaña no puede exceder los 250 caracteres.")
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self._anuncios = self._crear_anuncios(anuncios)  

    def _crear_anuncios(self, anuncios):
        """
        Método privado para crear la lista de anuncios de la campaña.
        Dependiendo del tipo de anuncio, crea instancias de Video, Display o Social.

        :param anuncios: Lista de diccionarios que contienen los datos de los anuncios.
        :return: Lista de objetos de las clases Video, Display o Social.
        """
        lista_anuncios = []
        for anuncio in anuncios:
            tipo = anuncio['tipo']
            if tipo == "Video":
                lista_anuncios.append(Video(
                    anuncio['ancho'], 
                    anuncio['alto'], 
                    anuncio['url_archivo'], 
                    anuncio['url_clic'], 
                    anuncio['sub_tipo'], 
                    anuncio['duracion']
                ))
            elif tipo == "Display":
                lista_anuncios.append(Display(
                    anuncio['ancho'], 
                    anuncio['alto'], 
                    anuncio['url_archivo'], 
                    anuncio['url_clic'], 
                    anuncio['sub_tipo']
                ))
            elif tipo == "Social":
                lista_anuncios.append(Social(
                    anuncio['ancho'], 
                    anuncio['alto'], 
                    anuncio['url_archivo'], 
                    anuncio['url_clic'], 
                    anuncio['sub_tipo']
                ))
        return lista_anuncios

    @property
    def anuncios(self):
        """
        Getter para obtener la lista de anuncios de la campaña.
        
        :return: Lista de anuncios de la campaña.
        """
        return self._anuncios

    def __str__(self):
        """
        Método especial que devuelve una representación en cadena de la campaña, mostrando los detalles
        de la campaña y la cantidad de anuncios de cada tipo (Video, Display, Social).
        
        :return: Una cadena que describe la campaña.
        """
        tipos = {"Video": 0, "Display": 0, "Social": 0}
        for anuncio in self._anuncios:
            tipos[type(anuncio).__name__] += 1  

        return (f"Nombre de la campaña: {self.nombre}\n"
                f"Fecha inicio: {self.fecha_inicio}\n"
                f"Fecha término: {self.fecha_termino}\n"
                f"Anuncios: {tipos['Video']} Video, {tipos['Display']} Display, {tipos['Social']} Social")
