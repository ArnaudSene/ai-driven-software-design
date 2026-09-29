# Phase 5 — Architecture logicielle

| Clé | Valeur |
|---|---|
| Question centrale | Comment organiser le système pour satisfaire les exigences qualité ? |
| Agent | [`prompts/architecte-logiciel.md`](../prompts/architecte-logiciel.md) |
| Entrées | Phases 1 à 4 validées ; en priorité les `QS-n` architecturalement significatifs et les `BC-n` |
| Sorties | `conception/05-architecture.md` (structure arc42), `conception/adr/`, `diagrammes/` |
| Identifiants créés | `ADR-nnnn` |
| Gabarits | [`templates/05-architecture.md`](../templates/05-architecture.md), [`templates/adr.md`](../templates/adr.md) |
| Gate | G5 |

---

## 1. Pourquoi cette phase

L'architecture est l'ensemble des décisions **coûteuses à défaire**. Cette phase les prend de façon délibérée, une par une, en justifiant chacune par une exigence, au lieu de les laisser émerger par accident au fil du code.

Principe directeur : **l'architecture la plus simple qui satisfait les `QS-n` significatifs.** Toute complexité supplémentaire (distribution, asynchronisme, multiples bases) doit être achetée par un scénario qualité précis.

## 2. Concepts et méthodes

### 2.1 Les dimensions de l'architecture ne s'excluent pas

On confond souvent des réponses à des questions différentes. Clean Architecture, architecture orientée événements et DDD (Domain-Driven Design, conception pilotée par le domaine) **se combinent** :

| Dimension | Question | Options typiques |
|---|---|---|
| Modélisation | Comment représenter le métier ? | Modèle riche (DDD tactique), script de transaction, CRUD (Create, Read, Update, Delete — création, lecture, mise à jour, suppression) simple |
| Organisation interne d'un module | Comment ranger le code d'un module ? | En couches, hexagonale (ports et adaptateurs), Clean, en oignon, tranches verticales |
| Découpage et déploiement | Combien d'unités déployables ? | Monolithe, monolithe modulaire, services, microservices, fonctions serverless |
| Communication | Comment les modules se parlent-ils ? | Appel direct en mémoire, requête-réponse synchrone, messages ou événements asynchrones |
| Données | Qui possède quelles données ? Quelle cohérence ? | Base partagée, base par module, cohérence forte ou à terme |
| Lecture et écriture | Un seul modèle pour lire et écrire ? | Modèle unique, CQRS (Command Query Responsibility Segregation, séparation des commandes et des requêtes), sourcing d'événements |

La modélisation peut **varier d'un contexte à l'autre** : modèle riche et architecture hexagonale pour un contexte *Cœur*, simple CRUD pour un contexte *Support*.

### 2.2 Catalogue des styles et de leurs compromis

| Style | Favorise | Coûte | À choisir quand |
|---|---|---|---|
| **Monolithe modulaire** | Simplicité d'exploitation, transactions locales, refactorisation facile, performance | Déploiement unique, passage à l'échelle global | **Par défaut.** Équipe de moins d'une dizaine de personnes ; frontières encore mouvantes. |
| **Microservices** | Déploiement et passage à l'échelle indépendants, autonomie des équipes | Complexité distribuée : réseau, cohérence à terme, observabilité, exploitation | Plusieurs équipes autonomes ; besoins d'échelle très différents entre contextes ; frontières stables. |
| **Serverless (fonctions)** | Aucun serveur à gérer, coût proportionnel à l'usage | Démarrage à froid, dépendance au fournisseur, test local difficile | Charge irrégulière, traitements courts et sans état. |
| **Orienté événements** | Découplage temporel, extensibilité, résilience | Débogage et traçage plus difficiles, cohérence à terme, ordre des messages | Réactions en chaîne entre contextes ; tolérance au délai ; absorption de pics. |
| **CQRS** | Lectures optimisées indépendamment des écritures | Deux modèles à maintenir, décalage de synchronisation | Lectures et écritures très asymétriques en volume ou en forme. |
| **Sourcing d'événements** | Historique complet et rejouable, audit natif | Complexité élevée, évolution des schémas d'événements | Exigence forte d'audit ou de reconstitution d'état ; domaine naturellement fait d'événements. |
| **Hexagonale / Clean** | Domaine testable et indépendant de l'infrastructure | Plus de code d'adaptation, indirections | Contextes *Cœur* à logique riche et à longue durée de vie. |
| **En couches** | Simplicité, familiarité | Fuite de la base de données vers le métier | Contextes *Support* simples. |

