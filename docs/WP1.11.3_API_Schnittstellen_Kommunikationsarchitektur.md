# WP 1.11.3 – API-, Schnittstellen- und Kommunikationsarchitektur

**Phase:** 1
**Status:** Draft 1.0
**Vorgänger:** WP 1.11.2 – Datenarchitektur und Datenflüsse
**Ziel:** Definition der Kommunikationswege zwischen Nexus-Gaja-Komponenten, Clients und externen Diensten.

## 1. Grundprinzip

Nexus Gaja soll nicht aus einer unkontrollierten Ansammlung direkter Datenbankzugriffe bestehen. Stattdessen gilt:
**Komponenten kommunizieren über definierte Schnittstellen und niemals über gegenseitige direkte Datenbankzugriffe.**

*FALSCH:*
`Message Service ─────► (direkte Abfrage) ─────► Identity Database`

*RICHTIG:*
```text
Message Service
      │
      ▼
Identity API
      │
      ▼
Identity Service
      │
      ▼
Identity Data
```
Damit bleiben unsere Systemgrenzen tatsächlich durchsetzbar.

## 2. Vier Kommunikationsarten

Wir definieren zunächst vier grundsätzliche Kommunikationsformen:

| Kommunikationsart | Zweck |
| :--- | :--- |
| **Synchronous API** | unmittelbare Antwort erforderlich |
| **Asynchronous API/Event** | zeitversetzte Verarbeitung |
| **Streaming** | kontinuierliche Datenströme |
| **Batch** | große Mengen / periodische Verarbeitung |

Für Nexus Gaja werden insbesondere **synchrone APIs** + **asynchrone Events** die beiden wichtigsten Mechanismen sein.

## 3. Synchrone Kommunikation

*Beispiel:* Ein Client fragt: „Welche Sprache ist für mich eingestellt?“

```text
Client
  │
  ▼
API Gateway
  │
  ▼
Account API
  │
  ▼
Response
```
Der Client wartet auf das Ergebnis. 
**Geeignet für:** Login, Profil, Einstellungen, Nachrichtenabruf, Berechtigungsprüfung, Übersetzungsanforderungen.

## 4. Asynchrone Kommunikation

Andere Vorgänge müssen nicht sofort beendet werden. Der Message Service muss nicht darauf warten, dass sämtliche Folgeprozesse abgeschlossen sind.

```text
Message Created
      │
      ▼
  Event Bus
 ┌────┼──────┬─────────┐
 ▼    ▼      ▼         ▼
AI   Media  Audit   Notification
```

## 5. Event Bus

Wir definieren deshalb den **Nexus Gaja Event Bus** als zentrale logische Kommunikationsschicht. Er verbindet fachliche Komponenten über Ereignisse.

**Beispiele für Events:**
- `Identity.Verification.Completed`
- `Message.Created`
- `Message.Edited`
- `Translation.Completed`
- `Moderation.ContentFlagged`
- `Case.Created`
- `Appeal.Submitted`
- `Donation.Received`
- `Grant.Allocated`

## 6. Event vs. Command

Eine wichtige Unterscheidung:
- **Event:** „Etwas ist geschehen.“ (Beispiel: `Message.Created`)
- **Command:** „Führe etwas aus.“ (Beispiel: `TranslateMessage`)

Wir sollten diese beiden Konzepte nicht vermischen.

## 7. Beispiel Message Flow

```text
Message Service
      │
      ├── Event: Message.Created
      │
      ▼
  Event Bus
      │
      ├──► Translation
      ├──► Moderation
      ├──► Notification
      └──► Audit
```

## 8. API Gateway

Alle externen Clientzugriffe (Web, Mobile, Desktop) laufen grundsätzlich über ein **Nexus Gaja API Gateway**.
Der Client kennt dadurch nicht die internen Netzwerkadressen der Services. Das Gateway übernimmt:
- Authentication
- Authorization
- Rate Limiting
- Request Validation
- Routing
- Observability

## 9. Interne APIs

Intern können Services beispielsweise so kommunizieren:
- `Message Service` ──► `Translation API`
- `Moderation Service` ──► `Media Analysis API`

Diese APIs werden **nicht öffentlich** exponiert.

## 10. External Integration Gateway Layer

