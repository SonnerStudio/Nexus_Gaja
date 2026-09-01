# Nexus Gaja

![Nexus Gaja Logo](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** é uma rede de comunicação inteligente e sensível ao contexto, projetada para revolucionar a comunicação global.

## Objetivo e Visão
Num mundo globalizado, a língua é muitas vezes a maior barreira. O principal objetivo do Nexus Gaja é permitir uma comunicação contínua, sem barreiras e contextualmente precisa entre as pessoas, independentemente de elas falarem um idioma comum.

It's not just about rigidly translating words, but about **transferring meaning**. Nexus Gaja connects people on a deeper level by understanding cultural, regional, and contextual nuances, thereby enabling genuine, authentic conversations.

## Possibilidades e recursos
- **Comunicação Multimídia**: O sistema processa não apenas texto, mas também imagem, áudio e vídeo. Isso permite conversas totalmente envolventes (por exemplo, chamadas de vídeo ou mensagens de voz) em tempo real, ultrapassando barreiras linguísticas.
- **Sensibilidade ao Contexto**: Reconhecimento de ironia, expressões idiomáticas, jargões e dialetos regionais que muitas vezes são mal compreendidos por tradutores convencionais.
- **Rede multiplataforma**: serve como base para bate-papos privados, tópicos de fórum (postagens com comentários) e interações da comunidade global.

---

## Arquitetura Técnica (Conceito Central)

O núcleo técnico do Nexus Gaja é um modelo de comunicação personalizado estritamente dividido em três camadas:

1. **Original**: The communication object (message) created by the sender always remains immutable.
2. **Semantic Interpretation**: The system analyzes not just the words, but the actual meaning.
3. **Target Language Representation**: The AI merely creates a temporary or cached representation of the original for the respective recipient based on their preferred language. Translations never overwrite the original message.

### Dependência de Contexto
As traduções no Nexus Gaja nunca visualizam as mensagens isoladamente. O mecanismo considera toda a hierarquia:
`Mensagem` → `Mensagens anteriores` → `Contexto do tópico` → `Contexto da comunidade` → `Idioma / região` → `Preferências do usuário`

### Eficiência por meio de tradução sob demanda
A tradução ocorre com eficiência de recursos apenas **mediante solicitação** (sob demanda). Quando um usuário solicita conteúdo, ele é traduzido para o idioma predefinido. Depois que uma tradução para um idioma específico é gerada, ela é armazenada permanentemente (cache) para acelerar drasticamente solicitações futuras.

## Moderação assistida por IA (WP 1.8.4)

Com a Moderação Assistida por IA, estamos a dar um passo significativo desde a ideia do produto até à arquitectura técnica, tendo em conta os regulamentos actuais da UE (requisitos de transparência da Lei da IA ​​da UE ao abrigo do Art. 50; Lei dos Serviços Digitais com justificações compreensíveis e opções de recurso).

### 1. Princípio Básico
A frase mais importante para a arquitetura é: **A IA de moderação é um sistema de revisão, não um sistema de governo autônomo.**
Ele foi projetado para ajudar os humanos com moderação, não para determinar quais opiniões podem existir no Nexus Gaja.
Diferenciamos entre três níveis:
- **Detecção:** "Pode haver uma violação de regra aqui."
- **Avaliação:** "A probabilidade de violação de regra é, por exemplo, 94%."
- **Decisão:** "Que medidas são realmente tomadas?"
O terceiro nível deve ser controlado por um humano em casos graves.

### 2. A IA de moderação como um subsistema
Em vez de uma única IA, é estabelecido um subsistema robusto:
```texto
                 MODERAÇÃO NEXUS GAJA AI
                          │
       ┌──────────────────┼──────────────────┐
       │ │ │
  Idioma IA Segurança IA Fraude IA
       │ │ │
       ├──────────────┬───┴──────────────┬───┤
       │ │ │
 Identidade do comportamento de tradução
 Sinais de análise de análise
       │ │ │
       └──────────────┼──────────────────┘
                      ▼
               Avaliação de Risco
                      │
                      ▼
               Revisão Humana
```

### 3. Os módulos de IA mais importantes
Nexus Gaja utiliza nove áreas de análise especializadas:
- **M1 – Compreensão do idioma**: detecta idioma, dialeto, gíria, indicadores de ironia, problemas de tradução.
- **M2 – Detecção de toxicidade/abuso**: Detecta insultos, ataques pessoais, assédio.
- **M3 – Detecção de ameaças**: Detecta possíveis ameaças, chantagens e anúncios de violência.
- **M4 – Detecção de ódio/desumanização**: detecta ataques direcionados a pessoas com base em afiliações específicas.
- **M5 – Detecção de Spam/Manipulação**: Detecta spam, comportamento de bot, manipulação coordenada.
- **M6 – Detecção de fraude**: detecta tentativas suspeitas de fraude, phishing e engenharia social.
- **M7 – Integridade de Identidade**: Verifica sinais sobre invasão de conta, múltiplas contas, evasão de banimento.
- **M8 – Segurança de Mídia**: Analisa imagens, áudio, vídeo, documentos.
- **M9 – Context Engine**: O módulo mais importante. Ele mescla as descobertas individuais.

### 4. Por que o mecanismo de contexto é crucial
Uma pesquisa pura por palavra-chave seria insuficiente. "Eu poderia matá-lo de tanto rir" contém semanticamente violência, mas é uma figura de linguagem. “Amanhã às 20h vou atirar nele na frente da casa dele” é uma situação completamente diferente. A IA deve compreender o que a afirmação significa no seu contexto específico.

### 5. Moderação multilíngue
A moderação não pode simplesmente comparar palavras. Deve analisar o nível semântico (por exemplo, expressões idiomáticas alemãs versus expressões idiomáticas japonesas versus expressões regionais).

### 6. Idioma Original + Tradução
Original e tradução são analisados separadamente. Só então ocorre a “Avaliação de Moderação Combinada”. Isso permite que o Nexus Gaja determine se a própria tradução pode ter agravado ou alterado os fatos.

### 7. Pontuação de confiança
Cada avaliação de IA recebe uma pontuação de confiança (por exemplo, Probabilidade de ameaça: 0,96). No entanto: **Pontuação de confiança ≠ Verdade.** Uma pontuação de 96% significa apenas que o modelo está altamente certo de sua classificação, não necessariamente que o usuário seja culpado.

### 8. Uncertainty Becomes a Signal Itself
If the AI is uncertain (e.g., Threat: 0.62, Satire: 0.54), it must not simply enforce harsh rules. Instead, uncertainty is built directly into the architecture: **Human Review Required**.

### 9. Four Decision Zones
- 🟢 **GREEN**: Highly likely compliant. → no action.
- 🟡 **YELLOW**: Possible violation. → monitor / provide a warning if necessary.
- 🟠 **ORANGE**: Probable violation. → moderation review.
- 🔴 **RED**: Severe possible violation. → immediate protective measure + human review.

### 10. No "AI Punishment"
**The AI imposes no final sanctions.** It can trigger technical immediate measures (e.g., temporarily holding back a message) for severe security concerns, but the final decision remains verifiable.

### 11. Protective Measures Can Occur Automatically
In the event of a concrete threat (Threat detected → High confidence → Temporary restriction → Human review → Decision), we protect the threatened user without turning the AI into a judge.

### 12. The AI Must Be Able to Justify Its Decisions
The DSA requires clear and specific reasons. The AI provides structured reasoning: Rule (NG-CONDUCT-004), Detected (Potential concrete threat), Confidence (0.94), Relevant context (Previous 4 messages), Recommended action (Human review).

### 13. A IA não deve alterar secretamente o conteúdo
**Moderação AI nunca deve alterar o conteúdo original despercebido.** Durante a correção, tradução ou resumo automático, o original é sempre preservado.

### 14. Conteúdo gerado por IA
Distinguimos entre: criados por humanos, assistidos por IA, gerados por IA e manipulados por IA. Isso se tornará parte dos metadados de conteúdo.

### 15. Rotulagem de conteúdo de IA e camada de proveniência de IA
De acordo com as regras de transparência da Lei de IA da UE (em vigor em agosto de 2026), o conteúdo gerado por IA deve ser identificável. Fornecemos uma camada de proveniência de IA que armazena metadados (AI-Origin, Model, Timestamp, Human Review).

### 16. Detecção de Deepfake
A arquitetura visa detectar imagens sintéticas, vozes clonadas e deepfakes. No entanto, a detecção não é uma prova automática.

### 17. Nenhuma "máquina da verdade" automática (moderação ≠ verificação de fatos)
Um sistema verifica: “O conteúdo viola as regras?” (Moderação de Conteúdo), outro fornece: “Quais informações e fontes estão disponíveis?” (Auxílio à Informação). As opiniões não são simplesmente excluídas por estarem “erradas”.

### 18. Proteção contra má interpretação cultural
A IA requer **Modelos de Contexto Cultural** para evitar que as normas de comunicação de um país sejam assumidas como um padrão global.

### 19. Ironia, Sátira e Humor
A IA usa contexto, emojis, histórico de conversas e estruturas de ironia conhecidas, mas deve permitir a incerteza quando os significados são ambíguos.

### 20. Sem punição com base em uma única pontuação de IA
Nenhuma intervenção de moderação severa pode ser baseada apenas em um único resultado de classificação automatizada (Texto + Contexto + Comportamento + Linguagem + Mídia + Mecanismo de Regras = Avaliação de Risco).

### 21. Sinais de comportamento do usuário e nenhum sistema de crédito social
Isso está relacionado a sinais técnicos de abuso (por exemplo, postagem de spam em massa), e não a um sistema geral de classificação social. Nexus Gaja não mantém um Sistema de Crédito Social – a moderação serve à segurança, não à avaliação do valor de uma pessoa.

### 22. A IA de moderação deve ser auditável
Todas as decisões automatizadas relevantes são registradas (ID do evento, ID da regra, confiança, revisão humana, etc.) para garantir a rastreabilidade.

### 23. Falsos Positivos, Falsos Negativos e Métricas de Qualidade
Os tipos de erros são monitorados. Um painel mede Precisão, Recall e especialmente a **Taxa de reversão de apelações** (número de apelações bem-sucedidas).

### 24. Equidade linguística e preconceito de tradução
A qualidade da moderação deve ser comparável em todos os idiomas suportados (Referência de Moderação Multilíngue). Se os resultados da moderação diferirem entre o original e a tradução (Conflito de Tradução), isso deverá ser revisado especificamente.

### 25. Proposta de arquitetura e mecanismo de política
As regras (mecanismo de política) não são codificadas nos modelos de IA. A IA fornece descobertas; o Policy Engine decide com base nas regras atuais. Isso permite **mudanças de modelo sem mudanças de regras**.

### 26. O humano continua sendo a autoridade final
- **NG-AI-MOD-001**: A IA auxilia na detecção e classificação, mas não substitui a revisão humana em decisões severas.
- **NG-AI-MOD-002**: As decisões de moderação automatizadas devem ser rastreáveis, registráveis ​​e verificáveis.

**Resumo**: Estamos construindo um sistema de quatro estágios: Detecção de IA, Análise de Contexto e Risco, Mecanismo de Políticas e Governança Humana. Isso permite uma automação forte sem criar uma arquitetura perigosa de “IA como juiz”.

## Princípios de Financiamento e Modelo de Receita (WP 1.10.1)

Para o Nexus Gaja, aplica-se um princípio econômico altamente importante: **Nenhuma publicidade tradicional na plataforma.**
Isto distingue fundamentalmente o Nexus Gaja de muitas das redes sociais atuais. No entanto, isso não significa que o Nexus Gaja não possa ter caráter comercial. Pelo contrário, a plataforma deve ser economicamente viável para que o seu propósito social possa perdurar. A atividade económica é um meio para um fim, não o objetivo principal da plataforma.

### 1. Princípio NG-FIN-001
Nexus Gaja financia suas operações por meio de fluxos de receitas transparentes, separados dos interesses dos usuários, e não por meio da monetização da atenção ou dos dados pessoais de seus usuários.

### 2. Sem publicidade tradicional
Especificamente proibidos são:
- Banners publicitários
- Anúncios pop-up
- Anúncios em vídeo de reprodução automática
- Postagens patrocinadas no feed padrão
- Perfis de publicidade personalizados
- Venda de perfis de usuários ou dados pessoais
- Publicidade derivada de conversas privadas.

Nexus Gaja continua sendo um **espaço de comunicação em vez de um espaço publicitário**.

### 3. Financiamento sem publicidade (os 6 pilares)
O financiamento assenta em seis pilares:
```texto
                 NEXO GAJA
                     │
       ┌─────────────┼─────────────┐
       ▼ ▼ ▼
   DOAÇÕES PARA ORGANIZAÇÕES PREMIUM
       │ │ │
       ├─────────────┼─────────────┤
       ▼ ▼ ▼
    SERVIÇOS DE PARCERIAS DE SUBSÍDIOS
```

#### Pilar 1 – Assinatura Básica Gratuita
**Nexus Gaja Free** permite compreensão internacional básica para todos (perfil, comunicação internacional, postagens, comunidades, chats, tradução básica) sem nenhum custo.

#### Pilar 2 – Ofertas Premium
Ofertas pagas voluntárias (**Nexus Gaja Plus**) que oferecem maiores limites de armazenamento, maior qualidade de mídia, cotas de IA expandidas e recursos organizacionais.
**Importante (Freemium em vez de Dark Freemium):** A comunicação básica nunca deve ser degradada artificialmente.

#### Pilar 3 – Organizações
Contas especiais para escolas, universidades, ONGs, empresas e municípios (**Nexus Gaja Organization**). As escolas podem ser apoiadas através de taxas institucionais como multiplicadores da compreensão internacional.

#### Pilar 4 – Doações
O **Nexus Gaja Funding Pool** aceita doações gerais e destinadas (por exemplo, "para comunicação internacional de jovens"). Um **Ledger de Alocação de Fundos** garante uma alocação transparente de fundos.
**Fundo Propósito e Tômbola:** Uma parte das doações alimenta um pool para uso gratuito/com desconto. Um mecanismo de lotaria/tômbola pode atribuir estes fundos de forma transparente e auditável.

#### Pillar 5 – Institutional Funding
Foundations, cultural funding programs, or state programs.
**NG-FIN-002:** Financial support does not buy editorial or technical control (Independence).

#### Pilar 6 – Serviços Comerciais
Serviços B2B como **Tradução como serviço** (API), comunicação organizacional ou salas de conferência internacionais, sem sobrecarregar o feed padrão do usuário.

### 4. Sem monetização de dados e economia de vigilância
**NG-FIN-003:** Os dados pessoais do usuário não são uma mercadoria. Nenhuma venda de listas, perfis ou históricos. Nexus Gaja não lucra com vigilância psicológica (Economia de Vigilância).

### 5. Transparência Financeira e Razão de Fundos
**Nexus Gaja Financial Transparency:** Publicação de estruturas financeiras agregadas. As doações destinadas recebem contabilidade técnica (ID do Fundo → Finalidade → Saldo → Alocação). Não há subsídio cruzado de fins sociais no marketing corporativo.

### 6. Modelo de Financiamento Solidário
O preço é baseado na orientação para os custos, na justiça e na solidariedade.
**Prêmio Solidário:** Uma opção voluntária para usuários Premium financiarem uma parte do acesso de outro usuário. A solidariedade forçada ou uma sociedade de classe premium (menos respeito/moderação para usuários gratuitos) é estritamente proibida.

### 7. KPIs econômicos em vez de economia de engajamento
Não há dependência de manter os usuários “on-line pelo maior tempo possível” (sem raiva, feeds infinitos).
Em vez disso, usamos métricas como:
- **Índice de Comunicação Global (GCI):** Relações de comunicação bem-sucedidas entre pessoas de diferentes regiões linguísticas/culturais.
- **Índice de Sustentabilidade da Plataforma (PSR):** Receita recorrente / custos operacionais recorrentes (Meta ≥ 1).

### 8. What We Explicitly Do Not Want (Negative List)
Nexus Gaja is **not** financed by:
❌ Sale of personal data
❌ Personalized traditional advertising
❌ Monitoring user behavior for advertising purposes
❌ Sale of private communication data
❌ Hidden AI data usage
❌ Manipulative Premium paywalls
❌ Artificial reach restriction for monetization
❌ Paid political influence
❌ Purchase of privileged moderation decisions.

### 9. Arquitetura Financeira Preliminar
```texto
                         NEXO GAJA
                              │
             ┌────────────────┼────────────────┐
             │ │ │
             ▼ ▼ ▼
          EMPRESA DE ORGANIZAÇÕES DE USUÁRIOS
             │ │ │
             └────────────────┼────────────────┘
                              │
                       SERVIÇOS DE PLATAFORMA
                              │
          ┌─────────────────── ┼───────────────────┐
          ▼ ▼ ▼
       API DE DOAÇÕES PREMIUM
                              │
                    ┌─────────┴─────────┐
                    ▼ ▼
               FUNDOS RESTRITOS DO FUNDO GERAL
                                        │
                                        ▼
                                  FINALIDADE SOCIAL
```

### Summary of Financing Principles (NG-FIN)
- **NG-FIN-001:** No financing through traditional advertising.
- **NG-FIN-002:** No editorial/technical control through financial support.
- **NG-FIN-003:** Personal data is not a commodity.
- **NG-FIN-004:** Basic communication remains accessible without payment.
- **NG-FIN-005:** Premium offerings must not degrade free users.
- **NG-FIN-006:** Earmarked funds are managed according to their purpose.
- **NG-FIN-007:** Transparent management of donations and grants.
- **NG-FIN-008:** Commercial B2B services do not compromise independence.
- **NG-FIN-009:** Focus on sustainability rather than maximum monetization.
- **NG-FIN-010:** The structure permanently secures the social purpose.

## API, interfaces e arquitetura de comunicação (WP 1.11.3)

To ensure system stability, security, and scalability, Nexus Gaja follows a strictly API-first and event-driven architecture. 

### Princípios Fundamentais
- **Sem acesso direto ao banco de dados:** Os componentes se comunicam exclusivamente por meio de interfaces definidas (APIs ou eventos), nunca por meio de consultas diretas ao banco de dados de outros serviços.
- **API Gateway:** todas as solicitações de clientes externos são roteadas por meio de um API Gateway que gerencia autenticação, roteamento e limitação de taxa.
- **Abstração de Provedor:** Serviços externos (modelos de IA, provedores de pagamento, mecanismos de tradução) são integrados por meio de camadas de abstração, evitando dependências codificadas e permitindo troca flexível de provedor.

### Padrões de comunicação
- **APIs síncronas (REST/HTTPS):** Usadas para solicitações imediatas, como login, configurações de perfil ou traduções diretas.
- **Eventos assíncronos (barramento de eventos):** O sistema nervoso central do Nexus Gaja para processamento atrasado e desacoplado (por exemplo, `Message.Created` acionando moderação, tradução e notificação de forma assíncrona).
- **Tempo real (WebSocket):** Canais dedicados para chat ao vivo e indicadores de digitação.

### Segurança e Confiabilidade
- **Modelo de confiança zero:** O tráfego de rede interna não é automaticamente confiável; a comunicação confidencial entre serviços requer autenticação.
- **Padrão de Idempotência e Caixa de Saída:** Operações críticas (como doações ou mensagens) são projetadas para serem idempotentes para evitar processamento duplicado, utilizando o padrão Caixa de Saída para garantir que os eventos nunca sejam perdidos, mesmo durante transações de banco de dados.

## Modelo de domínio MVP (WP 1.12)

Nexus Gaja emprega uma arquitetura MVP estritamente orientada por domínio (ADR-025), projetada como um monólito modular com limites de domínio claros. Essa estrutura evita a complexidade prematura dos microsserviços, ao mesmo tempo que mantém a flexibilidade para dividir domínios específicos posteriormente.

### Entidades de domínio principal
A arquitetura separa explicitamente conceitos distintos para garantir a integridade dos dados e evitar armadilhas estruturais como "Nome de usuário = Humano":
- **Identidade e contas:** `Pessoa` ≠ `Conta de usuário` ≠ `Verificação de identidade`. Uma pessoa verificada participa através de uma conta, mas as entidades permanecem separadas.
- **Comunicação:** `Mensagem` ≠ `Tradução`. A mensagem original permanece imutável; traduções são entidades vinculadas.
- **Moderação:** `Relatório` ≠ `Decisão de Moderação`. Um relatório é apenas uma afirmação; um caso de moderação conduz a investigação.
- **Finanças:** `Doação` ≠ `Saldo do Fundo`. Os pagamentos são contabilizados através de um livro razão imutável para um fundo, garantindo a transparência financeira.

### Domínios Interconectados
O sistema é dividido em domínios lógicos claros (Contextos Delimitados): Identidade, Conta, Organização, Comunicação, Comunidade, Idioma, Moderação, Notificação, Finanças e Governança. Estes domínios mapeiam todo o percurso desde entidades do mundo real (Utilizadores, Escolas, ONG) até às suas interações digitais e governação relacionada.

## Status do projeto
O projeto está atualmente em fase ativa de arquitetura e planejamento.
As decisões arquitetônicas em andamento são documentadas na pasta `/docs`.