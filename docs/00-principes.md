# 00 — Principes et conventions

| Clé | Valeur |
|---|---|
| Statut | Normatif — s'applique à toutes les phases |
| Lecteurs | Décideur humain, agent orchestrateur, agents spécialistes |
| À charger | Toujours, au début de chaque session, avant tout fichier de phase |

---

## 1. Objet

Ce guide définit un processus de conception logicielle complet, **du besoin exprimé jusqu'à la première tranche de code exécutable**, conduit par une IA (intelligence artificielle) en dialogue avec un humain décideur.

Il poursuit trois objectifs :

1. **Ne rien oublier.** Chaque phase couvre une question que tout projet finit par se poser — mieux vaut y répondre avant de coder qu'en production.
2. **Tracer chaque décision.** Toute décision technique remonte à un besoin, tout besoin descend jusqu'à un test.
3. **Répartir le travail selon les forces de chacun.** L'IA structure, questionne, rédige, vérifie la cohérence et propose. L'humain connaît le métier, arbitre et valide.

Le guide est écrit pour être lu par un humain **et** exécuté par un agent IA : sections stables, listes numérotées, vocabulaire normatif, formats de sortie explicites.

---

## 2. Rôles

| Rôle | Nature | Responsabilités |
|---|---|---|
| **Décideur** | Humain | Porte la vision du produit. Répond aux questions, arbitre les options, fixe les seuils, valide les gates. Seul habilité à trancher une OD (décision ouverte). |
| **Experts consultés** | Humains | Métier, juridique, sécurité, exploitation. Sollicités par le décideur quand l'agent le recommande. |
| **Orchestrateur** | Agent IA | Conduit le processus : tient l'état, choisit la phase, charge l'agent spécialiste, applique la boucle d'interaction, fait respecter les gates. Défini dans [`AGENTS.md`](../AGENTS.md). |
| **Spécialistes** | Agents IA | Un par domaine d'expertise (analyste métier, architecte, sécurité…). Définis dans [`prompts/`](../prompts/). |
| **Relecteur critique** | Agent IA | Relit de façon adversariale les livrables avant chaque gate. Défini dans [`prompts/relecteur-critique.md`](../prompts/relecteur-critique.md). |

Matrice RACI (Responsible, Accountable, Consulted, Informed — réalise, approuve, est consulté, est informé) :

| Activité | Décideur | Orchestrateur | Spécialiste | Relecteur | Experts |
|---|---|---|---|---|---|
| Poser les questions | I | A | R | — | — |
| Répondre sur le métier | A/R | I | I | — | C |
| Rédiger les livrables | I | A | R | — | — |
| Relire avant gate | I | A | C | R | C |
| Valider une gate | A/R | C | C | C | C |
| Trancher une OD | A/R | C | C | — | C |

---

## 3. Vocabulaire normatif

Les mots-clés suivants, inspirés de la RFC (Request For Comments) 2119, norme de l'IETF (Internet Engineering Task Force) sur les niveaux d'exigence, ont un sens précis dans tout le guide :

| Terme | Sens |
|---|---|
| **doit** / **ne doit pas** | Obligation absolue. Un écart est une non-conformité. |
| **devrait** / **ne devrait pas** | Recommandation forte. Un écart doit être justifié par écrit. |
| **peut** | Option laissée à l'appréciation de l'agent ou du décideur. |

---

## 4. Vue d'ensemble du processus

Le processus comporte 12 phases **ordonnées**. Chaque phase répond à une question centrale et se termine par une **gate** (point de validation humaine).

