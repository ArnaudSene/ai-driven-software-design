# Phase 11 — Plan de réalisation et squelette ambulant

| Clé | Valeur |
|---|---|
| Question centrale | Dans quel ordre construire, et comment démarrer sans risque ? |
| Agent | [`prompts/responsable-technique.md`](../prompts/responsable-technique.md) |
| Entrées | Toutes les phases validées, registres `OD-n` et `R-n` de `ETAT.md` |
| Sorties | `conception/11-plan-realisation.md`, consignes de développement pour les agents de code, revue de cohérence globale |
| Identifiants créés | `INC-n` |
| Gabarit | [`templates/11-plan-realisation.md`](../templates/11-plan-realisation.md) |
| Gate | G11 — fin de la conception initiale |

---

## 1. Pourquoi cette phase

La conception n'a de valeur que si elle se transforme en code sans se perdre en route. Cette phase :

1. découpe la réalisation en **incréments** qui apportent chacun une valeur observable ;
2. place en tête ce qui **réduit le plus de risque** ;
3. définit un **squelette ambulant** qui valide l'architecture de bout en bout avant d'investir dans les fonctionnalités ;
4. prépare les **consignes** que suivront les développeurs, humains ou agents IA (intelligence artificielle) ;
5. vérifie la **cohérence globale** de tous les livrables avant de clore la conception initiale.

## 2. Concepts et méthodes

### 2.1 Squelette ambulant (`INC-0`)

Le squelette ambulant (*walking skeleton*, Alistair Cockburn) est la **plus petite implémentation qui traverse toute l'architecture** : une fonction triviale, mais qui passe par l'interface, le domaine, la persistance et la chaîne de livraison, jusqu'à un environnement de type production.

Contenu type de `INC-0` :

| Élément | Exemple |
|---|---|
| Un cas d'utilisation minimal | Créer et relire une réservation, sans règle complexe |
| Toutes les couches | Interface → API (Application Programming Interface) → domaine → base de données |
| Structure des modules | Un module par `BC-n`, même vides, avec leurs frontières |
| Chaîne d'intégration continue (CI) et de livraison continue (CD) | Compilation, tests, analyses, déploiement automatique en préproduction |
| Observabilité | Journaux structurés, une métrique, une trace, un tableau de bord |
| Fonctions d'aptitude | `FF-n` de dépendances actives et bloquantes |
| Sécurité | Authentification réelle, même avec un seul rôle |
| Migration de schéma | Première migration versionnée |

Le squelette **valide les ADR** (Architecture Decision Records) les plus risqués au prix le plus bas. S'il révèle un problème, on revient en phase 5 ou 6 (§ 14 des principes) : c'est exactement son rôle.

### 2.2 Découpage en incréments (`INC-n`)

Chaque incrément est une **tranche verticale** : il livre un ou plusieurs `UC-n` complets, avec leurs `BR-n`, leurs `CA-n` et leurs tests, de l'interface à la base.

Critères d'ordonnancement, dans cet ordre :

1. **Risque** : ce qui peut invalider l'architecture ou le projet d'abord (intégration avec un tiers mal connu, `QS-n` difficile, règle métier floue).
2. **Valeur** : les `UC-n` *Must* qui servent les `OB-n` principaux.
3. **Dépendances** : ce qui débloque le reste.
4. **Apprentissage** : ce qui permet de vérifier tôt une hypothèse `H-n` auprès des utilisateurs.

La cartographie des récits (*story mapping*, Jeff Patton) aide à visualiser le découpage : les activités de l'utilisateur en colonnes, les incréments en lignes horizontales. La première ligne complète forme le MVP (Minimum Viable Product, produit minimum viable) : la plus petite version qui permet d'apprendre si le produit atteint ses objectifs.

Fiche d'incrément :

| Rubrique | Contenu |
|---|---|
| Identifiant et titre | `INC-3` Annulation et avoirs |
| Objectif | Valeur apportée, `OB-n` servi |
| Contenu | `UC-n`, `BR-n`, `CA-n`, `FF-n` et `SLO-n` concernés |
| Risques réduits | `R-n`, `H-n` vérifiées |
| Prérequis | Incréments, `OD-n` à trancher avant de démarrer |
| Critère de fin | DoD (Definition of Done, définition de « terminé ») de la phase 10 + critère propre à l'incrément |

### 2.3 Du cas d'utilisation aux tâches

Les `UC-n` se découpent en éléments de carnet de produit (récits utilisateur) de taille raisonnable, en respectant les critères INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable — indépendant, négociable, porteur de valeur, estimable, petit, testable). Chaque élément **doit** citer les identifiants qu'il réalise.

Techniques de découpage d'un cas trop gros : par scénario (nominal d'abord, extensions ensuite), par règle, par variante de données, par rôle, par niveau d'automatisation (manuel d'abord).

### 2.4 Consignes de développement

