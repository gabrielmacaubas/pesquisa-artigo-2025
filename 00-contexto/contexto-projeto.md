## 1. Identificação do projeto

* **Nome/título do projeto:** Automação de Recomendações e Certificações de Soft Skills em Programas de Capacitação Profissional (consta no TCC do Gabriel). Anteriormente nomeado como "Automação de Atividades Repetitivas em Processos de Gerenciamento de Projetos de Software" no edital de 2024 (consta na apresentação de 2024 e no resumo da Juliana, informado pelo autor).


* **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia da Paraíba (IFPB) - Unidade Acadêmica de Informação e Comunicação (consta no TCC do Gabriel).


* **Curso/programa:** Curso Superior de Tecnologia em Sistemas para Internet (consta no TCC do Gabriel).


* **Período exato:** Anos de 2024 e 2025 (consta no TCC do Gabriel). Estágio do Gabriel: 01/03/2024 a 31/12/2025 (consta no TCC do Gabriel V2). Projeto da Juliana: Outubro de 2024 a Janeiro de 2025 (informado pelo autor nesta conversa).


* **Financiamento/Edital:** Edital nº 02/2024 e Edital nº 02/2025 – Fluxo Contínuo (consta no resumo da Juliana, informado pelo autor, e no TCC do Gabriel).


* **Vínculo com programas externos:** Vinculado ao Polo de Inovação do IFPB e com apoio/parceria da EMBRAPII (Empresa Brasileira de Pesquisa e Inovação Industrial) no âmbito do programa "Capacitação 4.0" (consta no TCC do Gabriel).



## 2. Problema e motivação

* **Problema real:** Elevada carga de atividades manuais repetitivas que resultavam em fluxos de trabalho extensos, atrasos na entrega, descentralização e falta de padronização nas avaliações de competências socioemocionais (soft skills) (consta no TCC do Gabriel).


* **Quem sofria o problema:** Mentores do programa Capacitação 4.0 do IFPB/EMBRAPII (consta no TCC do Gabriel).


* **Como era feito antes:** A gestão era manual e descentralizada em planilhas eletrônicas (Google Sheets), o que dificultava a análise histórica e a correlação de dados evolutivos dos alunos (consta no TCC do Gabriel). O processo de cálculo de notas, geração de planilhas e resultados levava cerca de 1 hora por aluno (informado pelo autor nesta conversa).


* **Por que importava:** A automação era essencial para eliminar a subjetividade humana nos cálculos, centralizar os dados, padronizar os relatórios institucionais e dar suporte ágil e confiável para a tomada de decisão pedagógica (consta no TCC do Gabriel).



## 3. Pessoas e papéis

* **Equipe total:** 11 integrantes com diferentes níveis de especialidade (consta no TCC do Gabriel).


* **Gabriel Macaúbas Melo:** Autor do relatório/TCC, pesquisador de graduação, desenvolvedor backend e integrador de sistemas (consta no TCC do Gabriel).


* **Heremita Brasileiro Lira (Dra.):** Orientadora, coordenadora do projeto e mentora (consta no TCC do Gabriel e apresentação).


* **Francisco Petrônio:** Professor, orientador/coordenador técnico e mentor (consta no TCC do Gabriel e apresentação).


* **Nadja da Nóbrega:** Professora / Coordenação técnica (consta no TCC do Gabriel).


* **Juliana Dantas:** Professora / Coordenação técnica (consta no TCC do Gabriel).


* **Candido José Ramos Do Egypto (Ms.):** Coordenador do Curso de Sistemas para Internet (consta no TCC do Gabriel V2).


* **Jennifer Suelen de Amorim Barbosa:** Discente de mestrado, suporte acadêmico e pesquisa / equipe de desenvolvimento (consta no TCC do Gabriel e apresentação).


* **Jackson Fernandes:** Discente de mestrado, suporte acadêmico e pesquisa (consta no TCC do Gabriel).


* **Narjara Xavier:** Mentoria especializada em soft skills (consta no TCC do Gabriel e apresentação).


* **Jardielen de Souza Nascimento:** Pesquisadora de graduação / equipe de desenvolvimento (consta no TCC do Gabriel e apresentação).


* **Louise Fernandes Caetano:** Pesquisadora de graduação / equipe de desenvolvimento (consta no TCC do Gabriel e apresentação).


* **Juliana Ferreira Cavalcante:** Pesquisadora de graduação, equipe de desenvolvimento, autora do trabalho focado na automação de certificados (consta no TCC do Gabriel e resumo, informado pelo autor).


* **Alexandre D'Andrea:** Mentor (consta na apresentação de 2024).


* [[LACUNA: Ordem exata de autoria acordada para o artigo científico de 2025]].

