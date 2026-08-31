# WP 1.8.4 – KI-gestützte Moderation

Bei WP 1.8.4 – KI-gestützte Moderation machen wir einen deutlichen Schritt von der Produktidee zur späteren technischen Architektur, unter Berücksichtigung der aktuell geltenden EU-Vorgaben (Transparenzpflichten des EU-KI-Gesetzes nach Art. 50; Digital Services Act mit nachvollziehbaren Begründungen und Beschwerdemöglichkeiten).

## 1. Grundprinzip

Der wichtigste Satz für die Architektur lautet:

**Die Moderations-KI ist ein Prüfsystem und kein autonomes Herrschaftssystem.**

Sie soll Menschen bei der Moderation unterstützen, nicht selbst darüber bestimmen, welche Meinungen auf Nexus Gaja existieren dürfen.

Damit unterscheiden wir drei Dinge:

- **Erkennen:** „Hier könnte ein Regelverstoß vorliegen.“
- **Bewerten:** „Die Wahrscheinlichkeit eines Regelverstoßes beträgt beispielsweise 94 %.“
- **Entscheiden:** „Welche Maßnahme wird tatsächlich ergriffen?“

Die dritte Ebene muss bei schwerwiegenden Fällen menschlich kontrolliert werden.

## 2. Die Moderations-KI wird ein eigenes Subsystem

Ich würde sie nicht einfach als eine einzelne KI betrachten.

Stattdessen:

```text
                 NEXUS GAJA AI MODERATION
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
  Language AI        Safety AI          Fraud AI
       │                  │                  │
       ├──────────────┬───┴──────────────┬───┤
       │              │                  │
 Translation      Behaviour          Identity
 Analysis         Analysis            Signals
       │              │                  │
       └──────────────┼──────────────────┘
                      ▼
               Risk Assessment
                      │
                      ▼
               Human Review
```

Das ist wesentlich robuster als eine einzelne „Moderations-KI“.

## 3. Die wichtigsten KI-Module

Für Nexus Gaja sehe ich zunächst neun spezialisierte Analysebereiche:

- **M1 – Language Understanding**
  Erkennt: Sprache, Dialekt/Variante, gemischte Sprache, Umgangssprache, Slang, Ironieindikatoren, Übersetzungsprobleme.
- **M2 – Toxicity / Abuse Detection**
  Erkennt: Beschimpfungen, persönliche Angriffe, Belästigung, gezielte Provokation.
- **M3 – Threat Detection**
  Erkennt mögliche: Drohungen, Erpressungen, Gewaltankündigungen, Einschüchterungen.
- **M4 – Hate / Dehumanization Detection**
  Erkennt gezielte Angriffe auf Menschen aufgrund bestimmter Zugehörigkeiten.
- **M5 – Spam / Manipulation Detection**
  Erkennt: Spam, Massenposting, Botverhalten, künstliche Interaktion, koordinierte Manipulation.
- **M6 – Fraud Detection**
  Erkennt verdächtige: Betrugsversuche, Identitätstäuschungen, Phishing, Social Engineering.
- **M7 – Identity Integrity**
  Prüft Signale bezüglich: Kontoübernahme, ungewöhnlicher Identitätswechsel, Mehrfachkonten, Umgehung von Sperren.
- **M8 – Media Safety**
  Analysiert: Bilder, Audio, Video, Dokumente.
- **M9 – Context Engine**
  Das ist vielleicht das wichtigste Modul. Es führt die einzelnen Erkenntnisse zusammen.

## 4. Warum die Context Engine so wichtig ist

Eine reine Schlüsselwortsuche wäre für Nexus Gaja völlig unzureichend.

Beispiel: „Ich könnte ihn umbringen vor Lachen.“
Das enthält semantisch Gewalt, ist aber möglicherweise eine Redewendung.

Dagegen: „Morgen um 20 Uhr werde ich ihn vor seinem Haus erschießen.“
ist eine vollkommen andere Situation.

Die KI muss daher verstehen:
**Was bedeutet die Aussage in diesem konkreten Kontext?**

## 5. Mehrsprachige Moderation

Das ist für Nexus Gaja eine besondere Herausforderung.

