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

A ordem de apresentação acompanha o argumento construído nas seções anteriores.
Descreve-se primeiro a base de dados constituída, depois a cobertura longitudinal que ela
oferece e a consequente computabilidade da regra de certificação, em seguida o
comportamento observado da camada de intervenção e os tempos de execução, e por fim a
discussão do conjunto e as limitações que ele impõe. Os dados são reportados sem
interpretação nas subseções 4.1 a 4.4; a leitura à luz do problema formulado na introdução
concentra-se nas subseções 4.5 e 4.6.

### 4.1 A base de dados constituída no ciclo de 2025

A consulta de 27 de julho de 2026 encontrou 33 discentes cadastrados, com datas de
registro entre 23 de janeiro e 1º de abril de 2025, vinculados a três projetos sob
acompanhamento de dois mentores. Foram contabilizados 177 registros de autoavaliação,
abertos entre 23 de janeiro e 6 de setembro de 2025 e distribuídos em nove unidades. A
tabela de notas reúne 165 registros, dos quais 105 vinculados a competências macro e 60 a
subcompetências de inteligência emocional. As notas ocupam integralmente a escala
prevista, de 0,00 a 4,00, com média de 2,47, valor situado na faixa qualitativa adequada.
A [[@TAB:04-1]] consolida o conjunto.

[[TAB:04-1
  tipo: tabela
  status: pronto
  origem: consulta agregada ao banco de produção em 27/07/2026, registrada em mapa-de-fatos §6
  dados: mapa-de-fatos §6
  descricao: Quadro editável com as métricas agregadas do banco em 27/07/2026, em dois pares de colunas, métrica e valor. Linhas: discentes cadastrados, registros de autoavaliação, conjuntos completos de medições, discentes com notas lançadas, notas por tipo, faixa e média das notas, pares competência x discente com duas ou mais medições, mentores, projetos e registros de auditoria. Acrescentar uma linha com a distribuição dos registros pelas nove unidades (33, 33, 33, 33, 33, 7, 3, 1, 1), que substitui o gráfico de barras antes previsto. Nenhum dado individual. Corpo em TNR 10.
  legenda: Tabela 1 — Caracterização agregada da base de produção do ciclo de 2025, apurada em 27 de julho de 2026 (n=33 discentes), incluindo a distribuição dos registros de autoavaliação pelas nove unidades. Fonte: dados da pesquisa.
  largura: 1col
  altura_cm: 8
  arquivo: figuras/tab-04-1.md
]]

A distribuição das 165 notas entre os dois níveis da matriz é regular e confirma a
consistência do desdobramento descrito na subseção 3.1. Cada conjunto completo ocupa onze
linhas na tabela de notas: seis notas de competência macro, quatro notas de subcompetência
e uma nota macro adicional para inteligência emocional, que a interface calcula como a
média das quatro subcompetências no momento da gravação. As 105 notas macro e as 60 de
subcompetência correspondem, assim, a quinze conjuntos completos, cada um reunindo dez
medições independentes, sem registro parcial que exigisse tratamento de valor ausente no
cálculo das duas regras.

Esses quinze conjuntos distribuem-se por sete discentes e correspondem a quinze dos 177
registros de autoavaliação contabilizados. Os demais registros não têm notas associadas,
condição coerente com o uso da mesma instância como ambiente de operação e de
desenvolvimento, discutido na subseção 4.6. A consequência para a leitura dos resultados é
direta: a contagem de autoavaliações mede o volume de eventos gravados, ao passo que a
contagem de notas mede o material efetivamente disponível para análise, e é esta segunda
grandeza que limita todas as afirmações das subseções seguintes.

A tabela de auditoria do painel administrativo acumulou 1.792 registros no período, contra
177 registros de autoavaliação persistidos. Cada entrada corresponde a uma operação de
escrita conduzida por meio do painel, e não a uma consulta, de modo que o número
dimensiona a intervenção manual sobre a base durante a estabilização do fluxo de cadastro.
O valor interessa em dois sentidos: demonstra que a trilha de auditoria descrita na
subseção 3.3 opera de fato, e não apenas como declaração de esquema, e quantifica o
trabalho de correção que acompanhou o uso da instância também como ambiente de
desenvolvimento.