## 4. Parcerias

* **EMBRAPII:** Forneceu as diretrizes pedagógicas e a matriz de competências através do "Manual de Operação: Programas de Recursos Humanos: Capacitação 4.0. v 1.0. (2024)" (informado pelo autor nesta conversa e no TCC do Gabriel).


* **Polo de Inovação do IFPB:** Forneceu o ambiente, contexto institucional e os usuários finais (mentores e discentes) (consta no TCC do Gabriel).


* [[LACUNA: Quantidade exata de discentes/mentores que utilizaram o sistema como usuários reais em produção]].

## 5. Arquitetura técnica

* **Workflows n8n:** Monitoram a entrada de respostas no Google Sheets. Gatilho dispara requisição POST para a API Django. O n8n então recupera as informações tratadas para alimentar templates, unindo imagens e convertendo para PDF. No 2º ciclo, o n8n verifica critérios de certificação e aciona geração de documentos e envio automático de e-mails de recomendação (consta no TCC do Gabriel e apresentação). [[LACUNA: Detalhes do gatilho exato do n8n (cronjob ou webhook direto do Sheets?) e periodicidade exata de execução]].


* **API (Backend):** Desenvolvida em Python (versões 3.9 e 3.12 mencionadas nos scripts) utilizando o framework Django 4 (versão exata 4.2.11) e Django REST Framework 3.15.1. Possui arquitetura RESTful, utilizando ORM, `select_related`, `prefetch_related` e `bulk_create` para eficiência (consta no TCC do Gabriel).


* **Endpoints principais:** `/api/capacitacao/autoavaliacao_notas/` (POST), `/api/capacitacao/discentes/` (GET), `/api/capacitacao/discentes_aptos_certificacao/` (GET), `/login` e `/signup` (POST). Testados via ferramenta Insomnia durante o desenvolvimento (informado pelo autor e figura 4 do TCC).


* **Banco de Dados:** PostgreSQL (versão 15). Substituiu a estratégia anterior que utilizava o serviço Railway. O banco possui chaves estrangeiras (`models.PROTECT`) garantindo rastreabilidade histórica das avaliações (consta no TCC do Gabriel e correções do autor).


* **Hospedagem API:** Plataforma Vercel, operando em ambiente serverless configurado via arquivo `vercel.json` e script `build.sh` (consta no TCC do Gabriel). [[LACUNA: Limitações impostas pelo plano gratuito da Vercel (ex: timeouts de requisição, cold starts)]].


* **Hospedagem n8n:** A apresentação cita que hospedar no servidor próprio do IFPB reduziria o tempo que é gasto devido à comunicação com servidores nos Estados Unidos (consta na apresentação de 2024). [[LACUNA: Onde o n8n esteve hospedado durante a produção exata do projeto?]].


* **Conteinerização:** Docker e Docker Compose, empacotando o Django e PostgreSQL em ambiente padronizado (consta no TCC do Gabriel).


* **Geração de gráficos:** Gráficos do tipo "radar" (perfil socioemocional). [[LACUNA: Qual biblioteca/serviço exato gerou o gráfico no n8n (Chart.js, QuickChart, etc.?)]] (consta no TCC do Gabriel e apresentação).


* **Planilhas e relatórios:** Salvos em formato PDF e armazenados no Google Drive (consta no TCC do Gabriel e apresentação).


* **Autenticação/Segurança:** Protocolo JSON Web Token (JWT) usando variáveis de ambiente para proteção de credenciais e rotas blindadas com decoradores `IsAuthenticated` (consta no TCC do Gabriel).


* **Decisões não óbvias:** Uso de `bulk_create` para salvar notas massivas e diminuir tempo de resposta da API (consta no TCC do Gabriel).



## 6. Dados quantitativos — SEÇÃO MAIS IMPORTANTE

* **Tempo manual anterior:** Aproximadamente 1 hora de trabalho por aluno processado pelo mentor (informado pelo autor nesta conversa).
* **Tempo automatizado atingido:** 2 a 3 segundos para o registro das notas e 12 a 15 segundos para gerar cada gráfico e injetar no Google Drive (informado pelo autor e apresentação).


* **Matriz EMBRAPII:** 7 soft skills macro e 4 sub-soft skills (consta no TCC do Gabriel).


* **Escala de conversão qualitativa:** Notas numéricas de 0 a 4 convertidas em 4 níveis qualitativos: 0-1 (Abaixo do básico), 1-2 (Básico), 2-3 (Adequado), e 3-4 (Avançado) (informado pelo autor nesta conversa e relatório).


