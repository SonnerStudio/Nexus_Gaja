# WP 1.12 – MVP-Domänenmodell und fachliches Gesamtmodell

**Phase:** 1
**Status:** Draft 1.0
**Zweck:** Definition der zentralen fachlichen Objekte, Beziehungen, Zustände und Geschäftsregeln des Nexus-Gaja-MVP.

## 1. Ziel des Domänenmodells

Das Domänenmodell beantwortet eine zentrale Frage:
**Welche Dinge existieren in Nexus Gaja und wie stehen sie miteinander in Beziehung?**

Dabei unterscheiden wir bewusst zwischen:
- einer Person
- einer Identität
- einem Benutzerkonto
- einer Organisation
- einer verifizierten Identität
- einer Community
- einer Nachricht
- einem Beitrag
- einer Unterhaltung
- einer Übersetzung
- einer Moderationsentscheidung
- einer Meldung
- einem Einspruch
- einer Spende
- einem Förderfonds
- und den daraus entstehenden Berechtigungen.

Das ist wichtig, weil diese Dinge nicht dasselbe sind.

## 2. Oberstes Domänenmodell

Das Gesamtmodell lässt sich zunächst so darstellen:

```text
                         NEXUS GAJA
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
        IDENTITÄT        KOMMUNIKATION       FINANZEN
             │                │                │
       ┌─────┴─────┐      ┌───┴────┐       ┌───┴────┐
       ▼           ▼      ▼        ▼       ▼        ▼
    Person      Organisation      Content  Donation Fund
       │           │              │
       ▼           ▼              ▼
    Account     Organization    Message
       │                           │
       ▼                           ├── Post
 Verification                      ├── Comment
       │                           ├── Reaction
       ▼                           └── Media
 Permissions
```

Quer darüber liegen: Language, Translation, Moderation, Reporting, Appeals, Audit, Notification, Security.

## 3. Grundlegende Entitäten

Für den MVP definieren wir zunächst folgende Kernentitäten:

- **Identität:** Person, Organisation, Identity Record, Verification, Account, User Account, Organization Account, School Account, Student Account
- **Kommunikation:** Message, Post, Comment, Reaction, Conversation, Community, Membership
- **Sprache:** Language Profile, Translation, Translation Request
- **Sicherheit:** Role, Permission, Policy, Moderation Case, Report, Appeal, Audit Event
- **Finanzen:** Donation, Fund, Allocation, Benefit, Financial Transaction

## 4. Person und 5. Benutzerkonto

Eine **Person** repräsentiert einen real existierenden Menschen (`person_id`, `legal_name`, `date_of_birth`, `nationality`, `identity_status`).
Die Person ist **nicht identisch** mit dem Benutzerkonto.

Das **Benutzerkonto** (`UserAccount`) repräsentiert die technische Teilnahme an Nexus Gaja (`account_id`, `person_id`, `username`, `account_status`, `created_at`, `preferred_language`).
Eine Person kann grundsätzlich höchstens das ihr erlaubte Kontomodell besitzen; Mehrfachkonten müssen durch die Identitätsregeln kontrolliert werden.

## 6. Identitätsverifikation und 7. Verifikationsdaten

Die Verifikation ist ein eigener fachlicher Prozess (`Person` ──► `Verification Request` ──► `Identity Verification` ──► `Verification Result` ──► `Identity Status`).
Zustände: `UNVERIFIED`, `PENDING`, `VERIFIED`, `REJECTED`, `EXPIRED`, `SUSPENDED`.

Wir unterscheiden zwischen *Identitätsnachweis* und *Verifikationsergebnis*. Der externe Dienst kann bestätigen (`identity_verified = true`, `age_verified = true`), ohne dass Nexus Gaja das Ausweisdokument dauerhaft speichert (Datensparsamkeit).

## 8. Organisation und 9. Beziehung Person ↔ Organisation