### 4.2 Cobertura longitudinal e computabilidade da regra de certificação

A distribuição dos registros de autoavaliação pelas nove unidades é fortemente
assimétrica, conforme a [[@TAB:04-1]]. As cinco primeiras unidades apresentam 33 registros
cada, e da sexta em diante o número decai para 7, 3, 1 e 1. Esses valores contam eventos
de avaliação gravados, e não medições realizadas: como as 165 notas se distribuem em
quinze conjuntos, no máximo quinze dos 165 registros das cinco primeiras unidades carregam
nota associada. A assimetria descreve, portanto, o conteúdo da base, e não a adesão dos
participantes ao instrumento ao longo do tempo.

O decaimento observado a partir da sexta unidade tem consequência direta sobre as duas
regras. A condição de queda depende de comparação com a unidade imediatamente anterior, e
a regra de certificação depende do número de medições disponíveis por competência, de modo
que ambas perdem poder de discriminação à medida que as medições se rarefazem. Os quinze
conjuntos completos concentram, assim, toda a capacidade analítica da base, e é sobre eles
que os resultados das subseções seguintes devem ser lidos.

O resultado que sustenta diretamente a tese deste trabalho está no cruzamento entre
competência e discente. A consulta identificou 49 pares competência × discente com duas ou
mais medições registradas, insumo exatamente equivalente ao que o algoritmo de
certificação exige para comparar a menor medição às demais. Sem esses 49 pares não haveria
o que comparar, e a regra de dois terços permaneceria enunciado normativo sem
correspondente computável. A existência do conjunto demonstra que a estrutura de
persistência descrita na subseção 3.3 produz, em operação real, o insumo longitudinal que
a camada de decisão consome.

A forma como essa comparação chega ao mentor está reproduzida na [[@FIG:04-1]],
construída com dados sintéticos: o gráfico de perfil sobrepõe as medições de duas
unidades sucessivas sobre os mesmos eixos, e é dessa sobreposição que tanto a leitura
humana quanto as duas regras extraem a variação de cada competência.

[[FIG:04-1
  tipo: grafico-linhas
  status: pronto
  origem: elaborado a partir do formato de saída do fluxo "graficos", com valores sintéticos construídos para este artigo
  dados: valores sintéticos; a numeração dos eixos segue o Quadro 1
  descricao: Gráfico radar com os sete eixos das competências macro, numerados conforme o Quadro 1, e duas unidades sobrepostas em escala de 0 a 4. Sem nome e sem dado de discente real.
  legenda: Figura 3 — Gráfico de perfil de competências macro, com duas unidades sucessivas sobrepostas em escala de 0 a 4. Exemplo sintético, construído para ilustrar o formato da saída, sem dado de discente. Fonte: elaborado pelos autores.
  largura: 1col
  altura_cm: 9
  arquivo: figuras/fig-04-1.png
]]

O contraste com a organização anterior dos dados é o ponto central. Uma planilha em que
cada unidade sobrescreve a nota da competência preserva apenas o estado corrente e reduz a
zero o número de pares comparáveis, independentemente de quantas avaliações tenham sido
efetivamente conduzidas. Por meio da separação entre o evento de avaliação e o valor
medido, a mesma competência do mesmo discente passa a ocupar tantas linhas quantas forem
as unidades, e é essa multiplicação que converte um requisito de regulamento em consulta
executável.

A verificação da aptidão propriamente dita não pôde ser reportada. O filtro de permanência
mínima de 365 dias opera sobre a data de entrada do vínculo mais recente do discente com
um projeto, e os cadastros analisados concentram-se no primeiro trimestre de 2025, de
forma que o resultado do endpoint depende da data em que ele é consultado. A instância de
banco utilizada no ciclo foi posteriormente desativada, de modo que a contagem de
discentes retornada pelo endpoint não pôde ser apurada nem reproduzida. O que a base
sustenta é a computabilidade da regra, evidenciada pelos 49 pares competência × discente
com duas ou mais medições, e não o número de discentes que a satisfariam em uma data
determinada.

### 4.3 Comportamento observado das camadas de decisão e de intervenção

