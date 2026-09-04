---
secao: 01-introducao
titulo: Introdução
alvo_palavras: 1100
status: rascunho
---

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
