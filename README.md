Modelo de Probabilidade de Default (PD) com Regressão Logística

Este projeto implementa um modelo de probabilidade de inadimplência (PD) utilizando regressão logística, com foco em organização de artefatos, reprodutibilidade e preparação para deploy em ambiente produtivo.

Objetivo:
Desenvolver um modelo de crédito com pipeline estruturado que permita:

Treinamento consistente
Separação clara de artefatos
Reprodutibilidade das previsões
Integração com serviços de inferência via API
Implantação em ambiente cloud
Estrutura do Projeto
modelo-pd-rl/
│
├── artifacts/              # Artefatos do modelo treinado
│   ├── modelo_pd_rl.pkl
│   ├── encoder_ohe.pkl
│   ├── bins_woe.pkl
│   ├── colunas_modelo.pkl
│   └── metadata.pkl
│
├── data/                   # Dataset utilizado
│   └── credit_risk_dataset.csv
│
├── notebooks/              # Desenvolvimento e experimentação
│   └── caderno.ipynb
│
├── tests.py                # Testes de inferência do modelo
├── requirements.txt        # Dependências do projeto
├── desc_var.md             # Descrição das variáveis
├── readme.md               # Documentação do projeto
└── settings.json

Tecnologias Utilizadas:
Python
Pandas
NumPy
Scikit-learn
Joblib
FastAPI
Docker
AWS
Modelagem

O modelo foi desenvolvido utilizando:

Regressão Logística
Transformação de variáveis com WOE (Weight of Evidence)
Codificação de variáveis categóricas via One-Hot Encoding
Seleção e organização das variáveis de entrada

Todos os componentes necessários para inferência foram persistidos separadamente, garantindo consistência entre ambiente de desenvolvimento e execução.

Pipeline de Inferência

O processo de predição segue as seguintes etapas:

Recebimento dos dados de entrada
Aplicação das transformações:
Encoding das variáveis categóricas
Aplicação dos bins de WOE
Seleção e ordenação das variáveis
Aplicação do modelo de regressão logística
Retorno da probabilidade de inadimplência
Servir o Modelo via API

O modelo foi estruturado para ser exposto como um serviço de inferência utilizando FastAPI.

A API recebe dados em formato JSON, aplica o pipeline de transformação e retorna a probabilidade estimada pelo modelo. Essa abordagem permite desacoplamento entre modelagem e consumo, facilitando integração com sistemas externos.

Containerização com Docker

A aplicação pode ser empacotada em uma imagem Docker, garantindo:

Reprodutibilidade do ambiente
Portabilidade entre diferentes sistemas
Facilidade de deploy

O container inclui:

Código da API
Artefatos do modelo
Dependências definidas em requirements.txt
Deploy em Ambiente AWS

A arquitetura do projeto permite implantação em ambiente cloud, utilizando serviços como:

Amazon ECR para armazenamento da imagem Docker
Amazon ECS ou SageMaker para execução do container
Integração com serviços de rede para exposição do endpoint

Essa abordagem permite escalar o serviço de inferência conforme a demanda e manter separação entre desenvolvimento e produção.

Como Executar
Criar ambiente virtual:
python -m venv .venv
source .venv/bin/activate
Instalar dependências:
pip install -r requirements.txt
Executar os testes:
python tests.py

Observações:

O projeto foi estruturado com foco em boas práticas de organização de código, separação de responsabilidades e preparação para deploy em ambiente produtivo, permitindo fácil manutenção e evolução.