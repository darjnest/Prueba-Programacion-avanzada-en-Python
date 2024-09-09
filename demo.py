from campania import Campaña
from anuncio import Video
from error import LargoExcedidoError, SubTipoInvalidoError
from datetime import date

from datetime import date

def main():
    """
    Función principal para ejecutar la creación y modificación de una campaña publicitaria.
    Maneja la creación de una campaña con un anuncio de tipo Video, la modificación del nombre
    de la campaña y el subtipo del primer anuncio. También maneja las excepciones relacionadas
    con errores de longitud y tipos de subtipo inválidos, registrando estos errores en un archivo de log.
    """
    try:
        anuncios = [{'tipo': 'Video', 'ancho': 1920, 'alto': 1080, 'url_archivo': 'video.mp4', 'url_clic': 'http://video.com', 'sub_tipo': 'instream', 'duracion': 30}]
        campaña = Campaña("Campaña de Ejemplo", date(2024, 1, 1), date(2024, 12, 31), anuncios)

        nuevo_nombre = input("Ingrese nuevo nombre para la campaña: ")
        nuevo_sub_tipo = input("Ingrese nuevo subtipo para el anuncio: ")

        campaña.nombre = nuevo_nombre

        campaña.anuncios[0].sub_tipo = nuevo_sub_tipo

    except (LargoExcedidoError, SubTipoInvalidoError) as e:
        """
        Manejar excepciones de largo de nombre excedido y subtipo inválido.
        Registra los errores en un archivo de log llamado 'error.log'.
        
        :param e: Excepción capturada que contiene el mensaje de error.
        """
        with open('error.log', 'a') as f:
            f.write(f"Error: {str(e)}\n")
        print("Ha ocurrido un error, verifique el archivo error.log.")

if __name__ == "__main__":
    main()

  
