import os
from abc import ABC, abstractmethod
import json

class neuron_ops(ABC):
    """
    """

    @abstractmethod
    def run_operation(**kwargs):
        #interface to child classes
        pass


class mul_vectors(neuron_ops):
    """ multiplicar vector de entradas con vector de pesos
    """

    def run_operation(**kwargs):
        print("Multiplicar vector x con w")
        m = []
        for i in range(len(kwargs["pesos"])):
            #print(kwargs["inputs"]["i1"][i])
            inpts = list(kwargs["inputs"][kwargs["input_names"][i]])
            #print(inpts)
            mu = [x*w for w, x in zip(kwargs["pesos"][i], inpts)]
            m.append(mu)
        #print(m)
        kwargs["m"] = m

        return kwargs

class sum_vectors(neuron_ops):
    """ Sumar elementos del vector resultante de la multiplicacion
    """

    def run_operation(**kwargs):
        print("Sumar elementos del vector")
        kwargs["s"] = []
        for i in range(len(kwargs["m"])):
            kwargs["s"].append(sum(kwargs["m"][i]))

        return kwargs

class apply_bias(neuron_ops):
    """ Aplicar el bias
    """

    def run_operation(**kwargs):
        print("Aplicar bias")
        kwargs["sb"] = []
        for i in range(len(kwargs["s"])):
            #print(f"s {kwargs['s']}")
            #print(f"biases {kwargs['biases']}")
            kwargs["sb"].append(kwargs["s"][i] + kwargs["biases"][i])

        return kwargs

class apply_fa(neuron_ops):
    """ Aplicar la funcion de activacion
    """

    def run_operation(**kwargs):
        print("Aplicar la funcion de activacion")
        kwargs["o"] = []
        for i in range(len(kwargs["sb"])):
            if kwargs["fas"][i] == "ReLu":
                kwargs["o"].append(max(0, kwargs["sb"][i]))

        return kwargs

 
class success_msg(neuron_ops):
    """ Generar mensaje de exito
    """

    def run_operation(**kwargs):
        print("Generar mensaje de exito")
        kwargs["result"] = "Successful"

        return kwargs

class create_output_msgs(neuron_ops):
    """ Crear mensajes de salida para los destinos correspondientes
    """

    def run_operation(**kwargs):
        print("Crear mensajes de salida")
        output_msg = {
            'input_names': [kwargs["output_names"] for i in range(len(kwargs["input_names"]))],
            'inputs': {kwargs["output_names"]: kwargs["o"]}
        }
        kwargs["output_msg"] = output_msg
        print(output_msg)

        return kwargs


class NPUClusterOps:

    @staticmethod
    def run(**kwargs):
        for operation in neuron_ops.__subclasses__():
            kwargs = operation.run_operation(**kwargs)

        return kwargs






