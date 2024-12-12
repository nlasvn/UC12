class Funcionario:
    def __init__(self, nome, salario_base):
        self.__nome = nome
        self.__salario_base = salario_base

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        self.__salario_base = salario_base

    def calcular_salario(self):
        raise NotImplementedError("Subclasses devem implementar esse método.")


class Gerente(Funcionario):
    def calcular_salario(self):
        return self.salario_base + (self.salario_base * (20 / 100))


class Desenvolvedor(Funcionario):
    def calcular_salario(self):
        return self.salario_base + (self.salario_base * (10 / 100))


class Estagiario(Funcionario):
    def calcular_salario(self):
        return self.salario_base


class FuncionarioController:
    def __init__(self):
        self.__funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.__funcionarios.append(funcionario)

    def listar_funcionarios(self):
        return self.__funcionarios


class FuncionarioView:
    def exibir_info(self, funcionario):
        if isinstance(funcionario, Gerente):
            print(
                f"Nome: {funcionario.nome}\nCargo: Gerente\nSalário: {funcionario.calcular_salario()}\n"
            )
        elif isinstance(funcionario, Desenvolvedor):
            print(
                f"Nome: {funcionario.nome}\nCargo: Desenvolvedor\nSalário: {funcionario.calcular_salario()}\n"
            )
        else:
            print(
                f"Nome: {funcionario.nome}\nCargo: Estágiário\nSalário: {funcionario.calcular_salario()}\n"
            )


def validar_salario():
    while True:
        salario = ""
        salario = float(input("Digite o salario do funcionario: "))
        if type(salario) is not float:
            print("Salário inválido. Digite apenas números.")
            continue
        break

    return salario


def validar_func():
    while True:
        tipo_func = ""
        tipo_func = input("Tipo (Gerente, Desenvolvedor, Estagiário): ")
        if (
            tipo_func == "Gerente"
            or tipo_func == "Desenvolvedor"
            or tipo_func == "Estagiário"
        ):
            break
        print("Opção inválida, tente novamente.")
        continue

    return tipo_func


if __name__ == "__main__":
    view = FuncionarioView()
    controller = FuncionarioController()
    while True:
        print("- - - Sistema de Gerenciamento de Funcionários - - -")
        print("1. Adicionar funcionário")
        print("2. Listar funcionários")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                nome = input("Nome do funcionário: ")
                tipo_func = validar_func()
                salario = validar_salario()

                if tipo_func == "Gerente":
                    controller.adicionar_funcionario(Gerente(nome, salario))
                elif tipo_func == "Desenvolvedor":
                    controller.adicionar_funcionario(Desenvolvedor(nome, salario))
                else:
                    controller.adicionar_funcionario(Estagiario(nome, salario))

                op_continuar = input(
                    "Deseja adicionar mais funcionários? Digite 's' para continuar: "
                )

                if op_continuar != "s":
                    break

        elif opcao == "2":
            for funcionario in controller.listar_funcionarios():
                view.exibir_info(funcionario)
        elif opcao == "3":
            break
        else:
            print("Selecione uma opção válida")
