import pytest
from src.logic import adicionar_agua, verificar_meta

# 1. Caminho Feliz
def test_adicionar_agua_corretamente():
    assert adicionar_agua(1000, 500) == 1500

# 2. Entrada Inválida (Impedir valor negativo)
def test_adicionar_agua_negativa():
    with pytest.raises(ValueError, match="A quantidade não pode ser negativa."):
        adicionar_agua(500, -100)

# 3. Caso Limite (Atingiu exatamente a meta)
def test_verificar_meta_atingida():
    atingiu, msg = verificar_meta(2000, 2000)
    assert atingiu is True
    assert "Meta atingida" in msg