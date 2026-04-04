import pandas as pd

from .load_artifacts import carregar_artefatos


ARTIFACTS = carregar_artefatos()

bins_woe = ARTIFACTS["bins_woe"]
colunas_modelo = ARTIFACTS["colunas_modelo"]
encoder_ohe = ARTIFACTS["encoder_ohe"]
modelo_pd_rl = ARTIFACTS["modelo_pd_rl"]


def prever_pd(novo_cliente: dict) -> float:
    campos_necessarios = [
        "renda_anual_individuo",
        "valor_emprestimo",
        "percentual_renda_emprestimo",
        "tipo_posse_imovel",
        "proposito_emprestimo",
        "classificacao_emprestimo",
    ]

    faltando = [c for c in campos_necessarios if c not in novo_cliente]
    if faltando:
        raise ValueError(f"Campos ausentes: {faltando}")

    df = pd.DataFrame([novo_cliente])

    df["renda_anual_individuo_woe"] = bins_woe["renda_anual_individuo"].transform(
        df["renda_anual_individuo"], metric="woe"
    )

    df["valor_emprestimo_woe"] = bins_woe["valor_emprestimo"].transform(
        df["valor_emprestimo"], metric="woe"
    )

    df_cat = df[
        [
            "tipo_posse_imovel",
            "proposito_emprestimo",
            "classificacao_emprestimo",
        ]
    ]

    X_cat = encoder_ohe.transform(df_cat)

    df_ohe = pd.DataFrame(
        X_cat,
        columns=encoder_ohe.get_feature_names_out(df_cat.columns),
        index=df.index,
    )

    df_final = pd.concat(
        [
            df[
                [
                    "renda_anual_individuo_woe",
                    "valor_emprestimo_woe",
                    "percentual_renda_emprestimo",
                ]
            ],
            df_ohe,
        ],
        axis=1,
    )

    df_final = df_final.reindex(columns=colunas_modelo, fill_value=0)
    df_final = df_final.astype(float)

    pd_prevista = modelo_pd_rl.predict_proba(df_final)[:, 1][0]

    return float(pd_prevista)