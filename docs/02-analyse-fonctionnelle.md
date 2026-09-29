# Phase 2 — Analyse fonctionnelle

| Clé | Valeur |
|---|---|
| Question centrale | Que doit faire le système ? |
| Agent | [`prompts/analyste-metier.md`](../prompts/analyste-metier.md) |
| Entrées | `01-cadrage.md` validé (G1), `glossaire.md`, documents métier |
| Sorties | `conception/02-exigences-fonctionnelles.md`, `glossaire.md` enrichi, `tracabilite.md` |
| Identifiants créés | `UC-n`, `BR-n`, `BR-n.Ek`, `CA-n`, `OD-n` |
| Gabarit | [`templates/02-exigences-fonctionnelles.md`](../templates/02-exigences-fonctionnelles.md) |
| Gate | G2 |

---

## 1. Pourquoi cette phase

Elle transforme une intention (« gérer les réservations ») en un ensemble **vérifiable** de comportements attendus. À la fin de cette phase, on doit pouvoir écrire les tests d'acceptation **avant** d'avoir choisi le moindre outil.

Le critère de réussite est simple : si deux équipes lisent les exigences, elles doivent produire des systèmes qui se comportent de la même façon sur tous les exemples.

## 2. Concepts et méthodes

### 2.1 Les trois niveaux d'exigence fonctionnelle

| Niveau | Identifiant | Répond à | Exemple |
|---|---|---|---|
| Cas d'utilisation | `UC-n` | Quel objectif un acteur atteint-il avec le système ? | `UC-3` : un client annule une réservation. |
| Règle métier | `BR-n` | Quelle règle le système applique-t-il, quel que soit le cas ? | `BR-7` : une annulation à moins de 24 h du créneau n'est pas remboursée. |
| Critère d'acceptation | `CA-n` | À quelle condition considère-t-on le cas d'utilisation livré ? | `CA-11` : étant donné une réservation à J+3, quand le client annule, alors il reçoit un avoir et le créneau redevient libre. |

Une règle métier est **transverse** : `BR-7` s'applique aussi bien à l'annulation par le client (`UC-3`) qu'à l'annulation par un conseiller (`UC-8`). On l'écrit donc une seule fois et on la référence depuis les cas d'utilisation.

### 2.2 Cas d'utilisation (`UC-n`)

Format inspiré d'Alistair Cockburn, au niveau « objectif utilisateur » (une tâche qu'un acteur accomplit en une séance et qui lui apporte de la valeur) :

| Rubrique | Contenu |
|---|---|
| Acteur principal | Une `PP-n` ou un système externe |
| Objectif | Ce que l'acteur veut obtenir, en une phrase |
| Objectif métier | `OB-n` servi |
| Préconditions | Ce qui est vrai avant |
| Garanties en cas de succès | Ce qui est vrai après un succès |
| Garanties minimales | Ce qui reste vrai même en cas d'échec (rien n'est à moitié enregistré, par exemple) |
| Scénario nominal | Étapes numérotées, alternant l'acteur et le système |
| Extensions | Variantes et erreurs, numérotées d'après l'étape d'origine (`3a`, `3b`) |
| Règles appliquées | `BR-n` |
| Priorité | *Must*, *Should*, *Could* ou *Won't* |

Les récits utilisateur (« En tant que…, je veux…, afin de… ») peuvent compléter les cas d'utilisation pour le découpage du travail en phase 11. Ils ne les remplacent pas : un récit ne décrit ni les erreurs ni les garanties.

### 2.3 Règles métier (`BR-n`)

