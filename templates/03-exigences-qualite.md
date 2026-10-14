# 03 — Exigences qualité — <Nom du projet>

| Statut | Version | Date | Gate |
|---|---|---|---|
| Brouillon | 0.1 | <AAAA-MM-JJ> | G3 : — |

## 1. Profil de charge et volumétrie

| Grandeur | Aujourd'hui | À 1 an | À 3 ans | Source |
|---|---|---|---|---|
| Utilisateurs inscrits | | | | |
| Utilisateurs actifs simultanés au pic | | | | |
| Opérations métier clés par jour | | | | |
| Pic horaire ou saisonnier | | | | |
| Volume de données créé par an | | | | |
| Durée de conservation | | | | |

## 2. Couverture des caractéristiques de qualité

<!-- Les neuf caractéristiques de la norme ISO (International Organization for Standardization) / IEC (International Electrotechnical Commission) 25010. -->

| Caractéristique | Scénarios | Ou « sans objet », avec justification |
|---|---|---|
| Adéquation fonctionnelle | | |
| Efficacité de performance | | |
| Compatibilité | | |
| Capacité d'interaction | | |
| Fiabilité | | |
| Sécurité | | |
| Maintenabilité | | |
| Flexibilité | | |
| Innocuité | | |

## 3. Scénarios qualité

### QS-1 — <Titre>

- **Caractéristique** : <caractéristique › sous-caractéristique>
- **Source** :
- **Stimulus** :
- **Environnement** :
- **Artefact** :
- **Réponse** :
- **Mesure de la réponse** : <valeur chiffrée ou [seuil à fixer]>
- **Justification** :
- **Priorité** : Must / Should / Could / Won't
- **Liens** : OB-n, C-n, BR-n, IR-n
- **OD** (décision ouverte) : OD-n

## 4. Arbre d'utilité

| Scénario (QS) | Importance métier (H/M/B) | Difficulté technique (H/M/B) | Significatif pour l'architecture |
|---|---|---|---|
| QS-1 | | | Oui / Non |

## 5. Conflits et arbitrages

| Scénarios en tension | Nature du conflit | Options | Arbitrage ou OD |
|---|---|---|---|
| | | | |

## 6. Besoins d'interaction significatifs pour l'architecture

<!-- Si le système a des utilisateurs finaux : liste des scénarios d'utilisabilité du SEI (Software Engineering Institute),
     rapport `CMU/SEI-2001-TR-005`. Chaque besoin retenu devient un QS-n.
     Une ligne par scénario du rapport (vingt-six) ; les cinq lignes ci-dessous sont des exemples. -->

| Scénario du SEI | Retenu (oui / non) | Scénario qualité (QS) | Justification |
|---|---|---|---|
| Annuler une opération en cours | | | |
| Défaire | | | |
| Observer l'état du système | | | |
| Agréger des données | | | |
| Rester cohérent entre les vues | | | |
