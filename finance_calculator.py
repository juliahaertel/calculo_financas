# finance_calculator.py
from typing import Optional
import math

class FinanceCalculator:
    @staticmethod
    def juros_simples(capital: float, taxa: float, tempo: int) -> dict:
        """
        juros = capital * taxa * tempo
        montante = capital + juros
        """
        juros = capital * taxa * tempo
        montante = capital + juros
        return {"juros": round(juros, 6), "montante": round(montante, 6)}

    @staticmethod
    def juros_compostos(capital: float, taxa: float, tempo: int, periodos_por_ano: int = 1) -> dict:
        """
        montante = capital * (1 + taxa/periodos) ** (periodos * tempo)
        """
        effective_rate = taxa / periodos_por_ano
        expo = periodos_por_ano * tempo
        montante = capital * ((1 + effective_rate) ** expo)
        juros_totais = montante - capital
        return {"montante": round(montante, 6), "juros_totais": round(juros_totais, 6)}

    @staticmethod
    def valor_futuro(valor_presente: float, taxa: float, n_periodos: int, contribuicao_periodica: float = 0.0) -> dict:
        """
        VF:
        - Sem contribuições periódicas: VF = VP * (1+taxa)**n
        - Com contribuições: VF = VP*(1+taxa)**n + c * ( ( (1+taxa)**n - 1 ) / taxa )
        """
        if n_periodos < 0:
            raise ValueError("n_periodos deve ser >= 0")
        if taxa == -1 and contribuicao_periodica != 0:
            raise ValueError("taxa inválida para contribuições periódicas")

        vf = valor_presente * ((1 + taxa) ** n_periodos)
        if contribuicao_periodica != 0:
            if taxa == 0:
                # soma aritmética simples
                vf += contribuicao_periodica * n_periodos
            else:
                vf += contribuicao_periodica * (((1 + taxa) ** n_periodos - 1) / taxa)
        return {"valor_futuro": round(vf, 6)}

    @staticmethod
    def valor_presente(valor_futuro: float, taxa: float, n_periodos: int) -> dict:
        """
        VP = VF / (1+taxa)**n
        """
        vp = valor_futuro / ((1 + taxa) ** n_periodos)
        return {"valor_presente": round(vp, 6)}