Recommandation par défaut, à infirmer par un scénario qualité : **monolithe modulaire** dont les modules sont les `BC-n`, **architecture hexagonale** pour les contextes *Cœur*, **appels en mémoire** entre modules via des interfaces explicites, et **événements** là où une cohérence à terme est acceptable.

### 2.3 Des scénarios qualité aux tactiques

Pour chaque `QS-n` architecturalement significatif, l'agent propose des **tactiques** (au sens du SEI (Software Engineering Institute)) et les compare :

| Attribut | Tactiques usuelles |
|---|---|
| Performance | Cache, calcul anticipé, traitement asynchrone, pagination, index, réduction des allers-retours, parallélisme |
| Disponibilité | Redondance, réessai avec délai croissant, disjoncteur, file d'attente tampon, mode dégradé, contrôle de santé |
| Modifiabilité | Encapsulation, inversion des dépendances, configuration externe, règles paramétrables, frontières de modules |
| Sécurité | Défense en profondeur, moindre privilège, validation aux frontières, chiffrement, journalisation d'audit |
| Testabilité | Injection de dépendances, domaine pur sans entrées-sorties, horloge injectable, données de test reproductibles |
| Cohérence entre modules | Transaction locale, patron *outbox* transactionnel, saga avec compensation, idempotence des consommateurs |

Chaque tactique retenue est justifiée dans un ADR (Architecture Decision Record, registre de décision d'architecture).

### 2.4 Registres de décision d'architecture (`ADR-nnnn`)

Format dérivé de Michael Nygard et de MADR (Markdown Architectural Decision Records). Gabarit complet : [`templates/adr.md`](../templates/adr.md).

| Rubrique | Contenu |
|---|---|
| Statut | Proposé, Accepté, Déprécié, Remplacé par `ADR-nnnn` |
| Contexte | Le problème et les forces en présence, **avec les identifiants** (`QS-n`, `C-n`, `BR-n`) |
| Options considérées | Au moins deux options réalistes, dont souvent « ne rien faire » ou « la plus simple » |
| Analyse | Avantages et inconvénients de chaque option **au regard des exigences citées** |
| Décision | L'option retenue, formulée à l'affirmative |
| Conséquences | Positives, négatives, risques (`R-n`) et dette acceptée |
| Vérification | Comment on s'assure que la décision est respectée : `FF-n`, revue, `SLO-n` |

Critère pour écrire un ADR : la décision est **coûteuse à défaire**, **non évidente**, ou **controversée**. Un ADR fait une à deux pages ; au-delà, il cache plusieurs décisions.

### 2.5 Diagrammes C4

Le modèle C4 (Context, Containers, Components, Code — contexte, conteneurs, composants, code) de Simon Brown propose quatre niveaux de zoom :

| Niveau | Montre | Obligatoire |
|---|---|---|
| 1. Contexte du système | Le système, ses utilisateurs, les systèmes externes | Oui |
| 2. Conteneurs | Les unités déployables et les stockages (application web, service, base, file de messages) et leurs protocoles | Oui |
| 3. Composants | L'intérieur d'un conteneur : modules, ports, adaptateurs | Pour les contextes *Cœur* |
| 4. Code | Classes | Non : le code est la source de vérité |

Les diagrammes sont écrits en Mermaid (ou Structurizr DSL (Domain-Specific Language, langage dédié) pour les grands systèmes) dans `diagrammes/`. Au niveau 2, un « conteneur » n'est pas un conteneur Docker : c'est toute unité exécutable ou stockage distinct.

### 2.6 Document d'architecture arc42

`05-architecture.md` suit la structure arc42 (Gernot Starke, Peter Hruschka), dont plusieurs sections sont alimentées par d'autres phases :

| § arc42 | Section | Alimentée par |
|---|---|---|
| 1 | Introduction et objectifs | Phases 1 et 3 (résumé et renvois) |
| 2 | Contraintes | `C-n` |
| 3 | Contexte et périmètre | Diagramme de contexte, C4 niveau 1 |
| 4 | Stratégie de solution | **Cette phase** : style, découpage, choix clés |
| 5 | Vue des blocs de construction | C4 niveaux 2 et 3, `BC-n` → modules |
| 6 | Vue d'exécution | Diagrammes de séquence des `UC-n` *Must* et des scénarios d'erreur |
| 7 | Vue de déploiement | Phase 9 |
| 8 | Concepts transverses | **Cette phase** : erreurs, transactions, idempotence, journalisation, configuration, temps, internationalisation |
| 9 | Décisions d'architecture | Index des ADR |
| 10 | Exigences qualité | Renvoi à `03-exigences-qualite.md` |
| 11 | Risques et dette technique | `R-n` techniques |
| 12 | Glossaire | Renvoi à `glossaire.md` |

### 2.7 Concepts transverses à décider

L'agent **doit** examiner chacun de ces sujets et le trancher (dans la section 8 d'arc42 ou dans un ADR) :

