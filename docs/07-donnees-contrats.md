# Phase 7 — Données et contrats d'interface

| Clé | Valeur |
|---|---|
| Question centrale | Quelles données, détenues par qui, et quelles interfaces entre les parties du système et avec l'extérieur ? |
| Agent | [`prompts/architecte-donnees-interfaces.md`](../prompts/architecte-donnees-interfaces.md) |
| Entrées | `02-exigences-fonctionnelles.md`, `04-domaine.md`, `05-architecture.md`, `06-choix-techniques.md` |
| Sorties | `conception/07-donnees-contrats.md`, `conception/contrats/` |
| Identifiants créés | Aucun nouveau préfixe ; les contrats sont identifiés par leur nom et leur version |
| Gabarit | [`templates/07-donnees-contrats.md`](../templates/07-donnees-contrats.md) |
| Gate | G7 |

---

## 1. Pourquoi cette phase

Les données survivent au code : un programme se réécrit, une base mal conçue se traîne pendant des années. Les interfaces, elles, sont des **promesses** faites à d'autres ; les casser coûte cher à tous ceux qui en dépendent.

Cette phase fixe donc, **avant** l'implémentation, ce qui est le plus coûteux à changer ensuite : la structure et la propriété des données, et les contrats d'interface.

## 2. Concepts et méthodes

### 2.1 Propriété des données

Règle fondamentale : **chaque donnée a un et un seul contexte propriétaire** (`BC-n`), seul autorisé à l'écrire. Les autres contextes la lisent via une interface, la reçoivent par un événement, ou en gardent une copie locale en lecture seule.

| Donnée | Propriétaire | Consommateurs | Mode d'accès des consommateurs |
|---|---|---|---|
| Réservation | `BC-1` | `BC-2`, `BC-3` | Événements `BookingConfirmed`, `BookingCancelled` |

### 2.2 Modèle de données par contexte

Trois niveaux, à ne pas confondre :

| Niveau | Contenu | Quand |
|---|---|---|
| Conceptuel | Concepts métier et relations, sans attribut technique | Déjà amorcé en phase 4 |
| Logique | Entités, attributs, types abstraits, clés, cardinalités, contraintes d'intégrité | **Cette phase** |
| Physique | Tables, index, partitionnement, types du SGBD (système de gestion de base de données) | Cette phase pour les structures critiques ; le reste est laissé à l'implémentation |

Les diagrammes sont écrits en Mermaid `erDiagram`. Chaque contrainte d'intégrité qui matérialise une règle métier cite sa `BR-n`.

### 2.3 Choix transverses sur les données

L'agent **doit** faire trancher chacun de ces points :

| Sujet | Options et recommandation par défaut |
|---|---|
| Identifiants | Identifiant technique généré (UUID (Universally Unique Identifier) de version 7, ordonné dans le temps) plutôt qu'une clé métier susceptible de changer ; la clé métier reste unique par contrainte. |
| Montants | Décimal exact ou entier en plus petite unité (centimes), **jamais** de nombre à virgule flottante ; devise stockée avec le montant. |
| Dates et heures | Instants stockés en temps universel coordonné ; fuseau conservé quand il a un sens métier (« 14 h heure de Paris ») ; format ISO (International Organization for Standardization) 8601, norme de représentation des dates dans les échanges. |
| Suppression | Physique, logique (marquage) ou archivage : à décider par type de donnée, en cohérence avec les obligations d'effacement. |
| Historique et audit | Table d'audit, versionnement des lignes, journal d'événements : selon les `QS-n` d'auditabilité. |
| Multi-clients | Si le système sert plusieurs organisations clientes : base par client, schéma par client, ou colonne discriminante. Décision majeure, qui justifie un ADR (Architecture Decision Record). |
| Texte | Encodage UTF-8 (Unicode Transformation Format, 8 bits) partout ; règles de comparaison et de tri. |

### 2.4 Classification et cycle de vie

Chaque ensemble de données reçoit :