- Ein deutscher Nutzer schreibt: „Du hast ja nicht alle Tassen im Schrank.“
- Ein Japaner schreibt: eine japanische Redewendung mit vergleichbarer Bedeutung.
- Ein Spanier verwendet: einen regionalen Ausdruck.

Die Moderation darf nicht einfach Wörter vergleichen. Sie muss die Bedeutungsebene analysieren.

## 6. Originalsprache + Übersetzung

Unser bereits beschlossenes Prinzip wird hier zwingend:

```text
Original
   │
   ├── Original Language Analysis
   │
   └── Translation
            │
            └── Target Language Analysis

Erst danach:
Combined Moderation Assessment
```

So kann Nexus Gaja feststellen, ob möglicherweise die Übersetzung selbst den Sachverhalt verschärft oder verändert hat.

## 7. Confidence Score

Jede KI-Bewertung erhält einen Konfidenzwert.

Beispielsweise:
- Threat probability: 0.96
- Harassment probability: 0.21
- Satire probability: 0.08
- Translation uncertainty: 0.03

Aber: **Confidence Score ≠ Wahrheit.**

Ein Score von 96 % bedeutet: Das Modell ist sehr sicher, dass seine Klassifikation zutrifft.
Nicht: Der Nutzer ist schuldig.

## 8. Unsicherheit wird selbst zum Signal

Das halte ich für sehr wichtig.
Wenn die KI sagt:
- Threat: 0.62
- Satire: 0.54
- Context: insufficient

darf sie nicht einfach hart durchgreifen.
Stattdessen: **Human Review Required**

Damit bauen wir Unsicherheit direkt in die Architektur ein.

## 9. Vier Entscheidungsbereiche

Ich würde für die KI vier Zonen definieren:

- 🟢 **GREEN**: Sehr wahrscheinlich regelkonform. → keine Aktion.
- 🟡 **YELLOW**: Möglicher Verstoß. → beobachten / gegebenenfalls Hinweis.
- 🟠 **ORANGE**: Wahrscheinlicher Verstoß. → Moderationsprüfung.
- 🔴 **RED**: Schwerwiegender möglicher Verstoß. → sofortige Schutzmaßnahme + menschliche Prüfung.

## 10. Keine „KI-Strafe“

Das sollten wir ausdrücklich festschreiben:
**Die KI verhängt keine endgültigen Sanktionen.**

Sie kann bei bestimmten eindeutig definierten Situationen technische Sofortmaßnahmen auslösen, etwa eine Nachricht vorübergehend zurückhalten, wenn eine hohe Wahrscheinlichkeit eines schweren Sicherheitsproblems besteht.

Aber: Die endgültige Entscheidung bleibt überprüfbar.

## 11. Schutzmaßnahmen können automatisch erfolgen

Das ist beispielsweise bei einer konkreten Drohung sinnvoll.

```text
Threat detected
      ↓
High confidence
      ↓
Temporary restriction
      ↓
Human review
      ↓
Decision
```

Damit schützen wir den möglicherweise bedrohten Nutzer, ohne die KI zum Richter zu machen.

## 12. Die KI muss ihre Entscheidung begründen können

Nicht zwingend durch eine lange philosophische Erklärung, sondern strukturiert:

- **Rule:** NG-CONDUCT-004
- **Detected:** Potential concrete threat
- **Confidence:** 0.94
- **Relevant context:** Previous 4 messages
- **Translation uncertainty:** 0.02
- **Recommended action:** Human review

Der DSA verlangt bei Moderationsentscheidungen ohnehin klare und spezifische Gründe; unser Konzept geht damit bewusst in dieselbe Richtung.

## 13. KI darf nicht heimlich Inhalte verändern

Ein weiterer Grundsatz:
**Moderations-KI darf den Originalinhalt niemals unbemerkt verändern.**

Wenn ein Beitrag automatisch korrigiert, übersetzt, zusammengefasst oder anderweitig durch KI verarbeitet wird, bleibt das Original erhalten.

## 14. KI-generierte Inhalte

Hier kommt eine zusätzliche Dimension hinzu. Nexus Gaja selbst wird KI einsetzen.
Deshalb müssen wir unterscheiden:

- Nutzer erstellt Inhalt selbst → **Human-created**
- Nutzer nutzt KI zur Unterstützung → **AI-assisted**
- Inhalt wird vollständig von KI erzeugt → **AI-generated**
- Inhalt wurde durch KI manipuliert → **AI-manipulated**