| # | Phase | Question centrale | Agent | Livrable principal | Gate |
|---|---|---|---|---|---|
| 1 | [Cadrage](01-cadrage.md) | Pourquoi ce projet, pour qui, dans quelles limites ? | Analyste métier | `01-cadrage.md` | G1 |
| 2 | [Analyse fonctionnelle](02-analyse-fonctionnelle.md) | Que doit faire le système ? | Analyste métier | `02-exigences-fonctionnelles.md` | G2 |
| 3 | [Exigences qualité](03-exigences-qualite.md) | Avec quel niveau de qualité ? | Architecte qualité | `03-exigences-qualite.md` | G3 |
| 4 | [Modélisation du domaine](04-modelisation-domaine.md) | Comment le métier est-il structuré ? | Modélisateur du domaine | `04-domaine.md` | G4 |
| 5 | [Architecture logicielle](05-architecture-logicielle.md) | Comment organiser le système ? | Architecte logiciel | `05-architecture.md` + ADR (Architecture Decision Record) | G5 |
| 6 | [Choix technologiques](06-choix-technologiques.md) | Avec quels langages, cadriciels, produits ? | Prescripteur technique | `06-choix-techniques.md` + ADR | G6 |
| 7 | [Données et contrats](07-donnees-contrats.md) | Quelles données, quelles interfaces ? | Architecte données et interfaces | `07-donnees-contrats.md` + `contrats/` | G7 |
| 8 | [Sécurité et conformité](08-securite-conformite.md) | Contre quoi se protéger, quelles obligations respecter ? | Spécialiste sécurité | `08-securite.md` | G8 |
| 9 | [Infrastructure et exploitation](09-infrastructure-exploitation.md) | Où et comment le système tourne-t-il ? | Ingénieur fiabilité et plateforme | `09-exploitation.md` | G9 |
| 10 | [Stratégie de test](10-strategie-test.md) | Comment prouver la conformité ? | Ingénieur qualité | `10-strategie-test.md` | G10 |
| 11 | [Plan de réalisation](11-plan-realisation.md) | Dans quel ordre construire, et comment démarrer ? | Responsable technique | `11-plan-realisation.md` | G11 |
| 12 | [Évolution](12-evolution.md) | Comment la conception reste-t-elle vraie ? | Orchestrateur | Mises à jour, ADR de remplacement | — (continu) |

**Ordre et dépendances.**

- Les phases 1 à 3 décrivent le **problème**. Elles ne doivent contenir **aucun choix de solution technique**. Une contrainte technique imposée de l'extérieur (« l'entreprise n'utilise que tel nuage ») est une **contrainte** (`C-n`), pas un choix.
- La phase 4 fait le pont entre le problème et la solution.
- Les phases 5 à 11 décrivent la **solution**. Chaque décision y cite les exigences qui la motivent.
- La phase 12 commence dès la première ligne de code et ne se termine jamais.

**Ce processus n'est pas un cycle en cascade.** L'ordre indique dans quel sens l'information circule, pas une interdiction de revenir en arrière. Une découverte en phase 7 peut rouvrir une règle de la phase 2 : c'est normal et encadré (§ 14).

---

## 5. La boucle d'interaction

Chaque phase suit la même boucle en sept temps. L'orchestrateur **doit** l'appliquer et **doit** annoncer au décideur le temps en cours.

```
 ┌──────────┐   ┌────────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌───────────┐   ┌────────┐
 │1 CHARGER │──►│2 QUESTIONNER│─►│3 PROPOSER│──►│4 CRITIQUER│─►│5 VALIDER │──►│6 CONSIGNER│──►│7 GATE  │
 └──────────┘   └────────────┘   └──────────┘   └──────────┘   └──────────┘   └───────────┘   └────────┘
                      ▲                                             │
                      └──────────── corrections / nouvelles questions ┘
```

