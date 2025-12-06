# test_finance_calculator.py
import pytest
from finance_calculator import FinanceCalculator

def test_juros_simples():
    r = FinanceCalculator.juros_simples(1000, 0.05, 2)
    assert pytest.approx(r["juros"], rel=1e-6) == 100.0
    assert pytest.approx(r["montante"], rel=1e-6) == 1100.0

def test_juros_compostos():
    r = FinanceCalculator.juros_compostos(1000, 0.1, 2, periodos_por_ano=1)
    # montante = 1000 * 1.1^2 = 1210
    assert pytest.approx(r["montante"], rel=1e-6) == 1210.0
    assert pytest.approx(r["juros_totais"], rel=1e-6) == 210.0

def test_valor_futuro_sem_contribuicao():
    r = FinanceCalculator.valor_futuro(1000, 0.1, 2, 0.0)
    assert pytest.approx(r["valor_futuro"], rel=1e-6) == 1210.0

def test_valor_futuro_com_contribuicao():
    # VP=0, taxa=10%, n=2, contrib=100 => VF = 0 + 100*((1.1^2 -1)/0.1) = 100*(0.21/0.1)=100*2.1=210
    r = FinanceCalculator.valor_futuro(0, 0.1, 2, 100)
    assert pytest.approx(r["valor_futuro"], rel=1e-6) == 210.0

def test_valor_presente():
    r = FinanceCalculator.valor_presente(1210, 0.1, 2)
    assert pytest.approx(r["valor_presente"], rel=1e-6) == 1000.0
