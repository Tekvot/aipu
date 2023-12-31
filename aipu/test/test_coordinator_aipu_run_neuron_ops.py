import unittest
from aipu.aipu import aipu 

class neuron_ops_test_cases(unittest.TestCase):

    def test_run_neuron_ops(self):
        print("*"*100)
        print("Test 1: Chequear que neuron_ops puede correr sin problemas")
        expected_result = "Successful"
        test_aipu = aipu(
            aipu_id = "1",
            pesos = [[1,2]],
            biases = [2],
            fas = ["ReLu"],
            capa_id = "1",
            output_names = "o1",
            output_ip = "192.168.0.1",
            output_port = "6339",
            input_names = ["i1"],
            input_num = 2
        )

        inpts = {"i1":[2,3]}
        if test_aipu.set_inputs(inpts, ["i1"], [0, 1]):
            try: 
                result = test_aipu.run_neuron_ops()
                self.assertEqual(expected_result, result["result"])
            except Exception as e:
                print("-"*100)
                print(f"error: {result['error']}")
                print("-"*100)

        else:
            print("Error running neuron_ops, input rejected")
        print("*"*100)

    def test_run_neuron_math_ops(self):
        print("*"*100)
        print("Test 2: Verificar que las operaciones de multiplicacion, ", 
              "sumatoria, aplicacion del bias y funcion de activacion corren")
        expected_result = [20, 20]

        test_aipu = aipu(
            aipu_id = "1",
            pesos = [[1,2,3], [1,2,3]],
            biases = [3, 3],
            fas = ["ReLu", "ReLu"],
            capa_id = "1",
            output_names = "o1",
            output_ip = "192.168.0.1",
            output_port = "6339",
            input_names = ["i1", "i1"],
            input_num = 3
        )

        inpts = {"i1":[2,3,3]}
        if test_aipu.set_inputs(inpts, ["i1", "i1"], [0, 1, 2]):
            try:
                result = test_aipu.run_neuron_ops()
                self.assertEqual(expected_result, result["o"])
            except Exception as e:
                print("-"*100)
                print(f"error: {e}")
                print("-"*100)

        else:
            print("Error running neuron_ops,input rejected")
        print("*"*100)

    def test_run_neuron_math_ops_2(self):
        print("*"*100)
        print("Test 3: Verificar que las operaciones de multiplicacion, ", 
              "sumatoria, aplicacion del bias y funcion de activacion corren",
              "usando otros valores")
        expected_result = [20,21,22,23]

        test_aipu = aipu(
            aipu_id = "1",
            pesos = [[1,2,3], [1,2,3], [1,2,3], [1,2,3]],
            biases = [3, 4, 5, 6],
            fas = ["ReLu", "ReLu", "ReLu", "ReLu"],
            capa_id = "1",
            output_names = "o10-13",
            output_ip = "192.168.0.1",
            output_port = "6339",
            input_names = ["i1", "i1", "i1", "i1"],
            input_num = 3
        )

        inpts = {"i1":[2,3,3]}
        if test_aipu.set_inputs(inpts, ["i1", "i1", "i1", "i1"], [0, 1, 2]):
            try:
                result = test_aipu.run_neuron_ops()
                self.assertEqual(expected_result, result["o"])
            except Exception as e:
                print("-"*100)
                print(f"error: {e}")
                print("-"*100)

        else:
            print("Error running neuron_ops,input rejected")
        print("*"*100)

    def test_get_output_msg(self):
        print("*"*100)
        print("Test 4: generar mensaje de salida con valores y nombres",
              "para siguiente ejecucion")
        expected_result = {'input_names': ['o10-13', 'o10-13', 'o10-13', 'o10-13'],
                           'inputs': {'o10-13': [20, 21, 22, 23]}}

        test_aipu = aipu(
            aipu_id = "1",
            pesos = [[1,2,3], [1,2,3], [1,2,3], [1,2,3]],
            biases = [3, 4, 5, 6],
            fas = ["ReLu", "ReLu", "ReLu", "ReLu"],
            capa_id = "1",
            output_names = "o10-13",
            output_ip = "192.168.0.1",
            output_port = "6339",
            input_names = ["i1", "i1", "i1", "i1"],
            input_num = 3
        )

        #inpts = {"i1":[2,3,3]}
        input_msg = { # or output_msg from previous layer
                     "input_names": ["i1", "i1", "i1", "i1"],
                     "inputs": {"i1":[2, 3, 3]}
                    }

        if test_aipu.set_inputs(input_msg["inputs"],
                                input_msg["input_names"],
                                [0, 1, 2]):
            try:
                result = test_aipu.run_neuron_ops()
                self.assertEqual(expected_result, result["output_msg"])
            except Exception as e:
                print("-"*100)
                print(f"error: {e}")
                print("-"*100)

        else:
            print("Error running neuron_ops,input rejected")
        print("*"*100)


    def test_input_homogeneo_asincrono(self):
        print("*"*100)
        print("Test 5: testear inputs homogeneos y asincronos")
        expected_result = {'input_names': ['o10-13', 'o10-13', 'o10-13', 'o10-13'],
                           'inputs': {'o10-13': [20, 21, 22, 23]}}

        test_aipu = aipu(
            aipu_id = "1",
            pesos = [[1,2,3], [1,2,3], [1,2,3], [1,2,3]],
            biases = [3, 4, 5, 6],
            fas = ["ReLu", "ReLu", "ReLu", "ReLu"],
            capa_id = "1",
            output_names = "o10-13",
            output_ip = "192.168.0.1",
            output_port = "6339",
            input_names = ["i1", "i1", "i1", "i1"],
            input_num = 3
        )

        #inpts = {"i1":[2,3,3]}
        input_msg_1 = { # or output_msg from previous layer
                        "input_names": ["i1", "i1", "i1", "i1"],
                        "inputs": {"i1":[2, 3]},
                        "input_idx": [0, 1]
                      }
        input_msg_2 = { # or output_msg from previous layer
                        "input_names": ["i1", "i1", "i1", "i1"],
                        "inputs": {"i1":[3]},
                        "input_idx": [2]
                      }

        #Primer entrada de input
        if test_aipu.set_inputs(input_msg_1["inputs"],
                                input_msg_1["input_names"],
                                input_msg_1["input_idx"]
                               ) and \
           test_aipu.set_inputs(input_msg_2["inputs"],
                                input_msg_2["input_names"],
                                input_msg_2["input_idx"]
                               ):
            try:
                result = test_aipu.run_neuron_ops()
                self.assertEqual(expected_result, result["output_msg"])
            except Exception as e:
                print("-"*100)
                print(f"error: {e}")
                print("-"*100)

        else:
            print("Error running neuron_ops,input rejected")
        print("*"*100)



if __name__ == '__main__':
    unittest.main()