Das sollte Bestandteil der Content-Metadaten werden.

## 15. Kennzeichnung von KI-Inhalten

Nach den seit 2. August 2026 geltenden Transparenzregeln des EU-KI-Gesetzes müssen bestimmte KI-generierte bzw. manipulierte Inhalte erkennbar gemacht werden. Deshalb sollten wir technisch von Anfang an eine **AI Provenance Layer** vorsehen.

## 16. AI Provenance Layer

Jeder relevante Content kann intern Metadaten besitzen:

- **AI-Origin:** NONE / ASSISTED / GENERATED / TRANSFORMED
- **Model:** NG-Model-X
- **Timestamp:** ...
- **Human Review:** TRUE / FALSE

Das kann später für Transparenz, Moderation und rechtliche Nachvollziehbarkeit sehr wertvoll werden.

## 17. Deepfake-Erkennung

Da Bilder, Audio und Video zu Nexus Gaja gehören, sollte die Moderationsarchitektur perspektivisch erkennen können: synthetische Bilder, manipulierte Fotos, synthetische Stimmen, Deepfake-Videos, manipulierte Audiospuren.

Aber: **Erkennung ist nicht automatisch Beweis.** Auch hier brauchen wir Konfidenzwerte und gegebenenfalls menschliche Prüfung.

## 18. Besonders wichtig: Keine automatische „Wahrheitsmaschine“

Ich würde Fact Checking von Moderation trennen.
Ein Nutzer darf beispielsweise schreiben: „Ich glaube, dass Theorie X richtig ist.“ Das ist zunächst eine Meinungsäußerung.
Die Moderations-KI soll nicht entscheiden: „Diese Meinung ist falsch → löschen.“
Stattdessen könnte ein späteres Informationssystem anbieten: „Quellen und Gegenpositionen anzeigen.“

## 19. Moderation ≠ Fact Checking

Wir bekommen daher zwei getrennte Systeme:

```text
CONTENT MODERATION
        │
        └── Verstößt der Inhalt gegen Regeln?

INFORMATION ASSISTANCE
        │
        └── Welche Informationen und Quellen gibt es?
```

## 20. Schutz vor kultureller Fehlinterpretation

Ein Ausdruck kann in Deutschland beleidigend sein, in einem anderen Kulturkreis aber völlig normal. Die KI benötigt deshalb perspektivisch **Cultural Context Models**.

Sie darf nicht automatisch davon ausgehen: Deutsche Kommunikationsnorm = globale Kommunikationsnorm.
Unser globaler kleinster gemeinsamer Nenner bleibt: Menschenwürde + Höflichkeit + keine gezielte Schädigung.

## 21. Ironie, Satire und Humor

Eine der schwierigsten Aufgaben. Wir benötigen deshalb Kontext, Emojis, Gesprächsverlauf, bekannte Ironiestrukturen, sprachliche Besonderheiten, Community-Kontext – und trotzdem: **Unsicherheit zulassen.**

## 22. Keine Bestrafung aufgrund eines einzelnen KI-Scores

Ich würde ausdrücklich festlegen: Kein schwerer Moderationseingriff darf ausschließlich auf einem einzelnen automatisierten Klassifikationsergebnis beruhen.

```text
Text Analysis
+ Context Analysis
+ User Behaviour Signals
+ Language Analysis
+ Media Analysis
+ Rule Engine
        ↓
Risk Assessment
```

## 23. User Behaviour Signals

Es geht um technische Missbrauchssignale (z. B. 10.000 identische Nachrichten innerhalb einer Minute = Spam-Signal). Dagegen ist „Dieser Nutzer hat bereits zwei Verwarnungen“ eine andere Kategorie und sollte datenschutzrechtlich streng kontrolliert werden.

## 24. Kein Social Credit System

Nexus Gaja führt kein allgemeines soziales Bewertungssystem seiner Nutzer. Moderationsinformationen dienen der Sicherheit und dem Regelvollzug und nicht der Bewertung des „Wertes“ eines Menschen. Die Plattform soll Vielfalt fördern.

## 25. Moderations-KI muss auditierbar sein

