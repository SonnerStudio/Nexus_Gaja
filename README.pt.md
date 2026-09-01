# Nexus Gaja

![Logotipo do Nexus Gaja](assets/logo.jpg)

![Nexus Gaja Hero](assets/img/nexus_hero.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** é uma rede de comunicação inteligente e sensível ao contexto, projetada para revolucionar a comunicação global.

## Objetivo e Visão

![Visão Nexus Gaja](assets/img/nexus_vision.jpg)

Num mundo globalizado, a língua é muitas vezes a maior barreira. O principal objetivo do Nexus Gaja é permitir uma comunicação contínua, sem barreiras e contextualmente precisa entre as pessoas, independentemente de elas falarem um idioma comum.

Não se trata apenas de traduzir palavras rigidamente, mas de **transferir significado**. Nexus Gaja conecta pessoas em um nível mais profundo, compreendendo nuances culturais, regionais e contextuais, permitindo assim conversas genuínas e autênticas.

## Possibilidades e recursos
- **Comunicação Multimídia**: O sistema processa não apenas texto, mas também imagem, áudio e vídeo. Isso permite conversas totalmente envolventes (por exemplo, chamadas de vídeo ou mensagens de voz) em tempo real, ultrapassando barreiras linguísticas.
- **Sensibilidade ao Contexto**: Reconhecimento de ironia, expressões idiomáticas, jargões e dialetos regionais que muitas vezes são mal compreendidos por tradutores convencionais.
- **Rede multiplataforma**: serve como base para bate-papos privados, tópicos de fórum (postagens com comentários) e interações da comunidade global.

---

## Arquitetura Técnica (Conceito Central)

![Conceito de tradução do Nexus Gaja](assets/img/nexus_translation.jpg)

O núcleo técnico do Nexus Gaja é um modelo de comunicação personalizado estritamente dividido em três camadas:

1. **Original**: O objeto de comunicação (mensagem) criado pelo remetente permanece sempre imutável.
2. **Interpretação Semântica**: O sistema analisa não apenas as palavras, mas o significado real.
3. **Representação no idioma de destino**: A IA apenas cria uma representação temporária ou em cache do original para o respectivo destinatário com base no idioma de sua preferência. As traduções nunca substituem a mensagem original.

### Dependência de Contexto
As traduções no Nexus Gaja nunca visualizam as mensagens isoladamente. O mecanismo considera toda a hierarquia:
`Mensagem` → `Mensagens anteriores` → `Contexto do tópico` → `Contexto da comunidade` → `Idioma / região` → `Preferências do usuário`

### Eficiência por meio de tradução sob demanda
A tradução ocorre com eficiência de recursos apenas **mediante solicitação** (sob demanda). Quando um usuário solicita conteúdo, ele é traduzido para o idioma predefinido. Depois que uma tradução para um idioma específico é gerada, ela é armazenada permanentemente (cache) para acelerar drasticamente solicitações futuras.

## Moderação assistida por IA (WP 1.8.4)

![Moderação de IA do Nexus Gaja](assets/img/nexus_moderation.jpg)

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

### 3. The Most Important AI Modules
Nexus Gaja utilizes nine specialized analysis areas:
- **M1 – Language Understanding**: Detects language, dialect, slang, irony indicators, translation issues.
- **M2 – Toxicity / Abuse Detection**: Detects insults, personal attacks, harassment.
- **M3 – Threat Detection**: Detects potential threats, blackmail, violence announcements.
- **M4 – Hate / Dehumanization Detection**: Detects targeted attacks on people based on specific affiliations.
- **M5 – Spam / Manipulation Detection**: Detects spam, bot behavior, coordinated manipulation.
- **M6 – Fraud Detection**: Detects suspicious fraud attempts, phishing, social engineering.
- **M7 – Identity Integrity**: Checks signals regarding account takeovers, multiple accounts, ban evasion.
- **M8 – Media Safety**: Analyzes images, audio, video, documents.
- **M9 – Context Engine**: The most important module. It merges the individual findings.

### 4. Por que o mecanismo de contexto é crucial
Uma pesquisa pura por palavra-chave seria insuficiente. "Eu poderia matá-lo de tanto rir" contém semanticamente violência, mas é uma figura de linguagem. “Amanhã às 20h vou atirar nele na frente da casa dele” é uma situação completamente diferente. A IA deve compreender o que a afirmação significa no seu contexto específico.

### 5. Moderação multilíngue
A moderação não pode simplesmente comparar palavras. Deve analisar o nível semântico (por exemplo, expressões idiomáticas alemãs versus expressões idiomáticas japonesas versus expressões regionais).

### 6. Idioma Original + Tradução
Original e tradução são analisados separadamente. Só então ocorre a “Avaliação de Moderação Combinada”. Isso permite que o Nexus Gaja determine se a própria tradução pode ter agravado ou alterado os fatos.

### 7. Pontuação de confiança
Cada avaliação de IA recebe uma pontuação de confiança (por exemplo, Probabilidade de ameaça: 0,96). No entanto: **Pontuação de confiança ≠ Verdade.** Uma pontuação de 96% significa apenas que o modelo está altamente certo de sua classificação, não necessariamente que o usuário seja culpado.

### 8. A incerteza se torna um sinal em si
Se a IA for incerta (por exemplo, Ameaça: 0,62, Sátira: 0,54), ela não deve simplesmente impor regras severas. Em vez disso, a incerteza é incorporada diretamente na arquitetura: **É necessária revisão humana**.

### 9. Quatro zonas de decisão
- 🟢 **VERDE**: Altamente compatível. → nenhuma ação.
- 🟡 **AMARELO**: Possível violação. → monitorar/fornecer um aviso, se necessário.
- 🟠 **LARANJA**: Provável violação. → revisão de moderação.
- 🔴 **VERMELHO**: Possível violação grave. → medida protetiva imediata + revisão humana.

### 10. Sem "punição de IA"
**A IA não impõe sanções finais.** Ela pode desencadear medidas técnicas imediatas (por exemplo, reter temporariamente uma mensagem) para questões graves de segurança, mas a decisão final permanece verificável.

### 11. Medidas de proteção podem ocorrer automaticamente
No caso de uma ameaça concreta (Ameaça detectada → Alta confiança → Restrição temporária → Revisão humana → Decisão), protegemos o usuário ameaçado sem transformar a IA em juiz.

### 12. The AI Must Be Able to Justify Its Decisions
The DSA requires clear and specific reasons. The AI provides structured reasoning: Rule (NG-CONDUCT-004), Detected (Potential concrete threat), Confidence (0.94), Relevant context (Previous 4 messages), Recommended action (Human review).

### 13. AI Must Not Secretly Alter Content
**Moderation AI must never alter the original content unnoticed.** During automatic correction, translation, or summarization, the original is always preserved.

### 14. AI-Generated Content
We distinguish between: Human-created, AI-assisted, AI-generated, and AI-manipulated. This will become part of the content metadata.

### 15. Labeling of AI Content & AI Provenance Layer
According to the transparency rules of the EU AI Act (effective August 2026), AI-generated content must be identifiable. We provide an AI Provenance Layer that stores metadata (AI-Origin, Model, Timestamp, Human Review).

### 16. Deepfake Detection
The architecture aims to detect synthetic images, cloned voices, and deepfakes. However, detection is not automatically proof.

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

![Modelo Financeiro Nexus Gaja](assets/img/nexus_finance.jpg)

Para o Nexus Gaja, aplica-se um princípio econômico altamente importante: **Nenhuma publicidade tradicional na plataforma.**
Isto distingue fundamentalmente o Nexus Gaja de muitas das redes sociais atuais. No entanto, isso não significa que o Nexus Gaja não possa ter caráter comercial. Pelo contrário, a plataforma deve ser economicamente viável para que o seu propósito social possa perdurar. A atividade económica é um meio para um fim, não o objetivo principal da plataforma.

### 1. Princípio NG-FIN-001
Nexus Gaja financia suas operações por meio de fluxos de receitas transparentes, separados dos interesses dos usuários, e não por meio da monetização da atenção ou dos dados pessoais de seus usuários.

### 2. No Traditional Advertising
Specifically prohibited are:
- Banner ads
- Pop-up ads
- Auto-playing video ads
- Sponsored posts in the standard feed
- Personalized advertising profiles
- Sale of user profiles or personal data
- Advertising derived from private conversations.

Nexus Gaja remains a **communication space rather than an advertising space**.

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

#### Pilar 5 – Financiamento Institucional
Fundações, programas de financiamento cultural ou programas estaduais.
**NG-FIN-002:** O apoio financeiro não compra controle editorial ou técnico (Independência).

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

### 8. O que explicitamente não queremos (lista negativa)
Nexus Gaja **não** é financiado por:
❌ Venda de dados pessoais
❌ Publicidade tradicional personalizada
❌ Monitoramento do comportamento do usuário para fins publicitários
❌ Venda de dados de comunicação privada
❌ Uso oculto de dados de IA
❌ Paywalls Premium manipulativos
❌ Restrição de alcance artificial para monetização
❌ Influência política paga
❌ Compra de decisões de moderação privilegiadas.

### 9. Preliminary Financial Architecture
```text
                         NEXUS GAJA
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
          USERS          ORGANIZATIONS      ENTERPRISE
             │                │                │
             └────────────────┼────────────────┘
                              │
                       PLATFORM SERVICES
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
       PREMIUM             DONATIONS            API
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
               GENERAL FUND       RESTRICTED FUNDS
                                        │
                                        ▼
                                  SOCIAL PURPOSE
```

### Resumo dos Princípios de Financiamento (NG-FIN)
- **NG-FIN-001:** Sem financiamento através de publicidade tradicional.
- **NG-FIN-002:** Sem controle editorial/técnico através de apoio financeiro.
- **NG-FIN-003:** Dados pessoais não são uma mercadoria.
- **NG-FIN-004:** A comunicação básica permanece acessível sem pagamento.
- **NG-FIN-005:** As ofertas premium não devem prejudicar os usuários gratuitos.
- **NG-FIN-006:** Os recursos direcionados são administrados de acordo com sua finalidade.
- **NG-FIN-007:** Gestão transparente de doações e subsídios.
- **NG-FIN-008:** Os serviços comerciais B2B não comprometem a independência.
- **NG-FIN-009:** Foco na sustentabilidade em vez da monetização máxima.
- **NG-FIN-010:** A estrutura assegura permanentemente o propósito social.

## API, interfaces e arquitetura de comunicação (WP 1.11.3)

Para garantir a estabilidade, segurança e escalabilidade do sistema, o Nexus Gaja segue uma arquitetura estritamente baseada em API e orientada a eventos.

### Princípios Fundamentais
- **Sem acesso direto ao banco de dados:** Os componentes se comunicam exclusivamente por meio de interfaces definidas (APIs ou eventos), nunca por meio de consultas diretas ao banco de dados de outros serviços.
- **API Gateway:** todas as solicitações de clientes externos são roteadas por meio de um API Gateway que gerencia autenticação, roteamento e limitação de taxa.
- **Abstração de Provedor:** Serviços externos (modelos de IA, provedores de pagamento, mecanismos de tradução) são integrados por meio de camadas de abstração, evitando dependências codificadas e permitindo troca flexível de provedor.

### Padrões de comunicação
- **APIs síncronas (REST/HTTPS):** Usadas para solicitações imediatas, como login, configurações de perfil ou traduções diretas.
- **Eventos assíncronos (barramento de eventos):** O sistema nervoso central do Nexus Gaja para processamento atrasado e desacoplado (por exemplo, `Message.Created` acionando moderação, tradução e notificação de forma assíncrona).
- **Tempo real (WebSocket):** Canais dedicados para chat ao vivo e indicadores de digitação.

### Security and Reliability
- **Zero-Trust Model:** Internal network traffic is not automatically trusted; sensitive service-to-service communication requires authentication.
- **Idempotency & Outbox Pattern:** Critical operations (like donations or messaging) are designed to be idempotent to prevent duplicate processing, utilizing the Outbox pattern to ensure events are never lost even during database transactions.

## Modelo de domínio MVP (WP 1.12)

![Monólito Modular Nexus Gaja](assets/img/nexus_architecture.jpg)

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

---

---

## Licença e Propriedade Intelectual

> **© 2024–2026 SonnerStudio - Jan Friske Gründer, Inhaber, Direktor und Chefdesigner von SonnerStudio — Todos os direitos reservados.**

**Nexus Gaja** é propriedade intelectual exclusiva de **Jan Friske**, operando sob **SonnerStudio**.

Jan Friske é o único criador, arquiteto e proprietário do Nexus Gaja — incluindo todos os conceitos, arquitetura, modelos de domínio, identidade de marca e documentação associada.

**Nenhum direito, licença ou participação acionária é detido por terceiros**, independentemente de seu tamanho, posição de mercado ou influência no setor de tecnologia.

### O que NÃO é permitido sem consentimento explícito por escrito:
- Copiar, reproduzir ou distribuir este software ou sua documentação
- Modificar, adaptar ou criar trabalhos derivados
- Uso comercial de qualquer parte do Nexus Gaja
- Utilizar o conteúdo deste repositório como dados de treinamento para sistemas AI ou LLM
- Sublicenciar ou transferir quaisquer direitos a terceiros

### Propriedade Intelectual Protegida
Os seguintes conceitos originais são protegidos como segredos comerciais e criações proprietárias de Jan Friske:
- O modelo de comunicação em camadas (Original, Interpretação Semântica, Resultado Traduzido)
- O princípio da separação de identidade (Pessoa não é conta, não é verificação de identidade)
- O modelo de dissociação Mensagem-Tradução (Mensagem não é Tradução)
- A estrutura de governança de moderação de IA

### Contato
Para consultas de licenciamento: https://github.com/SonnerStudio

Nexus Gaja e o logotipo Nexus Gaja são marcas registradas de Jan Friske. É proibido o uso não autorizado do nome ou marca.

Veja os termos completos da licença no arquivo LICENSE.