| Rubrique | Valeurs |
|---|---|
| Sensibilité | Publique, Interne, Confidentielle, Secrète |
| Données personnelles | Non, Oui, Oui et sensibles au sens du RGPD (Règlement général sur la protection des données) : santé, opinions, biométrie… |
| Durée de conservation | Durée et fondement (loi, contrat, consentement) |
| Fin de vie | Archivage, anonymisation ou purge, et qui la déclenche |
| Volume estimé | Repris du profil de charge de la phase 3 |

Cette classification alimente directement la phase 8.

### 2.5 Évolution du schéma

1. Toute modification de schéma passe par une **migration versionnée**, rejouable, conservée dans le dépôt.
2. Pour une mise en production sans interruption, on applique le patron **étendre puis contracter** : ajouter la nouvelle structure, faire écrire les deux, migrer les données, basculer la lecture, puis supprimer l'ancienne structure dans une version ultérieure.
3. Les migrations de données volumineuses sont conçues pour être interrompues et reprises.

### 2.6 Reprise des données existantes

Si l'existant recensé en phase 1 contient des données à reprendre : inventaire des sources, correspondance des champs, règles de transformation et de nettoyage, traitement des rejets, volumétrie, stratégie de bascule, critères de réussite (comptages, sommes de contrôle, échantillons vérifiés par le métier).

### 2.7 Contrats d'interface

**L'interface est conçue avant son implémentation** : le contrat est un livrable de conception, écrit dans un format standard, relu, versionné, et utilisé pour générer tests et documentation.

| Type d'échange | Format de contrat |
|---|---|
| Requête-réponse sur HTTP (Hypertext Transfer Protocol), style REST (Representational State Transfer) | OpenAPI 3.x (`contrats/openapi.yaml`) |
| Appels de procédure distants à haute performance | gRPC (gRPC Remote Procedure Calls) + Protocol Buffers (`.proto`) |
| Événements et messages | AsyncAPI 3.x (`contrats/asyncapi.yaml`) + JSON (JavaScript Object Notation) Schema |
| Requêtes flexibles côté client | Schéma GraphQL |
| Fichiers échangés par lot | Spécification de format + JSON Schema ou description des colonnes |