A camada de decisão foi verificada por inspeção do código do método que a implementa e do
endpoint que a expõe, e não por observação de emissões efetivamente filtradas. A regra
está disponível como serviço autenticado e devolve a relação de aptos a partir dos quatro
filtros descritos na subseção 3.4. Já o fluxo de emissão exportado consome a listagem
geral de discentes e produz certificados de participação para todos os retornados, sem
aplicar o filtro. O resultado defensável, portanto, é a disponibilidade da camada de
decisão como serviço, não seu emprego no ato de emissão.

A camada de intervenção opera sobre a mesma base longitudinal e dispensa intervenção
humana entre a leitura das notas e a entrega da mensagem. O fluxo recupera o histórico
completo, ordena as autoavaliações por unidade, aplica as duas condições de disparo,
compõe o documento e o envia por correio eletrônico. A condição de queda depende de
medição anterior persistida e só se torna avaliável a partir da segunda unidade, o que faz
do volume de medições descrito na subseção 4.2 o limite superior do que essa camada
consegue detectar. O conjunto sobre o qual a condição pode ser verificada corresponde aos
49 pares competência × discente com duas ou mais medições.

Os artefatos que as duas camadas entregam estão reproduzidos na [[@FIG:04-2]], também
em exemplos sintéticos, uma vez que nenhum documento emitido para discente real pode ser
reproduzido em publicação aberta. O certificado registra a participação no programa, e a
mensagem de recomendação nomeia a competência apontada, a condição que disparou o
apontamento e a prática sugerida.

[[FIG:04-2
  tipo: diagrama-arquitetura
  status: pronto
  origem: elaborado a partir do modelo de documento do workflow "Certificados" e do template HTML do workflow "Gera recomendações"
  dados: exemplos sintéticos construídos para este artigo
  descricao: Dois painéis lado a lado, esquemáticos. À esquerda o certificado de participação, com nome fictício declarado como tal. À direita a mensagem de recomendação, com competência, motivo do disparo e prática sugerida. Sem dado de discente real.
  legenda: Figura 4 — Certificado de participação e mensagem de recomendação pedagógica, os dois artefatos entregues pelas camadas de decisão e de intervenção. Exemplos sintéticos, sem dado de discente. Fonte: elaborado pelos autores.
  largura: 1col
  altura_cm: 7
  arquivo: figuras/fig-04-2.png
]]

O envio das mensagens não é persistido em tabela do banco, de modo que o volume entregue
não dispõe de evidência transacional e não é reportado aqui. O mesmo vale para a emissão
dos certificados, cujos artefatos residem em serviço de armazenamento em nuvem, fora do
domínio transacional da aplicação. Ambas as camadas são reportadas como funcionalidades
implementadas e demonstradas em operação, sem afirmação de volume — uma escolha de
enunciação que preserva a correspondência entre o que se afirma e o que a evidência
disponível sustenta.

### 4.4 Tempo de execução

O processo manual que antecedeu a automação consumia 40 minutos por discente, considerando
a coleta das respostas, o cálculo das médias, a produção do gráfico de perfil e a
organização do material para o mentor. No ciclo anterior do projeto, a execução
automatizada do mesmo conjunto de etapas passou a demandar cerca de 12 segundos por
discente, redução superior a 99% do tempo empregado, e produziu mais de 160 relatórios de
perfil. No ciclo de 2025, o registro das notas de uma autoavaliação completa passou a
ocorrer em 2 a 3 segundos, e a geração do gráfico com o consequente armazenamento em
nuvem, em 12 a 15 segundos. A [[@TAB:04-2]] reúne as medições.

[[TAB:04-2
  tipo: tabela
  status: pronto
  origem: manuscrito do ciclo anterior do projeto (processo manual e ciclo de 2024) e medições da equipe durante a operação de 2025, registradas em mapa-de-fatos §9
  dados: mapa-de-fatos §9
  descricao: Quadro editável comparando o tempo do processo manual, o tempo do ciclo automatizado anterior e os tempos das etapas do ciclo de 2025. Colunas para a etapa, o tempo e o ciclo a que a medição pertence. Corpo em TNR 10.
  legenda: Tabela 2 — Tempo de execução por etapa, do processo manual às etapas automatizadas dos ciclos de 2024 e de 2025. Fonte: dados da pesquisa.
  largura: 1col
  altura_cm: 5
  arquivo: figuras/tab-04-2.md
]]

