## 1 Introdução

Programas de capacitação profissional voltados à formação para a inovação têm incorporado
ao seu desenho o acompanhamento sistemático de competências socioemocionais, tratadas como
objeto de avaliação periódica e não como resultado tácito da convivência em projeto. O
programa Capacitação 4.0, que constitui o contexto deste trabalho, opera segundo essa
orientação e estabelece uma matriz de sete competências macro, quatro subcompetências
vinculadas à inteligência emocional e uma escala de zero a quatro pontos, aplicada ao final
de cada unidade avaliativa do percurso do discente (Embrapii, 2021).

O acompanhamento assim desenhado produz, a cada unidade, um volume de medições que cresce
com o produto entre o número de participantes e o número de competências avaliadas, e o
trabalho de consolidação desse volume era conduzido manualmente em planilhas eletrônicas
mantidas pelos mentores do programa. O registro do ciclo anterior do projeto indica um custo
aproximado de quarenta minutos por discente para reunir as notas, produzir os gráficos de
acompanhamento e organizar o material devolvido. A carga imposta à equipe era, assim,
proporcional ao tamanho da turma e independente do valor analítico do resultado obtido.

Esse arranjo foi o alvo do ciclo de 2024 do projeto, que automatizou a coleta e a
consolidação por meio de fluxos construídos em ferramenta de baixo código. Esses fluxos
integravam-se a uma interface de programação de aplicações responsável pelo armazenamento das
notas, e produziam automaticamente os gráficos radar e as tabelas de acompanhamento. O tempo
de processamento por discente caiu para cerca de doze segundos, e a produção dos indicadores
deixou de depender da disponibilidade do mentor. O ganho é expressivo no eixo em que foi
medido, e é justamente a delimitação desse eixo que motiva o presente trabalho.

A automação entregue naquele ciclo encerrava-se na produção do indicador. O gráfico chegava
ao mentor, e permaneciam humanas as duas etapas que efetivamente fecham um ciclo formativo:
decidir se o percurso do discente satisfaz o critério que autoriza a certificação e devolver
a ele uma orientação capaz de alterar o desempenho antes da unidade seguinte. Ambas as
etapas eram executadas por leitura visual dos gráficos. A redução do tempo de consolidação
não se converteu, portanto, em redução do tempo até a decisão, que permanecia como gargalo
real do processo.

Há uma segunda limitação, menos visível e de consequência mais ampla, que diz respeito ao
meio em que as medições passaram a residir. A planilha eletrônica acumulava a função de
camada de persistência sem oferecer as garantias que essa função exige. Nada impede que uma
medição anterior seja sobrescrita, a nota não fica formalmente vinculada ao discente e à
competência que a originaram, e o momento da coleta se perde quando o arquivo é reorganizado
entre unidades. A série histórica de cada participante existia, portanto, por convenção de
uso, e não por construção.

Essa fragilidade importa porque os dois critérios que o programa formula são comparativos e
não pontuais. A certificação, tal como enunciada pela coordenação, exige evidência de
evolução em pelo menos dois terços das competências avaliadas, e a recomendação pedagógica
deve alcançar o discente cujo desempenho caiu em relação à unidade anterior, mesmo quando a
nota permanece dentro da faixa considerada adequada. Nenhum dos dois pode ser computado sobre
a medição mais recente isoladamente. Ambos perguntam como a competência variou entre unidades
sucessivas, e não em que ponto ela se encontra agora.

Diante disso, o problema que orienta este trabalho pode ser formulado nos seguintes termos:
quais componentes uma automação de ciclo formativo precisa incorporar para que a decisão de
certificação e a devolutiva ao discente deixem de depender de leitura manual de
indicadores, e que condições de persistência de dados essas duas camadas impõem à
arquitetura que as sustenta. A pergunta é de natureza arquitetural antes de ser de natureza
pedagógica, porque a viabilidade de ambas as camadas depende de uma propriedade da base de
dados que a planilha não oferece.

O objetivo geral consiste em descrever e avaliar a solução construída no ciclo de 2025 do
projeto, que estendeu a automação existente com uma camada de decisão e uma camada de
intervenção assentadas sobre persistência relacional com rastreabilidade histórica.
Especificamente, o trabalho descreve o modelo de dados adotado e as restrições de integridade
que preservam a série de medições. Apresenta também a operacionalização do critério de
certificação como consulta computável exposta em serviço, o fluxo de recomendação pedagógica
com envio autônomo por correio eletrônico e a caracterização da base efetivamente constituída
durante a operação.

A contribuição sobre o ciclo anterior está no deslocamento do limite da automação. Enquanto
o trabalho de 2024 respondia à pergunta de como produzir o indicador em menos tempo, o de
2025 responde à de como produzir a decisão e a intervenção a partir dele. Esse deslocamento
exige tanto a formalização do critério em código auditável quanto a substituição da planilha
por um banco de dados relacional capaz de responder pela trajetória de cada competência.
Somam-se a isso a migração da infraestrutura de hospedagem, conduzida no mesmo período, e a
exposição da regra de certificação como serviço consumível por qualquer cliente autorizado.

