# Phase 5 — Conception de l'interaction

| Clé | Valeur |
|---|---|
| Question centrale | Comment l'utilisateur accomplit-il ses tâches avec le système ? |
| Agent | [`prompts/concepteur-interaction.md`](../prompts/concepteur-interaction.md) |
| Entrées | Phases 1 à 4 validées ; en priorité le contexte d'usage (phase 1), les `UC-n`, les `IR-n` et les parcours (phase 2), les `QS-n` de capacité d'interaction et les besoins d'interaction significatifs pour l'architecture (phase 3), le glossaire du domaine (phase 4) |
| Sorties | `conception/05-interaction.md`, `conception/prototypes/` |
| Identifiants créés | Aucun nouveau préfixe ; les écrans sont nommés et rattachés aux `UC-n` et aux `IR-n` |
| Gabarit | [`templates/05-interaction.md`](../templates/05-interaction.md) |
| Gate | G5 |

---

## 1. Pourquoi cette phase

Les phases 2 et 3 disent ce que l'utilisateur doit pouvoir faire ou voir (`IR-n`, exigences d'interaction) et avec quelle qualité (`QS-n`, scénarios qualité). Cette phase conçoit la réponse : quels écrans, dans quel enchaînement, avec quels états.

Elle vient **avant l'architecture**, pour deux raisons :

1. Certains besoins d'interaction engagent l'architecture : annuler une commande, défaire une action, suivre la progression d'une opération longue, garder plusieurs vues cohérentes. Les travaux du SEI (Software Engineering Institute) montrent qu'ils exigent un support de l'architecture, et que les décisions d'architecture sont les plus difficiles à changer à mesure que la conception avance (Bass, John, Kates, 2001 ; Bass et John, 2003). Ces travaux ont ensuite proposé des patrons d'architecture au service de l'utilisabilité (Golden, John, Bass, 2005 ; John et al., 2009), et Folmer et Bosch (2004) en ont fait la synthèse. Découverts au codage, ces besoins coûtent cher.
2. Les normes ISO (International Organization for Standardization) / IEC (International Electrotechnical Commission) 25063 et 25064, qui accompagnent la norme ISO 9241-210 de conception centrée sur l'humain, situent l'activité « produire des solutions de conception » pendant la conception de l'architecture, l'implémentation et l'intégration, et non après (introduction de ces deux normes).

Principe directeur : **l'interaction avant l'apparence, la basse fidélité avant le détail.** Les couleurs, la typographie et le choix d'un système de composants viennent en phase 7, une fois les parcours validés.

