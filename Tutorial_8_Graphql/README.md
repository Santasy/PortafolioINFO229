GraphQL es un Query Language que permite utilizar los protocolos HTTP de una forma más flexible, superando los aspectos toscos de utilizar APIs REST, que generalmente necesitan hacer 2 o más llamadas al servidor para conseguir información específica de la base de datos. Utiliza llamados con una estructura similar a objetos json, y es fuertemente tipada, por lo que es bastante consistente y robusta en aspectos de seguridad.

Para la implementación de este tutorial, seguí el tutorial [Learn GraphQL In 40 minutes](https://www.youtube.com/watch?v=ZQL7tL2S0oQ), trabajando con un proyecto que consiste en datos de libros y sus autores.

- `simpledata.js` guarda la información a utilizar, y
- `server.js` guarda la lógica de una aplicación express que recibe mensajes HTTP en la ruta `localhost:5000/graphql`.

Para probar el programa, se debe ejecutar el comando `npm run devStart`, y dirigirse a la ruta ya nombrada. Ahí se una interfaz gráfica nativa `GraphiQL`, que permite realizar las interacciones.

Para el funcionamiento, es necesario aclarar la existencia de dos funcionalidades principales de GraphQL:
- `query`: Que trabaja la lógica de mensajes tipo `GET`, permitiendo obtener solo la información requerida, sin nada que sobre, permitiendo, con el diseño correcto, obtener lo necesario en solo un mensaje. Este será por defecto el comando entregado a un mensaje de GraphQL.
- `mutation`: Que trabaja con la lógica de los mensajes tipo `POST`, permitiendo crear una información para la aplicación. En este caso, esto funciona efectivamente, pero no hay persistencia de los datos al reiniciar el servidor, dado que la data es declarada como una constante en el archivo ya descrito. Debe ser especificado explícitamente en el mensaje.

Un ejemplo de `query` es:
```
query{
  book{
    name,
    author
  }
}
```
Donde `author` es un atributo que es parte de una query compuesta, pues book solo tiene el atributo `authorId`, pero este se busca en la lista de autores, comparando el id.

Un ejemplo de `mutation` para crear un autor:
```
mutation{
  addAuthor(name: "Albert Camus"){
    id
  }
}
```
Donde `name` es un argumento entregado para la creación, e `id` es un retorno del campo del nuevo autor creado.

Un ejemplo de `query` para crear un libro:
```
mutation{
  addBook(name: "La Peste", authorId: 4){
    id,
    name,
    author{
      name
    }
  }
}
```
Donde se entregan dos argumentos, y como retorno, entre otras cosas, se requiere la query compuesta `author`.