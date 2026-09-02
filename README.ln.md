# Nexus Gaja ezali
<br>
<video src="assets/video/Nexus_Gaja_TikTok_EN.mp4" controls width="100%"></video>



> *Mpo na kimia ya mokili mobimba mpe bososoli ya mokili mobimba*


![Logo ya Nexus Gaja](biloko/logo.jpg)

![Elombe ya Nexus Gaja](biloko/img/elombe_ya_nexus.jpg)

{{BLOQUE__NAV}}

**Nexus Gaja** ezali réseau ya communication ya mayele, oyo eyebi contexte oyo ebongisami pona ko révolutionner ba communications mondiales.

## Ntina mpe Bomoni

![Nexus Gaja Vision](biloko ya motuya/img/nexus_vision.jpg)

Na mokili oyo ezali na mokili mobimba, mbala mingi monɔkɔ nde epekisaka mingi. Mokano monene ya Nexus Gaja ezali ya kopesa nzela na bosololi ya kozanga boyokani, ya kozwama mpe ya sikisiki na contexte kati na bato - ata soki balobaka monoko moko to te. 

Ezali kaka te mpo na kobongola maloba na motó makasi, kasi mpo na **kopesa ndimbola**. Nexus Gaja ekangisaka bato na niveau ya mozindo na kososolaka ba nuances culturelles, régionales mpe contextuelles, ko permettre masolo ya solo, ya solo.

## Ba possibilités na ba fonctionnalités
- **Communication multimédia**: Système e traité kaka texte te, kasi pe bilili, audio na vidéo. Yango epesaka nzela na masolo ya kozindisa mobimba (e.g. kobenga na video to ba messages ya mongongo) na tango ya solo na ndelo ya nkota.
- **Sensibilité ya contexte** : Détection ya ironie, idiome, jargon na ba dialectes régionales oyo mbala mingi ba comprendre mabe na ba traducteurs traditionnels.
- **Réseau croisé-plateforme**: Ezali kosala lokola moboko ya ba chats privés, ba threads ya forum (ba posts na ba commentaires) mpe ba interactions ya communauté mondiale.

---

## Architecture technique (concept ya moboko)

![Likanisi ya libongoli ya Nexus Gaja](biloko/img/nexus_translation.jpg)

Noyau technique ya Nexus Gaja ezali modèle ya communication oyo esalemi yango moko, oyo ekabolami strictement na ba couches misato:

1. **Original**: Objet ya communication (message) oyo motindi asali etikalaka toujours inchangeable.
2. **Ndimbola ya sémantique**: Système e analyser kaka maloba te, kasi ndimbola ya solo.
3. **Représentation ya langue cible**: AI esala kaka représentation temporaire to cache ya original pona moyambi respectif sur la base ya langue oyo balingi. Mabongoli ekomaka ata moke te likoló ya nsango ya ebandeli.

### Dépendance ya contexte
Mabongoli etalaka jamais ba sango na Nexus Gaja na isolement. Moteur ezuaka hiérarchie mobimba na makanisi:
`Message` → `Messages ya kala` → `Context ya thread` → `Context ya communauté` → `Monoko / Etuka` → `Bolingi ya mosaleli`

### Efficacité na nzela ya traduction sur demande
Bobongoli esalemaka kaka **ntango babengi** (na bosenga) na ndenge ya kobomba makoki. Ntango mosaleli asɛngi makambo oyo ezali na kati, ebongolami na monɔkɔ na ye ya liboso. Mabongoli mpo na monoko moko boye ebombamaka mpo na libela (caching) mpo na kosala ete mituna oyo ekoya na nsima ezala mbangu mpenza.

## Modération oyo esalemi na AI (WP 1.8.4) .

![Bokangami ya AI ya Nexus Gaja](biloko/img/moderation_ya_nexus.jpg)

Na moderation oyo esungami na AI, tosali litambe monene kobanda na likanisi ya produit kino na architecture technique mpe tozuaka na makanisi mibeko ya UE oyo ezali lelo (mikumba ya polele ya Loi ya AI ya UE engebene na Art. 50; Loi ya Services numériques na ba justifications compréhensibles mpe ba options ya objection).

