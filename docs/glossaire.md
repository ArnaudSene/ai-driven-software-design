# Glossaire du guide

Ce glossaire définit les acronymes et les termes employés **dans le guide**. Le vocabulaire métier d'un projet conçu avec le guide va dans son propre `conception/glossaire.md` (phase 4).

Règle de rédaction appliquée à tout le dépôt : **à la première occurrence d'un acronyme dans chaque fichier, sa forme développée est donnée entre parenthèses.** La règle s'applique fichier par fichier, car un agent peut ne charger qu'un seul fichier. Le script [`scripts/check_acronyms.py`](../scripts/check_acronyms.py) la vérifie.

---

## 1. Acronymes

| Acronyme | Forme développée | Définition |
|---|---|---|
| **ABAC** | Attribute-Based Access Control | Contrôle d'accès fondé sur les attributs de l'utilisateur, de la ressource et du contexte. |
| **ACL** | Anti-Corruption Layer | Couche anticorruption : traduit le modèle d'un système externe pour protéger le modèle du domaine. *Ne pas confondre avec Access Control List, non employé dans ce guide.* |
| **ADR** | Architecture Decision Record | Registre de décision d'architecture : document court qui consigne une décision, son contexte, les options et les conséquences. |
| **AIPD** | Analyse d'impact relative à la protection des données | Étude exigée par le RGPD pour les traitements à risque élevé pour les personnes. |
| **ANSSI** | Agence nationale de la sécurité des systèmes d'information | Autorité française de cybersécurité. |
| **API** | Application Programming Interface | Interface de programmation par laquelle un logiciel expose ses services à d'autres. |
| **ASVS** | Application Security Verification Standard | Référentiel d'exigences de sécurité applicative publié par l'OWASP, en trois niveaux. |
| **ATAM** | Architecture Tradeoff Analysis Method | Méthode du SEI d'évaluation d'une architecture face à ses scénarios qualité. |
| **BC** | Bounded Context | Contexte délimité : frontière à l'intérieur de laquelle un modèle et son langage sont cohérents. Préfixe `BC-n`. |
| **BDD** | Behavior-Driven Development | Développement piloté par le comportement : spécifications sous forme d'exemples exécutables. |
| **BR** | Business Rule | Règle métier. Préfixe `BR-n`. |
| **C4** | Context, Containers, Components, Code | Modèle de diagrammes d'architecture de Simon Brown, en quatre niveaux de zoom. |
| **CA** | Critère d'acceptation | Condition, exprimée en *Étant donné / Quand / Alors*, à laquelle un cas d'utilisation est considéré comme livré. Préfixe `CA-n`. |
| **CD** | Continuous Delivery / Continuous Deployment | Livraison continue (chaque version est prête à être déployée) ou déploiement continu (chaque version est déployée automatiquement). |
| **CI** | Continuous Integration | Intégration continue : chaque modification est automatiquement compilée et testée. |
| **CNIL** | Commission nationale de l'informatique et des libertés | Autorité française de protection des données personnelles. |
| **CQRS** | Command Query Responsibility Segregation | Séparation des modèles d'écriture (commandes) et de lecture (requêtes). |
| **CRUD** | Create, Read, Update, Delete | Les quatre opérations élémentaires sur des données ; désigne un modèle sans logique métier riche. |
| **CVE** | Common Vulnerabilities and Exposures | Référentiel public des vulnérabilités connues. |
| **DAST** | Dynamic Application Security Testing | Test de sécurité d'une application en cours d'exécution. |
| **DDD** | Domain-Driven Design | Conception pilotée par le domaine (Eric Evans). |
| **DoD** | Definition of Done | Définition de « terminé » : conditions pour considérer un incrément achevé. |
| **DoR** | Definition of Ready | Définition de « prêt » : conditions pour démarrer un incrément. |
| **DORA** | Digital Operational Resilience Act | Règlement européen sur la résilience opérationnelle numérique du secteur financier. |
| **DSL** | Domain-Specific Language | Langage dédié à un domaine particulier. |
| **EARS** | Easy Approach to Requirements Syntax | Gabarits de phrases pour rédiger des exigences sans ambiguïté. |
| **FF** | Fitness Function | Fonction d'aptitude : test automatisé d'une caractéristique de l'architecture. Préfixe `FF-n`. |
| **gRPC** | gRPC Remote Procedure Calls | Protocole d'appel de procédure distante fondé sur HTTP/2 et Protocol Buffers. |
| **HDS** | Hébergeur de données de santé | Certification française exigée pour héberger des données de santé. |
| **HTTP** | Hypertext Transfer Protocol | Protocole de transfert du web. |
| **IA** | Intelligence artificielle | Ici : l'agent, fondé sur un grand modèle de langage, qui conduit le processus. |
| **IaaS** | Infrastructure as a Service | Infrastructure (machines, réseau, stockage) louée à la demande. |
| **IaC** | Infrastructure as Code | Infrastructure décrite par du code versionné et appliquée automatiquement. |
| **IEC** | International Electrotechnical Commission | Commission électrotechnique internationale, coéditrice de normes avec l'ISO. |
| **IETF** | Internet Engineering Task Force | Organisme de normalisation des protocoles de l'Internet. |
| **INC** | Incrément | Tranche verticale de réalisation. Préfixe `INC-n`. |
| **INVEST** | Independent, Negotiable, Valuable, Estimable, Small, Testable | Critères de qualité d'un récit utilisateur. |
| **ISO** | International Organization for Standardization | Organisation internationale de normalisation. |
| **JSON** | JavaScript Object Notation | Format texte d'échange de données structurées. |
| **LTS** | Long-Term Support | Version bénéficiant d'un support prolongé. |
| **MADR** | Markdown Architectural Decision Records | Gabarit d'ADR au format Markdown. |
| **MFA** | Multi-Factor Authentication | Authentification multifacteur. |
| **MIT** | Massachusetts Institute of Technology | Nom de la licence libre permissive sous laquelle le guide est distribué. |
| **MoSCoW** | Must, Should, Could, Won't | Méthode de priorisation : doit, devrait, pourrait, pas cette fois. |
| **MVP** | Minimum Viable Product | Produit minimum viable : plus petite version qui permet d'apprendre si le produit atteint ses objectifs. |
| **NIS** | Network and Information Security | Directive européenne (version 2) sur la sécurité des réseaux et des systèmes d'information. |
| **OB** | Objectif métier | Changement mesurable attendu dans le monde réel. Préfixe `OB-n`. |
| **OD** | Open Decision | Décision ouverte : question en attente d'arbitrage par le décideur. Préfixe `OD-n`. |
| **OHS** | Open Host Service | Service hôte ouvert : interface stable exposée à tous les consommateurs d'un contexte. |
| **OIDC** | OpenID Connect | Protocole d'authentification fédérée fondé sur OAuth 2. |
| **OWASP** | Open Worldwide Application Security Project | Fondation qui publie des référentiels de sécurité applicative. |
| **PaaS** | Platform as a Service | Plateforme d'exécution gérée, louée à la demande. |
| **PCA** | Plan de continuité d'activité | Dispositif qui maintient le service, éventuellement dégradé, pendant un sinistre. |
| **PCI DSS** | Payment Card Industry Data Security Standard | Norme de sécurité des données des cartes de paiement. |
| **PL** | Published Language | Langage publié : format d'échange documenté et partagé entre contextes. |
| **PoC** | Proof of Concept | Preuve de concept : prototype jetable qui répond à une question technique. |
| **PP** | Partie prenante | Personne ou organisation concernée par le système. Préfixe `PP-n`. |
| **PRA** | Plan de reprise d'activité | Procédure de redémarrage du service après un sinistre. |
| **QS** | Quality Scenario | Scénario d'attribut qualité à six parties (source, stimulus, environnement, artefact, réponse, mesure). Préfixe `QS-n`. |
| **RACI** | Responsible, Accountable, Consulted, Informed | Matrice de responsabilités : réalise, approuve, est consulté, est informé. |
| **RBAC** | Role-Based Access Control | Contrôle d'accès fondé sur les rôles. |
| **RED** | Rate, Errors, Duration | Méthode de supervision d'un service : débit, erreurs, durée. |
| **REST** | Representational State Transfer | Style d'architecture d'interfaces sur HTTP, centré sur les ressources. |
| **RFC** | Request For Comments | Série de documents de normalisation de l'IETF. |
| **RGAA** | Référentiel général d'amélioration de l'accessibilité | Référentiel français d'accessibilité numérique, fondé sur les WCAG. |
| **RGPD** | Règlement général sur la protection des données | Règlement européen 2016/679 sur les données personnelles. |
| **RPO** | Recovery Point Objective | Perte de données maximale admissible, exprimée en durée. |
| **RTO** | Recovery Time Objective | Durée d'interruption maximale admissible. |
| **SaaS** | Software as a Service | Logiciel fourni comme un service en ligne. |
| **SAST** | Static Application Security Testing | Analyse de sécurité du code source, sans exécution. |
| **SBOM** | Software Bill of Materials | Nomenclature logicielle : inventaire des composants et dépendances. |
| **SCA** | Software Composition Analysis | Analyse des dépendances tierces (vulnérabilités, licences). |
| **SEI** | Software Engineering Institute | Institut de l'Université Carnegie Mellon, auteur des scénarios qualité et de l'ATAM. |
| **SGBD** | Système de gestion de base de données | Logiciel qui stocke et interroge des données. |
| **SLA** | Service Level Agreement | Accord de niveau de service contractuel. |
| **SLI** | Service Level Indicator | Indicateur de niveau de service, mesuré du point de vue de l'utilisateur. |
| **SLO** | Service Level Objective | Objectif de niveau de service. Préfixe `SLO-n`. |
| **SRE** | Site Reliability Engineering | Ingénierie de la fiabilité des systèmes en production. |
| **SSO** | Single Sign-On | Authentification unique pour plusieurs applications. |
| **STRIDE** | Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege | Classification des menaces : usurpation, altération, répudiation, divulgation, déni de service, élévation de privilège. |
| **TCO** | Total Cost of Ownership | Coût total de possession. |
| **TDD** | Test-Driven Development | Développement piloté par les tests : le test est écrit avant le code. |
| **TLS** | Transport Layer Security | Protocole de chiffrement des communications. |
| **UC** | Use Case | Cas d'utilisation. Préfixe `UC-n`. |
| **URL** | Uniform Resource Locator | Adresse d'une ressource sur le web. |
| **USE** | Utilization, Saturation, Errors | Méthode de supervision d'une ressource : utilisation, saturation, erreurs. |
| **UTF** | Unicode Transformation Format | Famille d'encodages des caractères Unicode ; UTF-8 est la référence. |
| **UUID** | Universally Unique Identifier | Identifiant unique de 128 bits ; la version 7 est ordonnée dans le temps. |
| **WCAG** | Web Content Accessibility Guidelines | Règles internationales pour l'accessibilité des contenus web. |
| **YAML** | YAML Ain't Markup Language | Format texte de sérialisation lisible, utilisé pour les contrats et la configuration. |