Os tempos do ciclo de 2025 não são diretamente comparáveis aos 12 segundos do ciclo
anterior, porque medem etapas distintas de um fluxo que foi reorganizado: o cálculo migrou
das planilhas para a interface, e a operação de escrita passou a gravar as medições de uma
autoavaliação dentro de uma única transação. A grandeza que interessa aqui não é o ganho
adicional sobre a automação anterior, que seria marginal, e sim a preservação da ordem de
magnitude alcançada em 2024 mesmo com o acréscimo das duas camadas descritas neste
trabalho, das garantias de integridade referencial e da trilha de auditoria.

Essas medições cobrem um recorte específico. Elas dizem respeito ao tempo de execução das
etapas automatizadas, e não ao tempo total do ciclo avaliativo, que permanece determinado
pela disponibilidade dos discentes para responder ao formulário e pela decisão humana de
disparar cada fluxo. O ganho reportado é, portanto, de esforço da equipe, não de duração
do ciclo formativo. Essa distinção importa porque o processo manual de 40 minutos por
discente consumia trabalho qualificado de mentores, que passou a ser realocado para a
leitura dos perfis e para o acompanhamento propriamente dito.

A migração da persistência para a plataforma sem servidor introduziu latência de
inicialização a frio nas primeiras requisições após período de inatividade, característica
esperada desse modelo de execução. Como os fluxos são disparados sob demanda e não em
regime contínuo, essa latência incide com frequência apreciável no início de cada sessão
de trabalho. Os tempos reportados nesta subseção foram cronometrados em condições
correntes de uso, sem que a primeira requisição após inatividade fosse isolada das demais,
e portanto já incorporam a inicialização a frio quando ela ocorreu. Os valores descrevem,
assim, o comportamento percebido pelo operador, e não o melhor caso com a função
previamente ativa.

### 4.5 Discussão

O conjunto dos resultados delimita com precisão o que foi demonstrado. Há uma base
constituída em operação real, com 165 notas reunidas em quinze conjuntos completos de
medições e 49 pares competência × discente comparáveis longitudinalmente. Sobre essa base,
as duas camadas propostas estão implementadas: a de decisão como serviço consultável e a
de intervenção em execução autônoma até a entrega da mensagem. O que não foi demonstrado é
a escala, e tampouco o efeito pedagógico da devolutiva sobre o desempenho subsequente dos
discentes.

A separação entre esses dois planos é o que permite avaliar a contribuição sem
superestimá-la. O ciclo anterior do projeto já havia demonstrado que a produção de
indicadores é automatizável, com ganho de tempo superior a 99% e mais de 160 relatórios
gerados. O que os resultados acrescentam é que o encerramento do ciclo formativo, que
consiste em decidir quem cumpriu o critério e devolver orientação a quem não o cumpriu,
depende de uma propriedade da camada de dados, e não de sofisticação adicional na camada
de orquestração. Os 49 pares comparáveis são a forma mensurável dessa dependência.

A regra de certificação, ao ser explicitada como algoritmo, revelou-se mais restritiva do
que seu enunciado verbal sugere. Exigir salto de dois pontos na escala, tomar a menor
medição como referência e impor permanência mínima de um ano são decisões que permaneciam
implícitas enquanto o critério era aplicado por leitura de planilha, e que se tornaram
auditáveis ao serem codificadas. Esse ganho de explicitação é independente do ganho de
tempo, e provavelmente o mais relevante para a governança do programa, ainda que o
presente recorte não permita quantificá-lo. A separação entre a lógica de decisão e o
fluxo que a executa é tratada na literatura de gestão de processos como condição para que
o critério possa ser inspecionado e alterado sem que o processo precise ser reconstruído
(Bazhenova et al., 2019).

A divisão de responsabilidades entre orquestração e interface é o que torna o arranjo
transferível para outro programa formativo. Os fluxos de automação não contêm regra de
negócio: eles iteram sobre a relação de discentes e formatam a entrega, enquanto o cálculo
das médias, a agregação das subcompetências e os dois critérios de disparo residem na
interface, atrás de um contrato uniforme que oculta do cliente a implementação do serviço
consumido (Fielding, 2000) e é publicado em padrão aberto de documentação. Substituir a
matriz de competências ou o limiar de disparo é alteração localizada, que não exige
reconstruir os fluxos; substituir a ferramenta de orquestração, do mesmo modo, não afeta
as regras. Essa propriedade não foi testada em segundo contexto e permanece como
expectativa de projeto, ainda que a revisão sobre adoção de plataformas de baixo código
registre que manter a regra de negócio fora da ferramenta de orquestração é o que reduz a
dependência do fornecedor e preserva a possibilidade de migração (Ajimati; Carroll; Maher,
2025).

