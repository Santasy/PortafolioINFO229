// Es importante notar que es necesario que un
// archivo de testeo termine como "_test.go".

package greetings

import (
	"testing"
	"regexp"
)

// > Ambas funciones utilizan un puntero
//   al paquete testing.T, que se ocupa para reportar
//   y realizar logs desde el test.

// Prueba Hello() con un nombre.
func TestHelloName(t *testing.T) {
	name := "Sebastian"
	// Ejemplo de uso de expresiones regulares.
	want := regexp.MustCompile(`\b` + name + `\b`)
	mssg, err := Hello(name)
	if !want.MatchString(mssg) || err != nil {
		t.Fatalf(`Hello("%v") =\n(%q, %v) debe coincidir (%q, nil)`,
			name, mssg, err, want)
	}
}

// Prueba Hello() sin argumento.
func TestHelloEmpty(t *testing.T) {
	mssg, err := Hello("")
	if mssg != "" || err == nil {
		t.Fatalf(`Hello("") =\n(%q, %v) debe coincidir ("", error)`, 
			mssg, err)
	}
}