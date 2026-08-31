# Nexus Gaja

![Logo Nexus Gaja](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** è una rete di comunicazione intelligente e sensibile al contesto progettata per rivoluzionare la comunicazione globale.

## Scopo e visione
In un mondo globalizzato, la lingua è spesso la barriera più grande. L'obiettivo principale di Nexus Gaja è consentire una comunicazione fluida, priva di barriere e contestualmente accurata tra le persone, indipendentemente dal fatto che parlino o meno una lingua comune.

Non si tratta solo di tradurre rigidamente le parole, ma di **trasferire significato**. Nexus Gaja connette le persone a un livello più profondo comprendendo le sfumature culturali, regionali e contestuali, consentendo così conversazioni genuine e autentiche.

## Possibilità e caratteristiche
- **Comunicazione multimediale**: il sistema elabora non solo testo, ma anche immagini, audio e video. Ciò consente conversazioni completamente coinvolgenti (ad esempio, videochiamate o messaggi vocali) in tempo reale oltre le barriere linguistiche.
- **Sensibilità al contesto**: riconoscimento dell'ironia, degli idiomi, del gergo e dei dialetti regionali che spesso vengono fraintesi dai traduttori convenzionali.
- **Rete multipiattaforma**: funge da base per chat private, thread di forum (post con commenti) e interazioni con la comunità globale.

---

## Architettura tecnica (concetto fondamentale)

Il nucleo tecnico di Nexus Gaja è un modello di comunicazione personalizzato, rigorosamente suddiviso in tre livelli:

1. **Originale**: L'oggetto di comunicazione (messaggio) creato dal mittente rimane sempre immutabile.
2. **Interpretazione semantica**: il sistema analizza non solo le parole, ma il significato effettivo.
3. **Rappresentazione della lingua di destinazione**: l'IA crea semplicemente una rappresentazione temporanea o memorizzata nella cache dell'originale per il rispettivo destinatario in base alla lingua preferita. Le traduzioni non sovrascrivono mai il messaggio originale.

### Dipendenza dal contesto
Le traduzioni in Nexus Gaja non visualizzano mai i messaggi isolatamente. Il motore considera l'intera gerarchia:
`Messaggio` → `Messaggi precedenti` → `Contesto discussione` → `Contesto comunità` → `Lingua/Regione` → `Preferenze utente`

### Efficienza grazie alla traduzione on-demand
La traduzione avviene in modo efficiente in termini di risorse solo **su richiesta** (on-demand). Quando un utente richiede contenuto, questo viene tradotto nella lingua preimpostata. Una volta generata una traduzione per una lingua specifica, viene archiviata in modo permanente (caching) per accelerare drasticamente le richieste future.

## Moderazione assistita dall'intelligenza artificiale (WP 1.8.4)

Con la moderazione assistita dall’intelligenza artificiale facciamo un passo significativo dall’idea del prodotto all’architettura tecnica, tenendo conto delle attuali normative UE (requisiti di trasparenza della legge UE sull’AI ai sensi dell’articolo 50; legge sui servizi digitali con motivazioni comprensibili e possibilità di ricorso).

### 1. Principio fondamentale
La frase più importante per l'architettura è: **L'intelligenza artificiale di moderazione è un sistema di revisione, non un sistema di governo autonomo.**
È progettato per assistere gli umani con moderazione, non per determinare autonomamente quali opinioni possono esistere su Nexus Gaja.
Distinguiamo tre livelli:
- **Rilevamento:** "Potrebbe esserci una violazione delle regole qui."
- **Valutazione:** "La probabilità di una violazione delle regole è, ad esempio, del 94%."
- **Decisione:** "Quale azione viene effettivamente intrapresa?"
Il terzo livello deve essere controllato da un essere umano nei casi più gravi.

### 2. L'intelligenza artificiale della moderazione come sottosistema
Invece di una singola IA, viene creato un robusto sottosistema:
"testo".
                 MODERAZIONE AI NEXUS GAJA
                          │
       ┌──────────────────┼──────────────────┐
       │ │ │
  AI linguistica AI di sicurezza AI antifrode
       │ │ │
       ├──────────────┬───┴──────────────┬───┤
       │ │ │
 Identità comportamentale traduttiva
 Segnali di analisi di analisi
       │ │ │
       └──────────────┼──────────────────┘
                      ▼
               Valutazione del rischio
                      │
                      ▼
               Revisione umana
```

### 3. I moduli AI più importanti
Nexus Gaja utilizza nove aree di analisi specializzate:
- **M1 – Comprensione della lingua**: rileva lingua, dialetto, slang, indicatori di ironia, problemi di traduzione.
- **M2 – Rilevamento tossicità/abuso**: rileva insulti, attacchi personali, molestie.
- **M3 – Threat Detection**: rileva potenziali minacce, ricatti, annunci di violenza.
- **M4 – Rilevamento di odio/disumanizzazione**: rileva attacchi mirati contro persone in base ad affiliazioni specifiche.
- **M5 – Rilevamento spam/manipolazione**: rileva spam, comportamento bot e manipolazione coordinata.
- **M6 – Rilevamento frodi**: rileva tentativi sospetti di frode, phishing, ingegneria sociale.
- **M7 – Integrità dell'identità**: controlla i segnali riguardanti il ​​furto di account, account multipli, evasione dei ban.
- **M8 – Sicurezza multimediale**: analizza immagini, audio, video, documenti.
- **M9 – Context Engine**: il modulo più importante. Unisce i singoli risultati.

### 4. Perché il motore di contesto è fondamentale
Una semplice ricerca per parola chiave non sarebbe sufficiente. "Potrei ucciderlo dal ridere" contiene semanticamente violenza ma è un modo di dire. "Domani alle 20 gli sparerò davanti a casa" è una situazione completamente diversa. L'intelligenza artificiale deve comprendere cosa significa l'affermazione nel suo contesto specifico.

### 5. Moderazione multilingue
La moderazione non può semplicemente confrontare le parole. Deve analizzare il livello semantico (ad esempio, modi di dire tedeschi contro modi di dire giapponesi contro espressioni regionali).

### 6. Lingua originale + traduzione
Originale e traduzione vengono analizzati separatamente. Solo allora ha luogo la "valutazione della moderazione combinata". Ciò consente a Nexus Gaja di determinare se la traduzione stessa potrebbe aver intensificato o alterato i fatti.

### 7. Punteggio di fiducia
Ogni valutazione dell'intelligenza artificiale riceve un punteggio di confidenza (ad esempio, probabilità di minaccia: 0,96). Tuttavia: **Punteggio di confidenza ≠ Verità.** Un punteggio del 96% significa solo che il modello è altamente certo della sua classificazione, non necessariamente che l'utente è colpevole.

### 8. L'incertezza diventa essa stessa un segnale
Se l’IA è incerta (ad esempio, Minaccia: 0,62, Satira: 0,54), non deve semplicemente imporre regole dure. Invece, l’incertezza è integrata direttamente nell’architettura: **Revisione umana richiesta**.

### 9. Quattro zone decisionali
- 🟢 **VERDE**: molto probabilmente conforme. → nessuna azione.
- 🟡 **GIALLO**: Possibile violazione. → monitorare/fornire un avviso se necessario.
- 🟠 **ARANCIONE**: Probabile violazione. → revisione di moderazione.
- 🔴 **ROSSO**: possibile violazione grave. → misura protettiva immediata + revisione umana.

### 10. Nessuna "punizione dell'IA"
**L'intelligenza artificiale non impone sanzioni definitive.** Può attivare misure tecniche immediate (ad esempio, trattenere temporaneamente un messaggio) per gravi problemi di sicurezza, ma la decisione finale rimane verificabile.

### 11. Le misure protettive possono avvenire automaticamente
In caso di minaccia concreta (Minaccia rilevata → Confidenza elevata → Restrizione temporanea → Revisione umana → Decisione), proteggiamo l'utente minacciato senza trasformare l'IA in un giudice.

### 12. L'intelligenza artificiale deve essere in grado di giustificare le proprie decisioni
Il DSA richiede motivazioni chiare e specifiche. L'intelligenza artificiale fornisce un ragionamento strutturato: Regola (NG-CONDUCT-004), Rilevato (Minaccia potenziale concreta), Confidenza (0,94), Contesto pertinente (4 messaggi precedenti), Azione consigliata (Revisione umana).

### 13. L'intelligenza artificiale non deve alterare segretamente i contenuti
**La moderazione AI non deve mai alterare il contenuto originale senza che nessuno se ne accorga.** Durante la correzione automatica, la traduzione o il riepilogo, l'originale viene sempre preservato.

### 14. Contenuti generati dall'intelligenza artificiale
Distinguiamo tra: creato dall’uomo, assistito dall’intelligenza artificiale, generato dall’intelligenza artificiale e manipolato dall’intelligenza artificiale. Questo diventerà parte dei metadati del contenuto.

### 15. Etichettatura del contenuto dell'AI e del livello di provenienza dell'AI
Secondo le norme sulla trasparenza della legge UE sull’intelligenza artificiale (in vigore da agosto 2026), i contenuti generati dall’intelligenza artificiale devono essere identificabili. Forniamo un livello di provenienza AI che memorizza i metadati (origine AI, modello, timestamp, revisione umana).

### 16. Rilevamento di deepfake
L'architettura mira a rilevare immagini sintetiche, voci clonate e deepfake. Tuttavia, il rilevamento non è una prova automatica.

### 17. Nessuna "macchina della verità" automatica (moderazione ≠ verifica dei fatti)
Un sistema controlla: "Il contenuto viola le regole?" (Moderazione dei contenuti), un altro prevede: "Quali informazioni e fonti sono disponibili?" (Assistenza informativa). Le opinioni non vengono semplicemente cancellate perché "sbagliate".

### 18. Protezione contro interpretazioni errate a livello culturale
L’intelligenza artificiale richiede **modelli di contesto culturale** per evitare che le norme di comunicazione di un paese vengano assunte come standard globale.

### 19. Ironia, satira e umorismo
L’intelligenza artificiale utilizza il contesto, gli emoji, la cronologia delle conversazioni e le strutture dell’ironia conosciute, ma deve consentire l’incertezza quando i significati sono ambigui.

### 20. Nessuna punizione basata su un singolo punteggio AI
Nessun intervento di moderazione grave può basarsi esclusivamente su un singolo risultato di classificazione automatizzata (testo + contesto + comportamento + lingua + media + motore di regole = valutazione del rischio).

### 21. Segnali comportamentali degli utenti e assenza di sistema di credito sociale
Ciò si riferisce a segnali di abuso tecnico (ad esempio, pubblicazione di spam di massa), non a un sistema di classificazione sociale generale. Nexus Gaja non mantiene un sistema di credito sociale: la moderazione serve alla sicurezza, non alla valutazione del valore di una persona.

### 22. L'intelligenza artificiale della moderazione deve essere verificabile
Tutte le decisioni automatizzate rilevanti vengono registrate (ID evento, ID regola, fiducia, revisione umana, ecc.) per garantire la tracciabilità.

### 23. Falsi positivi, falsi negativi e metriche di qualità
I tipi di errore vengono monitorati. Una dashboard misura la precisione, il richiamo e soprattutto il **Tasso di annullamento del ricorso** (numero di ricorsi accolti).

### 24. Equità linguistica e pregiudizi traduttivi
La qualità della moderazione deve essere comparabile in tutte le lingue supportate (benchmark di moderazione multilingue). Se i risultati della moderazione differiscono tra l'originale e la traduzione (Conflitto di traduzione), questo deve essere specificamente esaminato.

### 25. Proposta di architettura e motore politico
Le regole (Policy Engine) non sono codificate nei modelli AI. L'intelligenza artificiale fornisce risultati; il Policy Engine decide in base alle regole attuali. Ciò consente **modifiche al modello senza modifiche alle regole**.

### 26. L'essere umano rimane l'autorità finale
- **NG-AI-MOD-001**: l'intelligenza artificiale assiste nel rilevamento e nella classificazione, ma non sostituisce la revisione umana nelle decisioni gravi.
- **NG-AI-MOD-002**: le decisioni di moderazione automatizzata devono essere tracciabili, registrabili e verificabili.

**Riepilogo**: Stiamo costruendo un sistema in quattro fasi: rilevamento dell'intelligenza artificiale, analisi del contesto e dei rischi, motore delle politiche e governance umana. Ciò consente una forte automazione senza creare una pericolosa architettura "AI as Judge".

## Principi di finanziamento e modello delle entrate (WP 1.10.1)

Per Nexus Gaja vale un principio economico molto importante: **nessuna pubblicità tradizionale all'interno della piattaforma.**
Ciò distingue fondamentalmente Nexus Gaja da molti dei social network odierni. Ciò però non significa che Nexus Gaja non possa avere carattere commerciale. Al contrario, la piattaforma deve essere economicamente sostenibile affinché il suo scopo sociale possa durare. L’attività economica è un mezzo per raggiungere un fine, non lo scopo principale della piattaforma.

### 1. Principio NG-FIN-001
Nexus Gaja finanzia le sue operazioni attraverso flussi di entrate trasparenti separati dagli interessi degli utenti e non attraverso la monetizzazione dell'attenzione o dei dati personali dei suoi utenti.

### 2. Nessuna pubblicità tradizionale
In particolare sono vietati:
- Banner pubblicitari
- Annunci pop-up
- Annunci video a riproduzione automatica
- Post sponsorizzati nel feed standard
- Profili pubblicitari personalizzati
- Vendita di profili utente o dati personali
- Pubblicità derivata da conversazioni private.

Nexus Gaja rimane uno **spazio di comunicazione piuttosto che uno spazio pubblicitario**.

### 3. Finanziamenti senza pubblicità (i 6 pilastri)
Il finanziamento si basa su sei pilastri:
"testo".
                 NEXUS GAJA
                     │
       ┌─────────────┼─────────────┐
       ▼ ▼ ▼
   DONAZIONI PREMIUM ALL'ORGANIZZAZIONE
       │ │ │
       ├─────────────┼─────────────┤
       ▼ ▼ ▼
    CONCEDE SERVIZI DI PARTNERSHIP
```

#### Pilastro 1 – Abbonamento base gratuito
**Nexus Gaja Free** consente a tutti la comprensione internazionale di base (profilo, comunicazione internazionale, post, community, chat, traduzione di base) senza alcun costo.

#### Pilastro 2 – Offerte Premium
Offerte volontarie a pagamento (**Nexus Gaja Plus**) che forniscono limiti di archiviazione maggiori, qualità multimediale più elevata, quote AI ampliate e funzionalità organizzative.
**Importante (Freemium invece di Dark Freemium):** La comunicazione di base non deve mai essere degradata artificialmente.

#### Pilastro 3 – Organizzazioni
Conti speciali per scuole, università, ONG, imprese e comuni (**Nexus Gaja Organization**). Le scuole possono essere sostenute attraverso tariffe istituzionali in quanto moltiplicatori della comprensione internazionale.

#### Pilastro 4 – Donazioni
Il **Nexus Gaja Funding Pool** accetta donazioni generali e mirate (ad esempio, "per la comunicazione giovanile internazionale"). Un **Registro di allocazione dei fondi** garantisce un'allocazione trasparente dei fondi.
**Scopo Fondo e Tombola:** Una parte delle donazioni alimenta un pool per l'utilizzo gratuito/scontato. Un meccanismo di lotteria/tombola può allocare questi fondi in modo trasparente e verificabile.

#### Pilastro 5 – Finanziamenti istituzionali
Fondazioni, programmi di finanziamento culturale o programmi statali.
**NG-FIN-002:** Il sostegno finanziario non acquista il controllo editoriale o tecnico (Indipendenza).

#### Pilastro 6 – Servizi commerciali
Servizi B2B come **Translation-as-a-Service** (API), comunicazione organizzativa o sale conferenze internazionali, senza gravare sul feed utente standard.

### 4. Nessuna economia di monetizzazione dei dati e di sorveglianza
**NG-FIN-003:** I dati personali degli utenti non sono una merce. Nessuna vendita di elenchi, profili o storie. Nexus Gaja non trae profitto dalla sorveglianza psicologica (Surveillance Economy).

### 5. Trasparenza finanziaria e registro dei fondi
**Trasparenza finanziaria di Nexus Gaja:** Pubblicazione di strutture finanziarie aggregate. Le donazioni destinate ricevono una contabilità tecnica (ID fondo → Scopo → Saldo → Allocazione). Nessuna sovvenzione incrociata degli scopi sociali nel marketing aziendale.

### 6. Modello di finanziamento basato sulla solidarietà
I prezzi si basano sull’orientamento ai costi, sull’equità e sulla solidarietà.
**Solidarity Premium:** Un'opzione volontaria per gli utenti Premium di finanziare una parte dell'accesso di un altro utente. La solidarietà forzata o una società di classe premium (meno rispetto/moderazione per gli utenti gratuiti) è severamente vietata.

### 7. KPI economici anziché Engagement Economy
Nessuna dipendenza dal mantenere gli utenti "online il più a lungo possibile" (niente ragebait, feed infiniti).
Utilizziamo invece parametri come:
- **Indice di comunicazione globale (GCI):** Relazioni comunicative di successo tra persone provenienti da diverse regioni linguistiche/culturali.
- **Rapporto di sostenibilità della piattaforma (PSR):** Entrate ricorrenti/costi operativi ricorrenti (Target ≥ 1).

### 8. Ciò che esplicitamente non vogliamo (elenco negativo)
Nexus Gaja **non** è finanziato da:
❌ Vendita di dati personali
❌ Pubblicità tradizionale personalizzata
❌ Monitoraggio del comportamento degli utenti per scopi pubblicitari
❌ Vendita di dati di comunicazioni private
❌ Utilizzo dei dati AI nascosti
❌ Paywall premium manipolativi
❌ Restrizione artificiale della portata per la monetizzazione
❌ Influenza politica retribuita
❌Acquisto delle decisioni di moderazione privilegiata.

### 9. Architettura finanziaria preliminare
"testo".
                         NEXUS GAJA
                              │
             ┌────────────────┼────────────────┐
             │ │ │
             ▼ ▼ ▼
          ORGANIZZAZIONI UTENTI IMPRESA
             │ │ │
             └────────────────┼────────────────┘
                              │
                       SERVIZI DELLA PIATTAFORMA
                              │
          ┌─────────────────── ┼───────────────────┐
          ▼ ▼ ▼
       API DONAZIONI PREMIUM
                              │
                    ┌─────────┴─────────┐
                    ▼▼
               FONDI GENERALI RISTRETTI
                                        │
                                        ▼
                                  SCOPO SOCIALE
```

### Sintesi dei principi di finanziamento (NG-FIN)
- **NG-FIN-001:** Nessun finanziamento tramite pubblicità tradizionale.
- **NG-FIN-002:** Nessun controllo editoriale/tecnico tramite supporto finanziario.
- **NG-FIN-003:** I dati personali non sono una merce.
- **NG-FIN-004:** La comunicazione di base rimane accessibile senza pagamento.
- **NG-FIN-005:** Le offerte Premium non devono degradare gli utenti gratuiti.
- **NG-FIN-006:** I fondi accantonati sono gestiti in base al loro scopo.
- **NG-FIN-007:** Gestione trasparente di donazioni e sussidi.
- **NG-FIN-008:** I servizi commerciali B2B non compromettono l'indipendenza.
- **NG-FIN-009:** Focus sulla sostenibilità piuttosto che sulla massima monetizzazione.
- **NG-FIN-010:** La struttura garantisce permanentemente lo scopo sociale.

## Stato del progetto
Il progetto è attualmente in fase di architettura e pianificazione attiva.
Le decisioni architetturali in corso sono documentate nella cartella "/docs".