PrimeReact es un framework de front-end adaptado para React, pues se origina de PrimeFaces, existiendo también compatibilidad con Angular, Vue y JavaServer Faces. Tiene similitudes con Bootstrap, e incluso plantillas css que se basan en él. Es bastante cómodo de utilizar, y me pareció mucho más confiable que Bootstrap, el cual bajo ciertas circunstancias no funciona muy bien.

En el presente ejemplo de integración ocuparé el administrador de paquetes `yarn`. Primero es necesario crear el proyecto react:
> `yarn create react-app tutorial_app`

Luego, es necesario agregar las librerías a utilizar:
> `yarn add primereact --save`: Librería base.<br>
> `yarn add primeicons --save`: Libería de íconos.<br>
> `yarn add primeflex --save`: Librería de componentes básicos,como sistemas de grilla, flexboxs, espaciadores, elevadores, entre otros.<br>
> `yarn add react-transition group`: Libería para manejar animaciones.

La implementación se puede revisar dentro de `src/components/FieldsetEjemplo`, donde primero se importan los css:
> `import 'primeflex/primeflex.css';`<br>
> `import 'primereact/resources/primereact.min.css';`<br>
> `import 'primereact/resources/themes/saga-blue/theme.css';`<br>
> `import 'primeicons/primeicons.css';`

Para utilizar los componentes, se deben importar de la forma:
> `import { Componente } from "primereact/componente";`

Los comentarios de la implementación se encuentran en el archivo mencionado, pero en general:
1. Realicé un ejemplo de "group-box" llamado `Fieldset` que enmarca una serie de componentes, que en este caso son `Acordeons`.
2. En el primer ejemplo, se muestra un uso de íconos con una animación giratoria.
3. El el segundo, se observa un botón y una barra de progreso. Al presionar el botón, comienza un temporizador que avanza la barra, la cual al llegar al 100% despliega un mensaje a través de un componente tipo `Toast`.

Para probar la aplicación, se utiliza:
> `yarn install`: Instala las librerías especificadas por package.json, y las versiones de yarn.lock.<br>
> `yarn start`: Que activa un servidor local con la página web.

No quise ahondar mucho en el uso de React, pues ya lo he ocupado con anterioridad, incluyendo este semestre, por lo que me centré en utilizar componentes de PrimeReact.