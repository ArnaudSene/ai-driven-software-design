# 11 — Stratégie de test — <Nom du projet>

| Statut | Version | Date | Gate |
|---|---|---|---|
| Brouillon | 0.1 | <AAAA-MM-JJ> | G11 : — |

## 1. De l'exigence au test

| Source | Type de test | Niveau | Outil | Exécution |
|---|---|---|---|---|
| Exemples des règles (BR-n.Ek) | Unitaire du domaine | | | À chaque modification |
| Critères d'acceptation (AC-n) | Acceptation | | | À chaque modification |
| Contrats | Contrat | | | À chaque modification |
| Adaptateurs | Intégration | | | À chaque modification |
| QS-n de performance | Charge | | | |
| QS-n de disponibilité et reprise | Résilience, restauration | | | |
| T-n | Sécurité | | | |
| Parcours critiques | Bout en bout | | | |
| Exigences d'interaction (IR-n) | Parcours | | | |
| QS-n de capacité d'interaction | Évaluation de l'utilisabilité (heuristiques, test avec des utilisateurs, SUS (System Usability Scale)) | | | |

## 2. Fonctions d'aptitude

| Id | Règle vérifiée | Exigence (QS-n, ADR (Architecture Decision Record)) | Outil | Moment | Seuil d'échec |
|---|---|---|---|---|---|
| FF-1 | | | | | |

## 3. Déterminisme et données de test

## 4. Contrôles de la chaîne

| Contrôle | Seuil | Bloquant |
|---|---|---|
| | | |

## 5. Définitions de « prêt » et de « terminé »

**Prêt** : …

**Terminé** : …

## 6. Convention de nommage des tests

Chaque test cite l'identifiant vérifié : `test_BR_7_E2_<description>`, étiquette `@AC-11`.