YAML (YAML Ain't Markup Language) est le format d'écriture recommandé des contrats OpenAPI et AsyncAPI.

Règles de conception d'une API (Application Programming Interface, interface de programmation) HTTP, à consigner et appliquer uniformément :

1. **Nommage** des ressources : noms au pluriel, en anglais, cohérents avec le glossaire.
2. **Erreurs** : format uniforme, de préférence celui de la RFC (Request For Comments) 9457, *Problem Details for HTTP APIs* ; codes d'erreur métier stables qui citent la `BR-n` violée quand c'est pertinent.
3. **Pagination, tri, filtre** : un seul mécanisme pour toutes les collections.
4. **Idempotence** : clé d'idempotence obligatoire sur les créations non idempotentes (paiement, commande).
5. **Concurrence** : contrôle optimiste (en-têtes `ETag` / `If-Match`) sur les ressources modifiables par plusieurs acteurs.
6. **Versionnement** : stratégie unique (dans le chemin, un en-tête, ou pas de version et évolutions uniquement compatibles).
7. **Compatibilité** : ajouter un champ optionnel est compatible ; supprimer, renommer ou rendre obligatoire ne l'est pas et exige une nouvelle version et une période de dépréciation annoncée.
8. **Sécurité** : mécanisme d'authentification de chaque point d'accès, précisé en phase 8.

### 2.8 Événements

| Sujet | Règle |
|---|---|
| Nommage | Fait passé, en anglais, dans le langage du domaine : `BookingConfirmed` |
| Enveloppe | Identifiant unique, type, version du schéma, instant d'occurrence, identifiant de corrélation, contexte émetteur |
| Contenu | Notification minimale (identifiant et type), ou transfert d'état (données utiles au consommateur) : à choisir par événement |
| Garantie de livraison | « Au moins une fois » par défaut ; les consommateurs **doivent** être idempotents |
| Ordre | Garanti par clé (par exemple par réservation) uniquement si un invariant l'exige |
| Publication fiable | Patron *outbox* transactionnel : l'événement est enregistré dans la même transaction que la modification |
| Évolution | Mêmes règles de compatibilité que les API ; registre des schémas si plusieurs équipes |

### 2.9 Intégrations externes

Pour chaque système externe : contrat utilisé (fourni par le tiers ou à négocier), couche anticorruption, authentification, limites d'appel, comportement en cas d'indisponibilité (lien avec les `QS-n` de mode dégradé), environnement de test fourni par le tiers.

## 3. Déroulé de l'atelier

| Étape | L'agent | Le décideur |
|---|---|---|
| 1 | Établit la table de propriété des données (§ 2.1). | Valide. |
| 2 | Produit le modèle logique de chaque contexte, en citant les `BR-n` portées par des contraintes. | Relit les cardinalités et les règles. |
| 3 | Fait trancher les choix transverses (§ 2.3). | Arbitre. |
| 4 | Classe les données et fixe leur cycle de vie (§ 2.4). | Donne les durées légales ou ouvre des OD (décisions ouvertes). |
| 5 | Conçoit la reprise des données si nécessaire. | Fournit les échantillons. |
| 6 | Rédige les règles de conception des API, puis les contrats des `UC-n` *Must*. | Relit. |
| 7 | Rédige le catalogue des événements et le contrat AsyncAPI. | Relit. |
| 8 | Décrit chaque intégration externe. | Fournit la documentation des tiers. |
| 9 | Passe la liste de contrôle et invoque le relecteur critique. | Valide G7. |

## 4. Banque de questions

1. Combien de temps doit-on conserver chaque type de donnée, et pourquoi ?
2. Faut-il pouvoir retrouver l'état d'un dossier tel qu'il était à une date passée ?
3. Qui, en dehors de l'application, lit ces données (décisionnel, comptabilité, partenaires) ?
4. Certaines données viennent-elles d'un système existant ? Dans quel état de qualité ?
5. Le système servira-t-il plusieurs organisations clientes dont les données doivent être cloisonnées ?
6. Des applications tierces consommeront-elles nos API ? Pouvez-vous les obliger à suivre nos évolutions ?

## 5. Livrables

| Fichier | Contenu minimal |
|---|---|
| `07-donnees-contrats.md` | Propriété, modèles logiques, choix transverses, classification et cycle de vie, stratégie de migration, reprise, règles d'API, catalogue d'événements, intégrations |
| `contrats/openapi.yaml` | Points d'accès des `UC-n` *Must* |
| `contrats/asyncapi.yaml` | Événements publiés entre contextes |
| `diagrammes/` | Modèles de données Mermaid |

## 6. Liste de contrôle de la gate G7

- [ ] ★ Chaque donnée a un contexte propriétaire unique.
- [ ] ★ Montants, dates et identifiants suivent les choix transverses tranchés.
- [ ] ★ Chaque ensemble de données personnelles a une durée de conservation et une fin de vie.
- [ ] ★ Les contrats des `UC-n` *Must* existent au format standard et sont valides selon leur schéma.
- [ ] Les contraintes d'intégrité citent les `BR-n` qu'elles garantissent.
- [ ] Les règles de conception des API sont écrites (erreurs, pagination, idempotence, versionnement, compatibilité).
- [ ] Chaque événement a une enveloppe, un propriétaire, une garantie de livraison et des consommateurs identifiés.
- [ ] La publication fiable des événements est traitée (*outbox* ou équivalent).
- [ ] Chaque intégration externe a un comportement défini en cas d'indisponibilité.
- [ ] La reprise des données est conçue si l'existant l'exige.

## 7. Anti-patterns

| Anti-pattern | Symptôme | Correction |
|---|---|---|
| Base d'intégration | Plusieurs contextes écrivent dans les mêmes tables | Un propriétaire par donnée ; intégration par interface ou événement. |
| Flottants monétaires | Montant stocké en nombre à virgule flottante | Décimal exact ou entier en centimes. |
| Heure locale ambiguë | Dates stockées sans fuseau | Temps universel coordonné + fuseau métier explicite. |
| API calquée sur la base | Points d'accès qui exposent les tables telles quelles | Concevoir l'API à partir des `UC-n`, pas du schéma. |
| Contrat après code | Documentation générée après coup, jamais relue | Contrat d'abord, relu, puis implémenté et testé. |
| Consommateur naïf | Consommateur d'événements non idempotent | Déduplication par identifiant d'événement. |
