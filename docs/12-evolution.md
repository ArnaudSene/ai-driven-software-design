# Phase 12 — Évolution de la conception

| Clé | Valeur |
|---|---|
| Question centrale | Comment la conception reste-t-elle vraie pendant toute la vie du système ? |
| Agent | Orchestrateur ([`AGENTS.md`](../AGENTS.md)), appuyé du spécialiste concerné par chaque changement |
| Entrées | `conception/` complet, code, résultats de production |
| Sorties | Livrables révisés, nouveaux ADR (Architecture Decision Records), journal de `ETAT.md` |
| Identifiants créés | Tous, selon les changements |
| Gate | Aucune gate globale ; chaque changement structurant est validé par le décideur |

---

## 1. Pourquoi cette phase

Une conception qui n'est pas maintenue devient **fausse**, et une documentation fausse est pire qu'une absence de documentation : elle trompe les humains comme les agents IA (intelligence artificielle), qui la suivront à la lettre.

La phase 12 commence avec la première ligne de code et ne s'arrête qu'au retrait du système.

## 2. Concepts et méthodes

### 2.1 Déclencheurs de mise à jour

| Déclencheur | Action |
|---|---|
| Nouvelle demande métier | Reprise en mode allégé des phases 2 (nouveaux `UC-n` et `BR-n`), puis 3 à 10 selon l'impact |
| Règle métier découverte pendant le développement | Nouvelle `BR-n` validée par le décideur **avant** d'être codée |
| Écart nécessaire avec un ADR | Nouvel ADR qui remplace l'ancien ; l'ancien passe à *Remplacé par* |
| OD (décision ouverte) tranchée | Mise à jour des éléments marqués [seuil à fixer] et des tests associés |
| Échec d'une fonction d'aptitude (`FF-n`) | Corriger le code, **ou** décider par ADR que la règle change ; jamais désactiver silencieusement |
| Incident de production | Analyse ; vérification des `QS-n`, `SLO-n` et `M-n` concernés ; mise à jour si l'exigence ou la mesure était fausse |
| `SLO-n` régulièrement manqué ou toujours largement tenu | Revoir le `QS-n` d'origine avec le décideur |
| Mesure des `OB-n` après mise en production | Retour en phase 1 si l'objectif n'est pas atteint : le problème était-il bien compris ? |
| Nouvelle vulnérabilité ou nouvelle obligation légale | Phase 8, puis impacts |
| Fin de support d'une technologie | Phase 6, nouvel ADR |

### 2.2 Procédure de changement

Elle applique le § 14 des [principes](00-principes.md#14-retours-en-arrière-et-gestion-du-changement) :

1. Identifier les éléments touchés.
2. Parcourir la matrice de traçabilité pour lister l'impact amont et aval.
3. Faire décider le décideur.
4. Modifier les livrables (mention de révision datée), écrire les nouveaux ADR, mettre à jour les tests.
5. Consigner dans le journal de `ETAT.md`.

### 2.3 Garde-fous automatiques contre la dérive

La conception reste vraie d'autant plus facilement qu'une partie est **vérifiée par la machine** :

| Élément de conception | Garde-fou |
|---|---|
| Règles de dépendance, frontières de modules | `FF-n` bloquantes dans la chaîne |
| Contrats d'interface | Tests de contrat, comparaison de compatibilité |
| `BR-n` et `CA-n` | Tests qui citent les identifiants ; matrice de traçabilité générée à partir des étiquettes de test |
| `QS-n` de performance | Tests de charge périodiques, `SLO-n` en production |
| Diagrammes | Générés à partir du code ou du modèle quand c'est possible ; sinon, revue à chaque incrément |

### 2.4 Travail des agents de code

Pendant la réalisation, un agent de code qui applique ce guide **doit** :

1. Avant de coder une fonctionnalité, lire les `UC-n`, `BR-n`, `CA-n`, ADR et `FF-n` qui la concernent.
2. Utiliser les noms du glossaire.
3. Écrire d'abord les tests dérivés des exemples et critères d'acceptation.
4. Citer les identifiants dans les tests, les messages de commit et la description de la pull request.
5. S'arrêter et demander au décideur au lieu de trancher seul une ambiguïté métier ; proposer une OD (décision ouverte).
6. Proposer un ADR au lieu de contourner une décision d'architecture.
7. Signaler toute divergence constatée entre le code existant et la conception.

### 2.5 Revues périodiques

| Rythme | Revue |
|---|---|
| À chaque incrément | OD tranchées, `R-n` à jour, traçabilité, glossaire |
| Chaque trimestre (profils *Produit* et *Critique*) | ADR encore valides ? `QS-n` encore justes au regard de la production ? Dette technique ? |
| Chaque année | Modèle de menaces, dépendances et fins de support, test du PRA (plan de reprise d'activité) |

### 2.6 Registre de la dette technique

La dette technique consciente est consignée comme un `R-n` de type « dette », avec : origine (ADR ou décision qui l'a acceptée), coût estimé de son maintien, déclencheur de remboursement, incrément prévu.

## 3. Liste de contrôle d'un changement

- [ ] Les éléments touchés et leur impact amont et aval sont listés.
- [ ] Le décideur a validé le changement.
- [ ] Les ADR remplacés ne sont pas modifiés ; un nouvel ADR les remplace.
- [ ] Les tests et les `FF-n` concernés sont mis à jour.
- [ ] La traçabilité et le glossaire sont à jour.
- [ ] Le journal de `ETAT.md` contient l'entrée datée.

## 4. Anti-patterns

| Anti-pattern | Symptôme | Correction |
|---|---|---|
| Documentation fossile | `conception/` décrit un système qui n'existe plus | Déclencheurs du § 2.1, garde-fous automatiques. |
| ADR réécrit | L'histoire des décisions est effacée | Un ADR accepté ne se modifie pas : il est remplacé. |
| Règle codée en douce | Une règle métier apparaît dans le code sans `BR-n` | Règle d'or 1 et consignes de développement. |
| Fonction d'aptitude désactivée | Test d'architecture commenté « temporairement » | Corriger, ou changer la règle par ADR. |
