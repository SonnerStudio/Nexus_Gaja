# Nexus Gaja

![Logo Nexus Gaja](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** est un réseau de communication intelligent et contextuel conçu pour révolutionner la communication mondiale.

## Objectif et vision
Dans un monde globalisé, la langue constitue souvent le plus grand obstacle. L'objectif principal de Nexus Gaja est de permettre une communication transparente, sans obstacle et contextuellement précise entre les personnes, qu'elles parlent ou non une langue commune.

Il ne s'agit pas seulement de traduire des mots de manière rigide, mais de **transférer du sens**. Nexus Gaja connecte les gens à un niveau plus profond en comprenant les nuances culturelles, régionales et contextuelles, permettant ainsi des conversations véritables et authentiques.

## Possibilités et fonctionnalités
- **Communication multimédia** : le système traite non seulement le texte, mais également l'image, l'audio et la vidéo. Cela permet des conversations totalement immersives (par exemple, des appels vidéo ou des messages vocaux) en temps réel, malgré les barrières linguistiques.
- **Sensibilité au contexte** : reconnaissance de l'ironie, des expressions idiomatiques, du jargon et des dialectes régionaux qui sont souvent mal compris par les traducteurs conventionnels.
- **Réseau multiplateforme** : sert de base aux discussions privées, aux fils de discussion (messages avec commentaires) et aux interactions de la communauté mondiale.

---

## Architecture technique (concept de base)

Le noyau technique de Nexus Gaja est un modèle de communication personnalisé strictement divisé en trois couches :

1. **Original** : L'objet de communication (message) créé par l'expéditeur reste toujours immuable.
2. **Interprétation sémantique** : Le système analyse non seulement les mots, mais aussi leur signification réelle.
3. **Représentation dans la langue cible** : l'IA crée simplement une représentation temporaire ou mise en cache de l'original pour le destinataire respectif en fonction de sa langue préférée. Les traductions n’écrasent jamais le message original.

### Dépendance du contexte
Les traductions dans Nexus Gaja ne visualisent jamais les messages de manière isolée. Le moteur considère toute la hiérarchie :
`Message` → `Messages précédents` → `Contexte du fil de discussion` → `Contexte de la communauté` → `Langue/Région` → `Préférences utilisateur`

### Efficacité grâce à la traduction à la demande
La traduction s'effectue de manière efficace en termes de ressources uniquement **sur demande** (à la demande). Lorsqu'un utilisateur demande du contenu, celui-ci est traduit dans sa langue prédéfinie. Une fois qu'une traduction pour une langue spécifique est générée, elle est stockée en permanence (mise en cache) pour accélérer considérablement les demandes futures.

## Modération assistée par l'IA (WP 1.8.4)

Avec la modération assistée par l'IA, nous franchissons une étape importante de l'idée du produit à l'architecture technique, en tenant compte des réglementations européennes en vigueur (exigences de transparence de la loi européenne sur l'IA en vertu de l'article 50 ; loi sur les services numériques avec justifications compréhensibles et possibilités de recours).

### 1. Principe de base
La phrase la plus importante pour l'architecture est : **L'IA de modération est un système de révision, pas un système de décision autonome.**
Il est conçu pour aider les humains avec modération, et non pour déterminer lui-même quelles opinions sont autorisées à exister sur Nexus Gaja.
Nous distinguons trois niveaux :
- **Détection :** "Il pourrait y avoir une violation des règles ici."
- **Évaluation :** "La probabilité d'une violation des règles est, par exemple, de 94 %."
- **Décision :** "Quelle mesure est réellement prise ?"
Le troisième niveau doit être contrôlé par un humain dans les cas graves.

### 2. L'IA de modération en tant que sous-système
Au lieu d’une seule IA, un sous-système robuste est établi :
```texte
                 MODÉRATION DE L'IA NEXUS GAJA
                          │
       ┌──────────────────┼──────────────────┐
       │ │ │
  IA de langage IA de sécurité IA de fraude
       │ │ │
       ├──────────────┬───┴──────────────┬───┤
       │ │ │
 Identité du comportement de traduction
 Signaux d'analyse d'analyse
       │ │ │
       └──────────────┼──────────────────┘
                      ▼
               Évaluation des risques
                      │
                      ▼
               Examen humain
```

### 3. Les modules d'IA les plus importants
Nexus Gaja utilise neuf domaines d'analyse spécialisés :
- **M1 – Compréhension du langage** : Détecte la langue, le dialecte, l'argot, les indicateurs d'ironie, les problèmes de traduction.
- **M2 – Détection Toxicité / Abus** : Détecte les insultes, les attaques personnelles, le harcèlement.
- **M3 – Détection des menaces** : Détecte les menaces potentielles, le chantage, les annonces de violence.
- **M4 – Détection de haine/déhumanisation** : Détecte les attaques ciblées contre des personnes en fonction d'affiliations spécifiques.
- **M5 – Détection de spam/manipulation** : Détecte le spam, le comportement des robots et les manipulations coordonnées.
- **M6 – Fraud Detection** : Détecte les tentatives de fraude suspectes, le phishing, l'ingénierie sociale.
- **M7 – Intégrité de l'identité** : Vérifie les signaux concernant les piratages de comptes, les comptes multiples, l'évasion d'interdiction.
- **M8 – Media Safety** : Analyse les images, l'audio, la vidéo, les documents.
- **M9 – Context Engine** : Le module le plus important. Il fusionne les résultats individuels.

### 4. Pourquoi le moteur contextuel est crucial
Une simple recherche par mots-clés serait insuffisante. "Je pourrais le tuer en riant" contient sémantiquement de la violence mais est une figure de style. "Demain à 20 heures, je lui tirerai dessus devant sa maison" est une situation complètement différente. L'IA doit comprendre ce que signifie la déclaration dans son contexte spécifique.

### 5. Modération multilingue
La modération ne peut pas simplement comparer les mots. Il doit analyser le niveau sémantique (par exemple, idiomes allemands, idiomes japonais et expressions régionales).

### 6. Langue originale + traduction
L'original et la traduction sont analysés séparément. Ce n'est qu'à ce moment-là qu'a lieu l'« évaluation de modération combinée ». Cela permet à Nexus Gaja de déterminer si la traduction elle-même a pu aggraver ou modifier les faits.

### 7. Score de confiance
Chaque évaluation de l'IA reçoit un score de confiance (par exemple, probabilité de menace : 0,96). Cependant : **Score de confiance ≠ Vérité.** Un score de 96 % signifie uniquement que le modèle est très certain de sa classification, pas nécessairement que l'utilisateur est coupable.

### 8. L'incertitude devient elle-même un signal
Si l’IA est incertaine (par exemple Menace : 0,62, Satire : 0,54), elle ne doit pas simplement appliquer des règles strictes. Au lieu de cela, l'incertitude est directement intégrée à l'architecture : **Examen humain requis**.

### 9. Quatre zones de décision
- 🟢 **VERT** : Très probablement conforme. → aucune action.
- 🟡 **JAUNE** : Violation possible. → surveiller / avertir si nécessaire.
- 🟠 **ORANGE** : Violation probable. → avis de modération.
- 🔴 **ROUGE** : Violation grave possible. → mesure de protection immédiate + examen humain.

### 10. Pas de « punition IA »
**L'IA n'impose aucune sanction finale.** Elle peut déclencher des mesures techniques immédiates (par exemple, retenir temporairement un message) en cas de graves problèmes de sécurité, mais la décision finale reste vérifiable.

### 11. Des mesures de protection peuvent survenir automatiquement
En cas de menace concrète (Menace détectée → Confiance élevée → Restriction temporaire → Examen humain → Décision), nous protégeons l'utilisateur menacé sans transformer l'IA en juge.

### 12. L'IA doit être capable de justifier ses décisions
Le DSA exige des raisons claires et précises. L'IA fournit un raisonnement structuré : Règle (NG-CONDUCT-004), Détecté (Menace potentielle concrète), Confiance (0,94), Contexte pertinent (4 messages précédents), Action recommandée (Revue humaine).

### 13. L'IA ne doit pas modifier secrètement le contenu
**L'IA de modération ne doit jamais modifier le contenu original sans que cela soit remarqué.** Lors d'une correction automatique, d'une traduction ou d'un résumé, l'original est toujours préservé.

### 14. Contenu généré par l'IA
Nous faisons la distinction entre : créé par l'homme, assisté par l'IA, généré par l'IA et manipulé par l'IA. Cela fera partie des métadonnées du contenu.

### 15. Étiquetage du contenu IA et de la couche de provenance IA
Selon les règles de transparence de la loi européenne sur l’IA (en vigueur en août 2026), le contenu généré par l’IA doit être identifiable. Nous fournissons une couche de provenance AI qui stocke les métadonnées (AI-Origin, Model, Timestamp, Human Review).

### 16. Détection des deepfakes
L'architecture vise à détecter les images synthétiques, les voix clonées et les deepfakes. Cependant, la détection ne constitue pas automatiquement une preuve.

### 17. Pas de « machine à vérité » automatique (modération ≠ vérification des faits)
Un système vérifie : « Le contenu enfreint-il les règles ? » (Modération du contenu), un autre précise : « Quelles informations et sources sont disponibles ? (Aide à l'information). Les opinions ne sont pas simplement supprimées parce qu’elles sont « fausses ».

### 18. Protection contre les interprétations culturelles erronées
L'IA nécessite des **Modèles de contexte culturel** pour éviter que les normes de communication d'un pays ne soient considérées comme une norme mondiale.

### 19. Ironie, satire et humour
L’IA utilise le contexte, les émojis, l’historique des conversations et les structures ironiques connues, mais doit tenir compte de l’incertitude lorsque les significations sont ambiguës.

### 20. Aucune punition basée sur un seul score d'IA
Aucune intervention de modération sévère ne peut être basée uniquement sur un seul résultat de classification automatisée (Texte + Contexte + Comportement + Langue + Média + Moteur de règles = Évaluation des risques).

### 21. Signaux de comportement des utilisateurs et absence de système de crédit social
Cela concerne les signaux techniques d'abus (par exemple, la publication massive de spam), et non un système général de notation sociale. Nexus Gaja ne maintient pas de système de crédit social – la modération sert la sécurité et non l'évaluation de la valeur d'une personne.

### 22. L'IA de modération doit être auditable
Toutes les décisions automatisées pertinentes sont enregistrées (Event-ID, Rule-ID, Confidence, Human-Review, etc.) pour garantir la traçabilité.

### 23. Faux positifs, faux négatifs et mesures de qualité
Les types d'erreurs sont surveillés. Un tableau de bord mesure la précision, le rappel et surtout le **taux d'annulation des appels** (nombre d'appels réussis).

### 24. Équité linguistique et biais en matière de traduction
La qualité de la modération doit être comparable dans toutes les langues prises en charge (Multilingual Moderation Benchmark). Si les résultats de la modération diffèrent entre l'original et la traduction (Conflit de traduction), cela doit être spécifiquement examiné.

### 25. Proposition d'architecture et moteur de politique
Les règles (Policy Engine) ne sont pas codées en dur dans les modèles d'IA. L'IA fournit des résultats ; le moteur de politique décide en fonction des règles en vigueur. Cela permet de **modifier le modèle sans modifier les règles**.

### 26. L'humain reste l'autorité finale
- **NG-AI-MOD-001** : L'IA aide à la détection et à la classification, mais ne remplace pas l'examen humain dans les décisions sévères.
- **NG-AI-MOD-002** : les décisions de modération automatisées doivent être traçables, consignées et vérifiables.

**Résumé** : Nous construisons un système en quatre étapes : détection de l'IA, analyse du contexte et des risques, moteur de politiques et gouvernance humaine. Cela permet une forte automatisation sans créer une architecture dangereuse « IA comme juge ».

## Principes de financement et modèle de revenus (WP 1.10.1)

Pour Nexus Gaja, un principe économique très important s'applique : **Pas de publicité traditionnelle au sein de la plateforme.**
Cela distingue fondamentalement Nexus Gaja de la plupart des réseaux sociaux actuels. Toutefois, cela ne signifie pas que Nexus Gaja ne peut pas avoir un caractère commercial. Au contraire, la plateforme doit être économiquement viable pour que sa finalité sociale puisse perdurer. L’activité économique est un moyen pour parvenir à une fin, et non l’objectif principal de la plateforme.

### 1. Principe NG-FIN-001
Nexus Gaja finance ses opérations grâce à des flux de revenus transparents, séparés des intérêts des utilisateurs, et non par la monétisation de l'attention ou des données personnelles de ses utilisateurs.

### 2. Pas de publicité traditionnelle
Sont spécifiquement interdits :
- Bannières publicitaires
- Annonces pop-up
- Annonces vidéo à lecture automatique
- Posts sponsorisés dans le flux standard
- Profils publicitaires personnalisés
- Vente de profils d'utilisateurs ou de données personnelles
- Publicité issue de conversations privées.

Nexus Gaja reste un **espace de communication plutôt qu'un espace publicitaire**.

### 3. Financement sans publicité (Les 6 piliers)
Le financement repose sur six piliers :
```texte
                 NEXUS GAJA
                     │
       ┌─────────────┼─────────────┐
       ▼ ▼ ▼
   DONS AUX ORGANISMES PREMIUM
       │ │ │
       ├─────────────┼─────────────┤
       ▼ ▼ ▼
    SUBVENTIONS, PARTENARIATS SERVICES
```

#### Pilier 1 – Adhésion de base gratuite
**Nexus Gaja Free** permet à tous une compréhension internationale de base (profil, communication internationale, publications, communautés, chats, traduction de base) sans frais.

#### Pilier 2 – Offres Premium
Offres payantes volontaires (**Nexus Gaja Plus**) offrant des limites de stockage plus élevées, une qualité multimédia supérieure, des quotas d'IA étendus et des fonctionnalités d'organisation.
**Important (Freemium au lieu de Dark Freemium) :** La communication de base ne doit jamais être artificiellement dégradée.

#### Pilier 3 – Organisations
Comptes spéciaux pour les écoles, universités, ONG, entreprises et municipalités (**Nexus Gaja Organization**). Les écoles peuvent être soutenues via des tarifs institutionnels en tant que multiplicateurs de compréhension internationale.

#### Pilier 4 – Dons
Le **Nexus Gaja Funding Pool** accepte les dons généraux et réservés (par exemple, « pour la communication internationale auprès des jeunes »). Un **Ledger d'allocation de fonds** garantit une allocation transparente des fonds.
**Purpose Fund & Tombola :** Une partie des dons alimente un pool pour une utilisation gratuite/à prix réduit. Un mécanisme de loterie/tombola peut allouer ces fonds de manière transparente et vérifiable.

#### Pilier 5 – Financement institutionnel
Fondations, programmes de financement culturel ou programmes étatiques.
**NG-FIN-002 :** Le soutien financier n'achète pas de contrôle éditorial ou technique (Indépendance).

#### Pilier 6 – Services commerciaux
Des services B2B tels que la **Translation-as-a-Service** (API), la communication organisationnelle ou les salles de conférence internationales, sans alourdir le flux utilisateur standard.

### 4. Pas d'économie de monétisation et de surveillance des données
**NG-FIN-003 :** Les données personnelles des utilisateurs ne sont pas une marchandise. Pas de vente de listes, profils ou historiques. Nexus Gaja ne bénéficie pas de surveillance psychologique (Surveillance Economy).

### 5. Transparence financière et registre des fonds
**Transparence financière Nexus Gaja :** Publication des structures financières agrégées. Les dons affectés font l'objet d'une comptabilité technique (ID du fonds → Objet → Solde → Allocation). Pas de subvention croisée d’objectifs sociaux dans le marketing d’entreprise.

### 6. Modèle de financement solidaire
La tarification est basée sur l’orientation vers les coûts, l’équité et la solidarité.
**Prime Solidaire :** Une option volontaire permettant aux utilisateurs Premium de financer une partie de l'accès d'un autre utilisateur. La solidarité forcée ou une société de classe premium (moins de respect/modération pour les utilisateurs gratuits) est strictement interdite.

### 7. Des KPI économiques au lieu d'une économie d'engagement
Aucune dépendance quant au maintien des utilisateurs « en ligne aussi longtemps que possible » (pas de ragebait, de flux infinis).
Au lieu de cela, nous utilisons des métriques telles que :
- **Global Communication Index (GCI) :** Relations de communication réussies entre des personnes de différentes régions linguistiques/culturelles.
- **Ratio de durabilité de la plateforme (PSR) :** Revenus récurrents / coûts opérationnels récurrents (Cible ≥ 1).

### 8. Ce que nous ne voulons explicitement pas (liste négative)
Nexus Gaja n'est **pas** financé par :
❌ Vente de données personnelles
❌ Publicité traditionnelle personnalisée
❌ Surveillance du comportement des utilisateurs à des fins publicitaires
❌ Vente de données de communication privées
❌ Utilisation des données cachées de l'IA
❌ Paywalls manipulateurs Premium
❌ Restriction artificielle de la portée pour la monétisation
❌ Influence politique rémunérée
❌ Achat de décisions de modération privilégiées.

### 9. Architecture financière préliminaire
```texte
                         NEXUS GAJA
                              │
             ┌────────────────┼────────────────┐
             │ │ │
             ▼ ▼ ▼
          ENTREPRISE ORGANISATIONS D'UTILISATEURS
             │ │ │
             └────────────────┼────────────────┘
                              │
                       SERVICES DE PLATEFORME
                              │
          ┌─────────────────── ┼───────────────────┐
          ▼ ▼ ▼
       API DE DONS PREMIUM
                              │
                    ┌─────────┴─────────┐
                    ▼ ▼
               FONDS GÉNÉRAL FONDS RESTREINTS
                                        │
                                        ▼
                                  OBJECTIF SOCIAL
```

### Résumé des principes de financement (NG-FIN)
- **NG-FIN-001 :** Aucun financement via la publicité traditionnelle.
- **NG-FIN-002 :** Aucun contrôle éditorial/technique via un soutien financier.
- **NG-FIN-003 :** Les données personnelles ne sont pas une marchandise.
- **NG-FIN-004 :** La communication de base reste accessible sans paiement.
- **NG-FIN-005 :** Les offres Premium ne doivent pas dégrader les utilisateurs gratuits.
- **NG-FIN-006 :** Les fonds affectés sont gérés en fonction de leur destination.
- **NG-FIN-007 :** Gestion transparente des dons et subventions.
- **NG-FIN-008 :** Les services commerciaux B2B ne compromettent pas l'indépendance.
- **NG-FIN-009 :** Concentrez-vous sur la durabilité plutôt que sur la monétisation maximale.
- **NG-FIN-010 :** La structure sécurise en permanence la finalité sociale.

## Statut du projet
Le projet est actuellement en phase active d’architecture et de planification.
Les décisions architecturales en cours sont documentées dans le dossier `/docs`.