---
secao: 02-referencial
titulo: Referencial teórico
alvo_palavras: 1600
status: rascunho
---
## 2 Referencial teórico

O objeto deste trabalho reúne três discussões que costumam ser tratadas separadamente na
literatura. A primeira trata da automação de processos administrativos e de sua
aplicação recente em instituições de ensino. A segunda trata das plataformas de baixo
código, que tornaram a construção de fluxos automatizados acessível a equipes pequenas e
levantaram a questão de onde deve residir a regra de negócio. A terceira trata da
avaliação de competências socioemocionais e das condições sob as quais uma medição pode
sustentar uma decisão. As quatro subseções seguintes percorrem essas discussões e
delimitam a lacuna que o ciclo de 2025 do projeto procurou preencher.

### 2.1 Automação de processos e sua aplicação em instituições de ensino

A automação é classificada pela substituição da intervenção humana em tarefas cuja
execução é repetitiva e cujo critério de decisão pode ser antecipado, o que a torna
aplicável tanto a processos industriais quanto a processos administrativos (Groover,
2010). O deslocamento do conceito para o trabalho de escritório trouxe consigo uma
diferença relevante, uma vez que o insumo deixou de ser material e passou a ser
registro, e a qualidade do resultado passou a depender da qualidade do dado disponível
no momento da execução.

Em instituições de ensino, essa transposição foi documentada com maior intensidade a
partir da difusão das ferramentas de automação robótica de processos. A revisão
conduzida por Bhardwaj e Kumar (2025) reúne relatos de aplicação em matrícula,
conferência documental, lançamento de frequência e atendimento a solicitações de
estudantes, e identifica como ganhos recorrentes a redução do tempo de execução e a
diminuição de erros de transcrição. Os mesmos autores observam que a maior parte das
implantações permanece na camada de tarefas administrativas de apoio, sem alcançar
processos que envolvem julgamento acadêmico.

Há ainda um segundo aspecto pouco explorado nos relatos de implantação, referente ao
meio em que o dado produzido pela automação passa a residir. A planilha eletrônica
acumula, na prática de muitos programas, a função de camada de persistência, sem
oferecer as garantias que essa função exige. Não há tipagem obrigatória das colunas, não
há restrição que impeça a exclusão de um registro do qual outro depende e não há
distinção formal entre uma medição nova e a sobrescrita de uma antiga, propriedades que
os sistemas gerenciadores de bancos de dados relacionais oferecem por construção
(Elmasri; Navathe, 2018). O efeito é que a série histórica de um mesmo indivíduo existe
apenas enquanto ninguém reorganizar a planilha.

### 2.2 Plataformas de baixo código e a fronteira entre orquestração e regra de negócio

As plataformas de baixo código e de código zero deslocaram a construção de fluxos
automatizados para fora das equipes de desenvolvimento, ao substituírem a escrita de
código pela composição visual de nós de integração. A revisão sistemática de Ajimati,
Carroll e Maher (2025) identifica como motivadores de adoção a redução do tempo de
entrega e a possibilidade de que profissionais sem formação em programação construam
soluções próprias, prática que a literatura designa por desenvolvimento cidadão. A
ferramenta n8n, empregada neste trabalho, integra essa categoria e permite ainda a
execução em infraestrutura própria (N8n, 2025).

A mesma revisão registra as limitações que acompanham a adoção. As mais citadas são a
dependência em relação ao fornecedor da plataforma, a dificuldade de versionamento e
teste dos artefatos visuais e a degradação da manutenibilidade à medida que a lógica de
negócio se acumula dentro dos fluxos (Ajimati; Carroll; Maher, 2025). O terceiro ponto é
o que condiciona a arquitetura descrita na seção 3, porque um critério de certificação
escrito como sequência de nós não pode ser lido, versionado nem auditado com o mesmo
custo de um critério escrito como código em repositório.

A literatura de gestão de processos de negócio trata dessa fronteira há mais tempo e
chegou a uma formulação explícita. Bazhenova et al. (2019) descrevem a separação entre o
modelo de processo, que define a sequência de atividades, e o modelo de decisão, que
define a lógica aplicada em cada ponto de escolha, e sustentam que manter a segunda fora
da primeira é o que permite alterar o critério sem reconstruir o fluxo. A recomendação
prática é que a regra resida em componente próprio, acessível ao processo por meio de
uma interface estável.