Eine **Organisation** ist eine eigenständige juristische oder institutionelle Einheit (Unternehmen, Verein, Schule, etc.).
Personen können Funktionen innerhalb von Organisationen besitzen (z. B. `Person A` ──► `administrator` ──► `School X`).

## 10. Schule, 11. Schulklasse und 12. Schülerkonto

Eine Schule ist fachlich eine spezielle Organisation (`type = SCHOOL`).
Eine Klasse erhält einen eigenen Kommunikationsraum (`School` ──► `Class` ──► `Teacher` / `Students`).
Das **Schülerkonto** (`Student Account`) ist an die schulische Verifikation gebunden. Es ist kein gewöhnlicher 18+-Account.

## 13. Account Status und 14. Lebenszyklus

Zustände: `PENDING`, `ACTIVE`, `LIMITED`, `SUSPENDED`, `LOCKED`, `DEACTIVATED`, `DELETED`.
Lebenszyklus: `Registration` ──► `Verification` ──► `Activation` ──► `Active`.

## 15. Sprache (Language Profile)

Die wichtigste Eigenschaft: Die bevorzugte Sprache ist die Standarddarstellung für den Benutzer.
Beinhaltet `preferred_language`, `additional_languages`, `source_language_preferences`.

## 16. Nachricht, 17. Post, 18. Kommentar, 19. Reaktionen

- **Message:** Kommunikative Einheit (Text, Image, Audio, Video, Attachments).
- **Post:** Eine veröffentlichte Nachricht, die soziale Interaktion ermöglicht (Comments, Reactions).
- **Comment:** Eine Nachricht, die sich auf einen Beitrag bezieht.
- **Reaction:** `LIKE`, `DISLIKE`, `OTHER`.

## 20. Unterhaltung (Conversation) und 21. Community

- **Conversation:** Chat-Kontext (1:1, Gruppe, Community).
- **Community:** Dauerhafter Kommunikationsraum (`Members`, `Roles`, `Posts`, `Conversations`, `Rules`, `Moderation`).

## 22. Community-Mitgliedschaft und 23. Community-Rollen

`User` ──► `Membership` ──► `Community`. Rollen: `OWNER`, `ADMIN`, `MODERATOR`, `MEMBER`, `GUEST`. (Nicht identisch mit globalen Rollen).

## 24. Globale Rollen, 25. Berechtigung, 26. Policy

Globale Rollen (z. B. `USER`, `VERIFIED_USER`, `MODERATOR`, `ADMIN`).
Rolle und Berechtigung werden getrennt (`Role` ──► `Permission`).
Eine **Policy** bestimmt, unter welchen Bedingungen eine Berechtigung gilt (`Permission` + `Context` ──► `Policy Decision`).

## 27. Translation, 28. Original, 29. Request, 30. Qualität

Eine Übersetzung ist eine eigenständige Entität. **Übersetzung verändert niemals das Original.**
Nutzer können eine bessere Übersetzung anfordern (`Translation Request`).
Qualitätsstatus: `AUTOMATIC`, `REVIEWED`, `USER_SUGGESTED`, `HUMAN_REVIEWED`, `SUPERSEDED`.

## 31. Mixed-Language Message

Eine Nachricht kann mehrere Ursprungssprachen besitzen. Der Übersetzungsdienst erzeugt daraus eine semantisch zusammenhängende Zielsprachversion.

## 32. Moderation Case, 33. Report, 34. Moderation, 35. Appeal

- **Report:** Ein Nutzer meldet einen Inhalt.
- **Moderation Case:** Ein eigener Prüfvorgang.
- **Appeal:** Einspruch gegen eine Entscheidung als eigene Entität.

## 36. Moderationslebenszyklus

`Content` ──► `Detection` ──► `Report / AI Detection` ──► `Moderation Case` ──► `Review` ──► `Decision` ──► `Notification` ──► `Appeal` ──► `Final Decision`.

## 37. Audit Event

