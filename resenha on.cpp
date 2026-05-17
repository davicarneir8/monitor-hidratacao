# 1. O programa faz a pergunta e já guarda a resposta do usuário
resposta = input('Você está com a mochila? (Digite "sim" ou "nao"): ')

# 2. A lógica do IF / ELSE
# Usamos o .strip() para remover espaços acidentais e .lower() para deixar tudo minúsculo
if resposta.strip().lower() == 'sim':
    print('Resenha on 🎒🔥')
else:
    print('Resenha off 🚫')