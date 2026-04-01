idade_individuo: Idade do indivíduo que está solicitando o empréstimo.

renda_anual_individuo: Renda anual do indivíduo.

tipo_posse_imovel: Tipo de posse de imóvel do indivíduo.

* aluguel: O indivíduo está atualmente alugando uma propriedade
* imovel_financiado: O indivíduo tem um financiamento sobre a propriedade que possui.
* imovel_proprio: O indivíduo possui sua casa/apto integralmente.
* imovel_proprio: Outras categorias de posse de imóvel que podem ser específicas ao conjunto de dados.

tempo_emprego_anos': Tempo de emprego do indivíduo em anos.

proposito_emprestimo: O propósito da solicitação do empréstimo.

classificacao_emprestimo: A classificação atribuída ao empréstimo com base na credibilidade do tomador.
* A: O tomador tem alta credibilidade, indicando baixo risco.
* B: O tomador tem risco relativamente baixo, mas não tão confiável quanto a Classe A.
* C: A credibilidade do tomador é moderada.
* D: O tomador é considerado de maior risco em comparação com as classes anteriores.
* E: A credibilidade do tomador é menor, indicando um risco maior.
* F: O tomador representa um risco de crédito significativo.
* G: A credibilidade do tomador é a mais baixa, significando o maior risco.

valor_emprestimo: O valor do empréstimo solicitado pelo indivíduo.

taxa_juros_emprestimo: A taxa de juros associada ao empréstimo.

Variavel Resposta:
status_emprestimo: Status do empréstimo, onde 0 indica não inadimplente e 1 indica inadimplente.
* 0: Não inadimplente - O tomador pagou o empréstimo conforme acordado, sem inadimplência.
* 1: Inadimplente - O tomador não pagou o empréstimo conforme os termos acordados e inadimpliu.

percentual_renda_emprestimo: A porcentagem da renda representada pelo valor do empréstimo, arredondado.

historico_inadimplencia: Histórico de inadimplência do indivíduo conforme registros do bureau de crédito.
* historico_inadimplencia: O indivíduo tem um histórico de inadimplências no seu arquivo de crédito.
* sem_historico_inadimplencia: O indivíduo não tem nenhum histórico de inadimplências.

duracao_historico_credito: A duração do histórico de crédito do indivíduo.