Externe Schnittstellen (Identitätsverifikation, Zahlungsdienstleister, E-Mail, SMS, externe KI, Übersetzungsanbieter, Storage Provider) werden besonders streng behandelt.
Dafür definieren wir einen **External Integration Gateway Layer**.

## 11. External Integration Gateway

Das verhindert, dass 15 verschiedene interne Services jeweils eigene Integrationen zu externen Anbietern implementieren.

```text
       Nexus Gaja
           │
           ▼
  Integration Gateway
           │
 ┌───┬─────┼─────┬──────────┐
 ▼   ▼     ▼     ▼          ▼
ID  Pay   AI  Messaging    etc.
```

## 12. Provider-Abstraktion

Besonders wichtig für KI und Übersetzung. Dadurch können Anbieter jederzeit ausgetauscht werden.

*Nicht:* `Translation Service` ──► `Provider X`
*Sondern:*
```text
Translation Service
         │
         ▼
Translation Provider Interface
         │
    ┌────┼────┐
    ▼    ▼    ▼
    A    B    C
```

## 13. AI Provider Abstraction

Dasselbe Prinzip gilt für KI. Das passt hervorragend zu Nexus Gajas langfristiger Strategie:

```text
       AI Gateway
           │
           ▼
Model Provider Interface
           │
  ┌────────┼──────────┐
  ▼        ▼          ▼
Local   Cloud A    Cloud B
```

## 14. Datenschutz durch Provider-Abstraktion

Die Abstraktion ermöglicht zusätzlich: Der **Datenschutz** entscheidet mit darüber, welcher Provider einen Auftrag erhält.
Ein besonders sensibler Inhalt könnte bevorzugt lokal verarbeitet werden:

```text
     Private Message
           │
           ▼
     Privacy Policy
           │
      ┌────┴─────┐
      ▼          ▼
    Local      Cloud
    Model      Model
```

## 15. API-Protokoll

Für die normalen APIs wird als primäre externe API **REST/HTTPS** festgelegt.
*Vorteile:* Weit verbreitet, einfach testbar, gute Browser-/Mobile-Unterstützung, klare Ressourcenmodelle, gute Tool-Unterstützung.

## 16. Internes RPC

Für hochfrequente interne Kommunikation kann später zusätzlich ein RPC-System eingesetzt werden (`Service A` ──► `Internal RPC` ──► `Service B`). Hier wird die konkrete Technologie noch nicht festgelegt.

## 17. WebSocket / Realtime

Für Chat und Echtzeitereignisse benötigen wir eine Realtime-Schnittstelle.
Geeignet für: Neue Nachrichten, Schreibstatus, Online-Status, Benachrichtigungen, Moderationsstatus.

```text
     Client
       ⇅
Realtime Gateway
       ⇅
   Messaging
```

## 18. Event Streaming vs. WebSocket

Der Event Bus ist nicht dasselbe wie WebSocket.
- **WebSocket:** Client-Kommunikation
- **Event Bus:** interne Systemkommunikation
Diese Trennung sollten wir strikt beibehalten.

## 19. API-Versionierung

Jede öffentliche API erhält eine Version (z. B. `/api/v1/...`, später `/api/v2/...`). Breaking Changes werden nicht einfach in eine bestehende Version eingebaut.

## 20. API Contract First

Ein zentraler Entwicklungsgrundsatz: **API-Verträge werden definiert, bevor die Implementierung beginnt.**
`Specification` ──► `Contract` ──► `Tests` ──► `Implementation`
(Für REST bietet sich beispielsweise OpenAPI an).

## 21. Request-ID und 22. Correlation-ID

- **`request_id`:** Jede API-Anfrage erhält eine eindeutige ID (um Fehler nachzuvollziehen).
- **`correlation_id`:** Für einen kompletten Geschäftsprozess (z. B. Message ──► Translation ──► Moderation ──► Notification). Alle Ereignisse dieser Kette gehören zur selben `correlation_id`.

## 23. Idempotency

Bei kritischen Operationen müssen Wiederholungen sicher sein (besonders Zahlungen, Spenden, Verifikationen).
*Beispiel:* `POST Donation` mit `Idempotency-Key: XYZ`. Wird dieselbe Anfrage zweimal übertragen, darf nicht zweimal gespendet werden.

## 24. Event-ID und 25. Event-Schema

