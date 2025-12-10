EntregaFinal_API
API => ( APPLICATION PROGRAMMING INTERFACE)

Se realizaran pruebas para las siguientes perticiones:
    GET => obetner datos
    POST => envio de datos => creacion de datos / login
    PUT => edicion de datos totales => todos
    PATCH => edicion de datos parciales => username
    DELETE => eliminar datos

Se requiere las siguientes instalaciones:
    pip install requests 
    pip install pytest-check
    pip install faker

Se deja como referencia las posibles respuestas que pueden devolver las peticiones: 
    1xx=> informacion
    2xx => exito
      201 => creacion
      204 => No Content puede no tener Content-Type 
    3xx => comunicacion / redireccion
    4xx => casos de error de cliente => frontend interface
    5xx=> sever falla => errores de srevidor