Chaque règle porte les six champs de [00-principes § 7.1](00-principes.md#71-structure-dune-règle) : Règle, Critère de conformité, Exemples, Source, Justification, Priorité.

Exemple complet :

```markdown
### BR-7 — Annulation tardive non remboursée

- **Règle** : Si un client annule une réservation moins de [seuil à fixer : 24 h ?] avant le début
  du créneau, alors le système ne doit émettre ni remboursement ni avoir.
- **Critère de conformité** : pour toute annulation dont l'horodatage est strictement postérieur à
  (début du créneau − délai), le montant remboursé est 0 et aucun avoir n'est créé.
- **Exemples** :
  - BR-7.E1 (nominal) — Créneau le 10/03 à 14:00, annulation le 09/03 à 13:59 → avoir intégral.
  - BR-7.E2 (limite) — Même créneau, annulation le 09/03 à 14:00:00 → avoir intégral (borne incluse ?) → OD-3
  - BR-7.E3 (échec) — Annulation le 10/03 à 09:00 → aucun avoir.
- **Source** : PP-2 (responsable d'agence), entretien du 2026-10-01 ; conditions générales § 4.
- **Justification** : un créneau libéré tardivement ne peut plus être revendu.
- **Priorité** : Must — une erreur de remboursement est financière et silencieuse (C-4).
- **Cas d'utilisation** : UC-3, UC-8.
```

Remarquer : le délai reste **[seuil à fixer]** tant que le décideur ne l'a pas confirmé, et la question de la borne (incluse ou exclue ?) devient une OD (décision ouverte) au lieu d'être tranchée au hasard par l'IA (intelligence artificielle) ou par le développeur.

### 2.4 Example Mapping

Technique de Matt Wynne pour faire émerger règles et exemples en atelier. On travaille un cas d'utilisation (ou un récit) à la fois, avec quatre types de cartes :

| Carte | Couleur d'usage | Devient |
|---|---|---|
| Le récit ou cas étudié | Jaune | `UC-n` |
| Une règle | Bleue | `BR-n` |
| Un exemple concret, avec des valeurs réelles | Verte | `BR-n.Ek` ou `CA-n` |
| Une question sans réponse | Rouge | `OD-n` |

Heuristiques de lecture :

- Beaucoup de cartes rouges : le sujet n'est pas mûr, il faut interroger le métier avant d'aller plus loin.
- Beaucoup de cartes bleues : le cas est trop gros, il faut le découper.
- Une règle sans exemple : elle n'est pas comprise.

L'IA simule l'atelier : pour chaque `UC-n`, elle **propose** des règles et des exemples concrets, et surtout des **exemples limites** (bornes, valeurs nulles, doublons, concurrence, annulation au milieu d'un traitement), puis le décideur confirme, corrige ou transforme en question.

### 2.5 Critères d'acceptation (`CA-n`)

Rédigés au format *Étant donné / Quand / Alors* (Gherkin) pour être directement transposables en tests automatisés en phase 10. La première ligne `# language: fr` est indispensable pour que les outils Gherkin reconnaissent les mots-clés français :

```gherkin
# language: fr
# CA-11 — vérifie UC-3, BR-7
Étant donné une réservation confirmée pour le 10/03 à 14:00
  Et nous sommes le 07/03 à 10:00
Quand le client annule la réservation
Alors un avoir de 45,00 € est émis
  Et le créneau du 10/03 à 14:00 est de nouveau disponible
```

### 2.6 Compléments fonctionnels

Selon le projet, la phase couvre aussi :

| Complément | Forme |
|---|---|
| Cycle de vie des objets métier | Diagramme d'états (Mermaid `stateDiagram`) pour chaque objet à états : commande, dossier, contrat |
| Processus métier transverses | Diagramme d'activité ou de séquence quand un processus traverse plusieurs cas d'utilisation |
| Rôles et droits | Matrice rôle × action (qui peut faire quoi). Les mécanismes techniques viennent en phase 8. |
| Notifications | Événement déclencheur, destinataire, canal, contenu |
| Éditions et rapports | Contenu, destinataire, fréquence |
| Parcours et écrans | Liste des écrans ou maquettes fil de fer, rattachés aux `UC-n` |
| Reprise de données | Données existantes à migrer et règles de transformation |

## 3. Déroulé de l'atelier

**Si une analyse fonctionnelle existe déjà** (source `SRC-n`), le déroulé ci-dessous s'applique en mode *Proposition* : chaque étape commence par la transposition de la source, et les questions ne portent que sur ses manques. Voir [00-principes § 16](00-principes.md#16-reprise-dun-existant).

| Étape | L'agent | Le décideur |
|---|---|---|
| 1 | Liste les acteurs à partir des `PP-n` et propose l'inventaire des `UC-n` (titre, acteur, objectif, `OB-n`). | Complète, priorise. |
| 2 | Pour chaque `UC-n` *Must*, par ordre de priorité : rédige le scénario nominal et les extensions. | Corrige le déroulé. |
| 3 | Pour ce même `UC-n`, conduit l'Example Mapping : règles, exemples nominaux et limites, questions. | Donne les valeurs réelles, tranche ou laisse ouvert. |
| 4 | Factorise les règles communes à plusieurs cas en `BR-n` uniques. | — |
| 5 | Rédige les `CA-n`. | Valide. |
| 6 | Traite les compléments (§ 2.6) pertinents pour le projet. | Répond. |
| 7 | Reprend les `UC-n` *Should* et *Could* avec un niveau de détail proportionné. | Priorise. |
| 8 | Enrichit le glossaire avec chaque terme métier apparu. | Corrige. |
| 9 | Met à jour la traçabilité, passe la liste de contrôle, invoque le relecteur critique. | Valide G2. |

## 4. Banque de questions

**Pour chaque cas d'utilisation**
1. Qui déclenche ce cas ? Peut-il être déclenché automatiquement (par une date, par un autre système) ?
2. Que doit-il être vrai avant ? Que se passe-t-il si ce n'est pas le cas ?
3. Qu'est-ce qui doit être vrai à la fin, même en cas d'échec ?
4. Que se passe-t-il si l'acteur abandonne au milieu ?
5. Deux personnes peuvent-elles faire la même chose en même temps sur le même objet ? Laquelle gagne ?

**Pour chaque règle**
1. Donnez-moi un exemple concret avec de vraies valeurs.
2. Que se passe-t-il exactement à la limite (égalité, zéro, vide, maximum) ?
3. Y a-t-il des exceptions ? Qui peut déroger à la règle, et comment est-ce tracé ?
4. D'où vient cette règle (loi, contrat, habitude) ? Peut-elle changer, et à quelle fréquence ?
5. Si le système l'appliquait mal, comment et quand s'en apercevrait-on ? *(sert à fixer la priorité)*

**Transverses**
1. Faut-il garder l'historique des modifications ? Qui a fait quoi, quand ?
2. Quels montants, dates, fuseaux horaires, devises, arrondis, langues ?
3. Qu'est-ce qui doit pouvoir être annulé, et jusqu'à quand ?
4. Quelles données saisies peuvent être fausses, et comment les corrige-t-on ?

## 5. Livrables

| Fichier | Contenu minimal |
|---|---|
| `02-exigences-fonctionnelles.md` | Acteurs, inventaire des `UC-n`, fiches `UC-n`, `BR-n` complètes, `CA-n`, compléments pertinents |
| `ETAT.md` | `OD-n` issues des cartes rouges |
| `glossaire.md` | Termes métier ajoutés |
| `tracabilite.md` | Liens `OB-n` → `UC-n` → `BR-n` / `CA-n` |

## 6. Liste de contrôle de la gate G2

- [ ] ★ Chaque `UC-n` remonte à un `OB-n`.
- [ ] ★ Chaque `BR-n` *Must* porte les six champs, dont au moins un exemple nominal et un exemple limite ou d'échec.
- [ ] ★ Aucune valeur métier n'a été inventée : chaque seuil est confirmé ou marqué [seuil à fixer] avec une OD.
- [ ] ★ Chaque `UC-n` *Must* a au moins un `CA-n`.
- [ ] Chaque `UC-n` a des extensions d'erreur et des garanties minimales.
- [ ] Chaque `BR-n` a une justification et une source.
- [ ] Les accès concurrents et l'annulation en cours de traitement ont été examinés pour chaque `UC-n` *Must*.
- [ ] Les objets métier à états ont un diagramme d'états.
- [ ] La matrice rôle × action est remplie.
- [ ] Aucun terme métier n'est employé sans figurer dans le glossaire.
- [ ] Aucune exigence ne mentionne une technologie (base, cadriciel, protocole).

## 7. Anti-patterns

| Anti-pattern | Symptôme | Correction |
|---|---|---|
| Règle sans exemple | « Le système calcule la remise selon la politique commerciale » | Exiger trois exemples chiffrés dont une borne. |
| Règle composée | « … et … et … » dans un même énoncé | Scinder en plusieurs `BR-n`. |
| Critère invérifiable | « Le système doit être intuitif » | C'est un attribut qualité : le déplacer en phase 3 avec une mesure. |
| Chemin heureux seulement | Aucune extension d'erreur | Poser systématiquement les questions 3 à 5 du bloc « cas d'utilisation ». |
| Interface déguisée en exigence | « Un bouton vert en haut à droite » | Remonter à l'intention ; la maquette est un complément, pas une règle. |
| Borne tranchée au hasard | « ≤ » ou « < » choisi par l'IA | Ouvrir une OD. |
