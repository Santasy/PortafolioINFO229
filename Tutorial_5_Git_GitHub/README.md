Para este tutorial, me centraré en describir mi uso aplicado y lo que encontré en la web, pues no pude asistir a la sesión de clases.

Para comenzar, un par de definiciones:
- **Git**: Es un sistema de control de versiones, libre y open source, creado por Linus Torvalds en 2005. Al ser un sistema distribuido, facilita el desarrollo remoto entre equipos de trabajos que no necesariamente trabajan en lo mismo, permitiendo un desarrollo en paralelo preparado para eventuales conflictos entre las modificaciones. Es el sistema de control de versiones más extendido en el mundo, por lo que se podría considerar como un estandar para el desarrollo de software. 
- **GitHub**: Es un servicio web de alojamiento (de proyectos o *repositorios*) desarrollado desde 2008, y comprado en 2018 por Microsoft. Permite la centralización del trabajo que se realiza con ayuda de Git, incorporando otras funcionalidades, dentro de la que se encuentran herramientas de analítica, gestión de permisos y licencias, aspectos sociales como seguir el trabajo de ciertas personas o proyectos, e inclusive "echar mano" a proyectos públicos, permitiendo incluso integrar el trabajo de terceros a proyectos inmensamente grandes, donde no necesariamente el autor conoce a los contribuidores.

Respecto a mi uso de ambas tecnologías, las he ocupado contínuamente durante el presente semestre en el desarrollo de nuestro proyecto en el ramo Taller de Ingeniería de Software. Realizamos integración contínua del proyecto, utilizando el software de Jenkins, que permite crear etapas de testeo y deploy que se sincronizan con el repositorio de GitHub. Logramos integrar nuestro proyecto completo con Docker-Compose, incluyendo la página web en React, un servidor de NodeJS para comunicación HTTP, y una base de datos postgres, todo habilitado en el servidor de la carrera.
- El repositorio [GitHub](https://github.com/Valrojo/merkit_code).
- La [página web](http://146.83.216.218:8007/) en el servidor de Informática.

Un compendio de los comandos Git, realizado con el apoyo de [Basic Git commands](https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html):

1. Para las etapas cruciales:

Comando|Descripción
---|---
`git init`|Inicia localmente un repositorio Git, creando un subdirectorio .git que llevará registro de los metadatos necesarios para el funcionamiento.
`git clone url`|Crea una copia del repositorio especificado a través de su url en GitHub. Por detrás, realiza un `git init`, y copia los respectivos archivos dentro. Si se reemplaza la url por una dirección local de archivos, también crea una copia.
`git add .`|Agrega a seguimiento todos los archivos dentro del repositorio. Se utiliza generalmente con ayuda del archivo `.gitignore`, para así evitar seguir archivos que no son útiles de compartir, como librerías instaladas o archivos caché. Se puede reemplazar el punto por algún o algunos archivos específicos.
`git commit -am "mensaje"`|Prepara todos los archivos trabajos para una entrega, que eventualmente puede ser subida al repositorio GitHub. La flag 'a' incluye los nuevos archivos añadidos con `git add`, y la flag 'm' permite entregar un mensaje relacionado al *commit*.
`git push <origin> <master>`|Envía finalmente un nuevo `commit` local al repositorio remoto en GitHub. `origin` y `master` pueden ser obviados, o reemplazados, siendo `origin` el destino, y `master` alguna rama del repositorio.
`git push --all origin`|Sube todas las ramas al repositorio remoto.

2. Para seguimiento de archivos y ramas:

Comando|Descripción
---|---
`git status`|Lista los archivos modificados, y los que no fueron incluídos por `add` o `commit`.
`git remote -v`|Lista los repositorios remotos configurados dentro del directorio de llamda.
`git remote add origin <server>`|Agrega un repositorio iniciado localmente al servidor especificado.
`git checkout -b <branch_name>`|Crea una nueva rama, y la selecciona como actual.
`git switch <branch_name>`|Selecciona la rama especificada como actual.
`git branch`|Lista las ramas disponibles, y muestra la actual.
`git branch -d <branch_name>`|Elimina la rama especificada.
`git push origin :<branch_name>`|Elimina la rama especificada del repositorio remoto.

3. Ajustes y cambios con el repositorio remoto:

Comando|Descripción
---|---
`git pull`|Descargar (fetch) y combinar (merge) cambios del repositorio remoto con el local.
`git merge <branch_name>`|Combinar la rama especificada con la actual.
`git diff`|Ver todos los conflictos de combinación
`git diff --base <filename>`|Ver los conflictos respecto al archivo base.
`git diff <source> <target>`|Ver los conflictos entre la rama source y la target (destino).
`git checkout -- <filename>`|Permite revertir cambios respecto a los últimos archivos confirmados con `git add`.
`git fetch origin && git reset --hard origin/master`|Revierte todos los cambios efectuados, y se alínea con los archivos del repositorio remoto.

4. Para `.gitignore`:

Comando|Descripción
---|---
`git rm -r --cached .`|Borra el caché de los archivos seguidos por `git add`, para actualizar el funcionamiento del archivo `.gitignore`. Para esto, debe ser seguido por `git add .`.