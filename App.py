from flask import Flask, jsonify, request
from control.FuncionarioController import FuncionarioController

app = Flask("API Funcionario")

# Função auxiliar para lidar com validações
def handle_validation_error(e):
    return jsonify({"erro": str(e)}), 400

# Endpoint POST: /funcionario/salario
@app.route('/funcionario/salario', methods=['POST'])
def calcular_salario_funcionario():
    try:
        # Recebe os dados do funcionário via JSON
        data = request.get_json()
        nome = data.get('nome')
        horas_trabalhadas = data.get('horas_trabalhadas')
        valor_por_hora = data.get('valor_por_hora')
        numero_filhos = data.get('numero_filhos')

        # Validação de entrada
        if None in [nome, horas_trabalhadas, valor_por_hora, numero_filhos]:
            raise ValueError("Todos os campos (nome, horas_trabalhadas, valor_por_hora, numero_filhos) são obrigatórios.")

        # Cria o controlador e calcula o salário
        funcionarioController = FuncionarioController()
        funcionarioController.criar_funcionario(nome, horas_trabalhadas, valor_por_hora, numero_filhos)

        salario_bruto = funcionarioController.calcular_salario_bruto()
        gratificacao = funcionarioController.calcular_gratificacao()
        salario_final = funcionarioController.calcular_salario_final()

        # Retorna os dados como JSON
        jsonResposta = {
            "nome": nome,
            "salario_bruto": salario_bruto,
            "gratificacao": gratificacao,
            "salario_final": salario_final
        }
        return jsonify(jsonResposta), 200

    except ValueError as e:
        return handle_validation_error(e)

# Inicia o servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
