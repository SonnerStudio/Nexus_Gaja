# WP 1.3 – Kommunikationsmodell (Nexus Gaja)

Dieses Dokument hält die konzeptionellen Grundlagen des Kommunikationsmodells für Nexus Gaja fest.

## Grundprinzipien

### 1. Die Unveränderlichkeit des Originals
**Das Original ist unveränderlich.** Die KI erzeugt lediglich eine zielsprachliche Darstellung des Originals für den jeweiligen Empfänger, basierend auf dessen bevorzugter Sprache. Übersetzungen überschreiben niemals die ursprüngliche Nachricht.

### 2. Die drei Ebenen der Kommunikation
1. **Ebene 1 – Original:** Was hat der Mensch tatsächlich geschrieben oder gesagt? (inkl. Originalsprache, Inhalt)
2. **Ebene 2 – Semantische Interpretation:** Was bedeutet die Äußerung nach Einschätzung des Systems? (z. B. Erkennung von Ironie, regionalen Ausdrücken, Metaphern oder unübersetzbaren Begriffen)
3. **Ebene 3 – Zielsprachliche Darstellung:** Wie wird diese Bedeutung für den Empfänger natürlich in der Zielsprache ausgedrückt?

### 3. Kontextabhängige Übersetzung
Jede Nachricht besitzt einen Kontext, der bei der semantischen Interpretation und Übersetzung berücksichtigt wird:
`Message` → `Previous Messages` → `Thread Context` → `Community Context` → `Language / Region` → `User Preferences` → `Translation`
(Hierbei müssen stets Datenschutz und Datenminimierung gewahrt bleiben.)

---

## Definitionen des Kommunikationsprotokolls

### 1. Was ist eine Nachricht? (Status: Definiert)
Eine Nachricht (*Message*) ist in Nexus Gaja das rein inhaltliche Basis-Objekt. Es ist ein digitales Kommunikationsobjekt, das aus einem oder mehreren Inhaltsmedien bestehen kann. Dazu gehören:
- Text
- Bild
- Audio
- Video
- Kombinationen dieser Medien

### 2. Was ist ein Beitrag? (Status: Definiert)
Ein Beitrag (*Post*) ist ein Struktur-Objekt, das eine Nachricht (die Inhalte aus Punkt 1) als Kern enthält **plus** die dazugehörigen sozialen und interaktiven Elemente. Dazu gehören:
- Kommentare
- "Gefällt mir" (Likes)
- "Gefällt mir nicht" (Dislikes)
- Weitere soziale Interaktionen

### 3. Was ist eine Unterhaltung? (Status: Definiert)
Eine Unterhaltung (*Conversation*) ist der direkte, fortlaufende Kommunikationskanal zwischen Nutzern und umfasst verschiedene (auch Echtzeit-) Modalitäten. Dazu gehören:
- Videotelefonie
- Sprachkommunikation (Audio)
- Chat (Textbasierter Direktaustausch)

### 4. Wann wird übersetzt? (Status: Definiert)
Die Übersetzung erfolgt **On-Demand (beim Aufruf)**:
- Übersetzt wird erst dann, wenn ein Nutzer den Inhalt abfragt (basierend auf der voreingestellten Sprache des Empfängers).
- **Caching / Speicherung**: Eine einmal geleistete Übersetzung für eine spezifische Sprache wird dauerhaft gespeichert. Nachfolgende Abfragen in derselben Sprache rufen die bestehende Übersetzung ab, was Ressourcen schont und die Geschwindigkeit erhöht.

### 5. Wie wird mit Übersetzungsfehlern umgegangen? (Status: Offen)
Kann der Nutzer eine bessere Übersetzung anfordern?

### 6. Wie werden mehrere Sprachen behandelt? (Status: Offen)
Beispielsweise, wenn ein Beitrag Deutsch, Englisch und einen Dialekt enthält.
