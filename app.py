
from colorama import Fore, Style, init

init(autoreset=True)

# Lista 
niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

def definir_cor(nivel):
    cores = [
        Fore.RED,
        Fore.YELLOW,
        Fore.GREEN,
        Fore.CYAN,
        Fore.BLUE
    ]

    return cores[nivel - 1]

for nivel in range(1, 6):
    mensagem = niveis[nivel - 1]
    cor = definir_cor(nivel)

    print(cor + mensagem + Style.RESET_ALL)
