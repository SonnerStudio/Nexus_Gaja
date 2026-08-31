# WP 1.10.1 – Finanzierungsprinzipien und Einnahmenmodell

## 1. Ausgangslage
Für Nexus Gaja gilt ein ungewöhnlich wichtiger wirtschaftlicher Grundsatz: **Keine klassische Werbung innerhalb der Plattform.** 
Damit unterscheidet sich Nexus Gaja konzeptionell von vielen heutigen sozialen Netzwerken. Das bedeutet aber nicht, dass Nexus Gaja keinen kommerziellen Charakter besitzen darf. Im Gegenteil: Die Plattform muss wirtschaftlich tragfähig sein, damit ihr gesellschaftlicher Zweck dauerhaft bestehen kann. Die wirtschaftliche Tätigkeit ist Mittel zum Zweck.

## 2. Grundsatz NG-FIN-001
Nexus Gaja finanziert seinen Betrieb durch transparente, vom Nutzerinteresse getrennte Einnahmequellen und nicht durch die Vermarktung der Aufmerksamkeit oder personenbezogener Daten seiner Nutzer.

## 3. Keine klassische Werbung
Nicht erlaubt sind insbesondere:
- Bannerwerbung
- Pop-up-Werbung
- automatisch eingespielte Werbevideos
- gesponserte Beiträge im normalen Feed
- personalisierte Werbeprofile
- Verkauf von Nutzerprofilen
- Verkauf personenbezogener Daten
- Werbung, die sich aus privaten Gesprächen ableitet.

Nexus Gaja bleibt ein **Kommunikationsraum statt Werbefläche**.

## 4. Finanzierung ohne Werbung (Die 6 Säulen)
Die Finanzierung ruht auf sechs Säulen:
```text
                 NEXUS GAJA
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
   PREMIUM       ORGANISATION    SPENDEN
       │             │             │
       ├─────────────┼─────────────┤
       ▼             ▼             ▼
   FÖRDERUNG      PARTNERSCHAFT   DIENSTE
```

### Säule 1 – Freie Grundmitgliedschaft
**Nexus Gaja Free** ermöglicht grundlegende Völkerverständigung für alle (Profil, internationale Kommunikation, Beiträge, Communities, Chats, Basis-Übersetzung) ohne Kosten.

### Säule 2 – Premium-Angebote
Freiwillige kostenpflichtige Angebote (**Nexus Gaja Plus**), die z. B. größere Speicherlimits, höhere Medienqualität, erweiterte KI-Kontingente und Organisationsfunktionen bieten. 
**Wichtig (Freemium statt Dark Freemium):** Keine grundlegende Kommunikation darf künstlich unbrauchbar gemacht werden.

### Säule 3 – Organisationen
Spezielle Konten für Schulen, Unis, NGOs, Unternehmen, Kommunen (z. B. **Nexus Gaja Organization**). Schulen können über institutionelle Tarife als Multiplikatoren der Völkerverständigung gefördert werden.

### Säule 4 – Spenden
Der **Nexus Gaja Förderfonds** nimmt allgemeine und zweckgebundene Spenden (z. B. "für internationale Jugendkommunikation") an. Hierfür wird ein **Fund Allocation Ledger** zur nachvollziehbaren Mittelzuordnung eingesetzt.

#### Förderpool & Tombola
Ein Teil der Spenden speist einen Pool für kostenlose/vergünstigte Nutzung.
```text
DONATIONS → PURPOSE FUND → ELIGIBILITY ENGINE → Free access / Discount / Quota
```
Auch die *Tombola* (zufällige, auditierbare Vergabe von Fördermitteln) kann hieraus finanziert werden.

### Säule 5 – Institutionelle Förderung
Stiftungen, Kulturförderprogramme oder staatliche Programme.
**NG-FIN-002:** Finanzielle Förderung kauft keine redaktionelle oder technische Kontrolle (Unabhängigkeit).

### Säule 6 – Kommerzielle Dienstleistungen
B2B-Dienste wie **Translation-as-a-Service** (API), Organisationskommunikation oder internationale Konferenzräume, ohne den normalen Nutzerfeed zu belasten.

## 5. Keine Datenvermarktung & Surveillance Economy
**NG-FIN-003:** Personenbezogene Nutzerdaten sind kein Handelsgut. Kein Verkauf von Listen, Profilen oder Historien. Nexus Gaja profitiert nicht von psychologischer Überwachung (Surveillance Economy).

## 6. Finanzielle Transparenz & Fördermittel-Ledger
**Nexus Gaja Financial Transparency:** Veröffentlichung aggregierter Finanzstrukturen. Zweckgebundene Spenden erhalten eine technische Buchführung (Fund ID → Purpose → Balance → Allocation). Es gibt keine Quersubventionierung von sozialen Zwecken in z. B. Unternehmensmarketing.

## 7. Solidarisches Finanzierungsmodell
Die Preisgestaltung orientiert sich an Kostenorientierung, Fairness und Solidarität. 
**Solidarisches Premium:** Freiwillige Möglichkeit für Premium-Nutzer, einen Teil des Zugangs anderer Nutzer zu finanzieren. Zwangssolidarität oder eine Premium-Klassengesellschaft (weniger Respekt/Moderation für Free-Nutzer) ist ausgeschlossen.

## 8. Wirtschaftliche KPI statt Engagement-Ökonomie
Keine Abhängigkeit davon, dass Nutzer "möglichst lange online bleiben" (keine Ragebaits, Endlos-Feeds). 
Stattdessen nutzen wir Kennzahlen wie:
- **Global Communication Index (GCI):** Erfolgreiche Kommunikationsbeziehungen zwischen Menschen unterschiedlicher Sprach-/Kulturregionen.
- **Platform Sustainability Ratio (PSR):** Wiederkehrende Einnahmen / wiederkehrende Betriebskosten (Ziel ≥ 1).

## 9. Was wir ausdrücklich nicht wollen (Negativliste)
Nexus Gaja finanziert sich **nicht** durch:
❌ Verkauf personenbezogener Daten
❌ personalisierte klassische Werbung
❌ Überwachung des Nutzerverhaltens zum Werbezweck
❌ Verkauf privater Kommunikationsdaten
❌ versteckte KI-Datennutzung
❌ manipulative Premium-Sperren
❌ künstliche Reichweitenbeschränkung zur Monetarisierung
❌ bezahlte politische Einflussnahme
❌ Kauf privilegierter Moderationsentscheidungen.

## 10. Vorläufige Architektur der Finanzen
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

## Zusammenfassung der Finanzierungsgrundsätze (NG-FIN)
- **NG-FIN-001:** Keine Finanzierung durch klassische Werbung.
- **NG-FIN-002:** Keine inhaltliche/technische Kontrolle durch finanzielle Förderung.
- **NG-FIN-003:** Personenbezogene Daten sind kein Handelsgut.
- **NG-FIN-004:** Basis-Kommunikation bleibt ohne Zahlung zugänglich.
- **NG-FIN-005:** Premium-Angebote dürfen Free-Nutzer nicht herabsetzen.
- **NG-FIN-006:** Zweckgebundene Mittel werden zweckgebunden verwaltet.
- **NG-FIN-007:** Transparente Verwaltung von Spenden und Fördermitteln.
- **NG-FIN-008:** Kommerzielle B2B-Dienste beeinträchtigen nicht die Unabhängigkeit.
- **NG-FIN-009:** Fokus auf Nachhaltigkeit statt maximaler Monetarisierung.
- **NG-FIN-010:** Die Struktur sichert dauerhaft den gesellschaftlichen Zweck.
