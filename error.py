class LargoExcedidoError(Exception):
    """
    Excepción personalizada que se lanza cuando el nombre de una campaña excede el límite de caracteres permitido.
    Hereda de la clase base Exception.
    """
    pass

class SubTipoInvalidoError(Exception):
    """
    Excepción personalizada que se lanza cuando el subtipo de un anuncio no es válido.
    Hereda de la clase base Exception.
    """
    pass
