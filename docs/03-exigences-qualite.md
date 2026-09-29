# Phase 3 — Exigences qualité (non fonctionnelles)

| Clé | Valeur |
|---|---|
| Question centrale | Avec quel niveau de qualité le système doit-il fonctionner ? |
| Agent | [`prompts/architecte-qualite.md`](../prompts/architecte-qualite.md) |
| Entrées | `01-cadrage.md` (G1), `02-exigences-fonctionnelles.md` (G2) |
| Sorties | `conception/03-exigences-qualite.md` |
| Identifiants créés | `QS-n`, `C-n` complémentaires, `OD-n` |
| Gabarit | [`templates/03-exigences-qualite.md`](../templates/03-exigences-qualite.md) |
| Gate | G3 |

---

## 1. Pourquoi cette phase

Deux systèmes qui offrent exactement les mêmes fonctions peuvent exiger des architectures radicalement différentes. Ce qui les distingue, ce sont les **attributs qualité** : performance, disponibilité, sécurité, facilité de modification…

**Ce sont eux, et non les fonctionnalités, qui dictent l'architecture.** Une architecture choisie sans exigences qualité explicites est choisie par habitude ou par effet de mode. Cette phase est donc le principal intrant des phases 5 à 9.

## 2. Concepts et méthodes

### 2.1 Modèle de qualité ISO/IEC 25010

La norme ISO (International Organization for Standardization) / IEC (International Electrotechnical Commission) 25010, version 2023, sert de **liste de contrôle** pour n'oublier aucune famille d'exigences :

| Caractéristique | Sous-caractéristiques utiles | Question type |
|---|---|---|
| Adéquation fonctionnelle | Complétude, exactitude, pertinence | Les calculs doivent-ils être exacts au centime ? |
| Efficacité de performance | Temps de réponse, capacité, consommation de ressources | Combien d'utilisateurs simultanés ? Quel délai acceptable ? |
| Compatibilité | Coexistence, interopérabilité | Avec quels systèmes échanger, selon quels formats ? |
| Capacité d'interaction | Facilité d'apprentissage, accessibilité, protection contre les erreurs | Des personnes en situation de handicap l'utiliseront-elles ? |
| Fiabilité | Disponibilité, tolérance aux pannes, récupérabilité | Combien de temps d'interruption est tolérable ? Combien de données peut-on perdre ? |
| Sécurité | Confidentialité, intégrité, non-répudiation, traçabilité, authenticité | Quelles données sont sensibles ? Faut-il prouver qui a fait quoi ? |
| Maintenabilité | Modularité, testabilité, facilité de modification | Quelles parties changeront souvent ? |
| Flexibilité | Adaptabilité, facilité d'installation, passage à l'échelle | Faudra-t-il changer d'hébergeur, déployer chez des clients ? |
| Innocuité (*safety*) | Fonctionnement sûr, alerte en cas de danger | Une défaillance peut-elle blesser quelqu'un ou causer un dommage matériel ? |

### 2.2 Scénario d'attribut qualité (`QS-n`)

Formalisme du SEI (Software Engineering Institute, Université Carnegie Mellon), tiré de *Software Architecture in Practice* (Bass, Clements, Kazman). Un scénario rend un attribut qualité **mesurable** :

| Partie | Question | Exemple |
|---|---|---|
| **Source** | Qui ou quoi déclenche ? | 500 clients |
| **Stimulus** | Que se passe-t-il ? | soumettent une réservation simultanément |
| **Environnement** | Dans quel état est le système ? | en charge normale, un samedi matin |
| **Artefact** | Quelle partie est concernée ? | le service de réservation |
| **Réponse** | Que doit faire le système ? | enregistre chaque réservation et la confirme |
| **Mesure de la réponse** | Comment vérifie-t-on ? | 95 % des confirmations en moins de [seuil à fixer : 300 ms ?], aucune double réservation |

