from src.predict import prever_pd

cliente_json = {
    "renda_anual_individuo": 50000,
    "valor_emprestimo": 12000,
    "percentual_renda_emprestimo": 0.30,
    "tipo_posse_imovel": "imovel_proprio",
    "proposito_emprestimo": "fins_pessoais",
    "classificacao_emprestimo": "G",
}

resultado = prever_pd(cliente_json)
print(f"PD prevista: {resultado:.4%}")