O relato apoia-se em evidência de operação real e não em ambiente construído para o
experimento, o que define tanto o seu alcance quanto os seus limites. A base analisada reúne
as autoavaliações registradas por trinta e três discentes ao longo de nove unidades
avaliativas do ciclo de 2025. Ela sustenta afirmações sobre a viabilidade das camadas
propostas em condições de uso, sem autorizar afirmação sobre escala ou sobre efeito
pedagógico da intervenção. Todos os dados utilizados são operacionais do próprio programa e
foram tratados de forma agregada, sem que qualquer registro individual seja reportado.

O texto está organizado em cinco seções. A seção 2 reúne a literatura sobre automação de
processos em instituições de ensino, sobre plataformas de baixo código e a fronteira entre
orquestração e regra de negócio, e sobre as condições de mensuração de competências
socioemocionais, delimitando a lacuna que o trabalho ocupa. A seção 3 descreve o método,
incluindo o recorte do estudo, a arquitetura da solução, o modelo de dados e a formulação
exata das regras de certificação e de recomendação. Nela também se registra o tratamento dado
aos dados pessoais. A seção 4 apresenta a base constituída, a cobertura longitudinal que ela
oferece, o comportamento observado das duas camadas e os tempos de execução, seguidos da
discussão desses resultados à luz da literatura e das limitações do estudo. A seção 5 retoma o
objetivo, sintetiza o que a evidência sustenta e aponta os desdobramentos previstos para os
ciclos seguintes.

## 2 Referencial teórico

O objeto deste trabalho reúne três discussões que costumam ser tratadas separadamente na
literatura. A primeira trata da automação de processos administrativos e de sua aplicação
recente em instituições de ensino. A segunda trata das plataformas de baixo código, que
tornaram a construção de fluxos automatizados acessível a equipes pequenas e levantaram a
questão de onde deve residir a regra de negócio. A terceira trata da avaliação de
competências socioemocionais e das condições sob as quais uma medição pode sustentar
decisão. As quatro subseções seguintes percorrem essas discussões e delimitam a lacuna que
o ciclo de 2025 do projeto procurou preencher.

### 2.1 Automação de processos e sua aplicação em instituições de ensino

A automação é classicamente definida pela substituição da intervenção humana em tarefas
cuja execução é repetitiva e cujo critério de decisão pode ser antecipado, o que a torna
aplicável tanto a processos industriais quanto a processos administrativos (Groover, 2010).
O deslocamento do conceito para o trabalho de escritório trouxe consigo uma diferença
relevante, uma vez que o insumo deixou de ser material e passou a ser registro, e a
qualidade do resultado passou a depender da qualidade do dado disponível no momento da
execução.

Em instituições de ensino, essa transposição foi documentada com maior intensidade a partir
da difusão das ferramentas de automação robótica de processos. A revisão conduzida por
Bhardwaj e Kumar (2025) reúne relatos de aplicação em matrícula, conferência documental,
lançamento de frequência e atendimento a solicitações de estudantes, e identifica como
ganhos recorrentes a redução do tempo de execução e a diminuição de erros de transcrição.
Os mesmos autores observam que a maior parte das implantações permanece na camada de
tarefas administrativas de apoio, sem alcançar processos que envolvem julgamento acadêmico.

Essa concentração explica um padrão que interessa diretamente ao presente trabalho. Os
processos automatizados com maior frequência são aqueles cujo produto é um documento ou um
registro, e não aqueles cujo produto é uma decisão sobre o percurso formativo de alguém.
Por meio da automação da coleta e da consolidação de dados, uma instituição obtém
indicadores em menos tempo, sem que isso altere quem decide o que fazer com eles nem em que
base a decisão é tomada. A etapa de decisão permanece manual, apoiada na leitura de
planilhas produzidas pela própria automação.

Há ainda um segundo aspecto pouco explorado nos relatos de implantação, referente ao meio
em que o dado produzido pela automação passa a residir. A planilha eletrônica acumula, na
prática de muitos programas, a função de camada de persistência, sem oferecer as garantias
que essa função exige. Não há tipagem obrigatória das colunas, não há restrição que impeça
a exclusão de um registro do qual outro depende e não há distinção formal entre uma medição
nova e a sobrescrita de uma antiga, propriedades que os sistemas gerenciadores de bancos de
dados relacionais oferecem por construção (Elmasri; Navathe, 2018). O efeito é que a série
histórica de um mesmo indivíduo existe apenas enquanto ninguém reorganizar a planilha.

### 2.2 Plataformas de baixo código e a fronteira entre orquestração e regra de negócio

