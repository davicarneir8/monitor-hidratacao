def adicionar_agua(atual, quantidade):
    if quantidade < 0:
        raise ValueError("A quantidade não pode ser negativa.")
    return atual + quantidade

def verificar_meta(atual, meta):
    if atual >= meta:
        return True, "Meta atingida! Parabéns por se manter hidratado!"
    return False, f"Faltam {meta - atual}ml para a sua meta diária."