Jedes Event erhält zusätzlich eine **`event_id`** (Duplikaterkennung).
Ein logisches Event-Schema könnte so aussehen:
```json
{
  "event_id": "...",
  "event_type": "Message.Created",
  "event_version": 1,
  "occurred_at": "...",
  "producer": "message-service",
  "correlation_id": "...",
  "data": {}
}
```

## 26. Schema-Versionierung

Events werden versioniert (`Message.Created v1`, `Message.Created v2`). Alte Konsumenten dürfen nicht durch eine neue Version zerstört werden.

## 27. Fehlerbehandlung und 28. Eigene Fehlercodes

APIs erhalten standardisierte HTTP-Fehler (400, 401, 403, 404, 409, 422, 429, 500, 503).
Zusätzlich besitzt Nexus Gaja eigene, maschinenlesbare Fehlercodes.
*Beispiel:*
```json
{
  "error": {
    "code": "NG-IDENTITY-VERIFICATION-REQUIRED",
    "message": "...",
    "request_id": "..."
  }
}
```

## 29. Rate Limiting

Das API Gateway begrenzt Requests (pro IP, pro Account, pro API-Key, für sensible Aktionen, Missbrauchsmuster).
Ein Nutzer darf nicht allein wegen gemeinsamer Infrastruktur mit anderen Nutzern unverhältnismäßig blockiert werden.

## 30. Authentifizierung und 31. Service-to-Service Auth

Die Authentifizierung wird zentralisiert. Die einzelnen Services validieren die erforderlichen Claims.
Auch interne Services dürfen einander nicht blind vertrauen (Service Identity für interne Kommunikation).

## 32. Zero-Trust-Prinzip

Nexus Gaja wird nach einem Zero-Trust-Modell entworfen: „Internal network“ bedeutet nicht automatisch „trusted“. Jede sensible Kommunikation wird authentifiziert und autorisiert.

## 33. Secrets

API-Schlüssel und Credentials gehören **nicht** in den Source Code, Git, Dockerfiles oder Konfigurationsdateien im Repository. Sie werden über einen Secret-Management-Mechanismus bereitgestellt.

## 34. Verschlüsselung

Externe Kommunikation erfolgt über HTTPS / TLS. Interne sensible Kommunikation wird ebenfalls verschlüsselt.

## 35. Asynchrone Zuverlässigkeit und 36. Keine verlorenen Nachrichten

Der Event Bus benötigt: Retry, Dead Letter Queue (DLQ), Consumer Acknowledgement, Duplicate Detection.
Für kritische Events gilt: **At-least-once delivery + idempotente Consumer** ist ein sehr pragmatisches Architekturmodell (besser als der Versuch von "exactly once").

## 37. Outbox Pattern und 38. Outbox Beispiel

Für besonders wichtige Ereignisse verwenden wir das Outbox Pattern, um das klassische Problem "Datenbankänderung erfolgreich, Event aber verloren" zu verhindern.
```text
BEGIN
   │
   ├── Save Message
   └── Save Message.Created to Outbox
COMMIT
   │
   ▼
Outbox Publisher ──► Event Bus
```

## 39. Finanztransaktionen und 40. Financial Reconciliation

Bei Finanzen gelten noch strengere Regeln. Eine Zahlung darf nicht allein aufgrund eines verlorenen Netzwerkpakets erneut ausgelöst werden.
Periodisch werden Abgleiche gefahren (`Payment Provider` ──► `Nexus Gaja Ledger` ──► `Reconciliation`). Abweichungen erzeugen einen Prüfungsfall.

## 41. API-Sicherheitsmodell

Jede Anfrage durchläuft logisch:
`Request` ──► `TLS` ──► `Authentication` ──► `Schema Validation` ──► `Authorization` ──► `Policy` ──► `Rate Limit` ──► `Business Logic`

## 42. Kein „Admin = alles“

Privileged Access is Explicit. Auch Administratoren erhalten nicht automatisch vollständigen Zugriff auf alle Daten, sondern nur die Berechtigungen, die ihre Aufgabe verlangt.

## 43. Break-Glass Access

Für außergewöhnliche Sicherheits- oder Rechtsfälle können wir später einen kontrollierten Break-Glass-Mechanismus vorsehen (Emergency Access ──► Strong Authentication ──► Explicit Reason ──► Temporary Permission ──► Complete Audit).