As plataformas de baixo código e de código zero deslocaram a construção de fluxos
automatizados para fora das equipes de desenvolvimento, ao substituírem a escrita de código
pela composição visual de nós de integração. A revisão sistemática de Ajimati, Carroll e
Maher (2025) identifica como motivadores de adoção a redução do tempo de entrega e a
possibilidade de que profissionais sem formação em programação construam soluções próprias,
prática que a literatura designa por desenvolvimento cidadão. A ferramenta n8n, empregada
neste trabalho, integra essa categoria e permite ainda a execução em infraestrutura própria
(N8n, 2025).

A mesma revisão registra as limitações que acompanham a adoção. As mais citadas são a
dependência em relação ao fornecedor da plataforma, a dificuldade de versionamento e teste
dos artefatos visuais e a degradação da manutenibilidade à medida que a lógica de negócio
se acumula dentro dos fluxos (Ajimati; Carroll; Maher, 2025). O terceiro ponto é o que
condiciona a arquitetura descrita na seção 3, porque um critério de certificação escrito
como sequência de nós não pode ser lido, versionado nem auditado com o mesmo custo de um
critério escrito como código em repositório.

A literatura de gestão de processos de negócio trata dessa fronteira há mais tempo e chegou
a uma formulação explícita. Bazhenova et al. (2019) descrevem a separação entre o modelo de
processo, que define a sequência de atividades, e o modelo de decisão, que define a lógica
aplicada em cada ponto de escolha, e sustentam que manter a segunda fora da primeira é o
que permite alterar o critério sem reconstruir o fluxo. A recomendação prática é que a
regra resida em componente próprio, acessível ao processo por meio de uma interface
estável.

Essa separação encontra na arquitetura de serviços em rede o mecanismo de implementação
correspondente. O estilo arquitetural que orienta a construção de interfaces de programação
sobre o protocolo da web define a interação entre cliente e servidor por meio de um
contrato uniforme, no qual o cliente desconhece a implementação interna do serviço que
consome (Fielding, 2000). Aplicado ao caso da automação, o arranjo permite que a ferramenta
de orquestração invoque um cálculo sem conter o cálculo, e que a substituição de qualquer
uma das duas partes não obrigue a reescrever a outra.

### 2.3 Competências socioemocionais e as condições de sua mensuração

O interesse por competências socioemocionais em programas de formação técnica decorre de
uma constatação recorrente sobre a prática profissional. Munir (2022), ao investigar a
percepção de engenheiros em exercício, verifica que a competência técnica é considerada
insuficiente para o desempenho esperado, e que atributos como comunicação, trabalho
colaborativo e resolução de problemas em equipe são apontados como determinantes em
contextos multidisciplinares. A autora observa que os currículos de engenharia seguem
concentrados na formação técnica, o que sustenta a inclusão dessas competências no desenho
de programas de capacitação.

O programa que constitui o contexto deste trabalho incorpora essa orientação em sua própria
estrutura de operação, ao estabelecer uma matriz de competências socioemocionais e uma
escala de avaliação aplicadas ao acompanhamento dos participantes (Embrapii, 2021). A
matriz não foi definida por esta pesquisa e é tomada como dado do contexto, de modo que a
discussão pertinente aqui não é a de quais competências avaliar, mas a de como tratar as
medições produzidas por esse instrumento.

A mensuração de competências socioemocionais depende, na maior parte das aplicações, de
instrumentos de autoavaliação em escala ordinal, escolha justificada pelo custo de
observação direta e pela natureza dos atributos avaliados. Al-Sa'di et al. (2023), ao
construírem e validarem um instrumento dessa natureza para educadores, descrevem o
procedimento de validação em duas etapas e registram as fragilidades conhecidas do formato,
entre as quais a desejabilidade social e a variação individual na interpretação dos pontos
da escala. A implicação prática é que uma medição isolada carrega incerteza suficiente para
desaconselhar seu uso como base de decisão.

Diante disso, a comparação entre medições sucessivas do mesmo indivíduo torna-se mais
informativa do que o valor absoluto de qualquer uma delas, porque parte do viés individual
tende a se manter constante entre as aplicações. A condição para essa comparação é de
natureza técnica e não metodológica, uma vez que exige que as medições anteriores
permaneçam recuperáveis, associadas ao mesmo discente e à mesma competência, com o momento
de coleta preservado. Bancos de dados relacionais atendem a esse requisito por meio das
restrições de integridade referencial, que impedem que a remoção de um registro relacionado
elimine silenciosamente as medições associadas (Silberschatz; Korth; Sudarshan, 2020).

### 2.4 Da geração de indicadores à devolutiva acionável

