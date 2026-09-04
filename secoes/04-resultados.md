---
secao: 04-resultados
titulo: Resultados e discussões
alvo_palavras: 2800
status: rascunho
---

## 4 Resultados e discussões

Os resultados apresentados nesta seção derivam de três fontes de evidência, tratadas de
forma independente e cruzadas apenas quando descrevem o mesmo fenômeno. A primeira é uma
consulta agregada ao banco de produção realizada em 27 de julho de 2026, que caracteriza a
base efetivamente constituída ao longo do ciclo de 2025. A segunda são as exportações dos
fluxos de automação, que documentam o comportamento implementado das camadas de decisão e
de intervenção. A terceira reúne as medições de tempo de execução registradas pela equipe
durante a operação, empregadas na comparação com o processo manual que antecedeu a
automação.

A ordem de apresentação acompanha o argumento construído nas seções anteriores. Descreve-se
primeiro a base de dados constituída, depois a cobertura longitudinal que ela oferece e a
consequente computabilidade da regra de certificação, em seguida o comportamento observado
da camada de intervenção e os tempos de execução, e por fim a discussão do conjunto e as
limitações que ele impõe. Os dados são reportados sem interpretação nas subseções 4.1 a
4.4; a leitura à luz do problema formulado na introdução concentra-se nas subseções 4.5 e
4.6.

### 4.1 A base de dados constituída no ciclo de 2025

A consulta de 27 de julho de 2026 encontrou 33
discentes cadastrados, com datas de registro entre 23 de janeiro e 1º de abril de 2025,
vinculados a três projetos sob acompanhamento de dois mentores. Foram contabilizadas 177 autoavaliações, registradas entre 23 de janeiro e 6
de setembro de 2025 e distribuídas em nove unidades avaliativas. A tabela de notas reúne
165 registros, dos quais 105 vinculados a competências macro e 60 a subcompetências de
inteligência emocional. As notas ocupam integralmente a escala prevista, de 0,00 a 4,00,
com média de 2,47, valor situado na faixa qualitativa adequada. A [[@TAB:04-1]] consolida o
conjunto.

[[TAB:04-1
  tipo: tabela
  status: criar
  origem: consulta agregada ao banco de produção em 27/07/2026, registrada em mapa-de-fatos §6
  dados: mapa-de-fatos §6
  descricao: Quadro editável com as métricas agregadas do banco em 27/07/2026 — discentes, autoavaliações, unidades, notas por tipo, faixa e média das notas, mentores, projetos e registros de auditoria. Uma coluna para a métrica e outra para o valor. Nenhum dado individual. Corpo em TNR 10.
  legenda: Tabela 1 — Caracterização agregada da base de produção do ciclo de 2025, apurada em 27 de julho de 2026 (n=33 discentes). Fonte: dados da pesquisa.
  largura: 1col
  altura_cm: 8
  arquivo: figuras/tab-04-1.md
]]

A distribuição das 165 notas entre os dois níveis da matriz é regular e confirma a
consistência do desdobramento descrito na subseção 3.1. As 105 notas de competência macro
correspondem a quinze conjuntos completos de sete medições, e as 60 notas de subcompetência
correspondem aos mesmos quinze conjuntos de quatro medições. A base contém, portanto,
quinze conjuntos íntegros de dez itens comparáveis, sem registro parcial que exigisse
tratamento de valor ausente no cálculo das duas regras. As notas lançadas concentram-se em
sete discentes, o que separa a população cadastrada da população efetivamente medida e
condiciona toda leitura de escala.

A razão entre discentes cadastrados e mentores responsáveis é de aproximadamente dezesseis
para um, distribuída em três projetos. Esse valor não é parâmetro de qualidade do
acompanhamento, mas explica a natureza do problema que motivou a automação: a produção
manual do perfil de cada discente recaía sobre uma equipe pequena e a cada unidade
avaliativa, o que multiplica o esforço pelo número de ciclos, e não apenas pelo número de
participantes. A carga acumulada ao longo de nove unidades é a grandeza que a solução
descrita neste trabalho desloca para a máquina.

A tabela de auditoria do painel administrativo acumulou 1.792 registros de operação no
período, contra 177 autoavaliações persistidas. A razão entre os dois números não expressa
retrabalho: o painel foi o instrumento de conferência e de correção usado pela equipe
durante a estabilização do fluxo de cadastro, e cada consulta ou ajuste manual deixa
registro próprio. O valor interessa como demonstração de que a trilha de auditoria descrita
na subseção 3.3 opera de fato, e não apenas como declaração de esquema.

### 4.2 Cobertura longitudinal e computabilidade da regra de certificação