## 2. Préfixes d'identifiants à une lettre

| Préfixe | Signification |
|---|---|
| `C-n` | Contrainte |
| `H-n` | Hypothèse |
| `M-n` | Menace |
| `R-n` | Risque |

Le registre complet des préfixes est dans [00-principes § 8](00-principes.md#8-identifiants).

## 3. Termes

| Terme | Définition |
|---|---|
| **Agrégat** | Groupe d'objets du domaine modifié comme un tout, qui garantit des invariants. Une transaction ne modifie qu'un agrégat. |
| **Architecturalement significatif** | Se dit d'un scénario qualité d'importance et de difficulté élevées, qui doit être traité explicitement par l'architecture. |
| **arc42** | Gabarit de documentation d'architecture en douze sections (Gernot Starke, Peter Hruschka). |
| **Architecture hexagonale** | Organisation du code où le domaine ne dépend de rien et communique avec l'extérieur par des *ports* implémentés par des *adaptateurs* (Alistair Cockburn). Aussi appelée « ports et adaptateurs ». |
| **Clean Architecture** | Variante de l'architecture hexagonale formalisée par Robert C. Martin, fondée sur la règle de dépendance vers le centre. |
| **Budget d'erreur** | Part d'indisponibilité ou d'erreurs tolérée par un SLO (Service Level Objective) sur une fenêtre de temps. |
| **Carte des contextes** | Diagramme des contextes délimités et des patrons de relation entre eux. |
| **Critère de conformité** | Condition mesurable qui permet d'écrire un test échouant de façon déterministe quand une règle est violée. |
| **Décideur** | Humain qui porte la vision du produit, arbitre et valide les gates. |
| **Event Storming** | Atelier de modélisation par les événements métier (Alberto Brandolini). |
| **Example Mapping** | Atelier de découverte des règles et des exemples à l'aide de quatre types de cartes (Matt Wynne). |
| **Frontière de confiance** | Point où une donnée ou une requête passe d'un niveau de confiance à un autre. |
| **Gate** | Point de validation humaine qui clôt une phase. |
| **Gherkin** | Syntaxe *Given / When / Then* (*Étant donné / Quand / Alors*) de description de scénarios de test. |
| **Idempotence** | Propriété d'une opération dont la répétition produit le même effet qu'une exécution unique. |
| **Langage omniprésent** | Vocabulaire partagé par le métier, la documentation et le code dans un contexte délimité (*ubiquitous language*). |
| **Monolithe modulaire** | Application déployée d'un seul bloc mais découpée en modules aux frontières strictes. |
| **Orchestrateur** | Agent IA (intelligence artificielle) qui conduit le processus de conception. |
| **Outbox transactionnel** | Patron qui enregistre un événement dans la même transaction que la modification métier, puis le publie de façon fiable. |
| **Saga** | Enchaînement de transactions locales avec des actions de compensation en cas d'échec. |
| **Seuil à fixer** | Marqueur « [seuil à fixer] » d'une valeur attendue du décideur ; toujours rattaché à une OD (Open Decision). |
| **Sourcing d'événements** | Persistance de l'état sous la forme de la suite des événements qui l'ont produit (*event sourcing*). |
| **Sous-domaine** | Partie du métier, classée *Cœur*, *Support* ou *Générique*. |
| **Squelette ambulant** | Implémentation minimale qui traverse toute l'architecture de bout en bout (*walking skeleton*). |
| **Tactique** | Technique de conception qui agit sur un attribut qualité (cache, redondance, disjoncteur…). |
| **Volere** | Cadre de spécification des exigences de Suzanne et James Robertson. |
