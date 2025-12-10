# Trabalho Final – Qualidade e Teste de Software  
### Tema: Finanças Pessoais  
### Autora: Julia Haertel

Este projeto implementa um sistema simples de cálculos financeiros, contendo:

- ✔️ Juros Simples  
- ✔️ Juros Compostos  
- ✔️ Valor Futuro  
- ✔️ Valor Presente  
- ✔️ Testes Unitários (pytest)  
- ✔️ API REST (FastAPI)  
- ✔️ Teste de Carga (JMeter com 50 requisições simultâneas)  

---

# 📌 1. Estrutura do Projeto

calculo_financas/
│ main.py
│ finance_calculator.py
│ test_finance_calculator.py
│ jmeter_test_plan.jmx
│ README.md


---

# 📌 2. Operações Implementadas

## ➤ Juros Simples
**Entrada:** capital, taxa, tempo  
**Fórmula:**  
juros = capital * taxa * tempo


---

## ➤ Juros Compostos
**Entrada:** capital, taxa, tempo, períodos por ano  
**Fórmula:**  
montante = capital * (1 + taxa / n)^(n*tempo)

---

## ➤ Valor Futuro
**Entrada:** valor_presente, taxa, n_parcelas, contribuicao_periodica (opcional)  

---

## ➤ Valor Presente
**Entrada:** valor_futuro, taxa, n_períodos  
**Fórmula:**  
VP = VF / (1 + taxa)^n


---

# 📌 3. Como Rodar o Projeto

### ➤ Instalar dependências
py -m pip install fastapi uvicorn pytest


### ➤ Rodar a API
uvicorn main:app --reload --port 8000


Com o servidor rodando, acesse o Swagger:
👉 http://127.0.0.1:8000/docs

---

# 📌 4. Rodar Testes Unitários
py -m pytest -q


---

# 📌 5. Teste de Carga (JMeter)

- Arquivo incluído: `jmeter_test_plan.jmx`  
- Contém 50 usuários simultâneos  
- Testa os 4 endpoints  
- Imagens do relatório: `summary_report.png` e `resultados_em_tabela.png`

---

# 📌 6. Tecnologias Utilizadas

- Python 3.x  
- FastAPI  
- Pytest  
- Uvicorn  
- JMeter  

---

# 📌 7. Vídeo da Apresentação

**(link do YouTube)**
 
