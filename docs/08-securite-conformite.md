# Phase 8 — Sécurité et conformité

| Clé | Valeur |
|---|---|
| Question centrale | Contre quoi le système doit-il se protéger, et quelles obligations doit-il respecter ? |
| Agent | [`prompts/specialiste-securite.md`](../prompts/specialiste-securite.md) |
| Entrées | `01-cadrage.md` (`C-n` légales), `02` (matrice rôle × action), `03` (`QS-n` de sécurité), `05` (C4 (Context, Containers, Components, Code) de niveau 2), `06`, `07` (classification des données, contrats) |
| Sorties | `conception/08-securite.md`, ADR (Architecture Decision Record) de sécurité, `BR-n` et `QS-n` complémentaires |
| Identifiants créés | `M-n` |
| Gabarit | [`templates/08-securite.md`](../templates/08-securite.md) |
| Gate | G8 |

---

## 1. Pourquoi cette phase

La sécurité ajoutée après coup coûte cher et reste fragile. Traitée à la conception, elle se résume souvent à quelques décisions bien placées : frontières de confiance, modèle d'autorisation, gestion des secrets, journalisation.

Cette phase vient **après** l'architecture et les données, car on ne peut modéliser les menaces que d'un système dont on connaît les flux et les données. Mais elle peut **rouvrir** ces phases : une menace peut imposer un changement d'architecture (§ 14 des principes).

## 2. Concepts et méthodes

### 2.1 Modélisation des menaces

Méthode fondée sur les quatre questions d'Adam Shostack :

1. **Sur quoi travaille-t-on ?** Diagramme de flux de données, construit à partir du C4 de niveau 2 : processus, stockages, flux, acteurs externes et **frontières de confiance** (tout point où l'on passe d'un niveau de confiance à un autre : Internet → application, application → base, application → tiers).
2. **Qu'est-ce qui peut mal tourner ?** Application de STRIDE (classification des menaces détaillée ci-dessous) à chaque élément et à chaque flux qui traverse une frontière.
3. **Que fait-on contre ?** Une mesure par menace retenue : éviter, réduire, transférer ou accepter.
4. **A-t-on bien travaillé ?** Revue et tests de sécurité (phase 10).

STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) :

| Catégorie | Menace | Propriété violée | Question type |
|---|---|---|---|
| **S**poofing | Usurpation d'identité | Authenticité | Quelqu'un peut-il se faire passer pour un utilisateur ou un service ? |
| **T**ampering | Altération | Intégrité | Une donnée peut-elle être modifiée en transit ou au repos ? |
| **R**epudiation | Répudiation | Non-répudiation | Un utilisateur peut-il nier une action faute de preuve ? |
| **I**nformation disclosure | Divulgation | Confidentialité | Une donnée peut-elle fuiter (réponse d'une interface, journaux, message d'erreur, sauvegarde) ? |
| **D**enial of service | Déni de service | Disponibilité | Peut-on épuiser une ressource ou bloquer le service ? |
| **E**levation of privilege | Élévation de privilège | Autorisation | Un utilisateur peut-il faire ce que son rôle n'autorise pas ? |

### 2.2 Fiche de menace (`M-n`)

| Rubrique | Contenu |
|---|---|
| Élément ou flux | Composant ou flux concerné, frontière traversée |
| Catégorie STRIDE | S, T, R, I, D ou E |
| Scénario | Comment l'attaque se déroule, concrètement |
| Vraisemblance | Faible, Moyenne, Élevée |
| Impact | Faible, Moyen, Élevé, en citant les données (classification de la phase 7) |
| Réponse | Éviter, Réduire, Transférer, Accepter (avec la signature du décideur) |
| Mesure | Contrôle retenu, avec renvoi vers `ADR`, `BR-n` ou `QS-n` |
| Vérification | Test ou contrôle qui prouve que la mesure fonctionne |
| Statut | Ouverte, Mitigée, Acceptée |

### 2.3 Niveau d'exigence de sécurité

On adosse les exigences de sécurité à l'ASVS (Application Security Verification Standard) publié par l'OWASP (Open Worldwide Application Security Project), plutôt que de les réinventer :

| Profil | Niveau ASVS visé |
|---|---|
| Prototype | Niveau 1 sur les chapitres authentification, contrôle d'accès, validation des entrées |
| Produit | Niveau 2 |
| Critique | Niveau 2 minimum, niveau 3 pour les composants qui traitent les données les plus sensibles |

Le Top 10 de l'OWASP sert de liste de sensibilisation, pas de référentiel d'exigences.