### 1. Mobeko ya moboko
Fraze ya motuya mingi pona architecture ezali : **AI ya moderation ezali système ya vérification et non système autonome ya bokonzi.**
Ezali na mokano ya kosunga bato na bokatikati, kasi te mpo na koyeba makanisi nini epesami nzela ya kozala na Nexus Gaja.
Na bongo, tokesenisaka makambo misato:
- **Detect:** “Ekoki kozala na violation ya mibeko awa.”
- **Taux:** “Ndakisa, probabilité ya kobuka mobeko ezali 94%.”
- **Bozwa mokano:** “Action nini ekosalema mpenza?”
Esengeli ko contrôler niveau ya misato na ndenge ya bomoto na ba cas graves.

### 2. AI ya moderation ekozala sous-système na yango moko
Na esika ya AI moko, sous-système ya makasi esalemi:
```mokanda
                 MODERATION YA NEXUS GAJA AI
                          │
       ┌─────────────────── ┼──────────────────┐
       │ │ │
  Monoko AI Bobateli AI Bokosi AI
       │ │ │
       ├─────────────────── ┴──────────────────┤
       │ │ │
 Identité ya bizaleli ya bobongoli
 Analyse Ba Signaux ya Analyse
       │ │ │
       └────────────────────────────────────┘
                      ▼
               Botali makama
                      │
                      ▼
               Botali ya bato
```

### 3. Ba modules ya AI ya motuya mingi
Ezali na ba domaines spécialisés ya analyse libwa pona Nexus Gaja:
- **M1 – Bososoli ya monoko**: Ezali ko détecter monoko, dialecte, argot, ba indicateurs ya ironie, ba problèmes ya traduction.
- **M2 – Détection ya toxicité / abuse**: Ezali ko détecter ba insultes, ba attaques personnelles, ba harassement.
- **M3 – Détection ya ba menaces**: Ezali ko détecter ba menaces oyo ekoki kozala, chantage, pe ba menaces ya mobulu.
- **M4 – Détection ya Hate / Déhumanisation**: Ezali ko détecter ba attaques ciblées na batu sur la base ya ba affiliations spécifiques.
- **M5 – Détection ya spam / Manipulation**: Ezali ko détecter ba spam, comportement ya bot, manipulation coordonnée.
- **M6 – Détection ya fraude**: Ezali ko détecter ba tentatives ya fraude suspect, phishing, ingénierie sociale.
- **M7 – Intégrité ya identité**: Ezali ko vérifier ba signaux oyo etali bozui ya compte, ba comptes ebele, bypass ya blocage.
- **M8 – Bobateli ya ba médias**: Ezali ko analyser bilili, audio, vidéo, mikanda.
- **M9 – Moteur ya contexte**: Module ya motuya mingi. Ezali kosangisa makambo oyo moto na moto amoni.

### 4. Mpo na nini Moteur ya Contexte ezali na ntina mingi
Boluki ya peto ya maloba ya ntina ekozala ekoki te. “Nakokaki koboma ye koseka” ezali na mobulu ya ndimbola, kasi ezali elilingi ya maloba. “Lobi na ngonga ya 8 p.m. nakobɛta ye masasi liboso ya ndako na ye” ezali likambo mosusu mpenza. AI esengeli a comprendre nini déclaration elingi koloba na contexte spécifique oyo.

### 5. Bokatikati na minoko mingi
Bokatikati ekoki te bobele kokokanisa maloba. Esengeli ko analyser niveau ya signification (e.g. ba idiomes allemands vs. ba idiomes japonais vs. expressions régionales).

### 6. Monoko ya ebandeli + libongoli
Batalelami na ebandeli mpe libongoli yango ekeseni. Kaka na sima nde “Evaluation combinée de moderation” esalemaka. Na ndenge yango, Nexus Gaja ekoki koyeba soki libongoli yango moko ekoki kozala ete likambo yango ebakisaki to ebongoli.

### 7. Point ya confiance
Botalisi moko moko ya AI ezuaka motuya ya bondimi (e.g. Probabilité ya likama: 0,96). Kasi: **Score ya confiance ≠ Solo.** Point ya 96% elakisi kaka que modèle ezali na confiance mingi na classification na yango, forcément te que usager azali na faute.

### 8. Incertitude yango moko ekomi signal
Soki AI ezali na ntembe (e.g. Menace: 0,62, Satire: 0,54), ekoki kaka te kosala action ya makasi. Na esika na yango, bozangi bondimi etongami mbala moko na kati ya architecture: **Esengeli botali ya bato**.

