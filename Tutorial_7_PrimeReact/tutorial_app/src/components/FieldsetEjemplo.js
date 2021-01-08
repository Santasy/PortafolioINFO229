import { Component, createRef } from 'react';

// Importa archivos css bases
import 'primeflex/primeflex.css';
import 'primereact/resources/primereact.min.css';
import 'primereact/resources/themes/saga-blue/theme.css';
import 'primeicons/primeicons.css';

// Import de componentes
// -- Ejemplo 1
import { Fieldset } from 'primereact/fieldset';
import { Accordion, AccordionTab } from 'primereact/accordion';
// -- Ejemplo 2
import { Button } from 'primereact/button';
import { Toast } from 'primereact/toast';
import { ProgressBar } from 'primereact/progressbar';

export default class FieldsetEjemplo extends Component {
    constructor() {
        super();
        console.log("Ejemplo con PrimeReact!");
    
        // Se inicia la variable para seguir el progreso,
        // con un valor inicial de 0.
        this.state = {
            progVal: 0,
            intervalId: null
        };
        this.setProgVal = (val) => {
            this.setState({
                progVal: val
            });
        }
        
        // Se crea referencias para avanzar la barra.
        this.toast = createRef(null);

        // Funcion que se ejecuta cada vez que el intervalo se cumple.
        this.timer = () => {
            console.log("Tick!");
            var val = this.state.progVal;
            val += Math.floor(Math.random() * 10) + 1;
            val = Math.min(val, 100);
            this.setState({
                progVal: val
            });
            if (val == 100){
                this.toast.current.show({
                    severity: 'info',
                    summary: '100%!',
                    detail: 'La barra se ha completado' });
                clearInterval(this.state.intervalId);
            }
        };

        // Funcion entregada al boton que comienza el contador
        this.changeBar = () => {
            if (this.state.intervalId == null){
                console.log("Iniciando!");
                var interval = setInterval(this.timer, 500);
                this.setState({
                    intervalId: interval
                });
            }else{
                console.log("Ya existe un contador.");
            }
        }
    }

    render() {
        const { changeBar, toast } = this;
        const { progVal } = this.state;
        return(
            <Fieldset legend="Ejemplos">
                <Toast ref={toast} />
                <Accordion>
                    <AccordionTab header="1. Iconos giratorios!">
                        <i className="pi pi-spin pi-times" />
                        <i className="pi pi-spin pi-eye" />
                        <i className="pi pi-spin pi-times" />
                    </AccordionTab>
                    <AccordionTab header="2. Progreso y Toast!">
                        <Button label="Comenzar" icon="pi pi-play"
                            onClick={changeBar} />
                        <ProgressBar value={progVal} />
                    </AccordionTab>
                </Accordion>
            </Fieldset>
        );
    }
}