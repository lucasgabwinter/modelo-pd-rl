from pydantic import BaseModel


class ClienteInput(BaseModel):
    renda_anual_individuo: float
    valor_emprestimo: float
    percentual_renda_emprestimo: float
    tipo_posse_imovel: str
    proposito_emprestimo: str
    classificacao_emprestimo: str


class PredicaoOutput(BaseModel):
    probabilidade_inadimplencia: float