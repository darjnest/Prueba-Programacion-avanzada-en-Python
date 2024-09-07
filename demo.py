from campania import Campaña
from anuncio import Video
from error import LargoExcedidoError, SubTipoInvalidoError
from datetime import date

def main():
    try: 
        #Crear campaña con un anuncion de tipo video
        anuncios = [{'tipo': 'Video', 'ancho': 1920, 'alto': 1080, 'url_archivo': 'video.mp4', 'url_clic': 'http://video.com', 'sub_tipo': 'instream', 'duracion': 30}]
        campaña = Campaña("Campaña de Ejemplo", date(2024, 1, 1), date(2024, 12, 31), anuncios)

        #Solicitar nuevo nombre y subtipo
        nuevo_nombre = input("Ingrese nuevo nombre para la campaña: ")
        nuevo_sub_tipo= input("Ingrese nuevo subtipo para el anuncio: ")

        #Modificar el nombre de la campaña
        campaña.nombre = nuevo_nombre

        #Modificar subtipo del primer anuncio
        campaña.anuncios[0].sub_tipo = nuevo_sub_tipo

    except(LargoExcedidoError, SubTipoInvalidoError) as e:
        with open('error.log','a') as f:
            f.write(f"Error: {str(e)}\n")
        print("Ha ocurrido un error, verifique el archivo error.log.")

if __name__ == "__main__":
    main()
  