### 9. Bitando minei ya mikano
- 🟢 **VERT**: Mingi mingi ekoki kotosa. → likambo moko te.
- 🟡 **JAUNE**: violation ekoki kozala. → tala / ko noter soki esengeli.
- 🟠 **ORANGE**: Probable ya violation. → Vérification ya moderation.
- 🔴 **ROGE**: Violation ya munene possible. → meko ya kobatela mbala moko + test ya bato.

### 10. “Etumbu ya AI” te .
**AI epesaka etumbu ya suka te.** Ekoki ko déclencher ba mesures techniques ya urgence (e.g. retenue message) soki ba soucis ya sécurité ya makasi, kasi mokano ya suka etikali vérifiable.

### 11. Ba mesures ya protection ekoki kozala automatique
Soki ezali na likama moko ya sikisiki (Likama oyo ezwami → Bondimi mingi → Bopekisami mpo na mwa ntango → Botali ya bato → Ekateli), tobatelaka mosaleli oyo azali na likama kozanga kosala ete AI azala zuzi.

### 12. Esengeli AI ezala na makoki ya kolongisa mokano na yango
DSA esengaka bantina ya polele mpe ya sikisiki. Ba raisons ya AI na ndenge ya structuré : Mobeko (NG-CONDUCT-004), Détecté (Potentiel menace concrète), Confiance (0,94), Contexte pertinent (4 messages ya kala), Action recommandé (Revue humain).

### 13. AI epesami nzela te ya kobongola na kobombana makambo oyo ezali na kati
**AI ya moderation esengeli ata moke te kobongola makambo ya ebandeli kozanga ete moto ayeba yango.** Ba correction automatique, ba traductions to ba résumés ebatelaka makambo ya ebandeli.

### 14. Makambo oyo esalemi na AI
Tokesenisaka : oyo esalemi na bato, oyo esalisami na AI, oyo esalemi na AI mpe oyo esalemi na AI. Yango ekomi eteni ya ba métadonnées ya contenus.

### 15. Etiquetage ya contenus ya AI & Couche ya provenance ya AI
Engebene na mibeko ya polele ya mobeko ya UE mpo na AI (kobanda sanza ya mwambe 2026), esengeli kosala ete makambo oyo esalemi na AI eyebana. Tozali kokanisa Couche ya Provenance ya AI oyo ebombaka ba métadonnées (origine ya AI, modèle, timbre de temps, revue humaine).

### 16. Bomonisi ya deepfake
Architecture ezali na tina ya ko détecter ba images synthétiques, ba voix stimulées na ba deepfakes. Kasi reconnaissance ezalaka automatiquement preuve te.

### 17. “Masini ya bosolo” ya automatique te (moderation ≠ vérification ya makambo) .
Système moko etalelaka boye: “Makambo oyo ezali na kati ebuki mibeko moko boye?” (Content Moderation), mosusu epesi: "Nsango nini mpe maziba nini ezali?" (Lisalisi ya sango). Makanisi elongolamaka kaka te lokola “mabe”.

### 18. Bobateli na ndimbola ya mabe ya mimeseno
AI esengi **Modèles de contexte culturel** mpo na kopekisa norme ya communication ya mboka moko ezwama lokola norme mondiale.

### 19. Ironie, satire mpe maseki
AI esalela contexte, emojis, ba flux ya masolo mpe ba structures ya ironie oyo eyebani malamu, kasi esengeli kopesa nzela na incertitude tango ba significations ezali claire te.

### 20. Etumbu te oyo etongami na score moko ya AI
Intervention moko te ya moderation grave ekoki kozala exclusivement na résultat ya classification automatique moko (Text + Context + Comportement + Langue + Media + Moteur ya mibeko = Évaluation ya ba risque).

### 21. Ba Signaux ya Comportement ya Mosaleli & Système ya Crédit Social te
Ezali mpo na ba signaux ya abuse technique (e.g. posting en masse spam), kasi système ya cote sociale générale te. Nexus Gaja esalaka système ya crédit social te - moderation ezali pona sécurité pe pona ko évaluer valeur ya mutu te.

### 22. AI ya moderation esengeli ezala auditable
Ba décisions nionso ya automatique oyo etali yango ekomami na journal (ID ya événement, ID ya mibeko, confiance, revue humaine, etc.) pona ko assurer traçabilité.

