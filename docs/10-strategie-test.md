# Phase 10 — Stratégie de test et de qualité

| Clé | Valeur |
|---|---|
| Question centrale | Comment prouver, de façon automatique et répétable, que le système est conforme ? |
| Agent | [`prompts/ingenieur-qualite.md`](../prompts/ingenieur-qualite.md) |
| Entrées | Toutes les phases précédentes, en particulier `BR-n.Ek`, `CA-n`, `QS-n`, `M-n`, ADR (Architecture Decision Record), `SLO-n`, contrats |
| Sorties | `conception/10-strategie-test.md`, `tracabilite.md` complété jusqu'aux tests |
| Identifiants créés | `FF-n` |
| Gabarit | [`templates/10-strategie-test.md`](../templates/10-strategie-test.md) |
| Gate | G10 |

---

## 1. Pourquoi cette phase

Les phases précédentes ont produit des critères de conformité conçus pour échouer de façon déterministe. Cette phase décide **quel type de test vérifie quoi, où et quand**, pour que chaque exigence ait une preuve automatique.

C'est aussi la phase qui protège l'architecture dans la durée : sans tests d'architecture, les frontières dessinées en phase 5 s'effacent en quelques mois.

## 2. Concepts et méthodes

### 2.1 De l'exigence au test

| Source | Type de test | Niveau | Exécuté |
|---|---|---|---|
| `BR-n.Ek` (exemples des règles) | Test unitaire du domaine | Domaine pur, sans entrées-sorties | À chaque modification |
| `CA-n` (critères d'acceptation) | Test d'acceptation (*Étant donné / Quand / Alors*) | Application, via ses ports ou son API (Application Programming Interface) | À chaque modification |
| Contrats (`contrats/`) | Test de contrat (fournisseur et consommateurs) | Frontière entre contextes ou avec les tiers | À chaque modification |
| Adaptateurs (base, messages, tiers) | Test d'intégration avec de vrais composants (base réelle en conteneur) | Adaptateur | À chaque modification |
| `QS-n` de performance | Test de charge et d'endurance | Système en préproduction | Avant chaque mise en production, ou chaque nuit |
| `QS-n` de disponibilité, de reprise | Test de résilience (injection de pannes), test de restauration | Système | Périodiquement |
| `M-n` (menaces) | Test de sécurité automatisé ; test d'intrusion pour le profil *Critique* | Système | À chaque modification (automatisé), périodiquement (manuel) |
| `QS-n` d'accessibilité | Analyse automatique + audit manuel | Interface | À chaque modification (automatique), avant mise en production (audit) |
| ADR et règles de structure | Fonction d'aptitude (`FF-n`) | Code et système | À chaque modification |
| `SLO-n` | Supervision en production | Production | En continu |
| Parcours critiques | Test de bout en bout (peu nombreux) | Système complet | Avant mise en production |

### 2.2 Répartition des tests

La pyramide des tests (Mike Cohn) reste la référence : **beaucoup** de tests unitaires rapides, **moins** de tests d'intégration, **très peu** de tests de bout en bout, lents et fragiles.

Pour une architecture hexagonale, on obtient naturellement :

- le domaine testé exhaustivement, sans base ni réseau (exemples des `BR-n`) ;
- chaque adaptateur testé contre la vraie technologie ;
- les cas d'utilisation testés via les ports, avec des adaptateurs en mémoire (`CA-n`) ;
- quelques parcours de bout en bout pour vérifier l'assemblage.

### 2.3 Fonctions d'aptitude (`FF-n`)

Une fonction d'aptitude (*fitness function*, Neal Ford, Rebecca Parsons, Patrick Kua — *Building Evolutionary Architectures*) est un **test automatisé qui vérifie une caractéristique de l'architecture** :

| Exemple | Vérifie | Outils possibles |
|---|---|---|
| `FF-1` : le paquet `domain` n'importe rien de `infrastructure` | Règle de dépendance hexagonale (ADR de stratégie) | ArchUnit, import-linter, dependency-cruiser |
| `FF-2` : aucun cycle de dépendance entre modules | Frontières des `BC-n` | Mêmes outils |
| `FF-3` : un module n'accède qu'à ses propres tables | Propriété des données (phase 7) | Test sur les requêtes, droits de base par module |
| `FF-4` : 95ᵉ centile de `POST /bookings` < [seuil de QS-3] sous charge nominale | `QS-3` | Outil de test de charge dans la chaîne |
| `FF-5` : aucune modification incompatible des contrats publiés | Règles de compatibilité (phase 7) | Comparateur de contrats OpenAPI / AsyncAPI |
| `FF-6` : aucune dépendance avec vulnérabilité critique connue | Politique des dépendances (phases 6 et 8) | Analyse des dépendances |

Fiche `FF-n` : exigence vérifiée (`QS-n`, ADR), règle, outil, moment d'exécution, seuil d'échec.

### 2.4 Tests pilotés par les exigences

- **Le nom ou l'étiquette de chaque test cite l'identifiant qu'il vérifie** : `test_BR_7_E2_late_cancellation_at_exact_limit` ou `@CA-11`. La matrice de traçabilité peut alors être générée à partir du code.
- Les tests d'acceptation peuvent être écrits en Gherkin (en français, avec la directive `# language: fr` en première ligne de chaque fichier de scénarios) et exécutés par un outil de BDD (Behavior-Driven Development, développement piloté par le comportement), ou écrits directement dans le langage de test, en gardant la structure *Étant donné / Quand / Alors*.
- Le TDD (Test-Driven Development, développement piloté par les tests) est recommandé pour le domaine des contextes *Cœur* : les exemples des `BR-n` sont déjà les premiers tests.
- **Tests écrits par une IA (intelligence artificielle)** : ils doivent être dérivés de la spécification (`BR-n.Ek`, `CA-n`), **pas** du code existant. Un test déduit du code confirme le code, y compris ses erreurs.

### 2.5 Déterminisme

Un test qui échoue « parfois » détruit la confiance dans toute la suite. Règles :

1. Horloge injectable : aucun test ne dépend de l'heure réelle.
2. Aléa contrôlé : graines fixées, identifiants générés de façon reproductible.
3. Isolation : chaque test prépare et nettoie ses propres données.
4. Pas d'attente arbitraire : attendre une condition, pas une durée.
5. Un test instable est mis en quarantaine **et** corrigé dans un délai fixé ; il n'est jamais simplement relancé jusqu'à ce qu'il passe.

### 2.6 Données de test

- Jeux de données synthétiques, construits par des fabriques ou des constructeurs de test lisibles.
- Données limites issues des exemples des `BR-n`.
- Jamais de données personnelles réelles, sauf anonymisation vérifiée (phase 8).

### 2.7 Contrôles de qualité dans la chaîne

| Contrôle | Seuil | Bloquant |
|---|---|---|
| Tous les tests passent | 100 % | Oui |
| Fonctions d'aptitude | Aucune violation | Oui |
| Couverture de code | Indicateur de tendance ; pas de cible absolue imposée | Non (alerte si baisse) |
| Tests de mutation sur le domaine *Cœur* | Score minimal [seuil à fixer] | Selon profil |
| Analyses de sécurité | Aucune vulnérabilité critique ou élevée non traitée | Oui |
| Formatage et analyse statique | Aucun écart | Oui |

La couverture mesure ce qui a été **exécuté**, pas ce qui a été **vérifié**. Les tests de mutation (introduire volontairement des erreurs et vérifier que les tests les détectent) mesurent mieux la qualité des tests du domaine.

### 2.8 Définition de « terminé » et de « prêt »

- **DoR** (Definition of Ready, définition de « prêt ») : un incrément peut démarrer quand ses `UC-n`, `BR-n` et `CA-n` sont validés, ses OD (décisions ouvertes) bloquantes tranchées et ses contrats écrits.
- **DoD** (Definition of Done, définition de « terminé ») : un incrément est terminé quand ses tests (exemples, `CA-n`, `FF-n` concernés) passent dans la chaîne, que la traçabilité est à jour, que la documentation modifiée est relue, et qu'il est déployé en préproduction.

## 3. Déroulé de l'atelier

| Étape | L'agent | Le décideur |
|---|---|---|
| 1 | Construit le tableau exigence → type de test (§ 2.1) pour le projet. | Valide. |
| 2 | Fixe la répartition des tests et les outils par niveau (en cohérence avec la phase 6). | Valide. |
| 3 | Rédige les `FF-n` à partir des ADR et des `QS-n` significatifs. | Valide. |
| 4 | Définit les règles de déterminisme et de données de test. | — |
| 5 | Définit les contrôles de la chaîne et leurs seuils. | Fixe les seuils. |
| 6 | Rédige la DoR et la DoD. | Valide. |
| 7 | Complète `tracabilite.md` jusqu'à la colonne « test prévu ». | — |
| 8 | Passe la liste de contrôle et invoque le relecteur critique. | Valide G10. |

## 4. Banque de questions

1. Qui valide fonctionnellement un incrément avant sa mise en production ?
2. Existe-t-il un environnement de test chez chaque tiers intégré ?
3. Quelles fonctions, si elles cassaient en production, seraient les plus graves ? *(elles méritent un test de bout en bout)*
4. Un audit d'accessibilité ou un test d'intrusion externe est-il exigé ou budgété ?
5. Quel temps maximal acceptez-vous pour la chaîne d'intégration ?

## 5. Livrables

| Fichier | Contenu minimal |
|---|---|
| `10-strategie-test.md` | Tableau exigence → test, répartition et outils, `FF-n`, déterminisme, données, contrôles de la chaîne, DoR, DoD |
| `tracabilite.md` | Colonne « test prévu » renseignée pour chaque `BR-n.Ek`, `CA-n`, `QS-n` *Must*, `M-n` |

## 6. Liste de contrôle de la gate G10

- [ ] ★ Chaque `CA-n` et chaque exemple de `BR-n` *Must* a un test prévu.
- [ ] ★ Les règles de dépendance de l'architecture sont vérifiées par au moins une `FF-n`.
- [ ] ★ La DoD est écrite.
- [ ] Chaque `QS-n` *Must* est couvert par un test, une `FF-n` ou un `SLO-n`.
- [ ] Chaque `M-n` mitigée a une vérification.
- [ ] Les contrats sont vérifiés par des tests de contrat.
- [ ] Les règles de déterminisme sont écrites.
- [ ] Les contrôles bloquants de la chaîne sont listés avec leurs seuils.
- [ ] Un test de restauration est prévu (phase 9).

## 7. Anti-patterns

| Anti-pattern | Symptôme | Correction |
|---|---|---|
| Pyramide inversée | Surtout des tests de bout en bout lents et instables | Descendre les vérifications au niveau le plus bas possible. |
| Culte de la couverture | « 80 % de couverture » exigé, assertions absentes | Couverture en indicateur ; tests de mutation sur le cœur. |
| Tests miroirs | Tests générés à partir du code, qui en reproduisent les erreurs | Dériver les tests des exemples et des critères. |
| Simulacres partout | Base et réseau simulés dans tous les tests | Tester les adaptateurs contre la vraie technologie. |
| Architecture non gardée | Règles de dépendance dans un document que personne ne lit | Les transformer en `FF-n` bloquantes. |