A transformação de dados educacionais em orientação para o estudante é o objeto do campo de
análise da aprendizagem, no qual os painéis de acompanhamento constituem o artefato mais
difundido. Uma revisão de painéis recentes verifica que a quase
totalidade deles opera em nível descritivo, apresentando ao estudante a sua posição atual
sem indicar que providência tomar, lacuna que os autores caracterizam como ausência de
análise prescritiva (Susnjak; Ramaswami; Mathrani, 2022). A apresentação de indicadores,
isoladamente, não produz a mudança de comportamento que justificaria a sua produção.

A superação dessa lacuna tem sido buscada por meio da vinculação entre a orientação
entregue e as causas identificadas no desempenho. Afzaal et al. (2021) combinam predição de
desempenho com técnicas de explicabilidade para gerar recomendações que indicam quais
fatores respondem pelo resultado projetado e que ação corretiva corresponde a cada um,
argumentando que a informação sobre o resultado provável, desacompanhada da explicação, não
sustenta a autorregulação do estudante. O trabalho evidencia que a devolutiva útil depende
de dados históricos suficientes para que a causa seja identificável.

A mesma dependência aparece do lado da decisão institucional. Um critério de certificação
que compare o desempenho de um discente com o seu próprio desempenho anterior só pode ser
executado sobre uma base que preserve as medições de todas as unidades avaliativas, com a
associação entre discente e competência mantida ao longo do tempo. A alternativa usual, que
consiste em aplicar o critério sobre a medição mais recente, mede posição e não trajetória,
e responde a uma pergunta diferente daquela que o programa formula.

As duas linhas convergem em um ponto que delimita a contribuição deste artigo. Tanto a
decisão sobre o cumprimento de um critério quanto a devolutiva dirigida a quem não o
cumpriu pressupõem acesso à série de medições de cada participante, e não ao seu valor mais
recente. Automatizar a produção de indicadores resolve o problema do tempo de consolidação
sem resolver o da decisão, que permanece dependente da existência de uma base capaz de
responder como cada competência variou entre unidades avaliativas sucessivas.

## 3 Método da pesquisa

Este trabalho caracteriza-se como pesquisa aplicada de natureza descritiva, conduzida
sobre a operação real de um programa de capacitação profissional, e não sobre um ambiente
construído para o experimento. O objeto de estudo é o próprio sistema em funcionamento no
ciclo de 2025 do programa Capacitação 4.0, cujos componentes foram construídos e operados
pela equipe de pesquisa ao longo de dois editais consecutivos de fluxo contínuo. A
descrição que segue privilegia o nível de detalhe necessário para que um terceiro reproduza
a solução em contexto equivalente, sem transcrever rotinas de implementação.

A evidência empregada provém de acervos distintos e verificáveis. O primeiro é o
código-fonte da interface de programação de aplicações, mantido em repositório versionado.
O segundo reúne as exportações em formato JSON dos fluxos construídos na ferramenta de
automação. O terceiro é uma consulta agregada ao banco de dados de produção, realizada em
27 de julho de 2026. Sempre que um valor numérico é apresentado, indica-se de qual acervo
foi extraído e em que data, uma vez que a base permanece em uso e um número sem data não é
reproduzível por terceiros.

### 3.1 Contexto e recorte do estudo

O programa Capacitação 4.0 vincula discentes a projetos de inovação conduzidos em parceria
entre um instituto federal e uma agência de fomento à pesquisa industrial, sob a
metodologia de aprendizagem baseada em problemas, com acompanhamento de mentores. O
programa distingue projetos reais, executados para demanda de empresa parceira, de
projetos espelho, que reproduzem a dinâmica do projeto real com finalidade formativa. O
acompanhamento do desenvolvimento socioemocional dos participantes integra a governança do
programa e é o processo sobre o qual a automação descrita neste trabalho atua.

A matriz de competências e a escala de avaliação não foram definidas por esta pesquisa:
elas seguem o manual de operação do programa (Embrapii, 2021), que estabelece sete
competências socioemocionais macro e quatro subcompetências vinculadas à inteligência
emocional. No processamento, a competência inteligência emocional é substituída por suas
quatro subcompetências, o que produz o conjunto de dez itens comparáveis apresentado na
Tabela 1. Esse achatamento é o que torna as medições homogêneas entre si e viabiliza
tanto a comparação longitudinal quanto as regras descritas nas subseções 3.4 e 3.5.


> ⚠️ IMAGEM AUSENTE: `figuras/tab-03-1.md` — Quadro editável com as dez competências avaliadas, indicando quais são macro e quais são subcompetências de inteligência emocional. Corpo em TNR 10.

**Tabela 1 — Competências socioemocionais avaliadas no ciclo de 2025, após o desdobramento da inteligência emocional em subcompetências. Fonte: elaborado pelos autores.**