La conception se traduit en règles de travail, écrites dans le dépôt du code pour que les développeurs **et les agents de code** les appliquent. L'agent rédige un fichier de consignes (`AGENTS.md` et, pour Claude Code, `CLAUDE.md`) à la racine du projet, qui contient au minimum :

1. **Où est la conception** : `conception/`, et quels fichiers lire avant de travailler sur une fonctionnalité (les `BR-n`, `CA-n` et ADR concernés).
2. **Langage** : utiliser les noms du glossaire ; ne pas inventer de synonyme.
3. **Structure** : un module par `BC-n` ; règles de dépendance (renvoi aux `FF-n`).
4. **Traçabilité** : les tests et les messages de commit citent les identifiants (`BR-7`, `CA-11`) ; les pull requests listent les identifiants réalisés.
5. **Écarts** : toute divergence nécessaire avec un ADR ou une règle se traite par une proposition d'ADR ou une OD (décision ouverte), jamais silencieusement dans le code.
6. **Valeurs métier** : ne jamais coder en dur une valeur marquée [seuil à fixer] ; la rendre configurable et le signaler.
7. **Conventions** : style de code, conventions de commit, stratégie de branches, revue de code.

### 2.5 Revue de cohérence globale

Avant G11, le relecteur critique conduit une revue transverse :

| Contrôle | Méthode |
|---|---|
| Éléments orphelins | Parcours de `tracabilite.md` : `UC-n` sans `OB-n`, `BR-n` *Must* sans test, `QS-n` *Must* sans ADR, `FF-n` ni `SLO-n`, ADR sans exigence |
| Contradictions | Entre `BR-n` et ADR, entre `QS-n` et topologie, entre classification des données et mesures de sécurité |
| OD en attente | Chaque OD ouverte a un responsable, une échéance, et l'incrément qu'elle bloque |
| Risques | Chaque `R-n` ouvert a une réponse et un incrément qui le traite |
| Glossaire | Chaque terme employé dans les livrables y figure |

## 3. Déroulé de l'atelier

| Étape | L'agent | Le décideur |
|---|---|---|
| 1 | Classe les `R-n`, les `H-n` et les `QS-n` difficiles par criticité. | Confirme. |
| 2 | Définit `INC-0` (squelette ambulant). | Valide. |
| 3 | Propose le découpage en `INC-n` et leur ordre, avec justification risque / valeur. | Réordonne selon ses priorités. |
| 4 | Délimite le MVP. | Tranche. |
| 5 | Rédige les consignes de développement (`AGENTS.md` / `CLAUDE.md` du projet). | Relit. |
| 6 | Conduit la revue de cohérence globale avec le relecteur critique. | Arbitre les écarts. |
| 7 | Met `ETAT.md` au statut « conception initiale close » et bascule en phase 12. | Valide G11. |

## 4. Banque de questions

1. Quelle est la toute première chose que des utilisateurs réels devraient pouvoir faire ?
2. Quelle hypothèse voulez-vous vérifier le plus tôt possible auprès des utilisateurs ?
3. Y a-t-il une date imposée (salon, obligation légale, fin de contrat d'un ancien système) ?
4. Qui développera : une équipe, des agents IA, les deux ? Qui relira le code ?
5. Quelle cadence de livraison et de démonstration souhaitez-vous ?

## 5. Livrables

| Fichier | Contenu minimal |
|---|---|
| `11-plan-realisation.md` | `INC-0`, `INC-n` ordonnés, MVP, découpage en récits des premiers incréments, résultat de la revue de cohérence |
| `AGENTS.md` / `CLAUDE.md` (racine du projet) | Consignes de développement |
| `ETAT.md` | Conception initiale close, OD et risques restants avec échéances |

## 6. Liste de contrôle de la gate G11

- [ ] ★ `INC-0` traverse toutes les couches et la chaîne de livraison.
- [ ] ★ Chaque `UC-n` *Must* est affecté à un incrément.
- [ ] ★ Les consignes de développement existent dans le dépôt du projet.
- [ ] ★ La revue de cohérence globale ne laisse aucun orphelin *Must* non traité.
- [ ] L'ordre des incréments est justifié par le risque et la valeur.
- [ ] Chaque OD ouverte a un responsable, une échéance et un incrément bloqué identifié.
- [ ] Le MVP est délimité.
- [ ] Les premiers incréments sont découpés en éléments conformes aux critères INVEST.

## 7. Anti-patterns

| Anti-pattern | Symptôme | Correction |
|---|---|---|
| Découpage horizontal | « Incrément 1 : la base ; incrément 2 : l'API ; incrément 3 : l'interface » | Tranches verticales qui apportent chacune une valeur. |
| Plaisir d'abord | Les fonctions faciles et visibles en premier, les risques à la fin | Le risque passe avant la valeur dans l'ordonnancement. |
| Squelette oublié | Fonctionnalités développées avant que la chaîne de livraison existe | `INC-0` d'abord, toujours. |
| Conception abandonnée | `conception/` jamais relu une fois le code commencé | Consignes de développement et phase 12. |