A distribuição das autoavaliações pelas nove unidades é fortemente assimétrica, conforme a
[[@FIG:04-1]]. As cinco primeiras unidades apresentam 33 registros cada, cobertura completa
da turma cadastrada. Da sexta unidade em diante o número decai para 7, 3, 1 e 1 registros.
O programa manteve, portanto, cobertura integral da turma cadastrada por cinco ciclos
avaliativos consecutivos, e o decaimento a partir do sexto acompanha o encerramento das
atividades previstas no edital.

[[FIG:04-1
  tipo: grafico-barras
  status: criar
  origem: consulta agregada ao banco de produção em 27/07/2026
  dados: mapa-de-fatos §6
  descricao: Gráfico de barras verticais com o número de autoavaliações registradas por unidade avaliativa, das unidades 1 a 9. Valores 33, 33, 33, 33, 33, 7, 3, 1 e 1. Eixo vertical rotulado em número de autoavaliações. Sem qualquer identificação de discente. Texto interno em TNR 18 ou maior, 300 dpi.
  legenda: Figura 3 — Autoavaliações registradas por unidade avaliativa no ciclo de 2025, entre 23 de janeiro e 6 de setembro (n=177). Fonte: dados da pesquisa.
  largura: 1col
  altura_cm: 6
  arquivo: figuras/fig-04-1.png
]]

O decaimento observado a partir da sexta unidade tem consequência direta sobre as duas
regras. A condição de queda depende de comparação com a unidade imediatamente anterior, e a
regra de certificação depende do número de medições disponíveis por competência, de modo
que ambas perdem poder de discriminação à medida que a cobertura se rarefaz. As cinco
unidades de cobertura integral concentram, assim, praticamente toda a capacidade analítica
da base, e é sobre elas que os resultados das subseções seguintes devem ser lidos.

O resultado que sustenta diretamente a tese deste trabalho está no cruzamento entre
competência e discente. A consulta identificou 49 pares competência × discente com duas ou
mais medições registradas, insumo exatamente equivalente ao que o algoritmo de certificação
exige para comparar a menor medição às demais. Sem esses 49 pares não haveria o que
comparar, e a regra de dois terços permaneceria enunciado normativo sem correspondente
computável. A existência do conjunto demonstra que a estrutura de persistência descrita na
subseção 3.3 produz, em operação real, o insumo longitudinal que a camada de decisão
consome.

O contraste com a organização anterior dos dados é o ponto central. Uma planilha em que
cada unidade sobrescreve a nota da competência preserva apenas o estado corrente e reduz a
zero o número de pares comparáveis, independentemente de quantas avaliações tenham sido
efetivamente conduzidas. Por meio da separação entre o evento de avaliação e o valor medido,
a mesma competência do mesmo discente passa a ocupar tantas linhas quantas forem as
unidades, e é essa multiplicação que converte um requisito de regulamento em consulta
executável.

A verificação da aptidão propriamente dita não pôde ser reportada. O filtro de permanência
mínima de 365 dias opera sobre a data de entrada do vínculo mais recente do discente com um
projeto, e os cadastros analisados concentram-se no primeiro trimestre de 2025, de forma que
o resultado do endpoint depende da data em que ele é consultado.
[[VERIFICAR: quantos discentes o endpoint /discentes_aptos_certificacao/ retorna hoje, e em que data a consulta foi feita?]]

### 4.3 Comportamento observado das camadas de decisão e de intervenção

A camada de decisão foi verificada por inspeção do código do método que a implementa e do
endpoint que a expõe, e não por observação de emissões efetivamente filtradas. A regra está
disponível como serviço autenticado e devolve a relação de aptos a partir dos quatro
filtros descritos na subseção 3.4. Já o fluxo de emissão exportado consome a listagem geral
de discentes e produz certificados de participação para todos os retornados, sem aplicar o
filtro. O resultado defensável, portanto, é a disponibilidade da camada de decisão como
serviço, não seu emprego no ato de emissão.

A camada de intervenção opera sobre a mesma base longitudinal e dispensa intervenção humana
entre a leitura das notas e a entrega da mensagem. O fluxo recupera o histórico completo,
ordena as autoavaliações por unidade, aplica as duas condições de disparo, compõe o
documento e o envia por correio eletrônico. A condição de queda depende de medição anterior
persistida e só se torna avaliável a partir da segunda unidade, o que faz da cobertura
descrita na subseção 4.2 o limite superior do que essa camada consegue detectar. Nas cinco
primeiras unidades, com 33 registros cada, a condição esteve disponível em quatro delas.

O envio das mensagens não é persistido em tabela do banco, de modo que o volume entregue
não dispõe de evidência transacional e não é reportado aqui. O mesmo vale para a emissão dos
certificados, cujos artefatos residem em serviço de armazenamento em nuvem, fora do domínio
transacional da aplicação. Ambas as camadas são reportadas como funcionalidades
implementadas e demonstradas em operação, sem afirmação de volume — uma escolha de
enunciação que preserva a correspondência entre o que se afirma e o que a evidência
disponível sustenta.