### 23. Ba positifs ya lokuta, ba négatifs ya lokuta & ba métriques ya qualité
Ba types ya erreur ezo surveiller. Tableau de bord emekaka précision, rappel mpe mingi mingi **Taux ya retour ya recours** (motango ya ba recours oyo elongi). 

### 24. Bosembo ya nkota & bias ya bobongoli
Quality ya moderation esengeli ekokana na minoko nionso oyo esungami (Multilingual Moderation Benchmark). Soki ba résultats ya moderation ekeseni entre original na traduction (conflit ya traduction), esengeli ko vérifier yango separatement.

### 25. Moteur ya Proposition & Politique ya Architecture
Mibeko (moteur politique) ezali hard-coded te na ba modèles AI. AI epesaka ba insights, moteur ya politique ezuaka ba décisions na kotalaka mibeko ya lelo. Yango epesaka nzela na **mbongwana ya modèle kozanga kobongola mibeko**.

### 26. Bato batikali bokonzi ya suka
- **NG-AI-MOD-001**: AI esungaka bomoni mpe botangi, kasi ezwi esika ya botali ya bato te tango ya kozwa mikano ya makasi.
- **NG-AI-MOD-002**: Ba décisions ya moderation automatique esengeli ezala traçable, enregistrable pe vérifier.

**Bokuse**: Tozali kotonga système ya niveau minei : détection ya AI, analyse ya contexte pe ya ba risque, moteur ya politique pe gouvernance humaine. Yango epesaka nzela na automatisation makasi sans ko créer architecture ya dangereuse « AI comme juge ».

## Mibeko ya misolo pe modèle ya mosolo (WP 1.10.1) .

![Modèle ya misolo ya Nexus Gaja](biloko/img/nexus_finance.jpg)

Principe économique ya base moko ya motuya mingi etali Nexus Gaja: **Piblisite classique te na kati ya plateforme.**
Yango ekomisaka Nexus Gaja conceptuellement différente na ba réseaux sociaux mingi ya lelo. Kasi yango elingi koloba te: Nexus Gaja esengeli te kozala na personnage commercial. Au contraire : plateforme esengeli ezala économiquement viable mpo but social na yango e continuer kozala na long terme. Yango wana, mosala ya nkita ezali nzela ya kokokisa mokano moko, kasi te ntina mpenza ya estrade.

### 1. Mobeko NG-FIN-001
Nexus Gaja e financer ba opérations na yango na nzela ya ba flux ya revenu transparent oyo ekabwani na ba intérêts ya usager mpe te na nzela ya marketing ya attention ya ba usagers na yango to ba données personnelles.

### 2. Piblisite ya classique te
Mingimingi, makambo oyo elandi elingaki kopesamela nzela te:
- Piblisite ya banner
- Piblisite ya pop-up
- Ba vidéos ya publicité oyo ebetamaka automatiquement
- ba posts sponsorisés na alimentation normale
- ba profils ya publicité personnalisé
- Koteka ba profils ya basaleli
- Boteki ya ba données personnelles
- Piblisite oyo euti na masolo ya bato.

Yango etiki esika ya bopanzi sango: **Esika ya bopanzi sango na esika ya esika ya piblisite.**

### 3. Financement sans publicité
Na esika na yango, misolo na biso ekoki kozala na makonzí mingi. To proposer liboso makonzí motoba:
```mokanda
                 NEXUS GAJA NA YE
                     │
       ┌───────────────────────────┐
       ▼ ▼ ▼
   ORGANISATION YA PREMIUM EPESA DONA
       │ │ │
       ├───────────────────────────┤
       ▼ ▼ ▼
   KOBIMISA BA SERVICES YA PARTENAIRE
```

#### Likonzí 1 – Bozali membre ya base ya ofele
**Nexus Gaja Free:** Participation ya base na compréhension internationale esengeli te e dépendre soki mutu aza na mbongo. Makambo oyo elandi ekoki kosalema ofele : profil personnel, communication internationale, ba contributions, ba commentaires, traduction ya base, ba communautés, ba chats, ba fonctions ya base ya media.

