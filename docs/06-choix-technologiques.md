# Phase 6 — Choix technologiques

| Clé | Valeur |
|---|---|
| Question centrale | Avec quels langages, cadriciels, produits et services construire l'architecture retenue ? |
| Agent | [`prompts/prescripteur-technique.md`](../prompts/prescripteur-technique.md) |
| Entrées | `05-architecture.md` et ADR (Architecture Decision Record) validés (G5), `C-n`, `QS-n` |
| Sorties | `conception/06-choix-techniques.md`, ADR de choix, comptes rendus de preuves de concept |
| Identifiants créés | `ADR-nnnn` |
| Gabarit | [`templates/06-choix-techniques.md`](../templates/06-choix-techniques.md) |
| Gate | G6 |

---

## 1. Pourquoi cette phase

L'architecture dit **quoi** (« une base relationnelle transactionnelle », « un courtier de messages »). Cette phase dit **avec quoi**. Elle vient après l'architecture pour que la technologie serve la conception, et non l'inverse.

Le meilleur choix technique est rarement le plus performant dans l'absolu : c'est celui que l'équipe saura **maîtriser, exploiter et faire évoluer** pendant toute la durée de vie du système.

## 2. Concepts et méthodes

### 2.1 Inventaire des choix à faire

L'agent dresse la liste des choix nécessaires à partir des conteneurs du diagramme C4 (Context, Containers, Components, Code) de niveau 2 et des concepts transverses :

Modèles d'hébergement cités : IaaS (Infrastructure as a Service, infrastructure à la demande), PaaS (Platform as a Service, plateforme à la demande), SaaS (Software as a Service, logiciel à la demande).

| Catégorie | Exemples de décisions |
|---|---|
| Langages | Langage du serveur, du client, des scripts |
| Cadriciels | Cadriciel web serveur, cadriciel d'interface, cadriciel de test |
| Persistance | SGBD (système de gestion de base de données), outil de migration de schéma, couche d'accès aux données |
| Communication | Format et protocole d'interface, courtier de messages |
| Services transverses | Fournisseur d'identité, envoi de courriels, stockage de fichiers, recherche plein texte, cache |
| Hébergement | Modèle (serveurs gérés soi-même, IaaS, PaaS, SaaS, fonctions serverless), fournisseur, région |
| Outillage | Gestion de version, intégration continue (CI) et livraison continue (CD), gestion des dépendances, analyse de code |
| Observabilité | Journaux, métriques, traces, alertes |

### 2.2 Méthode de sélection

Pour chaque choix structurant :

1. **Filtre éliminatoire.** On écarte toute option incompatible avec une `C-n` (technologie imposée ou interdite, licence, hébergement souverain, budget) ou avec un `QS-n` *Must*.
2. **Présélection.** Deux à quatre options réalistes. Au-delà, l'analyse devient superficielle.
3. **Grille pondérée.** Le décideur fixe les poids, l'agent propose les notes **en les justifiant**.
4. **Preuve de concept** si l'écart est faible ou si une incertitude technique subsiste (§ 2.4).
5. **ADR** qui consigne options, grille, décision et conséquences.

### 2.3 Critères d'évaluation

| Critère | Ce qu'on regarde |
|---|---|
| Adéquation aux exigences | Les `QS-n` et `C-n` concernés sont-ils satisfaits, et avec quelle marge ? |
| Compétences de l'équipe | L'équipe maîtrise-t-elle l'outil ? Coût et durée de montée en compétence ? |
| Maturité et pérennité | Âge, gouvernance du projet, fréquence des versions, politique de support à long terme (LTS (Long-Term Support)), nombre de mainteneurs actifs |
| Écosystème | Bibliothèques, intégrations, documentation, communauté |
| Recrutement | Facilité à trouver des profils sur le marché visé |
| Coût total | Licences, hébergement, formation, exploitation : le TCO (Total Cost of Ownership, coût total de possession) |
| Sécurité | Historique des vulnérabilités publiées (CVE (Common Vulnerabilities and Exposures)) et réactivité des correctifs |
| Licence | Compatibilité avec le modèle de distribution du produit (licences permissives ou à réciprocité) |
| Réversibilité | Coût de sortie : formats ouverts, standards, dépendance à un fournisseur |
| Exploitabilité | Supervision, sauvegarde, mise à jour, compétences d'exploitation disponibles |
| Sobriété | Consommation de ressources, si un `QS-n` le demande |

Exemple de grille :

| Critère | Poids | Option A | Option B | Option C |
|---|---|---|---|---|
| Adéquation `QS-2`, `QS-5` | 5 | 4 — justification | 5 — justification | 3 — justification |
| Compétences de l'équipe | 4 | 5 | 2 | 3 |
| Réversibilité | 2 | 4 | 3 | 5 |
| … | | | | |
| **Total pondéré** | | | | |

La grille éclaire la décision, elle ne la prend pas. Si le résultat contredit l'intuition du décideur, c'est qu'un critère ou un poids manque : on le cherche plutôt que d'ignorer l'un ou l'autre.

### 2.4 Preuve de concept