Essa separação encontra na arquitetura de serviços em rede o mecanismo de implementação
correspondente. O estilo arquitetural que orienta a construção de interfaces de
programação sobre o protocolo da web define a interação entre cliente e servidor por
meio de um contrato uniforme, no qual o cliente desconhece a implementação interna do
serviço que consome (Fielding, 2000). Aplicado ao caso da automação, o arranjo permite
que a ferramenta de orquestração invoque um cálculo sem conter o cálculo, e que a
substituição de qualquer uma das duas partes não obrigue a reescrever a outra.

### 2.3 Competências socioemocionais e as condições de sua mensuração

O interesse por competências socioemocionais em programas de formação técnica decorre de
uma constatação recorrente sobre a prática profissional. Munir (2022), ao investigar a
percepção de engenheiros em exercício, verifica que a competência técnica é considerada
insuficiente para o desempenho esperado, e que atributos como comunicação, trabalho
colaborativo e resolução de problemas em equipe são apontados como determinantes em
contextos multidisciplinares. A autora observa que os currículos de engenharia seguem
concentrados na formação técnica, o que sustenta a inclusão dessas competências no
desenho de programas de capacitação.

A mensuração de competências socioemocionais depende, na maior parte das aplicações, de
instrumentos de autoavaliação em escala ordinal, escolha justificada pelo custo de
observação direta e pela natureza dos atributos avaliados. Al-Sa'di et al. (2023), ao
construírem e validaram um instrumento dessa natureza para educadores, descrevem o
procedimento de validação em duas etapas e registram as fragilidades conhecidas do
formato, entre as quais a desejabilidade social e a variação individual na interpretação
dos pontos da escala. A implicação prática é que uma medição isolada carrega incerteza
suficiente para desaconselhar seu uso como base de decisão.

Diante disso, a comparação entre medições sucessivas do mesmo indivíduo torna-se mais
informativa do que o valor absoluto de qualquer uma delas, porque parte do viés
individual tende a se manter constante entre as aplicações. A condição para essa
comparação é de natureza técnica e não metodológica, uma vez que exige que as medições
anteriores permaneçam recuperáveis, associadas ao mesmo discente e à mesma competência,
com o momento de coleta preservado. Bancos de dados relacionais atendem a esse requisito
por meio das restrições de integridade referencial, que impedem que a remoção de um
registro relacionado elimine silenciosamente as medições associadas (Silberschatz;
Korth; Sudarshan, 2020).

### 2.4 Da geração de indicadores à devolutiva acionável

A transformação de dados educacionais em orientação para o estudante é o objeto do campo
de análise da aprendizagem, no qual os painéis de acompanhamento constituem o artefato
mais difundido. Uma revisão de painéis recentes (Susnjak; Ramaswami; Mathrani, 2022)
verifica que a quase totalidade deles opera em nível descritivo, apresentando ao
estudante a sua posição atual sem indicar que providência tomar, lacuna que os autores
caracterizam como ausência de análise prescritiva. A apresentação de indicadores,
isoladamente, não produz a mudança de comportamento que justificaria a sua produção.

A superação dessa lacuna tem sido buscada por meio da vinculação entre a orientação
entregue e as causas identificadas no desempenho. Afzaal et al. (2021) combinam predição
de desempenho com técnicas de explicabilidade para gerar recomendações que indicam quais
fatores respondem pelo resultado projetado e que ação corretiva corresponde a cada um,
argumentando que a informação sobre o resultado provável, desacompanhada da explicação,
não sustenta a autorregulação do estudante. O trabalho evidencia que a devolutiva útil
depende de dados históricos suficientes para que a causa seja identificável.

A mesma dependência aparece do lado da decisão institucional. Um critério de
certificação que compare o desempenho de um discente com o seu próprio desempenho
anterior só pode ser executado sobre uma base que preserve as medições de todas as
unidades avaliativas, com a associação entre discente e competência mantida ao longo do
tempo. A alternativa usual, que consiste em aplicar o critério sobre a medição mais
recente, mede posição e não trajetória, e responde a uma pergunta diferente daquela que
o programa formula.