### 4.4 Tempo de execução

O processo manual que antecedeu a automação consumia 40 minutos por discente, considerando
a coleta das respostas, o cálculo das médias, a produção do gráfico de perfil e a
organização do material para o mentor. No ciclo anterior do projeto, a execução automatizada
do mesmo conjunto de etapas passou a demandar cerca de 12 segundos por discente, redução
superior a 99% do tempo empregado, e produziu mais de 160 relatórios de perfil. No ciclo de
2025, o registro das notas de uma autoavaliação completa passou a ocorrer em 2 a 3 segundos,
e a geração do gráfico com o consequente armazenamento em nuvem, em 12 a 15 segundos. A
[[@TAB:04-2]] reúne as medições.

[[TAB:04-2
  tipo: tabela
  status: criar
  origem: manuscrito do ciclo anterior do projeto (processo manual e ciclo de 2024) e medições da equipe durante a operação de 2025, registradas em mapa-de-fatos §9
  dados: mapa-de-fatos §9
  descricao: Quadro editável comparando o tempo do processo manual, o tempo do ciclo automatizado anterior e os tempos das etapas do ciclo de 2025. Colunas para a etapa, o tempo e o ciclo a que a medição pertence. Corpo em TNR 10.
  legenda: Tabela 2 — Tempo de execução por etapa, do processo manual às etapas automatizadas dos ciclos de 2024 e de 2025. Fonte: dados da pesquisa.
  largura: 1col
  altura_cm: 6
  arquivo: figuras/tab-04-2.md
]]

Os tempos do ciclo de 2025 não são diretamente comparáveis aos 12 segundos do ciclo
anterior, porque medem etapas distintas de um fluxo que foi reorganizado: o cálculo migrou
das planilhas para a interface, e a operação de escrita passou a inserir as dez medições em
lote, dentro de uma única transação. A grandeza que interessa aqui não é o ganho adicional
sobre a automação anterior, que seria marginal, e sim a preservação da ordem de magnitude
alcançada em 2024 mesmo com o acréscimo das duas camadas descritas neste trabalho, das
garantias de integridade referencial e da trilha de auditoria.

Convém delimitar o que essas medições cobrem. Elas dizem respeito ao tempo de execução das
etapas automatizadas, e não ao tempo total do ciclo avaliativo, que permanece determinado
pela disponibilidade dos discentes para responder ao formulário e pela decisão humana de
disparar cada fluxo. O ganho reportado é, portanto, de esforço da equipe, não de duração do
ciclo formativo. Essa distinção importa porque o processo manual de 40 minutos por discente
consumia trabalho qualificado de mentores, que passou a ser realocado para a leitura dos
perfis e para o acompanhamento propriamente dito.

A migração da persistência para a plataforma sem servidor introduziu latência de
inicialização a frio nas primeiras requisições após período de inatividade, característica
esperada desse modelo de execução. Como os fluxos são disparados sob demanda e não em
regime contínuo, essa latência incide com frequência apreciável no início de cada sessão de
trabalho.
[[VERIFICAR: há medição do tempo de inicialização a frio nas primeiras requisições após inatividade?]]

### 4.5 Discussão

O conjunto dos resultados delimita com precisão o que foi demonstrado. Há uma base
constituída em operação real, com 165 notas íntegras, cobertura completa da turma em cinco
unidades consecutivas e 49 pares competência × discente comparáveis longitudinalmente. Sobre
essa base, as duas camadas propostas estão implementadas: a de decisão como serviço
consultável e a de intervenção em execução autônoma até a entrega da mensagem. O que não foi
demonstrado é a escala, e tampouco o efeito pedagógico da devolutiva sobre o desempenho
subsequente dos discentes.

A separação entre esses dois planos é o que permite avaliar a contribuição sem
superestimá-la. O ciclo anterior do projeto já havia demonstrado que a produção de
indicadores é automatizável, com ganho de tempo superior a 99% e mais de 160 relatórios
gerados. O que os resultados acrescentam é que o encerramento do ciclo formativo, que consiste em decidir
quem cumpriu o critério e devolver orientação a quem não o cumpriu, depende de uma
propriedade da camada de dados, e não de sofisticação adicional na camada de orquestração.
Os 49 pares comparáveis são a forma mensurável dessa dependência.

A regra de certificação, ao ser explicitada como algoritmo, revelou-se mais restritiva do
que seu enunciado verbal sugere. Exigir salto de dois pontos na escala, tomar a menor
medição como referência e impor permanência mínima de um ano são decisões que permaneciam
implícitas enquanto o critério era aplicado por leitura de planilha, e que se tornaram
auditáveis ao serem codificadas. Esse ganho de explicitação é independente do ganho de
tempo, e provavelmente o mais relevante para a governança do programa, ainda que o presente
recorte não permita quantificá-lo. A separação entre a lógica de decisão e o fluxo que a
executa é tratada na literatura de gestão de processos como condição para que o critério
possa ser inspecionado e alterado sem que o processo precise ser reconstruído (Bazhenova
et al., 2019).

