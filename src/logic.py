import requests

def adicionar_agua(atual, quantidade):
    if quantidade < 0:
        raise ValueError("A quantidade não pode ser negativa.")
    return atual + quantidade

def verificar_meta(atual, meta):
    if atual >= meta:
        return True, "Meta atingida! Parabéns por se manter hidratado!"
    return False, f"Faltam {meta - atual}ml para a sua meta diária."


#new
def buscar_dica_motivacional():
    """Consome uma API pública para buscar uma dica."""
    try:
        # Fazendo a requisição HTTP GET
        resposta = requests.get("https://api.adviceslip.com/advice", timeout=5)
        resposta.raise_for_status() # Verifica se deu erro 404, 500, etc.
        dados = resposta.json()
        return dados["slip"]["advice"]
    except Exception:
        # Fallback (Plano B) caso o computador esteja sem internet ou a API caia
        return "Beba água, respire fundo e cuide da sua saúde!"