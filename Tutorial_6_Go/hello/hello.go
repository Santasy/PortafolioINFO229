package main

// Cuando son varios los imports, se pueden encapsular en una
// sola llamada al comando import.
import(
	"fmt"
	"log"
	"example.com/greetings"
)

func main() {
	// Se establecen propiedades el Logger por defecto,
	// incluyendo un prefijo, y una flag que deshabilita
	// que se imprima la hora, archivo fuente y n° de linea.
	log.SetPrefix("greetrings: ")
	log.SetFlags(0)

	// -- Funcion individual --
	// El operador := declara e inicializa una variable.
	mssg, err := greetings.Hello("Sebastian")
	if err != nil {
		// Fatal ademas de escribir el error,
		// termina el programa.
		log.Fatal(err)
	}
	fmt.Println(mssg)

	// -- Funcion grupal --
	names := []string{"Aname", "Bname", "Cname"}
	mssgs, err := greetings.Hellos(names)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(mssgs)
}