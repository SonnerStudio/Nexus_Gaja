#Nexus Gaja

![Logo Nexusa Gaja](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** to inteligentna, kontekstowa sieć komunikacyjna zaprojektowana, aby zrewolucjonizować globalną komunikację.

## Cel i wizja
W zglobalizowanym świecie język jest często największą barierą. Głównym celem Nexus Gaja jest umożliwienie płynnej, pozbawionej barier i kontekstowo właściwej komunikacji między ludźmi – niezależnie od tego, czy mówią wspólnym językiem.

Nie chodzi tu tylko o sztywne tłumaczenie słów, ale o **przeniesienie znaczenia**. Nexus Gaja łączy ludzi na głębszym poziomie poprzez zrozumienie niuansów kulturowych, regionalnych i kontekstowych, umożliwiając w ten sposób autentyczne, autentyczne rozmowy.

## Możliwości i funkcje
- **Komunikacja multimedialna**: System przetwarza nie tylko tekst, ale także obraz, dźwięk i wideo. Umożliwia to prowadzenie w pełni wciągających rozmów (np. rozmów wideo lub wiadomości głosowych) w czasie rzeczywistym, bez względu na bariery językowe.
- **Wrażliwość na kontekst**: Rozpoznawanie ironii, idiomów, żargonu i dialektów regionalnych, które często są źle rozumiane przez konwencjonalnych tłumaczy.
- **Sieć wieloplatformowa**: Służy jako podstawa dla prywatnych czatów, wątków na forach (posty z komentarzami) i interakcji społeczności globalnej.

---

## Architektura techniczna (podstawowa koncepcja)

Technicznym rdzeniem Nexus Gaja jest szyty na miarę model komunikacji, który jest ściśle podzielony na trzy warstwy:

1. **Oryginał**: Obiekt komunikacyjny (wiadomość) utworzony przez nadawcę zawsze pozostaje niezmienny.
2. **Interpretacja semantyczna**: System analizuje nie tylko słowa, ale także ich rzeczywiste znaczenie.
3. **Reprezentacja języka docelowego**: sztuczna inteligencja tworzy jedynie tymczasową lub buforowaną reprezentację oryginału dla odpowiedniego odbiorcy w oparciu o jego preferowany język. Tłumaczenia nigdy nie zastępują oryginalnej wiadomości.

### Context Dependency
Translations in Nexus Gaja never view messages in isolation. The engine considers the entire hierarchy:
`Message` → `Previous Messages` → `Thread Context` → `Community Context` → `Language / Region` → `User Preferences`

### Wydajność dzięki tłumaczeniu na żądanie
Tłumaczenie odbywa się efektywnie pod względem zasobów **na żądanie** (na żądanie). Gdy użytkownik zażąda treści, zostanie ona przetłumaczona na ustawiony przez niego język. Po wygenerowaniu tłumaczenia na określony język jest ono trwale przechowywane (w pamięci podręcznej), aby drastycznie przyspieszyć przyszłe żądania.

## AI-Assisted Moderation (WP 1.8.4)

Dzięki AI-Assisted Moderation robimy znaczący krok od pomysłu na produkt do architektury technicznej, biorąc pod uwagę aktualne regulacje UE (wymogi przejrzystości unijnej ustawy o sztucznej inteligencji zgodnie z art. 50; ustawa o usługach cyfrowych ze zrozumiałymi uzasadnieniami i możliwościami odwoławczymi).

### 1. Podstawowa zasada
Najważniejsze zdanie dotyczące architektury brzmi: **Moderowana sztuczna inteligencja to system przeglądu, a nie autonomiczny system rządzący.**
Został zaprojektowany, aby pomagać ludziom w umiarze, a nie po to, aby samodzielnie decydować, jakie opinie mogą istnieć na Nexusie Gaja.
Rozróżniamy trzy poziomy:
- **Wykrywanie:** „Możliwe, że nastąpiło tu naruszenie zasad”.
- **Ocena:** „Prawdopodobieństwo naruszenia zasad wynosi np. 94%”.
- **Decyzja:** „Jakie działania zostały faktycznie podjęte?”
W ciężkich przypadkach trzeci poziom musi być kontrolowany przez człowieka.

### 2. Moderacyjna sztuczna inteligencja jako podsystem
Zamiast pojedynczej sztucznej inteligencji tworzony jest solidny podsystem:
```tekst
                 MODERACJA AI NEXUS GAJA
                          │
       ┌──────────────────┼──────────────────────┐
       │ │ │
  Język AI Bezpieczeństwo AI Oszustwo AI
       │ │ │
       ├──────────────┬───┴──────────────────┬───┤
       │ │ │
 Tożsamość zachowań tłumaczeniowych
 Analiza Sygnały analizy
       │ │ │
       └──────────────┼──────────────────┘
                      ▼
               Ocena ryzyka
                      │
                      ▼
               Przegląd ludzki
```

### 3. Najważniejsze moduły AI
Nexus Gaja wykorzystuje dziewięć wyspecjalizowanych obszarów analitycznych:
- **M1 – Rozumienie języka**: Wykrywa język, dialekt, slang, wskaźniki ironii, problemy z tłumaczeniem.
- **M2 – Wykrywanie toksyczności/nadużycia**: Wykrywa obelgi, ataki osobiste, molestowanie.
- **M3 – Wykrywanie zagrożeń**: Wykrywa potencjalne zagrożenia, szantaż, ogłoszenia o przemocy.
- **M4 – Wykrywanie nienawiści/dehumanizacji**: Wykrywa ataki ukierunkowane na osoby w oparciu o określone przynależności.
- **M5 – Wykrywanie spamu/manipulacji**: Wykrywa spam, zachowanie botów i skoordynowaną manipulację.
- **M6 – Wykrywanie oszustw**: Wykrywa podejrzane próby oszustwa, phishing, socjotechnikę.
- **M7 – Integralność tożsamości**: Sprawdza sygnały dotyczące przejęć kont, wielu kont, uchylania się od banów.
- **M8 – Bezpieczeństwo mediów**: Analizuje obrazy, dźwięk, wideo, dokumenty.
- **M9 – Silnik Kontekstowy**: Najważniejszy moduł. Łączy indywidualne ustalenia.

### 4. Dlaczego silnik kontekstowy jest kluczowy
Samo wyszukiwanie słów kluczowych byłoby niewystarczające. „Mogłbym go zabić ze śmiechu” semantycznie zawiera przemoc, ale jest figurą retoryczną. „Jutro o 20.00 zastrzelę go przed jego domem” to zupełnie inna sytuacja. Sztuczna inteligencja musi zrozumieć, co oznacza stwierdzenie w jego konkretnym kontekście.

### 5. Moderacja wielojęzyczna
Umiar nie może po prostu porównywać słów. Musi przeanalizować poziom semantyczny (np. idiomy niemieckie vs. idiomy japońskie vs. wyrażenia regionalne).

### 6. Język oryginalny + tłumaczenie
Oryginał i tłumaczenie analizowane są oddzielnie. Dopiero wtedy ma miejsce „Połączona ocena moderacji”. Dzięki temu Nexus Gaja może ustalić, czy samo tłumaczenie mogło spowodować eskalację lub zmianę faktów.

### 7. Poziom zaufania
Każda ocena AI otrzymuje poziom pewności (np. Prawdopodobieństwo zagrożenia: 0,96). Jednakże: **Wskaźnik zaufania ≠ Prawda.** Wynik 96% oznacza jedynie, że model ma dużą pewność co do swojej klasyfikacji, niekoniecznie oznaczając, że użytkownik jest winny.

### 8. Niepewność sama w sobie staje się sygnałem
Jeśli sztuczna inteligencja jest niepewna (np. Zagrożenie: 0,62, Satyra: 0,54), nie może po prostu narzucać surowych zasad. Zamiast tego niepewność jest wbudowana bezpośrednio w architekturę: **Wymagana weryfikacja człowieka**.

### 9. Cztery strefy decyzyjne
- 🟢 **ZIELONY**: Zgodność z dużym prawdopodobieństwem. → brak akcji.
- 🟡 **ŻÓŁTY**: Możliwe naruszenie. → monitoruj / ostrzegaj, jeśli to konieczne.
- 🟠 **POMARAŃCZOWY**: Prawdopodobne naruszenie. → przegląd moderacji.
- 🔴 **CZERWONY**: Możliwe poważne naruszenie. → natychmiastowe środki ochronne + przegląd przez człowieka.

### 10. Żadnej „kary AI”
**Sztuczna inteligencja nie nakłada żadnych ostatecznych sankcji.** Może uruchomić natychmiastowe środki techniczne (np. tymczasowe wstrzymanie wiadomości) w przypadku poważnych problemów związanych z bezpieczeństwem, ale ostateczna decyzja pozostaje możliwa do zweryfikowania.

### 11. Środki ochronne mogą zadziałać automatycznie
W przypadku konkretnego zagrożenia (Wykryte zagrożenie → Wysoka pewność → Tymczasowe ograniczenie → Przegląd przez człowieka → Decyzja) chronimy zagrożonego użytkownika, nie zamieniając AI w sędziego.

### 12. Sztuczna inteligencja musi umieć uzasadniać swoje decyzje
DSA wymaga jasnych i konkretnych powodów. Sztuczna inteligencja zapewnia ustrukturyzowane rozumowanie: reguła (NG-CONDUCT-004), wykryto (potencjalne konkretne zagrożenie), pewność (0,94), odpowiedni kontekst (poprzednie 4 komunikaty), zalecane działanie (weryfikacja manualna).

### 13. Sztuczna inteligencja nie może potajemnie zmieniać treści
**Moderowana sztuczna inteligencja nie może nigdy niezauważona zmieniać oryginalnej treści.** Podczas automatycznej korekty, tłumaczenia lub podsumowania oryginał jest zawsze zachowywany.

### 14. Treści generowane przez sztuczną inteligencję
Rozróżniamy: stworzone przez człowieka, wspomagane przez sztuczną inteligencję, generowane przez sztuczną inteligencję i zmanipulowane przez sztuczną inteligencję. Stanie się to częścią metadanych treści.

### 15. Etykietowanie treści AI i warstwa pochodzenia AI
Zgodnie z zasadami przejrzystości zawartymi w unijnej ustawie o sztucznej inteligencji (obowiązującej od sierpnia 2026 r.) treści generowane przez sztuczną inteligencję muszą być możliwe do zidentyfikowania. Zapewniamy warstwę pochodzenia AI, która przechowuje metadane (pochodzenie AI, model, znacznik czasu, weryfikacja przez człowieka).

### 16. Wykrywanie fałszywych informacji
Celem tej architektury jest wykrywanie syntetycznych obrazów, sklonowanych głosów i deepfakes. Jednak wykrycie nie jest automatycznie dowodem.

### 17. Brak automatycznej „maszyny prawdy” (umiar ≠ sprawdzanie faktów)
Jeden system sprawdza: „Czy treść narusza regulamin?” (Moderacja treści), inny podaje: „Jakie informacje i źródła są dostępne?” (Pomoc informacyjna). Opinii nie usuwa się po prostu dlatego, że jest „błędna”.

### 18. Ochrona przed błędną interpretacją kulturową
Sztuczna inteligencja wymaga **Modeli kontekstu kulturowego**, aby zapobiec uznawaniu norm komunikacyjnych jednego kraju za standard globalny.

### 19. Ironia, satyra i humor
Sztuczna inteligencja wykorzystuje kontekst, emotikony, historię rozmów i znane struktury ironii, ale musi uwzględniać niepewność, gdy znaczenia są niejednoznaczne.

### 20. Brak kary na podstawie pojedynczego wyniku AI
Żadna poważna interwencja moderacyjna nie może opierać się wyłącznie na pojedynczym wyniku automatycznej klasyfikacji (tekst + kontekst + zachowanie + język + media + silnik reguł = ocena ryzyka).

### 21. Sygnały dotyczące zachowań użytkowników i brak systemu kredytu społecznego
Dotyczy to sygnałów nadużyć technicznych (np. masowego wysyłania spamu), a nie ogólnego systemu ocen społecznościowych. Nexus Gaja nie utrzymuje Systemu Kredytu Społecznego – umiar służy bezpieczeństwu, a nie ocenie wartości człowieka.

### 22. Moderowana sztuczna inteligencja musi podlegać audytowi
Wszystkie istotne zautomatyzowane decyzje są rejestrowane (identyfikator zdarzenia, identyfikator reguły, zaufanie, weryfikacja manualna itp.), aby zapewnić identyfikowalność.

### 23. Fałszywie pozytywne, fałszywie negatywne i wskaźniki jakości
Typy błędów są monitorowane. Pulpit nawigacyjny mierzy precyzję, wycofanie, a zwłaszcza **Współczynnik wycofania odwołań** (liczba udanych odwołań).

### 24. Równość językowa i stronniczość w tłumaczeniu
Jakość moderacji musi być porównywalna we wszystkich obsługiwanych językach (test porównawczy moderacji wielojęzycznej). Jeśli wyniki moderacji różnią się między oryginałem a tłumaczeniem (konflikt w tłumaczeniu), należy to szczegółowo sprawdzić.

### 25. Architecture Proposal & Policy Engine
Rules (Policy Engine) are not hardcoded into the AI models. The AI provides findings; the Policy Engine decides based on current rules. This allows for **model changes without rule changes**.

### 26. The Human Remains the Final Authority
- **NG-AI-MOD-001**: The AI assists in detection and classification, but does not replace human review in severe decisions.
- **NG-AI-MOD-002**: Automated moderation decisions must be traceable, loggable, and verifiable.

**Summary**: We are building a four-stage system: AI Detection, Context and Risk Analysis, Policy Engine, and Human Governance. This enables strong automation without creating a dangerous "AI as Judge" architecture.

## Zasady finansowania i model przychodów (WP 1.10.1)

W przypadku Nexus Gaja obowiązuje bardzo ważna zasada ekonomiczna: **Brak tradycyjnych reklam na platformie.**
To zasadniczo odróżnia Nexus Gaja od wielu współczesnych sieci społecznościowych. Nie oznacza to jednak, że Nexus Gaja nie może mieć charakteru komercyjnego. Wręcz przeciwnie, platforma musi być opłacalna ekonomicznie, aby jej cel społeczny mógł przetrwać. Działalność gospodarcza jest środkiem do celu, a nie głównym celem platformy.

### 1. Zasada NG-FIN-001
Nexus Gaja finansuje swoją działalność poprzez przejrzyste źródła przychodów oddzielone od zainteresowań użytkowników, a nie poprzez monetyzację uwagi użytkowników lub danych osobowych.

### 2. Żadnych tradycyjnych reklam
Szczególnie zabronione są:
- Banery reklamowe
- Wyskakujące reklamy
- Automatyczne odtwarzanie reklam wideo
- Posty sponsorowane w kanale standardowym
- Spersonalizowane profile reklamowe
- Sprzedaż profili użytkowników lub danych osobowych
- Reklamy pochodzące z prywatnych rozmów.

Nexus Gaja pozostaje **przestrzenią komunikacyjną, a nie reklamową**.

### 3. Finansowanie bez reklam (6 filarów)
Finansowanie opiera się na sześciu filarach:
```tekst
                 NEXUS GAJA
                     │
       ┌─────────────┼─────────────┐
       ▼ ▼ ▼
   DARATKI NA ORGANIZACJĘ PREMIUM
       │ │ │
       ├─────────────┼──────────────┤
       ▼ ▼ ▼
    DOTACJE USŁUG PARTNERSKICH
```

#### Filar 1 – bezpłatne członkostwo podstawowe
**Nexus Gaja Free** umożliwia każdemu podstawowe zrozumienie międzynarodowego (profil, komunikacja międzynarodowa, posty, społeczności, czaty, podstawowe tłumaczenia) bez żadnych kosztów.

#### Filar 2 – Oferty Premium
Dobrowolne płatne oferty (**Nexus Gaja Plus**) zapewniające większe limity miejsca, wyższą jakość multimediów, większe limity AI i funkcje organizacyjne.
**Ważne (Freemium zamiast Dark Freemium):** Podstawowa komunikacja nie może być nigdy sztucznie degradowana.

#### Filar 3 – Organizacje
Specjalne konta dla szkół, uniwersytetów, organizacji pozarządowych, firm i gmin (**Organizacja Nexus Gaja**). Szkoły mogą być wspierane w ramach stawek instytucjonalnych jako czynniki pomnażające międzynarodowe zrozumienie.

#### Filar 4 – Darowizny
**Pula funduszy Nexus Gaja** przyjmuje darowizny ogólne i celowe (np. „na międzynarodową komunikację młodzieży”). **Księga alokacji funduszy** zapewnia przejrzystą alokację środków.
**Fundusz celowy i Tombola:** Część darowizn zasila pulę do bezpłatnego/zniżkowego wykorzystania. Mechanizm loterii/tomboli umożliwia przydzielanie tych środków w sposób przejrzysty i podlegający kontroli.

#### Filar 5 – Finansowanie Instytucjonalne
Fundacje, programy finansowania kultury lub programy państwowe.
**NG-FIN-002:** Wsparcie finansowe nie kupuje kontroli redakcyjnej ani technicznej (Niezależność).

#### Filar 6 – Usługi komercyjne
Usługi B2B, takie jak **Tłumaczenie jako usługa** (API), komunikacja organizacyjna lub międzynarodowe sale konferencyjne, bez obciążania standardowego kanału użytkownika.

### 4. Brak monetyzacji danych i ekonomia nadzoru
**NG-FIN-003:** Dane osobowe użytkownika nie są towarem. Zakaz sprzedaży list, profili i historii. Nexus Gaja nie czerpie korzyści z monitoringu psychologicznego (Ekonomia Nadzoru).

### 5. Przejrzystość finansowa i księga funduszy
**Przejrzystość finansowa Nexus Gaja:** Publikacja zagregowanych struktur finansowych. Darowizny celowe podlegają rozliczeniu technicznemu (ID funduszu → Cel → Saldo → Alokacja). Zakaz subsydiowania celów społecznych w marketingu korporacyjnym.

### 6. Solidarnościowy model finansowania
Ceny opierają się na zorientowaniu na koszty, uczciwości i solidarności.
**Solidarity Premium:** Dobrowolna opcja dla użytkowników Premium w celu sfinansowania części dostępu innego użytkownika. Wymuszona solidarność lub społeczeństwo klasy premium (mniejszy szacunek/umiarkowanie dla darmowych użytkowników) jest surowo zabronione.

### 7. Ekonomiczne KPI zamiast ekonomii zaangażowania
Brak zależności od utrzymywania użytkowników „online tak długo, jak to możliwe” (żadnych ragebaitów, nieskończonych kanałów).
Zamiast tego używamy wskaźników takich jak:
- **Global Communication Index (GCI):** Udane relacje komunikacyjne pomiędzy ludźmi z różnych regionów językowych/kulturowych.
- **Wskaźnik zrównoważonego rozwoju platformy (PSR):** Powtarzające się przychody / powtarzające się koszty operacyjne (Cel ≥ 1).

### 8. Czego wyraźnie nie chcemy (lista negatywna)
Nexus Gaja **nie** jest finansowany przez:
❌ Sprzedaż danych osobowych
❌Spersonalizowana reklama tradycyjna
❌ Monitorowanie zachowań użytkowników w celach reklamowych
❌ Sprzedaż prywatnych danych komunikacyjnych
❌ Ukryte wykorzystanie danych AI
❌ Manipulacyjne paywalle Premium
❌ Ograniczenie sztucznego zasięgu w celu monetyzacji
❌ Płatne wpływy polityczne
❌ Zakup uprzywilejowanych decyzji moderacyjnych.

### 9. Wstępna architektura finansowa
```tekst
                         NEXUS GAJA
                              │
             ┌────────────────┼────────────────┐
             │ │ │
             ▼ ▼ ▼
          ORGANIZACJE UŻYTKOWNIKÓW PRZEDSIĘBIORSTWA
             │ │ │
             └────────────────┼────────────────┘
                              │
                       USŁUGI PLATFORMY
                              │
          ┌─────────────────── ┼───────────────────┐
          ▼ ▼ ▼
       API PREMIUM DONATIONS
                              │
                    ┌─────────┴─────────┐
                    ▼ ▼
               FUNDUSZ OGÓLNY FUNDUSZE OGRANICZONE
                                        │
                                        ▼
                                  CEL SPOŁECZNY
```

### Podsumowanie zasad finansowania (NG-FIN)
- **NG-FIN-001:** Brak finansowania poprzez tradycyjną reklamę.
- **NG-FIN-002:** Brak kontroli redakcyjnej/technicznej poprzez wsparcie finansowe.
- **NG-FIN-003:** Dane osobowe nie są towarem.
- **NG-FIN-004:** Podstawowa komunikacja pozostaje dostępna bez opłat.
- **NG-FIN-005:** Oferty premium nie mogą degradować bezpłatnych użytkowników.
- **NG-FIN-006:** Fundusze celowe zarządzane są zgodnie z ich przeznaczeniem.
- **NG-FIN-007:** Przejrzyste zarządzanie darowiznami i grantami.
- **NG-FIN-008:** Komercyjne usługi B2B nie naruszają niezależności.
- **NG-FIN-009:** Skoncentruj się na zrównoważonym rozwoju, a nie na maksymalnej monetyzacji.
- **NG-FIN-010:** Obiekt trwale zabezpiecza cel społeczny.

## API, interfejsy i architektura komunikacyjna (WP 1.11.3)

Aby zapewnić stabilność, bezpieczeństwo i skalowalność systemu, Nexus Gaja opiera się na architekturze opartej wyłącznie na API i opartej na zdarzeniach.

### Podstawowe zasady
- **Brak bezpośredniego dostępu do bazy danych:** Komponenty komunikują się wyłącznie poprzez zdefiniowane interfejsy (API lub zdarzenia), nigdy poprzez bezpośrednie zapytania do baz danych innych usług.
- **Brama API:** wszystkie żądania klientów zewnętrznych są kierowane przez bramę API obsługującą uwierzytelnianie, routing i ograniczanie szybkości.
- **Atrakcja dostawców:** Usługi zewnętrzne (modele AI, dostawcy płatności, silniki tłumaczeniowe) są integrowane poprzez warstwy abstrakcji, co pozwala uniknąć zakodowanych na stałe zależności i umożliwia elastyczną wymianę dostawców.

### Wzorce komunikacji
- **Synchroniczne interfejsy API (REST/HTTPS):** Używane do natychmiastowych żądań, takich jak logowanie, ustawienia profilu lub bezpośrednie tłumaczenia.
- **Zdarzenia asynchroniczne (szyna zdarzeń):** Centralny układ nerwowy Nexusa Gaja do opóźnionego, oddzielonego przetwarzania (np. „Wiadomość. Utworzona” uruchamia asynchronicznie Moderację, Tłumaczenie i Powiadomienie).
- **Czas rzeczywisty (WebSocket):** Dedykowane kanały do ​​czatu na żywo i wskaźników pisania.

### Bezpieczeństwo i niezawodność
- **Model zerowego zaufania:** Wewnętrzny ruch sieciowy nie jest automatycznie ufany; wrażliwa komunikacja między usługami wymaga uwierzytelnienia.
- **Idempotencja i wzorzec skrzynki nadawczej:** Operacje krytyczne (takie jak darowizny lub wysyłanie wiadomości) są zaprojektowane tak, aby były idempotentne, aby zapobiec dublowaniu przetwarzania, wykorzystując wzorzec skrzynki nadawczej, aby zapewnić, że zdarzenia nigdy nie zostaną utracone nawet podczas transakcji w bazie danych.

## Model domeny MVP (WP 1.12)

Nexus Gaja wykorzystuje architekturę MVP opartą wyłącznie na domenie (ADR-025), zaprojektowaną jako modułowy monolit z wyraźnymi granicami domen. Taka struktura zapobiega przedwczesnej złożoności mikrousług, zachowując jednocześnie elastyczność późniejszego podziału określonych domen.

### Podstawowe jednostki domeny
Architektura wyraźnie oddziela różne koncepcje, aby zapewnić integralność danych i uniknąć pułapek strukturalnych, takich jak „Nazwa użytkownika = Człowiek”:
- **Tożsamość i konta:** `Osoba` ≠ `Konto użytkownika` ≠ `Weryfikacja tożsamości`. Zweryfikowana osoba uczestniczy poprzez konto, ale podmioty pozostają odrębne.
- **Komunikacja:** `Wiadomość` ≠ `Tłumaczenie`. Oryginalna wiadomość pozostaje niezmienna; tłumaczenia są elementami połączonymi.
- **Moderacja:** `Zgłoś` ≠ `Decyzja moderacji`. Raport jest jedynie roszczeniem; sprawa moderacyjna prowadzi dochodzenie.
- **Finanse:** `Darowizna` ≠ `Saldo funduszu`. Wpłaty księgowane są poprzez niezmienną księgę do funduszu, co zapewnia przejrzystość finansową.

### Połączone domeny
System jest podzielony na przejrzyste domeny logiczne (ograniczone konteksty): tożsamość, konto, organizacja, komunikacja, społeczność, język, moderacja, powiadamianie, finanse i zarządzanie. Domeny te odwzorowują całą podróż od podmiotów ze świata rzeczywistego (użytkowników, szkół, organizacji pozarządowych) do ich interakcji cyfrowych i powiązanego zarządzania.

## Stan projektu
Projekt jest obecnie na etapie aktywnej architektury i planowania.
Bieżące decyzje architektoniczne są dokumentowane w folderze `/docs`.