1. **Gestion des erreurs** : erreurs métier ou techniques, propagation, message à l'utilisateur.
2. **Transactions et cohérence** : où est la frontière transactionnelle ? Comment garantir la cohérence entre modules ?
3. **Idempotence** : que se passe-t-il si une requête ou un message arrive deux fois ?
4. **Concurrence** : verrouillage optimiste ou pessimiste pour les accès concurrents identifiés en phase 2.
5. **Temps** : horloge injectable, fuseaux horaires, stockage en temps universel coordonné.
6. **Configuration et secrets** : séparation code / configuration / secrets.
7. **Journalisation, métriques, traces** : préparation de la phase 9.
8. **Validation** : où valide-t-on les entrées (frontière) et les invariants (domaine) ?
9. **Internationalisation**, si requise par un `QS-n`.
10. **Règles de dépendance** entre modules et couches : lesquelles seront vérifiées automatiquement (phase 10, `FF-n`).

### 2.8 Revue ATAM allégée (profil *Critique*, recommandée en *Produit*)

L'ATAM (Architecture Tradeoff Analysis Method, méthode d'analyse des compromis d'architecture) confronte l'architecture aux scénarios. Version allégée conduite par le relecteur critique :

1. Pour chaque `QS-n` significatif, dérouler le scénario sur les diagrammes : quels composants interviennent ? La mesure est-elle atteignable ?
2. Relever les **points de sensibilité** : décisions dont dépend fortement un attribut.
3. Relever les **compromis** : décisions qui améliorent un attribut au détriment d'un autre.
4. Relever les **risques** (`R-n`) et les **non-risques** (décisions saines, confirmées).

## 3. Déroulé de l'atelier

| Étape | L'agent | Le décideur |
|---|---|---|
| 1 | Liste les `QS-n` significatifs, les `C-n` et les `BC-n` qui orientent l'architecture. | Confirme les priorités. |
| 2 | Propose la **stratégie de solution** : style de découpage, organisation interne par type de contexte, mode de communication. Rédige l'ADR correspondant avec au moins deux options. | Arbitre. |
| 3 | Pour chaque `QS-n` significatif : tactiques, options, ADR. | Arbitre les compromis. |
| 4 | Dessine C4 niveaux 1 et 2, puis niveau 3 pour les contextes *Cœur*. | Relit. |
| 5 | Dessine les vues d'exécution des `UC-n` *Must* et d'au moins un scénario de panne. | Relit. |
| 6 | Tranche les concepts transverses (§ 2.7). | Arbitre si nécessaire. |
| 7 | Conduit la revue ATAM allégée si le profil l'exige. | Arbitre les risques. |
| 8 | Passe la liste de contrôle et invoque le relecteur critique. | Valide G5. |

