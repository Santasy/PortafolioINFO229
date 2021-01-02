Los archivos de este directorio son:

**Dockerfile** : Archivo que inicia una imagen tipo nestor. Los tokens utilizados han sido anonimizados. \
**requirements.txt** : Archivo texto que lista las librerías python ocupadas. \
**nestorbot.py** : Clase NestorBot. \
**nestorbot_app.py** : \
	- Programa ejecutado por docker, que lista los canales leídos por Nestor, y saluda en #playground. \
***

Para ingresar elementos a mongo ocupé:
```
1. docker exec -it nestor_mongo bash
1. mongo
1. use nestor
1. nestor.frases.insertOne( { text: "Primera frase de mongo" } )
```