Cada discente registra, ao final de cada unidade avaliativa, uma autoavaliação com uma nota
de 0 a 4 para cada competência. A nota é convertida em quatro níveis qualitativos: abaixo
do básico, de 0 a 1; básico, de 1 a 2; adequado, de 2 a 3; e avançado, de 3 a 4. A unidade
é o ciclo avaliativo do programa e funciona como o eixo temporal de todas as comparações
feitas pelo sistema. O recorte analisado corresponde às autoavaliações registradas entre 23
de janeiro e 6 de setembro de 2025, distribuídas em nove unidades, conforme detalhado na
seção 4.

### 3.2 Arquitetura da solução

A solução distribui-se entre duas camadas. A orquestração foi construída na ferramenta de
automação de fluxos de trabalho n8n (N8n, 2025). A persistência e o processamento foram
implementados como interface de programação de aplicações em Django 4.2 com Django REST
Framework 3.15, sobre banco de dados PostgreSQL. A escolha por concentrar as regras de
negócio na interface, e não nos fluxos, responde a uma limitação identificada no ciclo
anterior do projeto. O cálculo dos indicadores vivia então disperso entre planilhas e nós
de automação, o que impedia auditar por que um determinado valor havia sido produzido. A
Figura 1 apresenta a disposição dos componentes.


> ⚠️ IMAGEM AUSENTE: `figuras/fig-03-1.png` — Diagrama esquemático em três faixas. Entrada, formulário e planilha de respostas. Orquestração, os quatro fluxos do n8n auto-hospedado. Núcleo, a API Django sobre PostgreSQL gerenciado. Saída, planilhas, gráficos, certificados em PDF no Drive e mensagens de correio eletrônico. Sem captura de tela e sem hostname. Texto interno em TNR 18 ou maior.

**Figura 1 — Arquitetura da solução no ciclo de 2025, com a orquestração em n8n e a interface de programação de aplicações como núcleo de persistência e de decisão. Fonte: elaborado pelos autores.**


Quatro fluxos compõem a orquestração, na nomenclatura adotada pela própria equipe. O
primeiro lê as respostas do formulário de autoavaliação, submete as notas à interface e
devolve os resultados a uma planilha. O segundo gera os gráficos de perfil e os armazena em
serviço de arquivos em nuvem. O terceiro identifica discentes com desempenho insatisfatório
e envia recomendações pedagógicas por correio eletrônico. O quarto emite os certificados de
participação. Os dois últimos constituem a contribuição do ciclo de 2025 e são detalhados
nas subseções 3.4 e 3.5.

A ferramenta de automação foi executada em contêiner Docker auto-hospedado, a partir da
imagem oficial do projeto, o que padronizou o ambiente entre as máquinas da equipe e
dispensou configuração manual a cada nova integração ao time (Merkel, 2014). O disparo dos
fluxos é manual em três deles; apenas o fluxo de recomendações dispõe também de um gatilho
por requisição web. Nenhum dos fluxos exportados possui agendamento periódico, o que
significa que a execução é sob demanda e que a periodicidade do ciclo formativo permanece
sob controle humano — limitação retomada na seção 5.

Ao longo de 2025, a infraestrutura de persistência migrou de uma plataforma de hospedagem
gerenciada, utilizada ao final de 2024, para um banco PostgreSQL gerenciado em nuvem
associado a implantação da interface em plataforma sem servidor, ambos em região
`us-east-1`. A migração não alterou o modelo de dados nem as regras de negócio. O que ela
substituiu foi o ambiente de execução, que deixou de ser contínuo e passou a operar sob
demanda. Essa mudança reduziu o custo de operação, mas introduziu latência de inicialização
a frio nas primeiras requisições após período de inatividade.

### 3.3 Modelo de dados e rastreabilidade histórica

O modelo relacional organiza-se em torno de sete entidades, apresentadas na Figura 2.
Discente e mentor concentram a identificação institucional dos participantes. A entidade
projeto classifica a iniciativa entre real e espelho e vincula-a a um mentor responsável. A
entidade associativa entre discente e projeto registra o tipo de vínculo e a data de
entrada no programa, campo que se mostra determinante para a regra de certificação. A
matriz de competências é representada por duas entidades hierarquizadas, em que cada
subcompetência aponta para a competência macro que a contém. Esse arranjo preserva a
flexibilidade para expansões futuras da matriz sem alteração de esquema.


> ⚠️ IMAGEM AUSENTE: `figuras/fig-03-2.png` — Diagrama entidade-relacionamento das sete entidades do domínio, com cardinalidades e a indicação dos campos de auditoria. Redesenhar, não capturar tela de ferramenta. Omitir os atributos que armazenam dado pessoal identificável, representando-os como "dados de identificação". Texto interno em TNR 18 ou maior.

**Figura 2 — Modelo entidade-relacionamento do domínio de avaliação de competências socioemocionais. Fonte: elaborado pelos autores.**