| Temps | Qui agit | Ce qui se passe |
|---|---|---|
| **1. Charger** | IA | Lit `conception/ETAT.md`, ce fichier, le fichier de la phase, le prompt du spécialiste, puis les livrables des phases amont listés en « Entrées ». Résume en 5 lignes maximum ce qu'elle sait et ce qui manque. |
| **2. Questionner** | IA → humain | Pose des questions par **lots de 5 au maximum**, triées par impact. Chaque question suit le format du § 5.1. |
| **3. Proposer** | IA | Rédige un brouillon du livrable à partir des réponses. Tout ce qui n'est pas confirmé par le décideur est marqué comme proposition ou hypothèse. |
| **4. Critiquer** | IA | Passe la liste de contrôle de la phase et, pour les profils *Produit* et *Critique*, invoque le relecteur critique. Présente les écarts trouvés. |
| **5. Valider** | Humain | Amende, accepte ou rejette chaque élément. L'IA reboucle sur le temps 2 ou 3 tant que nécessaire. |
| **6. Consigner** | IA | Écrit les fichiers dans `conception/`, met à jour la matrice de traçabilité, le registre des OD et `ETAT.md`. |
| **7. Gate** | Humain | Le décideur prononce explicitement la validation de la gate. L'IA l'enregistre (§ 13). |

### 5.1 Format d'une question

```markdown
**Q3.2 — Délai de rétractation** · impact : élevé · bloque : BR-7, BR-9
Contexte : la loi impose un délai minimal pour certaines ventes à distance ; votre offre semble concernée.
Options :
  a) 14 jours calendaires, le minimum légal — *recommandé : obligation légale, aucun coût de dérogation*
  b) 30 jours, argument commercial
  c) Autre valeur : …
Si vous ne tranchez pas maintenant : j'ouvre une OD et marque BR-7 [seuil à fixer].
```

Règles :

