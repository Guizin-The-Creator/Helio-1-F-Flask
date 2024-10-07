from model.Funcionario import Funcionario

class FuncionarioController:
    def __init__(self):
        self._funcionario = None

    def criar_funcionario(self, nome, horas_trabalhadas, valor_por_hora, numero_filhos):
        self._funcionario = Funcionario(nome, horas_trabalhadas, valor_por_hora, numero_filhos)

    def calcular_salario_bruto(self):
        if self._funcionario is None:
            raise ValueError("Funcionário não foi criado.")
        return self._funcionario.calcular_salario_bruto()

    def calcular_gratificacao(self):
        if self._funcionario is None:
            raise ValueError("Funcionário não foi criado.")
        return self._funcionario.calcular_gratificacao()

    def calcular_salario_final(self):
        if self._funcionario is None:
            raise ValueError("Funcionário não foi criado.")
        return self._funcionario.calcular_salario_final()

    def exibir_dados_funcionario(self):
        if self._funcionario is None:
            raise ValueError("Funcionário não foi criado.")
        self._funcionario.exibir_dados()

    # Getters e Setters
    @property
    def funcionario(self):
        return self._funcionario

    @funcionario.setter
    def funcionario(self, funcionario):
        self._funcionario = funcionario
