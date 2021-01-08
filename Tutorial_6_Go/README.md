Go (o Golang) es un lenguaje de programación con robustos enfoques de concurrencia y testeo unitario, desarrollado por Google desde 2008.

Definiciones útiles:
- **Módulos**: Conjunto de funciones con integración (opcional) de otros módulos, que permite su utilización en otros códigos.
- **Paquetes**: Corresponde a agrupaciones de módulos, que además define las versiones y contextos que permiten su integración en códigos más complejos.

`go mod init <nombre>`: Similar a un archito tipo package-log, con este comando Go crea un archivo `go.mod` que lista las dependencias necesarias para el módulo especificado.

> Dentro de `go.mod`, normalmente habrán directivas del tipo `require <url_modulo> <version>`, que especifican las urls de los módulos publicados (en la web), y su versión integrada en el proyecto.<br>
> También, se puede usar la directiva `replace <url_modulo> => <dir_path>`, que permite trabajar con módulos aún no publicados, cambiando el lugar de búsqueda a un directorio local.

`go build`: Compila el programa con los paquetes importados, y recalcula las versiones necesitadas por el archivo `go.mod`. Esto crea un ejecutable a ser utilizado de la forma `./programa`.

Dentro de un código, se pueden definir paquetes con `package <nombre>`, donde siempre un módulo que ejecuta debe llamarse `main`.

`go test`: Utiliza los archivos `_test.go` que hayan sido desarrollados, para realizar pruebas unitarias. Se le puede agregar la flag `-v` para ver más información de la ejecución.

`go list -f '{{.Target}}'`: Muestra el directorio donde se instalará a trabajar dentro del directorio.
---

#### Respecto al ejemplo
Utilicé la serie de tutoriales que comienzan con [crear un módulo](https://golang.org/doc/tutorial/create-module). En particular, trabajé:
- Crear un módulo, en este caso nombrado "example.com/greetings".
- Llamar a un módulo desde otro, donde en este caso, la url "example.com/greetings" fue redirigida a una directorio local.
- Retornar y manejar errores.
- Uso de random.
- Crear un test unitario, donde .
- Compilar e instalar la aplicación.

Todo directorio es parte del mismo proyecto, y se invita a revisar los comentarios dentro del código para una mejor comprensión de lo desarrollado y del lenguaje.

Para una expansión de conocimientos en temas que no revisé, tengo pendiente la web [Un tour de Go](https://tour.golang.org/list), pero que por temas de tiempo no pude revisar.