Une preuve de concept (en anglais *spike* ou PoC (Proof of Concept)) est un **prototype jetable, limité dans le temps**, qui répond à **une** question :

| Rubrique | Exemple |
|---|---|
| Question | Le cadriciel X tient-il `QS-3` (500 requêtes par seconde à moins de 300 ms au 95ᵉ centile) sur notre modèle de données ? |
| Durée maximale | 2 jours |
| Critère de réussite | Mesure du 95ᵉ centile sous charge simulée |
| Résultat | Consigné dans l'ADR, section « Analyse » |
| Sort du code | Jeté. Il n'est jamais promu en production. |

### 2.5 Acheter, réutiliser ou développer

Pour chaque sous-domaine *Générique* identifié en phase 4, l'option par défaut est d'**acheter ou de réutiliser** (service géré, produit, bibliothèque). Développer un sous-domaine générique doit être justifié par un ADR.

### 2.6 Politique des dépendances

Consignée dans `06-choix-techniques.md` :

1. Critères d'admission d'une bibliothèque tierce : licence, activité de maintenance, popularité, nombre de dépendances transitives.
2. Épinglage des versions et outil de mise à jour automatisée.
3. Production d'une SBOM (Software Bill of Materials, nomenclature logicielle) si le profil est *Critique* ou si un client l'exige.
4. Fréquence de revue des dépendances.

### 2.7 Vérifier plutôt que se souvenir

Les connaissances d'un modèle d'IA (intelligence artificielle) ont une date limite. Pour toute affirmation sur une **version**, une **fin de support**, une **licence** ou une **fonctionnalité** précise, l'agent **doit** soit la vérifier (documentation officielle, dépôt du projet), soit la marquer « à vérifier » (règle d'or 14). Une version inventée ou périmée dans un ADR est une erreur silencieuse.

## 3. Déroulé de l'atelier

| Étape | L'agent | Le décideur |
|---|---|---|
| 1 | Dresse l'inventaire des choix (§ 2.1) et marque ceux déjà imposés par une `C-n`. | Complète. |
| 2 | Recense les compétences de l'équipe et les préférences de l'organisation. | Répond. |
| 3 | Pour chaque choix structurant : filtre, présélection, proposition de grille. | Fixe les poids, discute les notes. |
| 4 | Propose les preuves de concept nécessaires, avec leur question et leur durée. | Accepte ou refuse. |
| 5 | Rédige les ADR. | Arbitre. |
| 6 | Consolide `06-choix-techniques.md` : pile retenue, versions, politique des dépendances. | Relit. |
| 7 | Passe la liste de contrôle et invoque le relecteur critique. | Valide G6. |

## 4. Banque de questions

1. Quels langages et cadriciels l'équipe maîtrise-t-elle vraiment, c'est-à-dire en ayant déjà mis un système en production ?
2. L'organisation impose-t-elle ou interdit-elle certains fournisseurs, langages ou licences ?
3. Qui maintiendra le système dans trois ans ? La même équipe, un prestataire, une équipe interne à recruter ?
4. Quel est le budget mensuel pour l'hébergement et les licences ?
5. Les données doivent-elles rester dans un pays ou chez un hébergeur qualifié ?
6. Êtes-vous prêts à dépendre d'un service propriétaire d'un fournisseur de nuage, en échange d'une exploitation simplifiée ?

## 5. Livrables

| Fichier | Contenu minimal |
|---|---|
| `06-choix-techniques.md` | Tableau de la pile : catégorie, choix, version, ADR, alternatives écartées ; politique des dépendances |
| `adr/` | Un ADR par choix structurant, avec la grille |
| `ETAT.md` | Hypothèses et risques techniques |

## 6. Liste de contrôle de la gate G6

- [ ] ★ Chaque conteneur du C4 de niveau 2 a une technologie désignée.
- [ ] ★ Chaque choix structurant a un ADR qui compare au moins deux options.
- [ ] ★ Aucun choix ne viole une `C-n`.
- [ ] Les compétences de l'équipe ont été prises en compte explicitement.
- [ ] Les versions et fins de support citées ont été vérifiées ou marquées « à vérifier ».
- [ ] Chaque sous-domaine générique est acheté ou réutilisé, ou son développement est justifié.
- [ ] Les preuves de concept prévues ont été réalisées et leur résultat est consigné.
- [ ] La politique des dépendances est écrite.
- [ ] Le coût mensuel estimé d'exploitation est comparé au budget.

## 7. Anti-patterns

| Anti-pattern | Symptôme | Correction |
|---|---|---|
| Nouveauté pour la nouveauté | Choix d'un outil que personne ne connaît, sans `QS-n` qui l'exige | Coût de montée en compétence dans la grille ; préférer l'éprouvé. |
| Choix par habitude | « On a toujours fait comme ça » sans alternative | Au moins deux options dans l'ADR. |
| Preuve de concept promue | Le prototype devient le produit | Le code de la preuve de concept est jeté par définition. |
| Enfermement non vu | Service propriétaire adopté sans évaluer la sortie | Critère de réversibilité dans chaque grille. |
| Versions hallucinées | Version ou fonctionnalité affirmée par l'IA sans vérification | Règle d'or 14. |