### 2.4 Décisions de sécurité à prendre

| Sujet | Décisions |
|---|---|
| **Authentification** | Délégation à un fournisseur d'identité via OIDC (OpenID Connect) ou gestion interne ; authentification multifacteur, dite MFA (Multi-Factor Authentication), pour quels rôles ; SSO (Single Sign-On, authentification unique) avec l'annuaire de l'entreprise ; politique de mots de passe ou connexion sans mot de passe |
| **Sessions et jetons** | Durée de vie, renouvellement, révocation, stockage côté client |
| **Autorisation** | Modèle : RBAC (Role-Based Access Control, contrôle d'accès par rôle), ABAC (Attribute-Based Access Control, par attributs), par relation ; construit à partir de la matrice rôle × action de la phase 2 ; contrôle **côté serveur** à chaque requête ; cloisonnement entre organisations clientes |
| **Validation des entrées** | À chaque frontière de confiance ; encodage des sorties |
| **Chiffrement** | En transit : TLS (Transport Layer Security) partout, y compris en interne si la frontière le justifie. Au repos : selon la classification des données. Gestion et rotation des clés. |
| **Secrets** | Coffre à secrets ; aucun secret dans le code, la configuration versionnée ou les journaux |
| **Journalisation de sécurité** | Événements tracés (connexions, échecs, changements de droits, accès aux données sensibles) ; intégrité et durée de conservation des journaux ; **aucune** donnée sensible ni secret journalisé |
| **Protection contre les abus** | Limitation du débit, protection contre l'automatisation, quotas |
| **Chaîne d'approvisionnement** | Analyse des dépendances, dite SCA (Software Composition Analysis) ; analyse statique du code, dite SAST (Static Application Security Testing) ; analyse dynamique, dite DAST (Dynamic Application Security Testing) ; SBOM (Software Bill of Materials, nomenclature logicielle) ; signature des artefacts |
| **Gestion des incidents** | Qui est alerté, qui décide, comment on notifie les personnes et les autorités, dans quels délais |

Chaque décision structurante fait l'objet d'un ADR.

### 2.5 Protection des données personnelles

Si le système traite des données personnelles (classification de la phase 7), le RGPD (Règlement général sur la protection des données) s'applique. L'agent vérifie avec le décideur :

| Point | Livrable ou décision |
|---|---|
| Finalités et base légale | Pour chaque traitement : pourquoi, et sur quel fondement (contrat, obligation légale, consentement, intérêt légitime…) |
| Minimisation | Chaque donnée collectée est-elle nécessaire à une finalité ? |
| Durées de conservation | Reprises de la phase 7 |
| Droits des personnes | Accès, rectification, effacement, portabilité, opposition : quel `UC-n` les met en œuvre ? |
| Sous-traitants | Hébergeur, prestataires : contrats, localisation, transferts hors de l'Union européenne |
| Registre des traitements | Entrée à créer ou à mettre à jour par le responsable de traitement |
| AIPD (analyse d'impact relative à la protection des données) | Obligatoire en cas de risque élevé pour les personnes (données sensibles à grande échelle, surveillance systématique, profilage…) |
| Délégué à la protection des données | À consulter si l'organisation en a désigné un |

L'agent **ne donne pas d'avis juridique** : il signale les obligations probables et recommande la consultation d'un juriste ou du délégué à la protection des données. Les références officielles, comme les recommandations de la CNIL (Commission nationale de l'informatique et des libertés) pour la France, doivent être vérifiées à la source.

### 2.6 Autres conformités fréquentes

À interroger selon le secteur, sans prétendre à l'exhaustivité ; chaque obligation retenue devient une `C-n` :

| Domaine | Exemples de référentiels |
|---|---|
| Santé | Hébergement agréé ou certifié HDS (hébergeur de données de santé) en France |
| Paiement par carte | PCI DSS (Payment Card Industry Data Security Standard) : souvent évité en déléguant la saisie de carte au prestataire de paiement |
| Services essentiels et importants | Directive européenne NIS (Network and Information Security, sécurité des réseaux et des systèmes d'information) 2 |
| Secteur financier | Règlement européen DORA (Digital Operational Resilience Act, résilience opérationnelle numérique) |
| Services publics | RGAA (Référentiel général d'amélioration de l'accessibilité), référentiels de sécurité de l'administration |
| Informatique en nuage sensible | Qualification SecNumCloud délivrée par l'ANSSI (Agence nationale de la sécurité des systèmes d'information) |

## 3. Déroulé de l'atelier

| Étape | L'agent | Le décideur |
|---|---|---|
| 1 | Construit le diagramme de flux de données et marque les frontières de confiance. | Valide. |
| 2 | Applique STRIDE à chaque élément et chaque flux traversant une frontière ; rédige les `M-n`. | Évalue l'impact métier. |
| 3 | Propose une réponse et une mesure pour chaque `M-n`. | Accepte ou refuse ; signe les risques acceptés. |
| 4 | Fixe le niveau ASVS et en extrait les exigences applicables sous forme de `QS-n` ou de `BR-n`. | Valide. |
| 5 | Fait trancher les décisions de sécurité (§ 2.4) et rédige les ADR. | Arbitre. |
| 6 | Conduit la revue de protection des données personnelles (§ 2.5). | Répond ; consulte le juriste si nécessaire. |
| 7 | Recense les autres conformités (§ 2.6) et les ajoute en `C-n`. | Confirme. |
| 8 | Signale les phases amont à rouvrir, le cas échéant. | Décide. |
| 9 | Passe la liste de contrôle et invoque le relecteur critique. | Valide G8. |

## 4. Banque de questions

1. Quelle serait la pire fuite de données possible ? Et la pire modification silencieuse ?
2. Qui sont les attaquants plausibles : opportunistes, concurrents, employés malveillants, fraudeurs, États ?
3. Existe-t-il un annuaire d'entreprise ou un fournisseur d'identité à utiliser ?
4. Un utilisateur peut-il appartenir à plusieurs organisations, avec des droits différents ?
5. Faut-il prouver juridiquement qu'un utilisateur a effectué une action (signature, horodatage) ?
6. Les données personnelles quittent-elles l'Union européenne, même pour du support ou de la sauvegarde ?
7. Existe-t-il une politique de sécurité de l'organisation, un responsable de la sécurité, un délégué à la protection des données ?
8. Qui doit être prévenu, et en combien de temps, en cas d'incident de sécurité ?

## 5. Livrables

| Fichier | Contenu minimal |
|---|---|
| `08-securite.md` | Diagramme de flux et frontières de confiance, registre des `M-n`, niveau ASVS, décisions de sécurité, revue de protection des données, conformités |
| `adr/` | Authentification, autorisation, gestion des secrets, chiffrement |
| `02`, `03`, `01` | `BR-n`, `QS-n` et `C-n` ajoutées, marquées « issues de la phase 8 » |

## 6. Liste de contrôle de la gate G8

- [ ] ★ Les frontières de confiance sont identifiées sur un diagramme.
- [ ] ★ Le modèle d'autorisation couvre toute la matrice rôle × action et le contrôle est fait côté serveur.
- [ ] ★ La gestion des secrets est décidée ; aucun secret n'est prévu dans le code ou la configuration versionnée.
- [ ] ★ La présence de données personnelles est établie et, le cas échéant, la revue RGPD est faite.
- [ ] Chaque flux traversant une frontière a été passé au crible de STRIDE.
- [ ] Chaque `M-n` a une réponse ; chaque risque accepté porte la décision explicite du décideur.
- [ ] Chaque mesure a une vérification prévue (test, analyse, revue).
- [ ] Le niveau ASVS est fixé et ses exigences applicables sont reprises.
- [ ] La journalisation de sécurité et la gestion des incidents sont définies.
- [ ] La chaîne d'approvisionnement logicielle est couverte (dépendances, analyses, artefacts).
- [ ] Les conformités sectorielles ont été interrogées.

## 7. Anti-patterns

| Anti-pattern | Symptôme | Correction |
|---|---|---|
| Sécurité par l'interface | Boutons masqués pour les rôles non autorisés, sans contrôle côté serveur | Autorisation vérifiée côté serveur, à chaque requête. |
| Authentification maison | Stockage et vérification de mots de passe développés sur mesure | Déléguer à un fournisseur d'identité éprouvé, sauf justification par ADR. |
| Journaux bavards | Jetons, mots de passe ou données personnelles dans les journaux | Liste explicite des champs interdits, filtrage automatique. |
| Risque accepté par défaut | Menaces sans réponse | Une réponse par menace ; l'acceptation est une décision signée. |
| Conformité supposée | « Nous ne sommes pas concernés par le RGPD » sans analyse | Parcourir la classification des données de la phase 7. |
| Agent juriste | Avis juridique définitif rendu par l'IA (intelligence artificielle) | Signaler, recommander un juriste ou le délégué à la protection des données. |