## 44. API für Schulen und 45. juristische Personen

Wir brauchen perspektivisch eine **Organization API**, über die z.B. eine Schule die Zugehörigkeit bestätigen kann, ohne Zugriff auf die private Kommunikation der Schüler zu erhalten. Dies gilt für Unternehmen, Vereine, NGOs und Bildungseinrichtungen.

## 46. Öffentliche API

Eine frei zugängliche Entwickler-API ist nicht Bestandteil des MVP. Sicherheit und Missbrauchsschutz sind zunächst wichtiger als maximale Offenheit.

## 47. API Gateway vs. Service Mesh

Wir unterscheiden zwischen API Gateway (externe Clients) und Service Mesh (interne Services). Ob wir später ein Service Mesh benötigen, entscheidet die Skalierung.

## 48. MVP-Kommunikationsarchitektur

Für den MVP beginnen wir bewusst einfach. Noch kein unnötig komplexes Microservice-Netz.

```text
                 CLIENTS
                    │
                    ▼
              API GATEWAY
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
    IDENTITY    COMMUNICATION  SAFETY
        │           │           │
        └───────────┼───────────┘
                    ▼
                AI GATEWAY
                    │
                    ▼
              TRANSLATION
                    │
                    ▼
                DATA LAYER

             + EVENT BUS
```

## 49. Skalierbare Zielarchitektur

Später können Komponenten (z. B. Translation unabhängig von Messaging) völlig unabhängig skaliert werden.

## 50. Kommunikationsarchitektur – Grundsätze (NG-API)

- **NG-API-001:** Externe Zugriffe erfolgen über definierte APIs.
- **NG-API-002:** Direkte Datenbankzugriffe zwischen fachlichen Komponenten sind verboten.
- **NG-API-003:** Jede sensible interne Kommunikation wird authentifiziert.
- **NG-API-004:** Events und Commands werden getrennt modelliert.
- **NG-API-005:** Kritische Operationen müssen idempotent sein.
- **NG-API-006:** Öffentliche APIs sind versioniert.
- **NG-API-007:** API-Verträge werden vor der Implementierung spezifiziert.
- **NG-API-008:** Externe Provider werden durch Abstraktionsschnittstellen gekapselt.
- **NG-API-009:** Jede relevante Transaktion erhält Request-/Correlation-/Event-Referenzen.
- **NG-API-010:** Sicherheits- und Datenschutzgrenzen dürfen nicht durch technische Bequemlichkeit umgangen werden.

## 51. Vorläufige API-Landkarte

- `/api/v1/auth`, `/api/v1/accounts`, `/api/v1/identity`, `/api/v1/verification`, `/api/v1/profiles`
- `/api/v1/messages`, `/api/v1/conversations`, `/api/v1/posts`, `/api/v1/comments`, `/api/v1/reactions`
- `/api/v1/communities`, `/api/v1/memberships`
- `/api/v1/translation`, `/api/v1/media`
- `/api/v1/reports`, `/api/v1/cases`, `/api/v1/appeals`
- `/api/v1/subscriptions`, `/api/v1/donations`, `/api/v1/funds`, `/api/v1/grants`
- `/api/v1/notifications`

## 52. Hybrides Kommunikationsmodell

Nexus Gaja verwendet ein hybrides Kommunikationsmodell:
- **Synchron:** REST/HTTPS (ggf. internes RPC)
- **Asynchron:** Event Bus
- **Realtime:** WebSocket (bzw. vergleichbarer Kanal)
- **Dateien:** Object Storage über kontrollierte Media APIs

## 53. Was wir ausdrücklich nicht tun

Kein Spaghetti-Code und durchgereichte Abhängigkeiten bis zur externen API: `Client ──► Service A ──► DB A ──► DB B ──► Service C ──► External API`.

Stattdessen klar gekapselt:
`Client ──► API ──► Service ──► Data`
Und zwischen Services:
`Service ⇅ API / Event ⇅ Service`

## 54. Ergebnis WP 1.11.3

Mit diesem Arbeitspaket steht jetzt die Kommunikationsgrundlage der Nexus-Gaja-Architektur. Damit ist die Architektur inzwischen weit genug konkretisiert, dass wir anschließend beginnen können, sie in technische Infrastruktur und konkrete Entwicklungsbausteine zu übersetzen.
