from datetime import date
from anuncio import Video, Display, Social
from error import LargoExcedidoError

class Campaña:
    def __init__(self, nombre, fecha_inicio, fecha_termino, anuncios):
        if len(nombre) > 250:
            raise LargoExcedidoError("El nombre de la campaña no puede exceder los 250 caracteres.")
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self._anuncios = self._crear_anuncios(anuncios)

    def _crear_anuncios(self, anuncios):
        lista_anuncios = []
        for anuncio in anuncios:
            tipo = anuncio['tipo']
            if tipo == "Video":
                lista_anuncios.append(Video(anuncio['ancho'], anuncio['alto'], anuncio['url_archivo'], anuncio['url_clic'], anuncio['sub_tipo'], anuncio['duracion']))
            elif tipo == "Display":
                lista_anuncios.append(Display(anuncio['ancho'], anuncio['alto'], anuncio['url_archivo'], anuncio['url_clic'], anuncio['sub_tipo']))
            elif tipo == "Social":
                lista_anuncios.append(Social(anuncio['ancho'], anuncio['alto'], anuncio['url_archivo'], anuncio['url_clic'], anuncio['sub_tipo']))
        return lista_anuncios

    @property
    def anuncios(self):
        return self._anuncios

    def __str__(self):
        tipos = {"Video": 0, "Display": 0, "Social": 0}
        for anuncio in self._anuncios:
            tipos[type(anuncio).__name__] += 1
        return (f"Nombre de la campaña: {self.nombre}\n"
                f"Fecha inicio: {self.fecha_inicio}\n"
                f"Fecha término: {self.fecha_termino}\n"
                f"Anuncios: {tipos['Video']} Video, {tipos['Display']} Display, {tipos['Social']} Social")