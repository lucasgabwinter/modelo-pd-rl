# Modelo de Probabilidade de Default (PD) com Regressão Logística

Este projeto implementa um modelo de probabilidade de inadimplência (PD) utilizando regressão logística. A proposta foi estruturar um pipeline simples, mas bem organizado, separando claramente as etapas de treinamento e inferência, com foco em reprodutibilidade e preparação para deploy.

## Objetivo

Desenvolver um modelo de crédito com uma estrutura que permita:

- Treinar o modelo de forma consistente
- Separar corretamente os artefatos gerados
- Reproduzir as previsões fora do ambiente de treino
- Disponibilizar o modelo via API
- Preparar o projeto para execução em ambiente cloud

## Estrutura do projeto
modelo-pd-rl/
│
├── artifacts/ # Artefatos do modelo
│ ├── modelo_pd_rl.pkl
│ ├── encoder_ohe.pkl
│ ├── bins_woe.pkl
│ ├── colunas_modelo.pkl
│ └── metadata.pkl
│
├── data/ # Dataset utilizado
│ └── credit_risk_dataset.csv
│
├── notebooks/ # Exploração e desenvolvimento
│ └── caderno.ipynb
│
├── src/ # Código de inferência
│ ├── predict.py
│ ├── load_artifacts.py
│ ├── schemas.py
| └── __init__.py
│
├── tests/ # Testes simples de inferência
│ └── tests_predict.py
│
├── main.py # API com FastAPI
├── run_local.py # Execução local
├── requirements.txt
├── Dockerfile
├── desc_var.md
├── settings.json
└── README.md


## Tecnologias utilizadas

- Python
- Pandas e NumPy
- Scikit-learn
- OptBinning
- Joblib
- FastAPI
- Docker
- AWS (ECR)
- AWS (App Runner)

## Modelagem

O modelo foi construído com regressão logística, utilizando:

- Transformação de variáveis com WOE (Weight of Evidence)
- Codificação de variáveis categóricas com One-Hot Encoding
- Seleção e organização das variáveis de entrada

A ideia foi manter um fluxo simples, mas próximo do que seria utilizado em produção.

## Artefatos

Os principais componentes do pipeline foram persistidos separadamente:

- Modelo treinado
- Encoder das variáveis categóricas
- Transformações de WOE
- Lista de colunas esperadas
- Metadados

Isso permite carregar todos os elementos necessários diretamente na etapa de inferência, sem dependência do ambiente de treino.

## API

A inferência é feita via API utilizando FastAPI. O serviço recebe os dados de entrada em formato JSON, aplica as transformações necessárias e retorna a probabilidade de default.

## Deploy

O projeto foi containerizado com Docker e preparado para execução no AWS App Runner.

## Observações

A estrutura foi pensada para separar responsabilidades e facilitar evolução futura, principalmente em cenários com deploy contínuo ou monitoramento do modelo.

## Variáveis de Entrada

A API espera as seguintes variáveis de entrada:

### Variáveis categóricas

#### Tipo de posse do imóvel (`tipo_posse_imovel`)

Valores possíveis:

- `aluguel`
- `imovel_proprio`
- `imovel_financiado`
- `imovel_outros`

#### Propósito do empréstimo (`proposito_emprestimo`)

Valores possíveis:

- `fins_consolidacao_debito`
- `fins_educacao`
- `fins_medicos`
- `fins_pessoais`
- `fins_negocios`
- `fins_reformas`

#### Classificação do empréstimo (`classificacao_emprestimo`)

Faixas de risco representadas por letras:

- `A` (menor risco)
- `B`
- `C`
- `D`
- `E`
- `F`
- `G` (maior risco)

### Variáveis numéricas

- `renda_anual_individuo`
- `valor_emprestimo`
- `percentual_renda_emprestimo`

## Exemplo de requisição

```json
{
  "renda_anual_individuo": 50000,
  "valor_emprestimo": 12000,
  "percentual_renda_emprestimo": 0.24,
  "tipo_posse_imovel": "imovel_proprio",
  "proposito_emprestimo": "fins_pessoais",
  "classificacao_emprestimo": "G"
}

Saida esperada:
```json
{
  "probabilidade_inadimplencia": 0.7046636022100472
}