#### Likonzí 2 – Ba Offres ya Premium
Ba offres ya volontaire oyo bafutaka (**Nexus Gaja Plus**). Matomba oyo ekoki kozala : ndelo ya bobateli ya monene, qualité ya media ya likolo, botindiki ya video ya molai, misala ya bobongoli oyo epanzani, masanga ya minene, misala ya ebongiseli ya kobakisa, quotas ya AI ya likolo.
**Fremium – kasi “Dark Freemium” te:** Version ya ofele ekoki kosalelama na mayele; Premium epanzani yango.

#### Likonzí ya 3 – Mabongisi
**Nexus Gaja Organization:** Ba comptes spéciaux pona ba écoles, ba universités, ba clubs, ba ONG, ba entreprises, ba municipalités, etc., na compte organisationnel central, gestion ya membre na ba fonctions ya administrateur. (Ndakisa: Eteyelo ezwaka nzela ya banakelasi ofele to na nzela ya tarif institutionnel).

#### Likonzí ya 4 – Makabo
**Fonds ya misolo ya Nexus Gaja:** Ba donateurs bakoki kopesa mbongo na bolingi na bango (makabo ya générale to oyo epesameli). 
**Piscine ya misolo na tombola:** Kosalela ofele to na mbongo ya nse ezwamaka na piscine ya makabo. Buku monene ya bopanzi misolo e assurer earmarking.
```mokanda
DONATIONS → FONDS YA NTINA → MOTEUR YA ELIGIBILITÉ → Accès gratuit / Réduction / Quota
```

#### Likonzí ya 5 – Lisungi ya bibongiseli
Ba parrains : Ba fondations, ba programmes ya financement culturel, ba programmes ya financement ya l’Etat.
**NG-FIN-002 (Lipanda):** Misolo ekoki kosomba te contrôle éditorial to technique na Nexus Gaja.

#### Likonzí ya 6 – Misala ya mombongo
Nexus Gaja ekoki kopesa ba services B2B lokola **Translation-as-a-Service (API)**, traduction professionnelle, communication organisationnelle to ba salles de conférences internationales sans ko charger alimentation normale ya usager na publicité.

### 4. Marketing ya ba données te mpe “économie ya surveillance” te .
**NG-FIN-003:** Ba données personnelles ya mosaleli ezali biloko ya Nexus Gaja te. (Koteka ba profils, ba histoires, ba données ya identité te). 
Nexus Gaja ezali te na mokano ya kozwa litomba na basaleli na yango oyo bazali kolandelama mingi mpe kokabolama na ndenge ya psychologique na ndenge ya sikisiki.

### 5. Bopanzani ya mosolo
Nexus Gaja Transparence financière: Revenu ekoki kobimisama selon ba catégories, volume ya don, ba frais ya exploitation, etc. 
**Buku ya misolo:** Makabo oyo epesameli mpo na ntina moko boye ekomami na ndenge ya comptabilité oyo ekoki kososolama (Makabo → ID ya misolo → Ntina → Solde oyo ezali → Bokabolami). Subvention croisée ezali te soki transparence ezali te.

### 6. Modèle ya financement ya prix pe solidarité
Ba prix esalemi na : orientation ya ba coûts, justice na solidarité.
**Prime ya Solidarity:** Mosaleli ya premium akoki kopona na bolingi na ye moko: “Na financer eteni ya accès ya mosaleli mosusu.” Solidarité forcée to société ya classe premium (moins respect to pire moderation mpo na ba usagers libres) elongolami.

### 7. KPI ya nkita
Tozali dépendant te na temps en ligne sans fin (nkita ya engagement manipulative te). Ba KPI na biso:
- **Indice mondial ya communication (GCI):** Boyokani boni ya boyokani ya malonga ebimaka kati ya bato oyo bawutaka na ba régions linguistiques to culturelles ndenge na ndenge?
- **Ratio ya bowumeli ya plateforme (PSR):** mosolo oyo ezongaka mbala na mbala / ba frais ya misala oyo ezongaka mbala na mbala (cible : PSR ≥ 1).

### 8. Oyo tolingi na ndenge ya polele te
Nexus Gaja ezali na misolo te na:
❌ Koteka makambo ya moto
❌ piblisite ya kala oyo esalemi na moto ye moko
❌ Kolandela bizaleli ya basaleli mpo na ntina ya piblisite
❌ Koteka ba données ya communication privée
❌ bosaleli ya ba données ya AI oyo ebombami
❌ ba serrures premium manipulatives
❌ Limite ya portée artificielle mpo na monetisation
❌ bopusi ya politiki oyo efutamaki
❌ Kosomba bikateli ya bokatikati oyo ezali na libaku malamu.