O registro de desempenho separa-se em dois níveis. A autoavaliação representa o evento de
avaliação de um discente em uma unidade e admite observação textual do mentor. A nota
vincula um valor numérico a uma competência macro ou a uma subcompetência dentro daquela
autoavaliação. Essa separação é o que permite que a mesma competência seja medida
repetidamente ao longo das unidades, sem sobrescrita do valor anterior. É também a condição
técnica que sustenta a tese defendida neste trabalho, pois nenhuma das duas regras descritas
adiante é computável sobre uma estrutura que guarde apenas o estado corrente.

A integridade referencial foi implementada com restrição de proteção em todas as chaves
estrangeiras (Django Software Foundation, 2026). A remoção de uma competência ou de um
discente com avaliações associadas é recusada pelo banco, em vez de propagar exclusão em
cascata. Somam-se a isso quatro campos de auditoria em cada entidade, que registram data de
criação, data de atualização e o usuário responsável por cada uma das duas operações. Por
meio dessa combinação, todo valor exibido em um relatório pode ser rastreado até a operação
de escrita que o produziu.

A gravação das dez medições de uma autoavaliação é executada registro a registro, na mesma
requisição que cria o evento de avaliação. As consultas de leitura empregam carregamento
antecipado dos objetos relacionados, o que evita a emissão de uma consulta por registro ao
percorrer os vínculos do discente com projeto e mentor. O acesso é restrito a requisições autenticadas por token,
com credenciais e chaves mantidas em variáveis de ambiente. A interface é documentada no
padrão OpenAPI, o que permite que a camada de orquestração descubra o contrato dos
endpoints sem depender de documentação externa.

### 3.4 Camada de decisão: operacionalização da regra de certificação

A regra de certificação do programa exige evolução de desempenho em ao menos dois terços
das competências avaliadas. Sua operacionalização como consulta sobre dados persistidos
está implementada na interface, no método de classe `aptosCertificacao` da entidade
discente, e é exposta em endpoint dedicado que devolve a relação de aptos. O algoritmo
encadeia quatro filtros, e o critério de dois terços é aplicado em dois níveis distintos,
primeiro dentro de cada competência e depois no conjunto delas, conforme o pseudocódigo
apresentado a seguir.

```
para cada discente com ao menos uma autoavaliacao:
    se (hoje - data_entrada do vinculo mais recente) < 365 dias: descartar
    agrupar as notas por competencia macro, agregando por media as subcompetencias
    se numero de competencias avaliadas < 3: descartar
    se alguma competencia tem medicao abaixo de 1,0: descartar

    competencias_aprovadas <- 0
    para cada competencia com ao menos 2 medicoes:
        referencia <- menor medicao da competencia
        restantes  <- demais medicoes
        saltos <- quantidade de medicoes em restantes tais que
                  medicao >= referencia + 2  ou  medicao = 4
        se saltos >= arredondar(|restantes| x 2/3):
            competencias_aprovadas <- competencias_aprovadas + 1

    se competencias_aprovadas >= arredondar(competencias_avaliadas x 2/3):
        marcar discente como apto
```

Três aspectos do critério merecem registro, por não serem evidentes em seu enunciado
verbal. O salto exigido dentro de cada competência é de dois pontos na escala de 0 a 4, ou
seja, de dois níveis qualitativos, e não de um. O valor máximo da escala é aceito como
equivalente ao salto, o que impede que um discente já avaliado em nível avançado seja
penalizado pela ausência de margem para crescer. A referência de comparação é a menor
medição registrada para aquela competência, e não a medição da primeira unidade. O critério
mede, portanto, a amplitude entre o pior desempenho e os demais, não a evolução
estritamente cronológica. O filtro de permanência mínima de um ano no programa, por fim,
opera sobre a data de entrada do vínculo mais recente do discente com um projeto.

A emissão do documento é conduzida pelo quarto fluxo de automação. Após autenticar-se na
interface, o fluxo percorre a relação de discentes em lote e normaliza a capitalização do
nome, que é armazenado em caixa baixa na origem. Em seguida preenche um modelo de documento
mantido em nuvem, converte o resultado em PDF e concede aos orientadores permissão de
edição sobre a versão editável do arquivo. Convém explicitar o alcance dessa etapa. A versão
exportada do fluxo consome a listagem geral de discentes, e não o endpoint que aplica a
regra de dois terços, de forma que os documentos emitidos são certificados de participação.
A camada de decisão está implementada e disponível como serviço, mas seu acoplamento ao
fluxo de emissão não está demonstrado pela evidência reunida.

### 3.5 Camada de intervenção: a regra de recomendação pedagógica

O terceiro fluxo implementa a devolutiva ao discente e é o mais extenso da solução. Após
recuperar da interface a relação de discentes e o histórico completo de notas, o fluxo
ordena as autoavaliações de cada discente por unidade e percorre cada competência em busca
de duas condições independentes. A primeira é o desempenho abaixo do limiar de 2,0, valor
que corresponde à fronteira entre os níveis básico e adequado da escala. A segunda é a
queda em relação à unidade imediatamente anterior, verificada apenas a partir da segunda
unidade avaliada, por depender de medição prévia persistida.

