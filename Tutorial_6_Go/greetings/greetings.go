package greetings

import(
	"errors"
	"fmt" // I/O
	"math/rand"
	"time" // para crear una semilla random
)

// Funcion que saluda a una persona
// > Los tipos de los argumentos se declaran a su derecha
// > El tipo de return se declara a la derecha de los argumentos
// > Que comience con mayus permite su exportacion
func Hello(name string) (string, error) {
	// Retorna un mensaje que integra la variable name

	// Si no hay nombre, retorna error
	if name == "" {
		return "", errors.New("falta nombre")
	}
	
	// > El operador := declara e inicializa una variable,
	//   determinan su tipo segun lo de la derecha
	// > Sino, debiese haberse escrito:
	//     var message string
	//     message = fmt(...)
	message := fmt.Sprintf(randomFormat(), name)
	// se entendera que nil significa que no hay erores
	return message, nil
}

// Funcion que saluda a una lista de personas,
// y retorna un mapa que asociada cada nombre con su saludo.
func Hellos(names []string) (map[string]string, error) {
	// Esta es la sintax para declarar un map,
	// de la forma [key_type]value_type.
	mssgs := make(map[string]string)

	// Itera cada nombre ingresado.
	// > Se ocupa un "blank identifier", "_",
	//   que ignora el indice de iteracion.
	for _, name := range names {
		mssg, err := Hello(name)
		if err != nil {
			return nil, err
		}
		mssgs[name] = mssg
	}
	return mssgs, nil
}

// -- Mensaje Random --

// Go siempre ejecuta las funciones init luego de haber
// declarado variables globales.
func init() {
	rand.Seed(time.Now().UnixNano())
}

// Funcion que retona aleatoriamente un formato
// dentro de la lista formats.
// > Notar que comienza con minuscula, por lo que
//   su acceso solo se permite dentro del paquete.
func randomFormat() string {
	// Esta estructura se conoce como "slice",
	// y funciona como un arreglo dinamico,
	// donde no se define su tamaño dentro de los "[]".
	formats := []string{
		"Hola %v!",
		"Saludando a %v",
		"Holachao %v",
	}

	// Un uso de indices y numeros random
	return formats[rand.Intn(len(formats))]
}