* **Métrica de certificação:** O discente deve comprovar evolução de nível em pelo menos dois terços (2/3) das competências avaliadas para receber certificado (consta no TCC do Gabriel).


* **Time do projeto:** 11 integrantes (consta no TCC do Gabriel).


* **Duração da bolsa/projeto do Gabriel:** 22 meses (01/03/2024 a 31/12/2025) (consta no TCC do Gabriel V2).


* **Duração do projeto da Juliana:** 4 meses (Outubro de 2024 a Janeiro de 2025) (informado pelo autor nesta conversa).
* [[LACUNA: Volume total de dados processados em produção (em GB/MB ou linhas)]].
* [[LACUNA: Número total de alunos atendidos/cadastrados e avaliações geradas]].
* [[LACUNA: Quantidade total de e-mails/certificados emitidos]].
* [[LACUNA: Custos exatos de infraestrutura, caso tenha havido fora do plano gratuito]].

## 7. Produção acadêmica

* **TCC 1 (Gabriel Macaúbas Melo, 2025):** Título: "SISTEMA INTEGRADO DE BACKEND E AUTOMAÇÃO PARA CERTIFICAÇÃO DE SOFT SKILLS NO PROGRAMA CAPACITAÇÃO 4.0". Recorte: Arquitetura de persistência, backend em Django, ORM, segurança JWT, Docker e modelagem de dados (consta no TCC do Gabriel e título criado pelo autor nesta conversa).


* **Trabalho 2 (Juliana Ferreira Cavalcante, 2025):** Título: "AUTOMAÇÃO DA EMISSÃO DE CERTIFICADOS EM PROJETOS EMBRAPII COM O USO DA FERRAMENTA N8N". Recorte: Uso do *low-code* n8n para otimizar especificamente o fluxo de certificação, economia de tempo e padronização (informado pelo autor nesta conversa).
* **Apresentação 1 (Equipe de 5 alunos, 29/10/2024):** Título: "AUTOMAÇÃO DE ATIVIDADES REPETITIVAS EM PROCESSOS DE GERENCIAMENTO DE PROJETOS DE SOFTWARE" (consta na apresentação).


* [[LACUNA: Dados exatos (título, autores, veículo e resultados) do "artigo publicado em 2024" mencionado no prompt, visto que apenas uma apresentação de slides de outubro foi disponibilizada nos arquivos]].
* [[LACUNA: Existem trabalhos específicos aprovados/escritos por Jardielen e Louise? O prompt diz "os TCCs produzidos", mas faltam detalhes sobre os demais membros]].

## 8. O que mudou entre 2024 e 2025

* **Ciclo de 2024 (Edital 02/2024):** O sistema atuava apenas como apoio básico para geração de gráficos, cadastros e relatórios em PDF com gráficos radar (consta no TCC do Gabriel).


* **Ciclo de 2025 (Edital 02/2025):** Evolução para fornecer dados estruturados granulares. Houve a inclusão de: (1) Automação completa e lógica da emissão de certificados com base na regra de evolução de 2/3 das competências, (2) Implementação de um módulo de recomendações pedagógicas de práticas *hands-on* / PBL e (3) Envio autônomo de *e-mails* a partir dos dados processados (consta no TCC do Gabriel e resumo de Juliana).



## 9. Limitações e problemas conhecidos

* **Latência de rede:** O tempo de 12 a 15 segundos para gerar relatórios é impactado significativamente pela comunicação com a API e banco de dados que estão localizados nos Estados Unidos (Vercel). A sugestão do time foi hospedar localmente no servidor do IFPB (consta na apresentação de 2024).


* [[LACUNA: Quais as restrições e eventuais quedas do plano gratuito na plataforma Vercel durante as operações massivas?]].
* [[LACUNA: Existem vieses nas autoavaliações dos alunos? Há mecanismos para evitar notas infladas preenchidas pelos próprios discentes?]].
* [[LACUNA: Quais foram os erros e bugs mais comuns durante a emissão de certificados na API/n8n?]].

## 10. Material visual existente

* **Figura 1 (TCC Gabriel):** Diagrama Entidade-Relacionamento (Discente, Mentor, SoftSkill, Autoavaliacao, etc.). Pode ser reaproveitado no artigo para explicar o modelo (consta no TCC do Gabriel).


* **Figura 2 (TCC Gabriel):** Diagrama do schema nativo do Django (Sessões, LogEntry, Auth). Muito técnico; reavaliar uso se o artigo for mais focado em processo (consta no TCC do Gabriel).


* **Figura 3 (TCC Gabriel):** Código Python/Django demonstrando as anotações JWT e o bulk_create (consta no TCC do Gabriel).


* **Figura 4 (TCC Gabriel):** Screenshot do Swagger/OpenAPI mostrando a interface interativa da API (consta no TCC do Gabriel).