### 9. Architecture ya liboso
```mokanda
                         NEXUS GAJA NA YE
                              │
             ┌─────────────────────────────────────
             │ │ │
             ▼ ▼ ▼
          ENTERPRISE YA BA ORGANISATIONS YA BOSALELI
             │ │ │
             └────────────────────────────────────┘
                              │
                       BA SERVICES YA PLATEFORME
                              │
          ┌──────────────────── ┼───────────────────┐
          ▼ ▼ ▼
       API YA BA DONATIONS YA PREMIUM
                              │
                    ┌───────────────────┐
                    ▼ ▼
               FOND GÉNÉRAL BA FONDS RESTRICTÉES
                                        │
                                        ▼
                                  NTINA YA SOCIAL
```

### Bokuse: Mibeko ya misolo (NG-FIN) .
- **NG-FIN-001:** Nexus Gaja ezwami na misolo ya piblisite ya bonkoko te.
- **NG-FIN-002:** Lisungi ya mosolo ezali te bopusi na bokatikati to na boyangeli.
- **NG-FIN-003:** Ba données personnelles ya usager ezali biloko ya mombongo te.
- **NG-FIN-004:** Mosala ya moboko ya communication internationale esengeli kotikala accessible sans kofuta.
- **NG-FIN-005:** Ba offres premium epanzani portée ya ba services, kasi esengeli te ko dégrader dignité pe ba options ya communication ya base ya ba usagers ya ofele.
- **NG-FIN-006:** Misolo oyo epesameli etambwisami mpo na ntina moko ya sikisiki.
- **NG-FIN-007:** Makabo pe misolo etambwisami na polele pe na ndenge ya kososola.
- **NG-FIN-008:** Ba services commerciales esengeli te e affecter indépendance ya plateforme.
- **NG-FIN-009:** Esengeli kotombola nkita ya Nexus Gaja ezala na tina ya bowumeli ya mikolo milayi kasi te na monetisation maximale ya basaleli.
- **NG-FIN-010:** Esengeli structure économique e permettre libela tina social - compréhension internationale, communication internationale pe boninga entre peuples.

## API, architecture ya interface mpe ya bopanzi sango (WP 1.11.3)

Mpo na kosala ete système ezala stabilité, sécurité mpe évolutivité, Nexus Gaja elandi architecture strictement basée na API mpe oyo etambwisami na événement.

### Mibeko ya moboko
- **Accès direct na base de données te:** Ba composants e communiquer exclusivement na nzela ya ba interfaces définies (APIs to ba événements), jamais na nzela ya ba requêtes directes ya base de données oyo ewutaka na ba services misusu.
- **API Gateway:** Ba demandes nionso ya client ya libanda elekaka na API Gateway oyo esimbaka authentification, routage na limitation ya taux.
- **Abstraction ya fournisseur:** Ba services ya libanda (ba modèles ya AI, ba fournisseurs ya kofuta, ba moteurs ya traduction) esangisi na nzela ya ba couches ya abstraction. Yango epekisaka ba dépendances ya câblage dur mpe epesaka nzela na commutation flexible ya fournisseur.

### Mitindo ya bosololi
- **API synchrone (REST/HTTPS):** Esalemaka mpo na masengi ya mbala moko lokola bokɔti, paramètres ya profil to mabongoli ya semba.
- **Events asynchrones (Event Bus):** Système nerveux central ya Nexus Gaja pona ba processus découplé (e.g. `Message.Created` e déclenchaka moderation, traduction na notification asynchrone).
- **Temps réel (WebSocket):** Ba chaînes dédiées pona chat en direct na état ya type.

### Bobateli mpe bondimi
- **Modèle ya confiance zéro:** Trafic ya réseau interne ezali automatiquement confiance te; communication sensible service-à-service esengaka bondimi.
- **Idempotence & Outbox Pattern:** Ba opérations critiques (lokola ba dons to ba messages) esalemi pona kozala idempotent pona kopekisa traitement ebele pe kosalela modèle ya outbox pona ko assurer que ba événements ebunga te ata na ba transactions ya base de données.

