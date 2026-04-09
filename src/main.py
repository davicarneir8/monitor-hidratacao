import sys
from logic import adicionar_agua, verificar_meta

def main():
    meta = 2000 # Meta de 2 litros
    atual = 0
    
    print("=== Monitor de Hidratação ===")
    print("Ajuda você a atingir sua meta diária de água.\n")
    
    while True:
        print(f"Status Atual: {atual}ml / {meta}ml")
        entrada = input("Quantos ml de água você bebeu agora? (ou digite 'sair'): ")

        if entrada.lower() == 'sair':
            print("Até logo! Beba água!")
            sys.exit(0)

        try:
            quantidade = int(entrada)
            atual = adicionar_agua(atual, quantidade)
            atingiu, mensagem = verificar_meta(atual, meta)
            
            print(f"\n--> {mensagem}\n")
            
            if atingiu:
                break
        except ValueError as e:
            if "negativa" in str(e):
                print(f"\n[ERRO] {e}\n")
            else:
                print("\n[ERRO] Por favor, digite um número inteiro válido.\n")

if __name__ == "__main__":
    main()