Wir sollten sämtliche relevanten automatisierten Entscheidungen protokollieren (Event-ID, Content-ID, Rule-ID, Model-ID, Model-Version, Input-Language, Confidence, Recommendation, Action, Human-Review, Final-Decision, Timestamp).

## 26. False Positives und False Negatives

Wir müssen beide Fehlerarten (False Positive & False Negative) messen und überwachen. Insbesondere bei politischen, religiösen und kulturellen Diskussionen ist ein hoher False-Positive-Anteil gefährlich.

## 27. Qualitätskennzahlen

Wir sollten später ein Moderation Dashboard entwickeln: Precision, Recall, False Positive Rate, False Negative Rate, Language Accuracy, Translation Impact, Appeal Reversal Rate, Human Agreement.
Eine hohe Appeal Reversal Rate deutet auf ein grundlegendes Problem hin.

## 28. Sprachgerechtigkeit

Die Moderationsqualität muss über Sprachen hinweg vergleichbar sein (Multilingual Moderation Benchmark).

## 29. Translation Bias

Ein besonderer Test:
Wenn die Moderation des Originals und die Moderation der Übersetzung unterschiedliche Ergebnisse liefern (Translation Conflict), muss dieser Fall erneut geprüft werden.

## 30. Moderations-KI und Privatsphäre

**Purpose Limitation**: Die Verarbeitung muss einem definierten Zweck dienen. Die KI darf nicht automatisch alle Daten analysieren, nur weil es technisch möglich wäre.

## 31. Architekturvorschlag

```text
                CONTENT INGESTION
                       │
                       ▼
              LANGUAGE DETECTION
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
   TEXT/MEDIA ANALYSIS       TRANSLATION ENGINE
          │                         │
          └────────────┬────────────┘
                       ▼
                 CONTEXT ENGINE
                       │
                       ▼
                POLICY ENGINE
                       │
                       ▼
                RISK ENGINE
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       GREEN        YELLOW       RED
          │            │            │
       Publish      Review       Immediate
                                  Protection
                                     │
                                     ▼
                              HUMAN MODERATION
                                     │
                                     ▼
                                FINAL ACTION
```

## 32. Policy Engine

Die eigentlichen Regeln werden nicht fest in den KI-Modellen codiert. Die KI liefert Erkenntnisse. Die Policy Engine entscheidet anhand der aktuell gültigen Nexus-Gaja-Regeln. Das macht das System wesentlich wartbarer.

## 33. Modellwechsel ohne Regeländerung

Wir können später das KI-Modell austauschen (Model A → Model B → Model C), ohne unser gesamtes Regelwerk neu zu programmieren.

## 34. Der Mensch bleibt letzte Instanz

- **NG-AI-MOD-001**: Die künstliche Intelligenz von Nexus Gaja unterstützt die Erkennung, Klassifikation und Priorisierung möglicher Regelverstöße. Sie ersetzt bei schwerwiegenden Moderationsentscheidungen nicht die menschliche Prüfung.
- **NG-AI-MOD-002**: Automatisierte Moderationsentscheidungen müssen nachvollziehbar, protokollierbar und – soweit erforderlich – durch eine menschliche Instanz überprüfbar sein.

## 35. Ein weiterer wichtiger Grundsatz: Die KI darf sich irren

Wir bauen kein System mit der Annahme: „KI erkennt den Regelverstoß.“, sondern: „KI berechnet eine begründete Wahrscheinlichkeit.“ Das führt zu einer wesentlich professionelleren Architektur.

## 36. Vorläufiges Ergebnis von WP 1.8.4

Damit haben wir jetzt ein vierstufiges Moderationssystem:

1. **Ebene 1 – KI-Erkennung**: Was könnte passiert sein?
2. **Ebene 2 – Kontext- und Risikoanalyse**: Wie wahrscheinlich und wie schwerwiegend ist es?
3. **Ebene 3 – Policy Engine**: Welche Nexus-Gaja-Regel ist betroffen und welche Maßnahme wäre angemessen?
4. **Ebene 4 – Human Governance**: Ist die vorgeschlagene Entscheidung tatsächlich gerechtfertigt?

Das System kann später sehr stark automatisiert werden, ohne dass wir von Anfang an eine gefährliche „KI als Richter“-Architektur bauen.