A camada de intervenção, por sua vez, alcança personalização de nível de competência, não
de nível individual. O sistema identifica corretamente qual competência motivou o
apontamento e distingue desempenho baixo estável de trajetória de queda, mas o texto
entregue é sorteado de um banco de práticas organizado por competência. Trata-se de
devolutiva dirigida, e não adaptativa, distinção que precisa acompanhar qualquer leitura
dos resultados desta camada. O limite corresponde ao que a literatura de análise da
aprendizagem atribui aos painéis de natureza descritiva, cuja orientação não decorre de
modelo ajustado ao percurso individual (Susnjak; Ramaswami; Mathrani, 2022), e que os
trabalhos de recomendação explicável procuram superar por meio da vinculação entre a
orientação entregue e os fatores identificados como responsáveis pelo desempenho de cada
discente (Afzaal et al., 2021).

A integridade referencial por proteção, adotada em todas as chaves estrangeiras,
mostrou-se compatível com a operação e não produziu bloqueio que exigisse contorno durante
o ciclo. A recusa de exclusão em cascata é o que garante que nenhuma medição desapareça
pela remoção de uma competência ou de um vínculo, condição sem a qual a comparação
longitudinal ficaria sujeita a lacunas silenciosas (Elmasri; Navathe, 2018). Em um domínio
cujo objeto é justamente a variação de um valor ao longo do tempo, a preservação do
histórico é requisito funcional, e não precaução administrativa.

### 4.6 Limitações

A instância analisada serviu simultaneamente à operação e ao desenvolvimento da solução,
de modo que as contagens de cadastro descrevem o conteúdo da base e não o universo do
programa. Os valores empregados nas análises desta seção não dependem dessa distinção,
porque exigem integridade interna do registro para existir: as 165 notas, os quinze
conjuntos completos de dez itens e os 49 pares competência × discente comparáveis são
pisos verificáveis. Nenhuma inferência sobre desempenho da turma, sobre efeito da
intervenção ou sobre comportamento do sistema em volume maior se sustenta sobre essa base,
e o que ela demonstra é a viabilidade das duas camadas em condições reais de uso.

O instrumento é a autoavaliação, e nenhum mecanismo de controle contra superestimação das
notas foi implementado. A média de 2,47 e o uso integral da escala, de 0,00 a 4,00,
indicam que não houve concentração no extremo superior, mas isso não substitui um
procedimento de validação. A observação textual do mentor, prevista no modelo de dados,
oferece o ponto de ancoragem para essa validação e não foi explorada neste ciclo.

O desenho do estudo também impõe limites. Trata-se de relato de uma implantação conduzida
pela própria equipe que a avalia, sem grupo de comparação e sem instrumento externo de
verificação, condição usual em pesquisa aplicada sobre sistema em operação, mas que
restringe as conclusões ao que é diretamente observável nos artefatos e nos dados
persistidos. Os tempos do processo manual, em particular, provêm do registro do ciclo
anterior do projeto e não foram remedidos neste ciclo, de modo que funcionam como linha de
base histórica, e não como medição controlada.

O acoplamento entre a camada de decisão e a emissão do certificado não está demonstrado, e
a apuração dos artefatos emitidos dependeria de contagem de arquivos em serviço de
armazenamento, não de registro transacional. Somam-se a isso a ausência de agendamento
periódico nos fluxos, que mantém a periodicidade do ciclo sob controle humano, e a
latência decorrente da hospedagem da interface e do banco em região geograficamente
distante dos usuários, para a qual a equipe apontou a hospedagem institucional local como
mitigação. O orquestrador, por sua vez, foi executado em contêiner instalado em estação de
trabalho de um integrante da equipe, e não em serviço mantido pela instituição, condição
que limita a continuidade da operação para além do período do vínculo desse integrante.
