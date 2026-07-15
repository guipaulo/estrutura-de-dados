from collections import deque
from colorama import Fore, Style, init

# autoreset=True restaura a cor depois de cada print.
init(autoreset=True)


class Navegador:
    def __init__(self):
        self.paginas_anteriores = deque(maxlen=5)
        self.paginas_seguintes = deque()
        self.pagina_atual = None

    def acessar_pagina(self, url):
        if self.pagina_atual is not None:
            self.paginas_anteriores.append(self.pagina_atual)

        self.pagina_atual = url

        self.paginas_seguintes.clear()

        print(f"\n{Fore.CYAN}Acessando: "f"{Fore.MAGENTA}{Style.BRIGHT}{self.pagina_atual}")

    def voltar(self):
        if not self.paginas_anteriores:
            print(f"\n{Fore.RED}{Style.BRIGHT}""Não há páginas anteriores.")
            return

        self.paginas_seguintes.appendleft(self.pagina_atual)
        self.pagina_atual = self.paginas_anteriores.pop()

        print(f"\n{Fore.YELLOW}Voltou para: "f"{Fore.MAGENTA}{Style.BRIGHT}{self.pagina_atual}")

    def avancar(self):
        if not self.paginas_seguintes:
            print(f"\n{Fore.RED}{Style.BRIGHT}""Não há páginas para avançar.")
            return

        self.paginas_anteriores.append(self.pagina_atual)
        self.pagina_atual = self.paginas_seguintes.popleft()

        print(f"\n{Fore.GREEN}Avançou para: "f"{Fore.MAGENTA}{Style.BRIGHT}{self.pagina_atual}")

    def mostrar_pagina_atual(self):
        if self.pagina_atual is None:
            print(f"\n{Fore.RED}""Nenhuma página foi acessada.")
        else:
            print(f"\n{Fore.WHITE}Página atual: "f"{Fore.MAGENTA}{Style.BRIGHT}{self.pagina_atual}")

    def mostrar_historico(self):
        if self.pagina_atual is None:
            print(f"\n{Fore.RED}""O histórico está vazio.")
            return

        print(f"\n{Fore.CYAN}{Style.BRIGHT}""========== HISTÓRICO ==========")

        print(f"\n{Fore.BLUE}{Style.BRIGHT}""PÁGINAS ANTERIORES:")

        if self.paginas_anteriores:
            for pagina in self.paginas_anteriores:
                print(f"{Fore.BLUE}  ← {pagina}")
        else:
            print(f"{Fore.WHITE}  Nenhuma página anterior.")

        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}""PÁGINA ATUAL:")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}"f"  >>> {self.pagina_atual}")

        print(f"\n{Fore.GREEN}{Style.BRIGHT}""PÁGINAS SEGUINTES:")

        if self.paginas_seguintes:
            for pagina in self.paginas_seguintes:
                print(f"{Fore.GREEN}  → {pagina}")
        else:
            print(f"{Fore.WHITE}  Nenhuma página seguinte.")

        print(f"\n{Fore.CYAN}{Style.BRIGHT}""===============================")

    def mostrar_menu(self):
        print(f"\n{Fore.CYAN}{Style.BRIGHT}""----- NAVEGADOR -----")

        print(f"{Fore.BLUE}{Style.BRIGHT}1 "f"{Fore.WHITE}- Acessar nova página")

        print(f"{Fore.YELLOW}{Style.BRIGHT}2 "f"{Fore.WHITE}- Voltar")

        print(f"{Fore.GREEN}{Style.BRIGHT}3 "f"{Fore.WHITE}- Avançar")

        print(f"{Fore.MAGENTA}{Style.BRIGHT}4 "f"{Fore.WHITE}- Mostrar página atual")

        print(f"{Fore.CYAN}{Style.BRIGHT}5 "f"{Fore.WHITE}- Mostrar histórico")

        print(f"{Fore.RED}{Style.BRIGHT}6 "f"{Fore.WHITE}- Sair")

    def iniciar(self):
        while True:
            self.mostrar_menu()

            opcao = input(f"{Fore.YELLOW}Escolha uma opção: ").strip()

            if opcao == "1":
                url = input(f"{Fore.BLUE}""Digite o endereço da página: ").strip()

                if url:
                    self.acessar_pagina(url)
                else:
                    print(f"\n{Fore.RED}{Style.BRIGHT}""O endereço não pode ficar vazio.")

            elif opcao == "2":
                self.voltar()

            elif opcao == "3":
                self.avancar()

            elif opcao == "4":
                self.mostrar_pagina_atual()

            elif opcao == "5":
                self.mostrar_historico()

            elif opcao == "6":
                print(f"\n{Fore.RED}{Style.BRIGHT}""Navegador encerrado.")
                break

            else:
                print(f"\n{Fore.RED}{Style.BRIGHT}""Opção inválida.")


navegador = Navegador()
navegador.iniciar()