Si le système n'a pas d'utilisateur final (contexte d'usage de la phase 1) et ne sert que d'autres systèmes ou des développeurs, la phase se réduit à l'ergonomie de son API (Application Programming Interface, interface de programmation) ou de sa ligne de commande : nommage, messages d'erreur, cohérence des commandes.

## 2. Concepts et méthodes

### 2.1 Ce que la phase produit

Le rapport technique ISO/TR (Technical Report) 25060:2023 nomme ce livrable « spécification de l'interaction utilisateur-système et de l'interface utilisateur ». Le guide le décompose ainsi :

| Livrable | Contenu | Méthode de référence |
|---|---|---|
| Carte des écrans | Les écrans (« lieux »), ce qu'on peut y faire (« affordances » : boutons, champs), et les liens entre eux | *Breadboarding* de *Shape Up* (Ryan Singer) |
| Schémas d'écran | Disposition grossière, sans couleur ni style, tracée « à gros traits » pour qu'on ne puisse pas y ajouter de détail | *Fat-marker sketches* de *Shape Up* |
| Spécification de l'interaction | Pour chaque parcours : étapes, informations affichées, actions possibles, retours du système, erreurs | ISO/TR 25060:2023, § 5.5 |
| États des écrans | Ce que montre chaque écran dans chacun des états du § 2.3 | — |
| Réponses aux besoins significatifs | L'interaction qui répond à chaque besoin d'interaction significatif pour l'architecture (§ 2.4) | Scénarios d'utilisabilité du SEI |
| Besoins par écran | Les données que chaque écran lit et les actions qu'il envoie | Entrée de la phase 8 |
| Prototype jetable | Prototype HTML (HyperText Markup Language) cliquable des parcours *Must* | § 2.5 |

### 2.2 Partir des parcours, pas des écrans

On ne dessine pas d'écran avant d'avoir le parcours qu'il sert. La carte des parcours de la phase 2 (les activités de l'utilisateur, dans l'ordre où il les mène, à la manière de la *story map* de Jeff Patton) fournit l'ossature ; chaque écran s'y accroche.

Quand le contexte d'usage est mal connu, une recherche auprès des utilisateurs précède la phase : observation en situation (*Contextual Design*, Karen Holtzblatt et Hugh Beyer), ou personas et scénarios (*Goal-Directed Design*, Alan Cooper).

Règles (détail dans [00-principes § 7.4](00-principes.md#74-exigences-dinteraction-ir-n)) :

1. Tout écran remonte à au moins un `UC-n` (cas d'utilisation) ; toute `IR-n` est satisfaite par au moins un écran.
2. Un écran ne porte jamais de règle métier : il affiche et transmet. Une validation qui n'existerait que dans l'écran est une `BR-n` (règle métier) oubliée : on la remonte en phase 2.
3. Les libellés reprennent les termes du glossaire du domaine (phase 4) : le langage omniprésent va jusqu'à l'écran ; il ne s'arrête pas au code.

### 2.3 Les états d'un écran

Un écran n'a pas un seul état. Les états oubliés sont une source classique de défauts : l'agent **doit** les énumérer pour chaque écran.

| État | Question à trancher |
|---|---|
| Vide | Que voit l'utilisateur la première fois, quand il n'y a encore rien ? Que lui propose-t-on ? |
| Chargement | Que voit-il pendant l'attente ? Au-delà de quelle durée lui montre-t-on la progression ? Peut-il annuler ? |
| Erreur | Que lui dit-on, avec quels mots ? Que peut-il faire ensuite ? Sa saisie est-elle conservée ? |
| Partiel | Une partie seulement des données est disponible : l'affiche-t-on, et comment le signale-t-on ? |
| Périmé | La donnée affichée n'est plus à jour : le voit-il ? Depuis quand ? |
| Droits insuffisants | Que voit un rôle qui n'a pas accès à une action (matrice rôle × action de la phase 2) ? |
| Succès | Comment sait-il que son action a réussi ? Peut-il la défaire ? |

### 2.4 Les besoins d'interaction significatifs pour l'architecture

La phase 3 a passé la liste des scénarios d'utilisabilité du SEI et transformé chaque besoin retenu en `QS-n` ([03 § 2.6](03-exigences-qualite.md#26-besoins-dinteraction-significatifs-pour-larchitecture)). Ici, l'agent décrit l'interaction qui y répond, par exemple :

| Besoin (scénario du SEI) | Interaction à décrire | Ce que la phase 6 devra permettre |
|---|---|---|
| Annuler une opération en cours (*Canceling Commands*) | Bouton d'annulation pendant un traitement long ; état après annulation | Interrompre un traitement en cours et revenir à un état cohérent |
| Observer l'état du système (*Observing System State*) | Progression, état d'une tâche lancée, alerte quand une donnée change | Exposer l'avancement et pousser les changements, ou permettre de les interroger |
| Défaire (*Supporting Undo*) | Action « défaire », sa portée et sa durée | Conserver de quoi revenir en arrière |
| Agréger (*Aggregating Data*) | Agir sur plusieurs éléments en une seule fois | Traiter un lot comme une opération |
| Rester cohérent entre les vues (*Operating Consistently Across Views*) | Plusieurs vues des mêmes données, synchronisées | Propager une modification à toutes les vues |

Chaque réponse est transmise à la phase 6, qui la traite par un ADR (Architecture Decision Record, registre de décision d'architecture). Si la réponse révèle un besoin que la phase 3 n'avait pas vu, on y revient ([00-principes § 14](00-principes.md#14-retours-en-arrière-et-gestion-du-changement)).

### 2.5 Prototype jetable

Au temps *Proposer*, l'agent **devrait** générer un prototype HTML des parcours *Must*, cliquable, dans `conception/prototypes/`. Le décideur valide en manipulant plutôt qu'en lisant : une interaction se juge à l'usage.

Le prototype est **jetable** : il ne contient aucune règle métier, il n'est jamais repris dans le produit, et ses données sont fictives et signalées comme telles (règle d'or 1). Il peut servir à une première évaluation : l'activité « évaluer » commence dès les premiers stades du projet (ISO/IEC 25063, introduction), par exemple avec quelques utilisateurs du contexte d'usage (ISO 9241-210, § 7.5.4).

### 2.6 Ce que la phase ne fait pas

| Sujet | Où il est traité |
|---|---|
| Règles métier | Phase 2 (`BR-n`) |
| Mesures de la qualité d'usage (efficacité, efficience, satisfaction) | Phase 3 (`QS-n`) |
| Mécanismes qui rendent possibles l'annulation, la progression ou la synchronisation | Phase 6 (ADR) |
| Cadriciel d'interface, système de composants, apparence | Phase 7 |
| Contrats d'API servis aux écrans | Phase 8, à partir des besoins par écran |
| Tests d'utilisabilité sur le produit | Phase 11 |

## 3. Déroulé de l'atelier

| Étape | L'agent | Le décideur |
|---|---|---|
| 1 | Relit le contexte d'usage, les `UC-n`, les `IR-n`, les parcours, les `QS-n` de capacité d'interaction et le glossaire. Liste les besoins d'interaction significatifs. | Confirme. |
| 2 | Propose la carte des écrans et de la navigation, rattachée aux `UC-n`. | Corrige. |
| 3 | Pour chaque `UC-n` *Must* : rédige la spécification de l'interaction et trace les schémas d'écran. | Corrige le déroulé. |
| 4 | Énumère les états de chaque écran (§ 2.3). | Tranche chaque cas. |
| 5 | Décrit la réponse d'interaction à chaque besoin significatif et ce qu'elle exige de l'architecture (§ 2.4). | Arbitre. |
| 6 | Génère le prototype jetable des parcours *Must* (§ 2.5). | Manipule, corrige. |
| 7 | Liste, par écran, les données lues et les actions envoyées. | — |
| 8 | Passe la liste de contrôle et invoque le relecteur critique, qui confronte aussi le prototype aux dix heuristiques de Jakob Nielsen. | Valide G5. |

## 4. Banque de questions

1. Le contexte d'usage de la phase 1 vaut-il pour cet écran, ou sert-il une situation particulière ?
2. Que doit-il voir en premier pour décider ?
3. Quand une opération dure plus de quelques secondes, que doit-il pouvoir faire : attendre, continuer ailleurs, annuler ?
4. Quelles actions doivent pouvoir être défaites, et jusqu'à quand ?
5. Que doit-il voir quand la donnée affichée n'est plus à jour ?
6. Quelles erreurs peut-il commettre ici ? Le système doit-il les empêcher, les signaler ou permettre de les corriger ?
7. Doit-il voir plusieurs vues des mêmes données en même temps ? Doivent-elles rester synchronisées ?

## 5. Livrables

| Fichier | Contenu minimal |
|---|---|
| `05-interaction.md` | Carte des écrans, spécification de l'interaction des `UC-n` *Must*, états des écrans, réponses aux besoins significatifs, besoins par écran |
| `prototypes/` | Prototype jetable des parcours *Must* |
| `ETAT.md` | `OD-n` (décisions ouvertes) issues de la phase |
| `tracabilite.md` | Liens `IR-n` → écran |

## 6. Liste de contrôle de la gate G5

- [ ] ★ Chaque écran remonte à au moins un `UC-n`, et chaque `IR-n` est satisfaite par au moins un écran.
- [ ] ★ Chaque besoin d'interaction significatif pour l'architecture a sa réponse d'interaction, transmise à la phase 6.
- [ ] ★ Chaque écran des `UC-n` *Must* a ses états décrits (§ 2.3), ou marqués « sans objet ».
- [ ] Aucun écran ne porte de règle métier.
- [ ] Les libellés reprennent les termes du glossaire du domaine.
- [ ] Le décideur a manipulé les parcours *Must* sur le prototype, ou y a explicitement renoncé.
- [ ] Les exigences d'accessibilité de la phase 3 sont prises en compte dans les schémas.
- [ ] Les données lues et les actions envoyées par chaque écran sont listées pour la phase 8.
- [ ] Aucun choix d'apparence ni de cadriciel n'est fait (phase 7).
- [ ] Le relecteur critique a confronté le prototype aux dix heuristiques de Jakob Nielsen (profils *Produit* et *Critique*) ; cette revue à un seul évaluateur ne remplace pas l'évaluation de la phase 11.

## 7. Anti-patterns

| Anti-pattern | Symptôme | Correction |
|---|---|---|
| Écran avant parcours | On dessine des écrans avant d'avoir les `UC-n` et les `IR-n` | Partir de la carte des parcours (§ 2.2). |
| Règle cachée dans l'écran | Une validation métier n'existe que dans un schéma | La remonter en `BR-n` (phase 2). |
| Chemin heureux seulement | Aucun état d'erreur, de chargement ou de donnée périmée | Énumérer les états de chaque écran (§ 2.3). |
| Finition visuelle prématurée | On débat des couleurs avant d'avoir validé les parcours | Basse fidélité ; l'apparence vient en phase 7. |
| Prototype devenu produit | Le code du prototype est repris tel quel | Prototype jetable, dans `prototypes/`, jamais livré. |
| Besoin significatif découvert au codage | « Il faudrait pouvoir annuler ce calcul », une fois l'architecture figée | Liste du SEI en phase 3, réponse d'interaction ici, ADR en phase 6. |