Cada apontamento gerado recebe o rótulo da condição que o originou, o que preserva no
documento entregue ao mentor a distinção entre um discente com desempenho baixo estável e
outro em trajetória de queda a partir de patamar adequado. O texto da recomendação é
sorteado de um banco de práticas mantido em planilha e organizado por competência. Um
controle impede a repetição de uma mesma recomendação para o mesmo discente enquanto
houver alternativas disponíveis. Esgotado o banco, o sistema registra explicitamente a
exaustão em vez de repetir conteúdo. Discentes sem qualquer apontamento são desviados do
fluxo por condicional e não recebem mensagem.

O conjunto de apontamentos é composto em documento estruturado, convertido em PDF e enviado
por correio eletrônico ao destinatário. Duas características dessa camada precisam ser
consideradas na leitura dos resultados. A seleção do texto é aleatória dentro da competência
apontada, e não adaptada ao perfil do discente, o que significa que a personalização
alcançada é de nível de competência, não de nível individual. Além disso, o envio não é
registrado em tabela do banco, de modo que o volume de mensagens efetivamente entregues não
dispõe de evidência transacional.

### 3.6 Tratamento dos dados e procedimentos éticos

A base de produção armazena dados pessoais dos participantes associados a avaliações de
competências socioemocionais. Constam desse conjunto o nome e o número de inscrição no
cadastro de pessoas físicas, bem como a matrícula e o endereço de correio eletrônico
institucional. Os dados
analisados neste trabalho são operacionais do programa de capacitação, produzidos como
registro ordinário de sua governança, e não foram coletados para finalidade de pesquisa com
seres humanos.

Toda extração empregada na redação deste artigo foi conduzida por consultas agregadas, com
funções de contagem, média e valores extremos, sem recuperação de linhas individuais.
Nenhum dado individual de discente é reportado no texto, nas tabelas ou nas figuras, e as
ilustrações foram redesenhadas como diagramas esquemáticos em lugar de capturas de tela,
justamente para eliminar a via mais provável de exposição acidental. Os identificadores de
infraestrutura, como nomes de servidor e credenciais de acesso, permanecem em variáveis de
ambiente e não são reproduzidos aqui.

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
com média de 2,47, valor situado na faixa qualitativa adequada. A Tabela 2 consolida o
conjunto.


> ⚠️ IMAGEM AUSENTE: `figuras/tab-04-1.md` — Quadro editável com as métricas agregadas do banco em 27/07/2026 — discentes, autoavaliações, unidades, notas por tipo, faixa e média das notas, mentores, projetos e registros de auditoria. Uma coluna para a métrica e outra para o valor. Nenhum dado individual. Corpo em TNR 10.

**Tabela 2 — Caracterização agregada da base de produção do ciclo de 2025, apurada em 27 de julho de 2026 (n=33 discentes). Fonte: dados da pesquisa.**


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
Figura 3. As cinco primeiras unidades apresentam 33 registros cada, cobertura completa
da turma cadastrada. Da sexta unidade em diante o número decai para 7, 3, 1 e 1 registros.
O programa manteve, portanto, cobertura integral da turma cadastrada por cinco ciclos
avaliativos consecutivos, e o decaimento a partir do sexto acompanha o encerramento das
atividades previstas no edital.


> ⚠️ IMAGEM AUSENTE: `figuras/fig-04-1.png` — Gráfico de barras verticais com o número de autoavaliações registradas por unidade avaliativa, das unidades 1 a 9. Valores 33, 33, 33, 33, 33, 7, 3, 1 e 1. Eixo vertical rotulado em número de autoavaliações. Sem qualquer identificação de discente. Texto interno em TNR 18 ou maior, 300 dpi.

**Figura 3 — Autoavaliações registradas por unidade avaliativa no ciclo de 2025, entre 23 de janeiro e 6 de setembro (n=177). Fonte: dados da pesquisa.**


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
o resultado do endpoint depende da data em que ele é consultado. A instância de banco
utilizada no ciclo foi posteriormente desativada, de modo que a contagem de discentes
retornada pelo endpoint não pôde ser apurada nem reproduzida. O que a base sustenta é a
computabilidade da regra, evidenciada pelos 49 pares competência × discente com duas ou mais
medições, e não o número de discentes que a satisfariam em uma data determinada.

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
Tabela 3 reúne as medições.


> ⚠️ IMAGEM AUSENTE: `figuras/tab-04-2.md` — Quadro editável comparando o tempo do processo manual, o tempo do ciclo automatizado anterior e os tempos das etapas do ciclo de 2025. Colunas para a etapa, o tempo e o ciclo a que a medição pertence. Corpo em TNR 10.

