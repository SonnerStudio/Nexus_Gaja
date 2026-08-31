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

## Possibilities and Features
- **Multimedia Communication**: The system processes not just text, but also image, audio, and video. This allows for fully immersive conversations (e.g., video calls or voice messages) in real-time across language barriers.
- **Context Sensitivity**: Recognition of irony, idioms, jargon, and regional dialects that are often misunderstood by conventional translators.
- **Cross-Platform Network**: Serves as a foundation for private chats, forum threads (posts with comments), and global community interactions.

---

## Architektura techniczna (podstawowa koncepcja)

Technicznym rdzeniem Nexus Gaja jest szyty na miarę model komunikacji, który jest ściśle podzielony na trzy warstwy:

1. **Original**: The communication object (message) created by the sender always remains immutable.
2. **Semantic Interpretation**: The system analyzes not just the words, but the actual meaning.
3. **Target Language Representation**: The AI merely creates a temporary or cached representation of the original for the respective recipient based on their preferred language. Translations never overwrite the original message.

### Zależność od kontekstu
Tłumaczenia w Nexusie Gaja nigdy nie wyświetlają wiadomości w izolacji. Silnik uwzględnia całą hierarchię:
`Wiadomość` → `Poprzednie wiadomości` → `Kontekst wątku` → `Kontekst społeczności` → `Język / region` → `Preferencje użytkownika`

### Wydajność dzięki tłumaczeniu na żądanie
Tłumaczenie odbywa się efektywnie pod względem zasobów **na żądanie** (na żądanie). Gdy użytkownik zażąda treści, zostanie ona przetłumaczona na ustawiony przez niego język. Po wygenerowaniu tłumaczenia na określony język jest ono trwale przechowywane (w pamięci podręcznej), aby drastycznie przyspieszyć przyszłe żądania.

## Moderacja wspomagana sztuczną inteligencją (WP 1.8.4)

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

### 16. Deepfake Detection
The architecture aims to detect synthetic images, cloned voices, and deepfakes. However, detection is not automatically proof.

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

### 25. Propozycje architektury i silnik zasad
Reguły (silnik zasad) nie są zakodowane na stałe w modelach AI. Sztuczna inteligencja dostarcza ustaleń; Silnik zasad podejmuje decyzję na podstawie bieżących zasad. Pozwala to na **zmiany modelu bez zmiany reguł**.

### 26. Człowiek pozostaje ostatecznym autorytetem
- **NG-AI-MOD-001**: Sztuczna inteligencja pomaga w wykrywaniu i klasyfikacji, ale nie zastępuje kontroli człowieka w przypadku poważnych decyzji.
- **NG-AI-MOD-002**: Zautomatyzowane decyzje moderacyjne muszą być identyfikowalne, rejestrowalne i weryfikowalne.

**Podsumowanie**: Budujemy czteroetapowy system: wykrywanie sztucznej inteligencji, analiza kontekstu i ryzyka, silnik polityki oraz zarządzanie ludźmi. Umożliwia to silną automatyzację bez tworzenia niebezpiecznej architektury „AI jako sędzia”.

## Project Status
The project is currently in the active architecture and planning phase.
Ongoing architectural decisions are documented in the `/docs` folder.