Chaque `QS-n` porte en plus les champs communs de [00-principes § 7.1](00-principes.md#71-structure-dune-règle) : Source (d'où vient l'exigence), Justification, Priorité, et le lien vers les `OB-n`, `C-n` ou `BR-n` qui la motivent.

Exemple complet :

```markdown
### QS-4 — Perte de données maximale après incident

- **Caractéristique** : Fiabilité › récupérabilité
- **Source** : panne matérielle de l'hébergement principal
- **Stimulus** : perte totale du stockage principal
- **Environnement** : exploitation normale, en journée
- **Artefact** : données de réservation et de paiement
- **Réponse** : le service est restauré à partir des sauvegardes
- **Mesure** : perte de données ≤ [seuil à fixer] minutes (RPO) ; service rétabli en ≤ [seuil à fixer] heures (RTO)
- **Justification** : une réservation perdue est un client lésé et un litige (OB-2).
- **Priorité** : Must — la perte serait silencieuse jusqu'à la réclamation du client.
- **Liens** : OB-2, BR-3, C-5
- **OD** : OD-9 (valeurs RPO/RTO à arbitrer contre le coût de l'infrastructure)
```

RPO (Recovery Point Objective) désigne la perte de données maximale admissible, RTO (Recovery Time Objective) la durée d'interruption maximale admissible.

### 2.3 Profil de charge et volumétrie

Aucun scénario de performance n'a de sens sans ordres de grandeur. L'agent **doit** les obtenir du décideur, même approximatifs, et **ne doit pas** les inventer :

| Grandeur | Aujourd'hui | À 1 an | À 3 ans | Source |
|---|---|---|---|---|
| Utilisateurs inscrits | | | | |
| Utilisateurs actifs simultanés au pic | | | | |
| Opérations métier clés par jour (par type) | | | | |
| Pic horaire ou saisonnier | | | | |
| Volume de données créé par an | | | | |
| Durée de conservation légale | | | | |

Une fourchette (« entre 100 et 1 000 ») vaut mieux qu'un vide : elle suffit souvent à trancher entre deux architectures.

### 2.4 Arbre d'utilité et priorisation

On classe chaque `QS-n` selon deux axes, notés H/M/B (haut, moyen, bas) :

- **importance métier**, fixée par le décideur ;
- **difficulté technique**, estimée par l'agent.

Les scénarios (H, H) et (H, M) sont **architecturalement significatifs** : la phase 5 doit répondre explicitement à chacun d'eux par un ADR (Architecture Decision Record, registre de décision d'architecture) ou un choix de style documenté.

### 2.5 Exigences transverses souvent oubliées

