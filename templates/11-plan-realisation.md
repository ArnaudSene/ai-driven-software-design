# 11 — Plan de réalisation — <Nom du projet>

| Statut | Version | Date | Gate |
|---|---|---|---|
| Brouillon | 0.1 | <AAAA-MM-JJ> | G11 : — |

## 1. Risques à traiter en priorité

| Élément (R-n, H-n, QS-n) | Criticité | Incrément qui le traite |
|---|---|---|
| | | |

## 2. Squelette ambulant — INC-0

| Élément | Contenu |
|---|---|
| Cas d'utilisation minimal | |
| Couches traversées | |
| Modules créés | BC-n → … |
| Chaîne de livraison | |
| Observabilité | |
| Fonctions d'aptitude actives | FF-n |
| Authentification | |
| Décisions (ADR) validées par le squelette | ADR-nnnn |

## 3. Incréments

| Id | Titre | Objectif (OB-n) | Contenu (UC-n, BR-n, CA-n) | Risques réduits | Prérequis (incréments, décisions ouvertes (OD)) | Critère de fin |
|---|---|---|---|---|---|---|
| INC-1 | | | | | | Définition de « terminé » + … |

**Produit minimum viable** : INC-0 à INC-n (à préciser).

## 4. Découpage des premiers incréments

| Élément du carnet | Réalise | Incrément |
|---|---|---|
| | UC-n, BR-n, CA-n | INC-1 |

## 5. Consignes de développement

Fichiers créés à la racine du projet : `AGENTS.md` (consignes) et `CLAUDE.md` (`@AGENTS.md`).

Structure attendue de `AGENTS.md` du projet :

```markdown
# Consignes de développement

## Conception
- La conception fait foi : `<CONCEPTION_DIR>` (par défaut `conception/`). Avant de coder une fonctionnalité, lire les cas d'utilisation (UC, Use Case), règles métier (BR, Business Rule), critères d'acceptation (CA), décisions d'architecture (ADR, Architecture Decision Record) et fonctions d'aptitude (FF, Fitness Function) concernés.
- Toute ambiguïté métier : s'arrêter et demander ; proposer une décision ouverte (OD) dans `conception/ETAT.md`.
- Tout écart avec une décision d'architecture : proposer un nouvel ADR, ne jamais contourner silencieusement.
- Ne jamais coder en dur une valeur marquée [seuil à fixer] : la rendre configurable et le signaler.

## Langage
- Noms du code en anglais, conformes à `conception/glossaire.md` ; aucun synonyme.

## Structure
- Un module par contexte délimité : <liste>.
- Règles de dépendance : <résumé> ; vérifiées par <FF-n>.

## Traçabilité
- Tests : le nom ou l'étiquette cite l'identifiant vérifié (BR-7.E2, CA-11).
- Commits et demandes de fusion : citer les identifiants réalisés.

## Conventions
- Style, commits, branches, revue : <…>
```

## 6. Revue de cohérence globale

| # | Gravité | Élément | Objection | Décision |
|---|---|---|---|---|
| | | | | |