A divisão de responsabilidades entre orquestração e interface é o que torna o arranjo
transferível para outro programa formativo. Os fluxos de automação não contêm regra de
negócio: eles iteram sobre a relação de discentes e formatam a entrega, enquanto o cálculo das médias, a
agregação das subcompetências e os dois critérios de disparo residem na interface, atrás de
um contrato documentado em padrão aberto (Fielding, 2000). Substituir a matriz de
competências ou o limiar de disparo é alteração localizada, que não exige reconstruir os
fluxos; substituir a ferramenta de orquestração, do mesmo modo, não afeta as regras. Essa
propriedade não foi testada em segundo contexto e permanece como expectativa de projeto,
ainda que a revisão sobre adoção de plataformas de baixo código registre que manter a regra
de negócio fora da ferramenta de orquestração é o que reduz a dependência do fornecedor e
preserva a possibilidade de migração (Ajimati; Carroll; Maher, 2025).

A camada de intervenção, por sua vez, alcança personalização de nível de competência, não de
nível individual. O sistema identifica corretamente qual competência motivou o apontamento e
distingue desempenho baixo estável de trajetória de queda, mas o texto entregue é sorteado
de um banco de práticas organizado por competência. Trata-se de devolutiva dirigida, e não
adaptativa, distinção que precisa acompanhar qualquer leitura dos resultados desta camada.
O limite corresponde ao que a literatura de análise da aprendizagem atribui aos painéis de
natureza descritiva, cuja orientação não decorre de modelo ajustado ao percurso individual
(Susnjak; Ramaswami; Mathrani, 2022), e que os trabalhos de recomendação explicável
procuram superar por meio da vinculação entre a orientação entregue e os fatores
identificados como responsáveis pelo desempenho de cada discente (Afzaal et al., 2021).

A integridade referencial por proteção, adotada em todas as chaves estrangeiras, mostrou-se
compatível com a operação e não produziu bloqueio que exigisse contorno durante o ciclo. A
recusa de exclusão em cascata é o que garante que nenhuma medição desapareça pela remoção de
uma competência ou de um vínculo, condição sem a qual a comparação longitudinal ficaria
sujeita a lacunas silenciosas (Elmasri, 2018). Em um domínio cujo objeto é justamente a
variação de um valor ao longo do tempo, a preservação do histórico é requisito funcional, e
não precaução administrativa.

### 4.6 Limitações

A instância analisada serviu simultaneamente à operação e ao desenvolvimento da solução, de
modo que as contagens de cadastro descrevem o conteúdo da base e não o universo do programa.
Os valores empregados nas análises desta seção não dependem dessa distinção, porque exigem
integridade interna do registro para existir: as 165 notas, os quinze conjuntos completos de
dez itens e os 49 pares competência × discente comparáveis são pisos verificáveis. Nenhuma
inferência sobre desempenho da turma, sobre efeito da intervenção ou sobre comportamento do
sistema em volume maior se sustenta sobre essa base, e o que ela demonstra é a viabilidade
das duas camadas em condições reais de uso.

O instrumento é a autoavaliação, e nenhum mecanismo de controle contra superestimação das
notas foi implementado. A média de 2,47 e o uso integral da escala, de 0,00 a 4,00, indicam
que não houve concentração no extremo superior, mas isso não substitui um procedimento de
validação. A observação textual do mentor, prevista no modelo de dados, oferece o ponto de
ancoragem para essa validação e não foi explorada neste ciclo.

O desenho do estudo também impõe limites. Trata-se de relato de uma implantação conduzida
pela própria equipe que a avalia, sem grupo de comparação e sem instrumento externo de
verificação, condição usual em pesquisa aplicada sobre sistema em operação, mas que restringe
as conclusões ao que é diretamente observável nos artefatos e nos dados persistidos. Os
tempos do processo manual, em particular, provêm do registro do ciclo anterior do projeto e
não foram remedidos neste ciclo, de modo que funcionam como linha de base histórica, e não
como medição controlada.

O acoplamento entre a camada de decisão e a emissão do certificado não está demonstrado, e a
apuração dos artefatos emitidos dependeria de contagem de arquivos em serviço de
armazenamento, não de registro transacional. Somam-se a isso a ausência de agendamento
periódico nos fluxos, que mantém a periodicidade do ciclo sob controle humano, e a latência
decorrente da hospedagem da interface e do banco em região geograficamente distante dos
usuários, para a qual a equipe apontou a hospedagem institucional local como mitigação.