## Modèle ya domaine MVP (WP 1.12)

![Monolith modulaire ya Nexus Gaja](biloko/img/architecture_nexus.jpg)

Nexus Gaja esalela architecture MVP oyo etambwisami na domaine strictement (ADR-025), oyo esalemi lokola monolith modulaire na ba frontières ya domaine ya polele. Structure oyo epekisaka complexité ya microservice ya liboso tout en gardant flexibilité ya ko outsource ba domaines spécifiques sima.

### Ba entités ya moboko ya technique
Architecture ekabolaka na bozindo makanisi mpo na ko assurer intégrité ya ba données mpe ko éviter ba erreurs lokola “kombo ya mosaleli = moto”:
- **Identité & Comptes:** `Moto` ≠ `Comte ya mosaleli` ≠ `Vérification ya identité`. Moto oyo a vérifié a participer na nzela ya compte moko, kasi ba entités etikalaka separate.
- **Bosololi:** `Nsango` ≠ `Bobongoli`. Nsango ya ebandeli ekoki kobongwana te; Mabongoli ezali biloko oyo ezali na boyokani.
- **Bokatikati:** `Lapolo` ≠ `Mokano ya bokatikati`. Nsango ezali kaka elembo; mokambi moko nde asalaka bolukiluki yango.
- **Misolo:** `Makabo` ≠ `Solde ya misolo`. Bafutami etiamaka na ndenge ya kobongwana te na fonds na nzela ya buku monene (buku ya mbongo).

### Ba domaines ya sujet oyo ekangami
Système ekabolami na ba domaines logique (contextes limités): Identité, Compte, Organisation, Communication, Communauté, Langue, Modération, Notification, Finances na Gouvernance. Bazali komonisa monyololo mobimba kobanda na ba acteurs ya solo (basaleli, biteyelo, ba ONG) kino na ba interactions numériques na bango.

## Ezalela ya projet
Projet ezali na phase ya architecture mpe ya planification active.
Mikano ya architecture oyo ezali kosalama ekomami na dossier `/docs`.

---

## Licence & Biloko ya mayele

> **© 2024-2026 SonnerStudio - Jan Friske Mobandisi, Nkolo, Mokambi mpe Mokeli monene ya SonnerStudio — Makoki nyonso mazali ya yo.**

**Nexus Gaja** ezali propriété intellectuelle exclusive ya **Jan Friske**, oyo ezali kosala na se ya **SonnerStudio**.

Jan Friske azali mokeli se moko, architecte mpe nkolo ya Nexus Gaja — bakisa mpe makanisi nyonso, architectures, modèles ya domaine, identité ya marque mpe mikanda oyo etali yango.

**Makoki, ndingisa to matomba ya propriété epesami te na moto ya misato** ata soki ezali bonene, esika na yango na zando to bopusi na yango na mosala ya tekiniki.

### Oyo epesami nzela TE kozanga ndingisa ya polele na mokanda:
- ❌ Kosala kopi, kobimisa to kokabola logiciel oyo to mikanda na yango
- ❌ Kobongola, kobongisa to kosala misala oyo euti na yango
- ❌ Kosalela na mombongo eteni nyonso ya Nexus Gaja
- ❌ Kosalela makambo ya ebombelo lokola **ba données ya formation pona ba systèmes AI/LLM** .
- ❌ Sous-licence to bopesi makoki na bato ya misato

### Biloko ya mayele oyo ebatelami
Ba concepts originales oyo elandi ebatelami lokola ba secrets commerciales mpe ba créations propriétaires ya Jan Friske:
- Modèle ya communication multi-couche *(Intérpretation originale / sémantique / Edition traduite)*
- Mobeko ya bokabwani ya bomoto *(moto ≠ compte ya mosaleli ≠ botalisi ya bomoto)*
- Modèle ya découplage ya message-traduction *(message ≠ traduction)*
- Cadre ya gouvernance ya moderation ya AI

### Bokutana na yango
Mpo na mituna ya licence: [github.com/SonnerStudio](https://github.com/SonnerStudio)

*“Nexus Gaja” mpe logo ya Nexus Gaja ezali bilembo ya mombongo ya Jan Friske. Kosalela nkombo to elembo ya mombongo na ndingisa te.*

➡️ Maloba ya licence mobimba na [LICENSE](LICENSE) .