Les choix de **produits** (quelle base de données, quel cadriciel) ne sont **pas** faits ici. On décide « une base relationnelle transactionnelle » ou « un courtier de messages avec garantie d'ordre par clé », et la phase 6 choisit le produit. Exception : les contraintes `C-n` qui imposent déjà un produit.

## 4. Banque de questions

1. Combien de personnes développeront et maintiendront ce système ? En combien d'équipes ? *(loi de Conway : l'architecture tend à reproduire l'organisation)*
2. L'équipe a-t-elle déjà exploité un système distribué en production ?
3. Ce traitement peut-il avoir lieu quelques secondes plus tard, ou l'utilisateur doit-il en voir le résultat immédiatement ?
4. Ce contexte a-t-il des besoins d'échelle très différents des autres ?
5. Si ce système externe tombe, que doit-il se passer de notre côté ?
6. Accepteriez-vous plus de complexité aujourd'hui pour pouvoir séparer ce module plus tard ?

## 5. Livrables

| Fichier | Contenu minimal |
|---|---|
| `05-architecture.md` | Sections arc42 1 à 6, 8, 9, 11 remplies ; 7 en attente de la phase 9 |
| `adr/ADR-0001-*.md` … | Stratégie de solution, une décision par `QS-n` significatif, concepts transverses structurants |
| `diagrammes/` | C4 niveaux 1, 2, (3), séquences |

## 6. Liste de contrôle de la gate G5

- [ ] ★ La stratégie de solution fait l'objet d'un ADR qui compare au moins deux options.
- [ ] ★ Chaque `QS-n` significatif est traité par un ADR ou une section nommée du document.
- [ ] ★ Les diagrammes C4 de niveaux 1 et 2 existent et sont cohérents avec la carte des contextes.
- [ ] Chaque ADR cite les exigences qui le motivent et indique comment il sera vérifié.
- [ ] Chaque `BC-n` correspond à un module ou à un service identifié.
- [ ] Les dix concepts transverses du § 2.7 sont tranchés ou explicitement reportés.
- [ ] Au moins un scénario de panne est déroulé en vue d'exécution.
- [ ] Toute complexité distribuée (plusieurs unités déployables, asynchronisme, plusieurs bases) est justifiée par un `QS-n` ou un `C-n`.
- [ ] Aucun produit n'est choisi sans `C-n` qui l'impose (les produits relèvent de la phase 6).
- [ ] Revue ATAM allégée faite si le profil est *Critique*.

## 7. Anti-patterns

| Anti-pattern | Symptôme | Correction |
|---|---|---|
| Architecture vitrine | Microservices, Kubernetes et sourcing d'événements pour trois écrans | Exiger le `QS-n` qui justifie chaque élément de complexité. |
| Monolithe en boule de boue | Aucune frontière interne, tout dépend de tout | Modules = `BC-n`, dépendances vérifiées par `FF-n`. |
| Microservices à base partagée | Plusieurs services écrivent dans les mêmes tables | Une base (ou un schéma) par propriétaire ; intégration par interface ou événement. |
| ADR a posteriori | ADR rédigés après coup pour justifier le code | Rédiger l'ADR avant d'implémenter, au statut *Proposé*. |
| Option unique | ADR sans alternative | Toujours au moins deux options, dont la plus simple. |
| Chemin heureux seulement | Aucune vue d'exécution d'une panne | Dérouler au moins un scénario de panne par dépendance externe. |