Dokumentiert sicherheits- oder verwaltungsrelevante Aktionen (`actor`, `action`, `target`, `timestamp`, `correlation_id`).

## 38. Spende, 39. Förderfonds, 40. Allocation, 41. Berechtigung, 42. Tombola

- **Donation:** Technische Zahlungsabwicklung bleibt getrennt von der internen Finanzbuchungslogik.
- **Fund:** Förderfonds (`GENERAL`, `LANGUAGE_SUPPORT`, `SOLIDARITY`, etc.).
- **Allocation:** Bestimmt, wofür Mittel verwendet werden (z. B. für Free Access).
- **Eligibility:** Ein Benutzer erhält Förderungen nach Kriterien (`User` ──► `Eligibility` ──► `Program` ──► `Benefit`).
- **Tombola:** Zufällige Zuteilung von Mitteln (Kryptografisch sichere Auswahl).

## 43. Notification

Keine Nachricht im sozialen Sinn, sondern Systemhinweise (z. B. „Dein Einspruch wurde bearbeitet.“).

## 44. Fachliches Gesamtbild

```text
PERSON
  │
  ├──────────────► USER ACCOUNT
  │                    │
  │                    ├── Language Profile
  │                    ├── Roles
  │                    ├── Memberships
  │                    └── Permissions
  │
  └──────────────► VERIFICATION
                       │
                       ▼
                  Verified Status


USER ACCOUNT
      │
      ├──► MESSAGE
      │      ├── Post
      │      ├── Comment
      │      ├── Media
      │      └── Translation
      │
      ├──► CONVERSATION
      │
      ├──► COMMUNITY
      │
      ├──► REPORT
      │      └── Moderation Case
      │             └── Appeal
      │
      ├──► DONATION
      │
      └──► NOTIFICATION


ORGANIZATION
      │
      ├── School
      │     └── Class
      │          └── Student Accounts
      │
      └── Organization Members
```

## 46. - 49. Besonders wichtige Trennungen

- **Person ≠ Account ≠ Identity Verification:** Verhindert das "Username = Mensch"-Problem.
- **Message ≠ Translation:** Erlaubt Übersetzungsverbesserungen ohne das Original zu ändern.
- **Report ≠ Moderation Decision:** Ein Report ist nur ein Hinweis, erst die Prüfung erzeugt die Entscheidung.
- **Donation ≠ Fund Balance:** Einzelzahlung ist nicht gleich verfügbarer Fondsbestand. Wichtig für Transparenz.

## 50. Domänenstruktur und 51. Architekturentscheidung (ADR-025)

**ADR-025 – Domain-Driven MVP Architecture:**
Nexus Gaja wird fachlich in klar getrennte Domänen strukturiert (Identity, Communication, Finance, etc.). Der MVP implementiert diese Domänen zunächst möglichst als **modularen Monolithen** mit klaren Schnittstellen. Eine spätere Extraktion in eigenständige Services bleibt möglich.
Das vermeidet eine verfrühte "Microservices-Architekturhölle".

## 52. MVP-Domänenmodell – Version 1.0 (Entitäten)
Definierte Fach-Objekte in Identität, Accounts, Kommunikation, Sprache, Governance, Finanzen und System.

## 53. Ergebnis von WP 1.12

Die fachliche Landkarte von Nexus Gaja steht:
`VISION` ──► `ZIELE` ──► `NUTZER` ──► `FUNKTIONEN` ──► `REGELN` ──► `DATENSCHUTZ` ──► `GESCHÄFTSMODELL` ──► `TECHNISCHE ARCHITEKTUR` ──► `NFR` ──► `DOMÄNENMODELL` ──► `DATENMODELL / API-MODELL` ──► `IMPLEMENTIERUNG`.

Wir haben ein zusammenhängendes Systemkonzept geschaffen! Als nächster Schritt folgt **WP 1.12.1 – Fachliches Entity-Relationship-Modell (ER-Modell) und Kardinalitäten**.