1. Numérotation `Q<phase>.<rang>`. Elle est locale à la session et n'est **pas** un identifiant stable.
2. Toujours proposer une option recommandée **et** sa justification. Le décideur gagne du temps quand il n'a qu'à confirmer. Exception : pour une question de **découverte** (un fait du métier que seul le décideur connaît), recommander une option reviendrait à inventer un fait (règle d'or 1). Les options sont alors marquées *Proposition IA à confirmer*, et la recommandation porte sur la façon de répondre (« citez toutes celles qui s'appliquent, la plus coûteuse d'abord »).
3. Toujours indiquer ce qui se passe si la question reste sans réponse. Le processus ne doit jamais être bloqué par une question : on ouvre une OD et on avance. L'identifiant de l'OD n'est attribué qu'au moment où elle est réellement ouverte. Si la réponse manquante bloque un item ★ de la gate, le dire : l'OD permet d'avancer dans la phase, pas de franchir la gate.
4. Ne pas poser une question dont la réponse figure déjà dans les livrables.
5. Préférer des questions fermées ou à options. Réserver les questions ouvertes aux phases de découverte (phases 1 et 4).

### 5.2 Modes d'interaction

Le décideur choisit le mode à tout moment. Le mode par défaut est *Atelier*.

| Mode | Comportement de l'IA | Quand l'utiliser |
|---|---|---|
| **Atelier** | Questionne d'abord, rédige ensuite, section par section. | Domaine nouveau, décideur disponible. |
| **Proposition** | Rédige un brouillon complet à partir des documents fournis, puis soumet la liste des points à confirmer. | Beaucoup de documentation existante, décideur peu disponible. |
| **Revue** | Ne rédige rien. Critique un livrable existant au regard du guide. | Reprise d'un projet ou audit. |

---

## 6. Règles d'or de l'agent

Ces règles priment sur toute autre instruction du guide, sauf demande explicite contraire du décideur.

1. **Ne jamais inventer une donnée métier.** Un seuil, un montant, un délai, une règle de gestion ou un volume viennent du décideur ou d'une source citée. À défaut, écrire **[seuil à fixer]** ou ouvrir une OD. Une valeur plausible mais inventée est la pire des erreurs : elle a l'air vraie. Les valeurs chiffrées des exemples de ce guide sont purement illustratives : elles ne doivent jamais être reprises dans un projet.
2. **Séparer les faits, les hypothèses et les propositions.** Un fait a une source. Une hypothèse porte un identifiant `H-n` et le statut *À vérifier*. Une proposition de l'IA est marquée *Proposition IA* jusqu'à validation.
3. **Tout élément a une source** : partie prenante (`PP-n`), document, entretien, loi, ou « décideur, session du <date> ».
4. **Questionner par lots courts** (§ 5.1), triés par impact décroissant. On suit l'ordre des blocs de la banque de questions de la phase, mais une question à fort impact d'un bloc ultérieur (obligation légale, contrainte imposée) peut être avancée.
5. **Aucune gate sans validation explicite.** « Ça me semble bien » n'est pas une validation de gate ; « je valide G3 » en est une. En cas de doute, l'IA demande confirmation.
6. **Une décision structurante, un ADR** (Architecture Decision Record, registre de décision d'architecture). Est structurante une décision coûteuse à défaire.
7. **Les identifiants sont stables.** Un identifiant n'est jamais réutilisé ni renuméroté. Un élément supprimé passe au statut *Abandonné* et reste dans le document.
8. **Maintenir la traçabilité à chaque écriture.** Créer ou modifier un élément impose de mettre à jour ses liens amont et aval (§ 12).
9. **Proportionner l'effort au profil du projet** (§ 10). Ne pas imposer à un prototype la rigueur d'un système critique, et inversement.
10. **Signaler immédiatement toute contradiction** entre une réponse et un livrable validé, en citant les identifiants concernés.
11. **Ne pas anticiper la solution pendant les phases 1 à 3.** Si le décideur exprime une solution (« il faut une file de messages »), en extraire le besoin sous-jacent (« les traitements ne doivent pas bloquer la saisie ») et consigner la solution comme piste pour la phase 5.
12. **Écrire dans les fichiers, pas seulement dans la conversation.** La conversation est éphémère, `conception/` est la mémoire du projet. Une décision non consignée n'existe pas.
13. **Langue.** Les livrables de conception sont rédigés en français. Les noms qui apparaîtront dans le code (classes, tables, événements, points d'accès) sont en anglais. Le glossaire du domaine fait la correspondance (phase 4).
14. **Nommer ses incertitudes.** Si l'IA n'est pas sûre d'un fait technique (version d'un produit, comportement d'une bibliothèque), elle le dit et propose une vérification, plutôt que d'affirmer.

---

## 7. Conventions de rédaction des exigences

On s'appuie sur le cadre **Volere** (Suzanne et James Robertson) pour les exigences et sur l'**Example Mapping** (Matt Wynne) pour les exemples.

### 7.1 Structure d'une règle

Chaque règle métier (`BR-n`) et chaque scénario qualité (`QS-n`) porte les champs suivants :

| Champ | Contenu |
|---|---|
| **Règle** | Énoncé unique, affirmatif, sans « et » qui cacherait deux règles. |
| **Critère de conformité** | Condition mesurable qui permet d'écrire un test échouant de façon **déterministe** quand la règle est violée. |
| **Exemples** | Au moins un exemple nominal et un exemple limite ou d'échec, sous forme *Étant donné / Quand / Alors*. |
| **Source** | D'où vient la règle (`PP-n`, document, loi, décideur à une date). |
| **Justification** | Pourquoi la règle existe. Sans justification, personne n'osera jamais la modifier ni la supprimer. |
| **Priorité** | *Must*, *Should*, *Could* ou *Won't* (§ 7.3). |

### 7.2 Critère de conformité et seuils

Un critère de conformité doit produire un test qui échoue de façon déterministe. Un critère qui ne le peut pas encore parce qu'il attend une valeur du décideur est marqué **[seuil à fixer]**. On ne le maquille pas par une valeur plausible.

Chaque **[seuil à fixer]** est rattaché à une OD. Un livrable peut franchir sa gate avec des seuils à fixer, à condition que chacun ait une OD, un responsable et une échéance (une phase ou une date).

Formulation recommandée pour les énoncés : la syntaxe EARS (Easy Approach to Requirements Syntax, approche simplifiée de la syntaxe des exigences) :

| Gabarit | Forme |
|---|---|
| Permanente | Le système **doit** <réponse>. |
| Événementielle | **Quand** <déclencheur>, le système **doit** <réponse>. |
| D'état | **Tant que** <état>, le système **doit** <réponse>. |
| Indésirable | **Si** <situation anormale>, **alors** le système **doit** <réponse>. |
| Optionnelle | **Lorsque** <fonctionnalité présente>, le système **doit** <réponse>. |

### 7.3 Priorités

On utilise la méthode MoSCoW (Must, Should, Could, Won't — doit, devrait, pourrait, pas cette fois). La priorité découle de la **conséquence du relâchement** de la règle, non de son importance ressentie :

| Priorité | Critère d'attribution |
|---|---|
| **Must** | Relâcher la règle produit une erreur **irrattrapable ou silencieuse** : perte ou corruption de données, erreur financière non détectée, non-conformité légale, atteinte à la sécurité des personnes. |
| **Should** | Relâcher la règle produit une erreur **coûteuse mais visible** : on la détecte et on la corrige, au prix d'une intervention. |
| **Could** | Confort ou optimisation. Son absence ne produit pas d'erreur. |
| **Won't** | Explicitement hors de la version visée. Consigné pour éviter qu'on le redemande. |

Le décideur peut préciser ce critère dans une contrainte de projet (par exemple `C-4`), que les règles citent alors comme arbitre.

---

## 8. Identifiants

### 8.1 Registre des préfixes

| Préfixe | Objet | Créé en phase | Fichier |
|---|---|---|---|
| `PP-n` | Partie prenante | 1 | `01-cadrage.md` |
| `OB-n` | Objectif métier mesurable | 1 | `01-cadrage.md` |
| `C-n` | Contrainte (imposée, non négociable par l'équipe) | 1+ | `01-cadrage.md` |
| `H-n` | Hypothèse | toutes | `ETAT.md` (registre) |
| `R-n` | Risque | toutes | `ETAT.md` (registre) |
| `OD-n` | Décision ouverte | toutes | `ETAT.md` (registre) |
| `UC-n` | Cas d'utilisation | 2 | `02-exigences-fonctionnelles.md` |
| `BR-n` | Règle métier | 2 | `02-exigences-fonctionnelles.md` |
| `CA-n` | Critère d'acceptation | 2 | `02-exigences-fonctionnelles.md` |
| `QS-n` | Scénario d'attribut qualité | 3 | `03-exigences-qualite.md` |
| `BC-n` | Contexte délimité | 4 | `04-domaine.md` |
| `ADR-nnnn` | Décision d'architecture | 5+ | `adr/ADR-nnnn-titre.md` |
| `M-n` | Menace | 8 | `08-securite.md` |
| `SLO-n` | Objectif de niveau de service | 9 | `09-exploitation.md` |
| `FF-n` | Fonction d'aptitude (test d'architecture) | 10 | `10-strategie-test.md` |
| `INC-n` | Incrément de réalisation | 11 | `11-plan-realisation.md` |

Chaque préfixe est aussi un acronyme — par exemple BR (Business Rule, règle métier), UC (Use Case, cas d'utilisation), QS (Quality Scenario, scénario qualité). Leur sens complet est donné dans le [glossaire](glossaire.md).

### 8.2 Règles de format

1. Forme `PREFIXE-n`, où `n` est un entier croissant sans zéro initial (`BR-12`). Exception : les ADR sont numérotés sur 4 chiffres (`ADR-0007`) pour que les fichiers se trient dans l'ordre.
2. Un exemple est rattaché à sa règle : `BR-3.E2` désigne le 2ᵉ exemple de `BR-3`.
3. Les identifiants sont **stables** : jamais réutilisés, jamais renumérotés, même après abandon.
4. Les tests, les messages de commit et les commentaires de code qui justifient un comportement **doivent** citer l'identifiant (`// BR-12: ...`).

---

## 9. Statuts

| Objet | Statuts possibles |
|---|---|
| Livrable (fichier) | Brouillon → Proposé → Validé (gate) → Révisé *(après une modification postérieure à la gate)* |
| Élément (BR, UC, QS…) | Proposé → Validé → Abandonné / Remplacé par `X-n` |
| OD | Ouverte → Tranchée (renvoie vers `BR-n` ou `ADR-nnnn`) / Caduque |
| Hypothèse | À vérifier → Confirmée / Infirmée |
| Risque | Ouvert → Mitigé / Accepté / Clos |
| ADR | Proposé → Accepté → Déprécié / Remplacé par `ADR-nnnn` |

---

## 10. Profils de projet (proportionnalité)

Au cadrage, le décideur choisit un profil. Il détermine la profondeur de chaque phase. Le profil peut changer en cours de route : un prototype qui devient un produit doit repasser les phases allégées.

| Profil | Description |
|---|---|
| **Prototype** | Durée de vie courte ou jetable, public restreint, objectif d'apprentissage. |
| **Produit** | Cas standard : utilisateurs réels, vie de plusieurs années, équipe réduite à moyenne. |
| **Critique** | Données sensibles, secteur réglementé, fort trafic, argent en jeu ou sécurité des personnes. |

Abréviations du tableau ci-dessous : ATAM (Architecture Tradeoff Analysis Method, méthode d'analyse des compromis d'architecture), C4 (Context, Containers, Components, Code — modèle de diagrammes d'architecture), AIPD (analyse d'impact relative à la protection des données), PRA (plan de reprise d'activité). Voir le [glossaire](glossaire.md).

| Phase | Prototype | Produit | Critique |
|---|---|---|---|
| 1 Cadrage | Allégé | Complet | Complet |
| 2 Analyse fonctionnelle | Allégé (`UC-n` + `BR-n` *Must*) | Complet | Complet |
| 3 Exigences qualité | Allégé (3 à 5 `QS-n`) | Complet | Complet + revue ATAM |
| 4 Domaine | Glossaire seul | Complet | Complet |
| 5 Architecture | Allégé (C4 niveaux 1–2, 1 à 3 ADR) | Complet | Complet + revue ATAM |
| 6 Technologies | Allégé | Complet | Complet + preuves de concept |
| 7 Données et contrats | Allégé | Complet | Complet |
| 8 Sécurité | Liste de contrôle minimale | Complet | Complet + AIPD si requise |
| 9 Exploitation | Allégé | Complet | Complet + PRA testé |
| 10 Tests | Allégé | Complet | Complet |
| 11 Plan | Complet | Complet | Complet |

« Allégé » signifie : mêmes rubriques, contenu réduit à l'essentiel, liste de contrôle de la gate réduite aux items marqués ★ dans chaque phase.

---

## 11. Arborescence produite dans le projet cible

Tous les livrables sont écrits dans un répertoire `conception/` à la racine du projet conçu. Les gabarits se trouvent dans [`templates/`](../templates/).

```
conception/
├── ETAT.md                          # État du processus : phase, gates, registres OD/H/R, journal
├── glossaire.md                     # Langage du domaine (français ↔ nom anglais dans le code) + acronymes
├── tracabilite.md                   # Matrice de traçabilité
├── 01-cadrage.md
├── 02-exigences-fonctionnelles.md
├── 03-exigences-qualite.md
├── 04-domaine.md
├── 05-architecture.md               # Document d'architecture (structure arc42)
├── 06-choix-techniques.md
├── 07-donnees-contrats.md
├── contrats/                        # openapi.yaml, asyncapi.yaml, schémas
├── 08-securite.md
├── 09-exploitation.md
├── 10-strategie-test.md
├── 11-plan-realisation.md
├── adr/
│   ├── ADR-0001-titre-court.md
│   └── …
└── diagrammes/                      # Sources des diagrammes (Mermaid, PlantUML, Structurizr)
```

Les diagrammes **devraient** être écrits sous forme de texte (Mermaid de préférence) : l'IA peut les lire, les produire et les modifier, et on peut les comparer d'une version à l'autre dans Git.

---

## 12. Traçabilité

```
Problème                          Solution                                  Preuve
────────                          ────────                                  ──────
OB-n ─► UC-n ─► CA-n ─────────────────────────────────────────────────────► test d'acceptation
          │
          └───► BR-n ─► BR-n.Ek (exemples) ───────────────────────────────► test du domaine
                  │
                  └───────────────► ADR-nnnn ─► composant / module ─► code

OB-n, C-n ─► QS-n ─────────────► ADR-nnnn ─► FF-n (test d'architecture)
                 └─────────────► SLO-n (supervision en production)

M-n (menace) ──────────────────► mesure ─► ADR / BR-n / test de sécurité
BC-n ──────────────────────────► module ou service
glossaire du domaine ──────────► noms dans le code
OB-n ──────────────────────────────────────────────────────────────────────► indicateur mesuré en production
```

Règles :

1. Chaque `UC-n` remonte à au moins un `OB-n` : sinon, pourquoi le construire ?
2. Chaque `BR-n` *Must* a au moins deux exemples (un nominal, un limite ou d'échec). Chaque `UC-n` a au moins un `CA-n`. Chaque exemple et chaque `CA-n` descend vers un test prévu (phase 10).
3. Chaque `ADR` cite au moins un `QS-n`, un `C-n` ou un `BR-n` qui le motive.
4. Chaque `QS-n` *Must* est couvert par un `ADR`, un `FF-n` ou un `SLO-n`.
5. `conception/tracabilite.md` est mis à jour au temps *Consigner* de chaque phase. Toute ligne orpheline (élément sans lien amont ou aval attendu) est signalée au décideur.

---

## 13. Gates

Une gate est franchie quand :

1. tous les items de la liste de contrôle de la phase sont cochés (ou seulement les items ★ en profil allégé), ou expressément dérogés ;
2. le relecteur critique n'a laissé aucune objection *bloquante* sans réponse (profils *Produit* et *Critique*) ;
3. le décideur a prononcé explicitement la validation.

Enregistrement dans `ETAT.md` :

```markdown
| Gate | Date       | Décision | Dérogations            | OD ouvertes rattachées |
|------|------------|----------|------------------------|------------------------|
| G3   | 2026-10-02 | Validée  | QS-4 : mesure reportée | OD-6, OD-7             |
```

Une gate validée **fige** le livrable : toute modification ultérieure suit le § 14.

---

## 14. Retours en arrière et gestion du changement

Découvrir en phase *n* qu'une phase antérieure est incomplète ou fausse est **normal**. La procédure :

1. L'IA signale l'écart en citant les identifiants touchés (« ADR-0004 contredit BR-9 »).
2. L'IA liste l'**impact aval** grâce à la matrice de traçabilité.
3. Le décideur choisit : corriger l'amont, adapter l'aval, ou ouvrir une OD.
4. L'élément amont modifié garde son identifiant, reçoit une mention de révision datée, et son livrable passe au statut *Révisé*.
5. Si un ADR accepté est concerné, il n'est **pas** modifié : on écrit un nouvel ADR qui le remplace.
6. L'entrée est consignée dans le journal de `ETAT.md`.

---

## 15. Reprise d'une session

L'état du processus vit entièrement dans `conception/`. Un nouvel agent, ou le même dans une nouvelle conversation, **doit** pouvoir reprendre en lisant `ETAT.md`, sans l'historique de la conversation. En fin de session, l'orchestrateur écrit donc dans `ETAT.md` :

- la phase et le temps de boucle en cours ;
- les questions posées restées sans réponse ;
- la prochaine action prévue.
