---
secao: 03-metodo
titulo: Método da pesquisa
alvo_palavras: 2200
status: rascunho
---

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
quatro subcompetências, o que produz o conjunto de dez itens comparáveis apresentado no
[[@TAB:03-1]]. Esse achatamento é o que torna as medições homogêneas entre si e viabiliza
tanto a comparação longitudinal quanto as regras descritas nas subseções 3.4 e 3.5.

[[TAB:03-1
  tipo: tabela
  status: criar
  origem: nó "Definir competências" do workflow "Gera recomendações" (exportação de set/2025) cruzado com o manual de operação do programa
  dados: mapa-de-fatos §5
  descricao: Quadro editável com as dez competências avaliadas, indicando quais são macro e quais são subcompetências de inteligência emocional. Corpo em TNR 10.
  legenda: Quadro 1 — Competências socioemocionais avaliadas no ciclo de 2025, após o desdobramento da inteligência emocional em subcompetências. Fonte: elaborado pelos autores.
  largura: 1col
  altura_cm: 7
  arquivo: figuras/tab-03-1.md
]]

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
de automação, o que impedia auditar por que um determinado valor havia sido produzido. O
[[@FIG:03-1]] apresenta a disposição dos componentes.

[[FIG:03-1
  tipo: diagrama-arquitetura
  status: criar
  origem: elaborado a partir das quatro exportações de workflow em api-repo/n8n_files/ e do código da API em api-repo/automacao-deploy-main/
  dados: mapa-de-fatos §4, §14
  descricao: Diagrama esquemático em três faixas. Entrada, formulário e planilha de respostas. Orquestração, os quatro fluxos do n8n auto-hospedado. Núcleo, a API Django sobre PostgreSQL gerenciado. Saída, planilhas, gráficos, certificados em PDF no Drive e mensagens de correio eletrônico. Sem captura de tela e sem hostname. Texto interno em TNR 18 ou maior.
  legenda: Figura 1 — Arquitetura da solução no ciclo de 2025, com a orquestração em n8n e a interface de programação de aplicações como núcleo de persistência e de decisão. Fonte: elaborado pelos autores.
  largura: 1col
  altura_cm: 8
  arquivo: figuras/fig-03-1.png
]]

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

O modelo relacional organiza-se em torno de sete entidades, apresentadas no [[@FIG:03-2]].
Discente e mentor concentram a identificação institucional dos participantes. A entidade
projeto classifica a iniciativa entre real e espelho e vincula-a a um mentor responsável. A
entidade associativa entre discente e projeto registra o tipo de vínculo e a data de
entrada no programa, campo que se mostra determinante para a regra de certificação. A
matriz de competências é representada por duas entidades hierarquizadas, em que cada
subcompetência aponta para a competência macro que a contém. Esse arranjo preserva a
flexibilidade para expansões futuras da matriz sem alteração de esquema.

[[FIG:03-2
  tipo: diagrama-arquitetura
  status: criar
  origem: redesenhado a partir dos modelos em api-repo/automacao-deploy-main/capacitacao/models/ (Figura 1 do relatório de estágio, não reutilizada por ser documento interno)
  dados: mapa-de-fatos §4, §14
  descricao: Diagrama entidade-relacionamento das sete entidades do domínio, com cardinalidades e a indicação dos campos de auditoria. Redesenhar, não capturar tela de ferramenta. Omitir os atributos que armazenam dado pessoal identificável, representando-os como "dados de identificação". Texto interno em TNR 18 ou maior.
  legenda: Figura 2 — Modelo entidade-relacionamento do domínio de avaliação de competências socioemocionais. Fonte: elaborado pelos autores.
  largura: 1col
  altura_cm: 9
  arquivo: figuras/fig-03-2.png
]]

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

A gravação das notas de uma autoavaliação ocorre em operação única, com inserção em lote das
dez medições. As consultas de leitura empregam carregamento antecipado dos objetos
relacionados, o que evita a emissão de uma consulta por registro ao percorrer os vínculos
entre discente, projeto e mentor. O acesso é restrito a requisições autenticadas por token,
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

A base de produção armazena dados pessoais dos participantes, entre eles nome, número de
inscrição no cadastro de pessoas físicas, matrícula e endereços de correio eletrônico
institucionais, associados a avaliações de competências socioemocionais. Os dados
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
