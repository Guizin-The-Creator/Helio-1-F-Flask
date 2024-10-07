class Funcionario:
    def __init__(self, nome, horas_trabalhadas, valor_por_hora, numero_filhos):
        self._nome = nome
        self._horas_trabalhadas = horas_trabalhadas
        self._valor_por_hora = valor_por_hora
        self._numero_filhos = numero_filhos

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def horas_trabalhadas(self):
        return self._horas_trabalhadas

    @horas_trabalhadas.setter
    def horas_trabalhadas(self, value):
        if value < 0:
            raise ValueError("Horas trabalhadas não podem ser negativas.")
        self._horas_trabalhadas = value

    @property
    def valor_por_hora(self):
        return self._valor_por_hora

    @valor_por_hora.setter
    def valor_por_hora(self, value):
        if value < 0:
            raise ValueError("Valor por hora não pode ser negativo.")
        self._valor_por_hora = value

    @property
    def numero_filhos(self):
        return self._numero_filhos

    @numero_filhos.setter
    def numero_filhos(self, value):
        if value < 0:
            raise ValueError("Número de filhos não pode ser negativo.")
        self._numero_filhos = value

    # Calcula o salário bruto com base nas horas trabalhadas e no valor por hora
    def calcular_salario_bruto(self):
        return self.horas_trabalhadas * self.valor_por_hora

    # Calcula a gratificação (3% por filho acima de 3 filhos)
    def calcular_gratificacao(self):
        if self.numero_filhos > 3:
            gratificacao = 0.03 * self.calcular_salario_bruto() * (self.numero_filhos - 3)
            return gratificacao
        return 0

    # Calcula o salário final somando o salário bruto com a gratificação, se houver
    def calcular_salario_final(self):
        salario_bruto = self.calcular_salario_bruto()
        gratificacao = self.calcular_gratificacao()
        return salario_bruto + gratificacao

    # Método para retornar os dados do funcionário
    def obter_dados(self):
        salario_bruto = self.calcular_salario_bruto()
        gratificacao = self.calcular_gratificacao()
        salario_final = self.calcular_salario_final()

        return {
            "nome": self.nome,
            "salario_bruto": salario_bruto,
            "gratificacao": gratificacao,
            "salario_final": salario_final
        }
