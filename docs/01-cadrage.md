# Phase 1 — Cadrage

| Clé | Valeur |
|---|---|
| Question centrale | Pourquoi ce projet, pour qui, dans quelles limites ? |
| Agent | [`prompts/analyste-metier.md`](../prompts/analyste-metier.md) |
| Entrées | Idée ou demande initiale, documents existants déclarés comme sources `SRC-n` (cahier des charges, analyse fonctionnelle, maquettes, courriels, études) |
| Sorties | `conception/01-cadrage.md`, `conception/ETAT.md` initialisé, `conception/glossaire.md` amorcé |
| Identifiants créés | `PP-n`, `OB-n`, `C-n`, premiers `H-n`, `R-n`, `OD-n` |
| Gabarit | [`templates/01-cadrage.md`](../templates/01-cadrage.md) |
| Gate | G1 |

---

## 1. Pourquoi cette phase

Un projet sans cadrage explicite se construit sur des malentendus : chacun imagine un produit, un public et une ambition différents. Le cadrage fixe **le problème à résoudre, les personnes concernées, le succès attendu et les limites** avant qu'une seule fonctionnalité soit discutée.

C'est aussi ici que l'on choisit le **profil du projet** (*Prototype*, *Produit* ou *Critique*, voir [00-principes § 10](00-principes.md#10-profils-de-projet-proportionnalité)), qui dose l'effort de toutes les phases suivantes.

## 2. Concepts et méthodes

### 2.1 Énoncé de vision

Une phrase qui tient dans un ascenseur, selon le gabarit de Geoffrey Moore :

> **Pour** <public cible> **qui** <besoin ou problème>, **<nom du produit>** est un <catégorie de produit> **qui** <bénéfice clé>. **Contrairement à** <alternative actuelle>, notre produit <différence essentielle>.

Si le décideur ne parvient pas à remplir ce gabarit, le projet n'est pas encore mûr pour la suite. C'est une information précieuse, pas un échec.

### 2.2 Parties prenantes (`PP-n`)

Toute personne ou organisation qui **utilise** le système, est **affectée** par lui, le **finance**, l'**exploite** ou peut s'**opposer** à lui. Le modèle en oignon de Volere aide à n'oublier personne :

| Couche | Exemples |
|---|---|
| Le produit | Utilisateurs directs, opérateurs, administrateurs |
| Le système métier | Services internes qui consomment ou produisent les données |
| L'organisation | Commanditaire, direction, juridique, sécurité, support |
| L'environnement | Clients finaux, régulateurs, partenaires, concurrents, grand public |

Pour chaque partie prenante on note son rôle, son intérêt, son influence, et le **représentant** qu'on peut interroger.

### 2.3 Objectifs métier mesurables (`OB-n`)

Un objectif décrit un **changement observable dans le monde réel**, pas une fonctionnalité. Chacun porte un indicateur, une valeur de départ, une cible et une échéance.

| Mauvais | Bon |
|---|---|
| « Avoir un portail de déclaration en ligne » | `OB-1` : réduire le délai moyen de traitement d'une déclaration de sinistre de 10 jours à 3 jours, d'ici 6 mois après l'ouverture. *(valeurs illustratives)* |
| « Être rapide » | Ce n'est pas un objectif métier. C'est un attribut qualité, traité en phase 3. |

Si le décideur ne connaît pas la valeur de départ, on écrit **[seuil à fixer]** et on ouvre une OD (décision ouverte) avec pour action de la mesurer.

### 2.4 Périmètre

- **Dans le périmètre** : ce que la version visée couvre.
- **Hors périmètre** : ce qu'on exclut **explicitement**. C'est la liste la plus utile, car elle désamorce les attentes implicites.
- **Plus tard** : ce qui est envisagé pour une version ultérieure.

Un **diagramme de contexte métier** montre le système comme une boîte noire entourée de ses acteurs et des systèmes externes avec lesquels il échange. On le dessine en Mermaid, sans aucun détail technique interne.

### 2.5 Contraintes (`C-n`)

Une contrainte est une limite **imposée** à l'équipe, qu'elle n'a pas le pouvoir de négocier : budget, délai, obligation légale, technologie imposée par l'entreprise, compétences disponibles, hébergement obligatoire dans un pays, système existant à conserver.

Une contrainte se distingue d'un choix : « nous devons utiliser le nuage de l'entreprise » est une contrainte, « nous préférons tel langage » est un choix qui sera instruit en phase 6.

### 2.6 Hypothèses et risques initiaux

- Hypothèse (`H-n`) : ce que l'on tient pour vrai sans l'avoir vérifié (« les utilisateurs ont un smartphone récent »). On note comment et quand la vérifier.
- Risque (`R-n`) : événement incertain qui compromettrait le projet. On note sa probabilité, son impact et une réponse (éviter, réduire, transférer, accepter).

### 2.7 Existant

Systèmes, données, processus manuels ou tableurs que le projet remplace ou avec lesquels il cohabite. L'existant est la meilleure source de règles métier implicites : un tableur utilisé depuis dix ans contient des règles que personne n'a jamais écrites.

## 3. Déroulé de l'atelier

| Étape | L'IA (intelligence artificielle) | Le décideur |
|---|---|---|
| 1 | Crée `conception/` à partir des gabarits, initialise `ETAT.md` (phase 1, temps *Charger*). | — |
| 2 | Lit tous les documents fournis et en fait un résumé factuel : faits, zones floues, contradictions. | Fournit les documents, corrige le résumé. |
| 3 | Pose les questions sur le problème et la vision (§ 4, bloc A). Propose un énoncé de vision. | Répond, reformule la vision. |
| 4 | Fait l'inventaire des parties prenantes (bloc B) et propose une liste `PP-n`. | Complète et nomme les représentants. |
| 5 | Transforme les attentes exprimées en objectifs `OB-n` mesurables (bloc C). | Fixe les cibles ou les laisse [seuil à fixer]. |
| 6 | Délimite le périmètre et dessine le diagramme de contexte (bloc D). | Tranche ce qui entre et ce qui sort. |
| 7 | Recense les contraintes, l'existant, les hypothèses et les risques (blocs E et F). | Confirme. |
| 8 | Recommande un profil de projet, justifié par les réponses. | Choisit le profil. |
| 9 | Amorce le glossaire avec les termes métier rencontrés. | Corrige les définitions. |
| 10 | Rédige `01-cadrage.md`, passe la liste de contrôle, présente la synthèse de gate. | Valide G1. |

## 4. Banque de questions

L'IA choisit dans cette banque les questions encore sans réponse et les pose par lots de 5 au maximum, selon le format de [00-principes § 5.1](00-principes.md#51-format-dune-question).

**A. Problème et vision**
1. Quel problème concret résout-on ? Qui le subit aujourd'hui, et comment le contourne-t-il ?
2. Que se passe-t-il si on ne fait rien ?
3. Pourquoi maintenant ?
4. À quoi ressemble le succès dans un an ? Qu'est-ce qui aura changé pour les utilisateurs ?
5. Existe-t-il une solution concurrente ou un outil actuel ? Qu'est-ce qui ne va pas avec lui ?

**B. Parties prenantes**
1. Qui utilisera le système au quotidien ? Avec quelle fréquence, sur quel appareil, avec quel niveau d'aisance numérique ?
2. Qui paie ? Qui décide ? Qui peut bloquer le projet ?
3. Qui exploitera le système et assurera le support ?
4. Des tiers (partenaires, régulateurs, clients de vos clients) sont-ils affectés ?
5. Qui peut répondre aux questions métier détaillées ?

**C. Objectifs**
1. Quels indicateurs suivez-vous déjà, et lesquels le projet doit-il faire bouger ?
2. Quelle valeur de départ, quelle cible, quelle échéance ?
3. Quel est l'ordre de grandeur du nombre d'utilisateurs aujourd'hui et dans trois ans ?

**D. Périmètre**
1. Quelles sont les trois fonctions sans lesquelles le produit n'a aucun intérêt ?
2. Qu'est-ce qui est explicitement exclu de la première version ?
3. Avec quels systèmes externes faut-il échanger (paiement, messagerie, annuaire, logiciel de gestion) ?

**E. Contraintes et existant**
1. Budget, date butoir, taille et compétences de l'équipe ?
2. Obligations légales ou réglementaires connues (données personnelles, santé, finance, accessibilité) ?
3. Technologies, hébergeurs ou fournisseurs imposés ou interdits ?
4. Quels systèmes, données ou processus manuels existent aujourd'hui ? Faut-il reprendre des données ?

**F. Risques**
1. Qu'est-ce qui vous empêche de dormir à propos de ce projet ?
2. Quelle hypothèse, si elle se révélait fausse, tuerait le projet ?

## 5. Livrables

| Fichier | Contenu minimal |
|---|---|
| `01-cadrage.md` | Vision, `PP-n`, `OB-n`, périmètre (dans, hors, plus tard), diagramme de contexte, `C-n`, existant, profil choisi et sa justification |
| `ETAT.md` | Phase courante, profil, registres `H-n`, `R-n`, `OD-n`, journal |
| `glossaire.md` | Premiers termes métier (terme, définition, synonymes à proscrire) |

## 6. Liste de contrôle de la gate G1

Les items marqués ★ suffisent en profil allégé.

- [ ] ★ L'énoncé de vision est rempli et approuvé par le décideur.
- [ ] ★ Chaque `OB-n` a un indicateur, une cible et une échéance, ou un [seuil à fixer] rattaché à une OD.
- [ ] ★ Le hors-périmètre est explicite (au moins 3 éléments).
- [ ] ★ Le profil du projet est choisi et justifié.
- [ ] Chaque `PP-n` a un rôle, un intérêt, une influence et un représentant (ou « à identifier »).
- [ ] Le diagramme de contexte montre tous les acteurs et systèmes externes cités.
- [ ] Les contraintes légales ont été explicitement interrogées, même si la réponse est « aucune ».
- [ ] Chaque `R-n` a une probabilité, un impact et une réponse.
- [ ] Aucun choix technique ne figure dans le document, hormis sous forme de `C-n`.

## 7. Anti-patterns

| Anti-pattern | Symptôme | Correction |
|---|---|---|
| Objectif-fonctionnalité | « Objectif : avoir un tableau de bord » | Demander « pour changer quoi ? » jusqu'à atteindre un effet mesurable. |
| Partie prenante oubliée | Le support ou le juridique découvre le projet à la mise en production | Parcourir les quatre couches de l'oignon. |
| Périmètre implicite | Aucun hors-périmètre écrit | Exiger au moins trois exclusions explicites. |
| Solution déguisée en besoin | « Le besoin est d'avoir des microservices » | Appliquer la règle d'or 11 : extraire le besoin, noter la piste pour la phase 5. |
| Chiffre inventé | Une cible « raisonnable » proposée par l'IA et jamais validée | Appliquer la règle d'or 1 : [seuil à fixer] + OD. |