**Tabela 3 — Tempo de execução por etapa, do processo manual às etapas automatizadas dos ciclos de 2024 e de 2025. Fonte: dados da pesquisa.**


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
trabalho. Os tempos reportados nesta subseção foram cronometrados em condições correntes de
uso, sem que a primeira requisição após inatividade fosse isolada das demais, e portanto já
incorporam a inicialização a frio quando ela ocorreu. Os valores descrevem, assim, o
comportamento percebido pelo operador, e não o melhor caso com a função previamente ativa.

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
usuários, para a qual a equipe apontou a hospedagem institucional local como mitigação. O
orquestrador, por sua vez, foi executado em contêiner instalado em estação de trabalho de um
integrante da equipe, e não em serviço mantido pela instituição, condição que limita a
continuidade da operação para além do período do vínculo desse integrante.

# REFERÊNCIAS

AFZAAL, Muhammad; NOURI, Jalal; ZIA, Aayesha; PAPAPETROU, Panagiotis; FORS, Uno; WU, Yongchao; LI, Xiu; WEEGAR, Rebecka. **Explainable AI for data-driven feedback and intelligent action recommendations to support students self-regulation**. Frontiers in Artificial Intelligence, v. 4, art. 723447, 2021. Disponível em: https://doi.org/10.3389/frai.2021.723447. Acesso em: 03 set. 2026.

AJIMATI, Matthew Oladeji; CARROLL, Noel; MAHER, Mary. **Adoption of low-code and no-code development: a systematic literature review and future research agenda**. Journal of Systems and Software, v. 222, art. 112300, 2025. Disponível em: https://doi.org/10.1016/j.jss.2024.112300. Acesso em: 03 set. 2026.

AL-SA'DI, Ahmed; YAMJAL, Parina; AHMAD, Esraa; PANJABI, Richa; ALLOTT MCPHEE, Cam; GULER, Olkan. **Assessing educators' soft skills: developing a self-assessment instrument**. Administrative Sciences, v. 13, n. 9, art. 208, 2023. Disponível em: https://doi.org/10.3390/admsci13090208. Acesso em: 03 set. 2026.

BAZHENOVA, Ekaterina; ZERBATO, Francesca; OLIBONI, Barbara; WESKE, Mathias. **From BPMN process models to DMN decision models**. Information Systems, v. 83, p. 69-88, 2019. Disponível em: https://doi.org/10.1016/j.is.2019.02.001. Acesso em: 03 set. 2026.

BHARDWAJ, Vivek; KUMAR, Mukesh. **Transforming higher education with robotic process automation: enhancing efficiency, innovation, and student-centered learning**. Discover Sustainability, v. 6, n. 1, art. 356, 2025. Disponível em: https://doi.org/10.1007/s43621-025-01198-6. Acesso em: 03 set. 2026.

DJANGO SOFTWARE FOUNDATION. **Django documentation**. documentação oficial, versão 4.2, 2026. Disponível em: https://docs.djangoproject.com/en/4.2/. Acesso em: 03 fev. 2026.

ELMASRI, Ramez; NAVATHE, Shamkant B. **Sistemas de banco de dados**. 7. ed. Rio de Janeiro: Pearson, 2018.

EMBRAPII. **Manual do Programa Capacitação 4.0**. v. 1.0. Brasília: Empresa Brasileira de Pesquisa e Inovação Industrial, 2021.

FIELDING, Roy Thomas. **Architectural styles and the design of network-based software architectures**. Tese (Doutorado em Informação e Ciência da Computação) – University of California, Irvine, 2000.

GROOVER, Mikell P. **Automação industrial e sistemas de manufatura**. 3. ed. São Paulo: Pearson Prentice Hall, 2010.

MERKEL, Dirk. **Docker: lightweight Linux containers for consistent development and deployment**. Linux Journal, n. 239, p. 2, 2014.

MUNIR, Fouzia. **More than technical experts: engineering professionals' perspectives on the role of soft skills in their practice**. Industry and Higher Education, v. 36, n. 3, p. 294-305, 2022. Disponível em: https://doi.org/10.1177/09504222211034725. Acesso em: 03 set. 2026.

N8N. **n8n documentation**. documentação oficial, 2025. Disponível em: https://docs.n8n.io. Acesso em: 30 jun. 2025.

SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S. **Sistema de banco de dados**. 7. ed. Rio de Janeiro: Elsevier, 2020.

SUSNJAK, Teo; RAMASWAMI, Gomathy Suganya; MATHRANI, Anuradha. **Learning analytics dashboard: a tool for providing actionable insights to learners**. International Journal of Educational Technology in Higher Education, v. 19, n. 1, art. 12, 2022. Disponível em: https://doi.org/10.1186/s41239-021-00313-7. Acesso em: 03 set. 2026.