| Sujet | Question à poser |
|---|---|
| Accessibilité | Le service est-il soumis au RGAA (Référentiel général d'amélioration de l'accessibilité), qui transpose les WCAG (Web Content Accessibility Guidelines, règles pour l'accessibilité des contenus web) ? Quel niveau viser ? |
| Internationalisation | Langues, formats de date et de nombre, fuseaux horaires, devises ? |
| Auditabilité | Faut-il pouvoir reconstituer qui a fait quoi, quand, et avec quelle valeur avant et après ? Pendant combien de temps ? |
| Archivage et purge | Durées de conservation légales ; droit à l'effacement des personnes. |
| Mode dégradé | Que doit continuer à fonctionner quand un système externe est indisponible ? |
| Hors connexion | L'application doit-elle fonctionner sans réseau ? |
| Coût d'exploitation | Plafond mensuel d'hébergement et de licences ? |
| Empreinte environnementale | Objectif de sobriété numérique ? |
| Exploitabilité | Qui surveille le système, à quelles heures ? Qui est réveillé la nuit ? |

## 3. Déroulé de l'atelier

| Étape | L'agent | Le décideur |
|---|---|---|
| 1 | Relit les phases 1 et 2 et en extrait les attributs qualité implicites (« les agences ouvrent à 8 h » → disponibilité le matin). | — |
| 2 | Collecte le profil de charge (§ 2.3). | Donne les ordres de grandeur. |
| 3 | Parcourt les caractéristiques ISO/IEC 25010 une à une et pose les questions pertinentes. | Répond, signale ce qui ne s'applique pas. |
| 4 | Rédige un `QS-n` pour chaque exigence exprimée, avec ses six parties. | Fixe les seuils ou les laisse [seuil à fixer]. |
| 5 | Propose la difficulté de chaque `QS-n`. | Fixe l'importance. |
| 6 | Identifie les **conflits** entre scénarios (sécurité contre ergonomie, cohérence contre disponibilité, coût contre redondance) et les présente comme des arbitrages. | Arbitre ou ouvre des OD (décisions ouvertes). |
| 7 | Passe la liste de contrôle et invoque le relecteur critique. | Valide G3. |

## 4. Banque de questions

1. Le système peut-il être indisponible ? Quand (la nuit, le week-end) et combien de temps sans conséquence grave ?
2. Si le système perdait les données de la dernière heure, quelle serait la conséquence ?
3. Au-delà de combien de secondes d'attente un utilisateur abandonne-t-il ?
4. Quelles données seraient les plus graves à voir fuiter ? À voir modifiées sans qu'on s'en aperçoive ?
5. Quelles parties du métier changent le plus souvent (tarifs, règles, formulaires) ? Qui doit pouvoir les modifier : un développeur ou un utilisateur habilité ?
6. Quelle est la durée de vie prévue du système ? Qui le maintiendra ?
7. Le système sera-t-il déployé une seule fois ou chez plusieurs clients (multi-clients, installation sur site) ?
8. Existe-t-il des pics prévisibles (soldes, clôture mensuelle, rentrée) ?
9. Quel budget mensuel d'exploitation est acceptable ?
10. Quelles normes ou certifications sont exigées par les clients ou le secteur ?

## 5. Livrables

| Fichier | Contenu minimal |
|---|---|
| `03-exigences-qualite.md` | Profil de charge, `QS-n` complets, arbre d'utilité, conflits et arbitrages |
| `ETAT.md` | `OD-n` sur les seuils ; `R-n` techniques révélés |

## 6. Liste de contrôle de la gate G3

- [ ] ★ Le profil de charge est rempli, au moins en ordres de grandeur, ou chaque trou est une OD.
- [ ] ★ Chaque `QS-n` a une mesure de la réponse chiffrée ou un [seuil à fixer] rattaché à une OD.
- [ ] ★ La disponibilité et la perte de données admissible (RPO et RTO) ont été explicitement interrogées.
- [ ] ★ Les `QS-n` architecturalement significatifs sont identifiés.
- [ ] Chacune des neuf caractéristiques ISO/IEC 25010 a été examinée, et celles jugées sans objet sont notées comme telles.
- [ ] Les conflits entre scénarios sont listés avec leur arbitrage ou leur OD.
- [ ] Les obligations d'accessibilité, d'auditabilité et de conservation sont traitées.
- [ ] Aucun `QS-n` ne prescrit une technologie (« utiliser un cache » est une solution ; « 95 % des lectures en moins de 100 ms » est une exigence).

## 7. Anti-patterns

| Anti-pattern | Symptôme | Correction |
|---|---|---|
| Adjectif sans mesure | « Le système doit être rapide, sécurisé et évolutif » | Transformer chaque adjectif en scénario à six parties. |
| Tout est prioritaire | Tous les `QS-n` sont *Must* et (H, H) | Forcer un classement relatif : « si vous deviez sacrifier l'un des deux ? ». |
| Disponibilité magique | « 100 % de disponibilité » | Montrer le coût de chaque « 9 » supplémentaire et demander le coût réel d'une heure d'arrêt. |
| Chiffres inventés | 10 000 utilisateurs simultanés supposés par l'IA (intelligence artificielle) | Appliquer la règle d'or 1. |
| Solution déguisée | « Le système doit utiliser Kubernetes » | Si c'est imposé, c'est une `C-n` ; sinon, extraire le besoin sous-jacent. |