* **Figura 5 (TCC Gabriel):** Diagrama visual complexo do fluxo do n8n com nós de conexão (API, Merge, PDF, Google Drive) (consta no TCC do Gabriel).


* **Figuras 6 e 7 (TCC Gabriel):** Screenshots de código dos arquivos de infraestrutura `docker-compose`, `Dockerfile` e `vercel.json` (consta no TCC do Gabriel).


* **Apresentação 2024:** Exemplos visuais reais dos "Gráficos Radar" qualitativos gerados e uma tabela no Google Sheets simulando a planilha final formatada com notas convertidas (consta na apresentação de 2024).



## 11. Ética e dados

* O sistema manipulou registros com nomes reais de estudantes (ex: derik gustavo, matheus carvalho), números de CPF, matrículas e e-mails acadêmicos, associados a resultados de avaliações socioemocionais sensíveis (consta na apresentação de 2024 e no TCC do Gabriel).


* [[LACUNA: Houve aprovação pelo Comitê de Ética em Pesquisa (CEP)?]].
* [[LACUNA: Os discentes assinaram Termo de Consentimento Livre e Esclarecido (TCLE)?]].
* [[LACUNA: Houve anonimização criptográfica desses dados na base de dados para garantir a LGPD?]].

## 12. Vocabulário do projeto

* **Soft Skills:** Competências socioemocionais macros, num total de 7 (ex: Inteligência Emocional, Empreendedorismo) (consta no TCC do Gabriel e apresentação).


* **Subsoft Skills:** 4 habilidades menores agregadas dentro de uma competência macro (consta no TCC do Gabriel).


* **PBL (Aprendizagem Baseada em Problemas):** Metodologia *hands-on* adotada no projeto, cujas práticas são alvo do sistema de recomendações (consta no TCC do Gabriel).


* **Projeto Real/Espelho:** Categorização das atividades dos discentes registradas no banco de dados (consta no TCC do Gabriel e figura 1).


* **Discente:** O aluno bolsista ou voluntário avaliado (consta no TCC do Gabriel).


* **Níveis Qualitativos:** Categorias padronizadas convertidas pelo sistema: Abaixo do Básico (0-1), Básico (1-2), Adequado (2-3) e Avançado (3-4) (informado pelo autor nesta conversa).

## 13. Lacunas consolidadas

1. [[LACUNA: Ordem exata de autoria acordada para o artigo científico de 2025]]
2. [[LACUNA: Quantidade exata de discentes/mentores que utilizaram o sistema como usuários reais em produção]]
3. [[LACUNA: Detalhes do gatilho exato do n8n (cronjob ou webhook direto do Sheets?) e periodicidade exata de execução]]
4. [[LACUNA: Limitações impostas pelo plano gratuito da Vercel (ex: timeouts de requisição, cold starts)]]
5. [[LACUNA: Onde o n8n esteve hospedado durante a produção exata do projeto?]]
6. [[LACUNA: Qual biblioteca/serviço exato gerou o gráfico no n8n (Chart.js, QuickChart, etc.?)]]
7. [[LACUNA: Volume total de dados processados em produção (em GB/MB ou linhas)]]
8. [[LACUNA: Número total de alunos atendidos/cadastrados e avaliações geradas]]
9. [[LACUNA: Quantidade total de e-mails/certificados emitidos]]
10. [[LACUNA: Custos exatos de infraestrutura, caso tenha havido fora do plano gratuito]]
11. [[LACUNA: Dados exatos (título, autores, veículo e resultados) do "artigo publicado em 2024" mencionado no prompt, visto que apenas uma apresentação de slides de outubro foi disponibilizada nos arquivos]]
12. [[LACUNA: Existem trabalhos específicos aprovados/escritos por Jardielen e Louise? O prompt diz "os TCCs produzidos", mas faltam detalhes sobre os demais membros]]
13. [[LACUNA: Quais as restrições e eventuais quedas do plano gratuito na plataforma Vercel durante as operações massivas?]]
14. [[LACUNA: Existem vieses nas autoavaliações dos alunos? Há mecanismos para evitar notas infladas preenchidas pelos próprios discentes?]]
15. [[LACUNA: Quais foram os erros e bugs mais comuns durante a emissão de certificados na API/n8n?]]
16. [[LACUNA: Houve aprovação pelo Comitê de Ética em Pesquisa (CEP)?]]
17. [[LACUNA: Os discentes assinaram Termo de Consentimento Livre e Esclarecido (TCLE)?]]
18. [[LACUNA: Houve anonimização criptográfica desses dados na base de dados para garantir a LGPD?]]