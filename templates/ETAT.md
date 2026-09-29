# État de la conception — <Nom du projet>

<!-- Fichier tenu par l'agent orchestrateur. C'est la mémoire du processus :
     un agent qui reprend le projet sans historique de conversation doit pouvoir
     continuer en lisant ce seul fichier. Mettre à jour à chaque temps « Consigner »
     et en fin de session. -->

## 1. Situation

| Clé | Valeur |
|---|---|
| Projet | <Nom du projet, ou « à nommer »> |
| Répertoire de conception | <chemin de CONCEPTION_DIR> |
| Profil | À choisir / Prototype / Produit / Critique |
| Mode d'interaction | Atelier / Proposition / Revue |
| Phase en cours | <n> — <nom> |
| Temps de boucle | <1 à 7> — <Charger, Questionner, Proposer, Critiquer, Valider, Consigner, Gate> |
| Prochaine action | <action précise> |
| Dernière mise à jour | <AAAA-MM-JJ> |

## 2. Registre des sources (`SRC-n`)

<!-- Documents existants lus sans être modifiés (principes § 16). Supprimer la ligne d'exemple à l'initialisation. -->

| Id | Titre | Emplacement | Version lue (numéro, date ou commit) | Phases alimentées | Statut (à transposer, transposée, archivée) |
|---|---|---|---|---|---|
| SRC-n (exemple) | | | | | |

## 3. Gates

| Gate | Date | Décision | Dérogations | OD (décisions ouvertes) rattachées |
|---|---|---|---|---|
| G1 | | | | |

## 4. Questions en attente

<!-- Texte complet des questions posées restées sans réponse, pour pouvoir les reposer telles quelles. -->

1. …

## 5. Registre des décisions ouvertes (`OD-n`)

<!-- Supprimer la ligne d'exemple ci-dessous à l'initialisation. -->

| Id | Question | Options | Recommandation | Bloque | Responsable | Échéance | Statut | Résolution |
|---|---|---|---|---|---|---|---|---|
| OD-n (exemple) | | | | BR-n, QS-n, INC-n… | | Phase <n> ou date | Ouverte | → BR-n / ADR-nnnn |

## 6. Registre des hypothèses (`H-n`)

| Id | Hypothèse | Source | Vérification prévue (comment, quand) | Statut |
|---|---|---|---|---|
| H-n (exemple) | | | | À vérifier |

## 7. Registre des risques (`R-n`)

| Id | Risque | Type (projet, technique, dette) | Probabilité | Impact | Réponse (éviter, réduire, transférer, accepter) | Action | Incrément | Statut |
|---|---|---|---|---|---|---|---|---|
| R-n (exemple) | | | | | | | | Ouvert |

## 8. Journal

<!-- Une entrée datée par session et par décision notable. Ne jamais réécrire une entrée passée. -->

| Date | Phase | Événement |
|---|---|---|
| <AAAA-MM-JJ> | 1 | Initialisation de la conception. |
