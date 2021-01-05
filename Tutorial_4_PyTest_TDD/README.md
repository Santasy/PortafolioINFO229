#### Respecto a los ejercicios
Los que realicé, los hice trabajando con TDD pero sin refactoring (reconociendo que son mejorables).\
En el caso de Trading Cards, no encontraba difícil la implementación, pero creo que era bastante extenso (pues habría que determinar criterios para las jugadas, considerando que serían automáticas, además de varias condiciones para el avance), por lo que por temas de tiempo decidí no implementarlo.

---

#### Respecto a la tarea
No supe bien como plantear tests que incluyeran RabbitMQ, probando si es que los mensajes llegaron a sus colas o no, o también revisar desde slack si es que hay resultados, pues esto volvería dependiente algunos componentes de otros.\
Sin embargo, planteo lo siguiente, pero sin desarrollar, pues sería implementar cosas parecidas a las trabajadas en los ejercicios:
- Para el reader, encapsular la función que testea si el mensaje contiene o no "[wikipedia] o [traducir]", con su retorno adecuado (algo como [] si no es válido, o ["wikipedia", "busqueda"]).
- Para los consumers wikipedia y traducir, guardaría una query de ejemplo, a ser imitada en ejecución. Esto sería un archivo de texto con los objetos json correspondientes, comparado con lo conseguido de las APIs.
- Para el writer realizaría algo similar, teniendo una "salida" de ejemplo, con el objeto json que representa un mensaje Slack (block, text, etc.).
