# PROMPT — Application web de multiplication pour enfants

Copiez-collez le texte ci-dessous dans votre outil de développement IA (Claude Code, Claude.ai, ou autre) pour générer l'application.

---

## RÔLE

Tu es un développeur front-end senior spécialisé en design d'interfaces ludiques pour enfants. Crée une application web complète, en un seul fichier HTML autonome (HTML + CSS + JS inclus), responsive (mobile, tablette, ordinateur).

## OBJECTIF

Une application d'entraînement aux tables de multiplication, personnalisable par un parent, avec système de points, de vitesse, et de récompense financière virtuelle.

## FONCTIONNALITÉS DÉTAILLÉES

### 1. Écran de configuration (parent)
- Accessible uniquement via un code secret : **8213**
- Le parent doit pouvoir définir, pour chaque enfant :
  - Un intervalle de nombres (ex : de 1 à 10)
  - Une ou plusieurs tables de multiplication à travailler (ex : table de 7)
  - Le **temps accordé par question** (en secondes)
  - Le **temps total accordé pour l'ensemble de la session** (en minutes/secondes)
  - Le **nombre de questions** de la session (remplace la valeur fixe de 20, devient paramétrable)
  - Le **montant de la récompense en dirhams** attribué pour chaque série réussie sans faute
- Possibilité de créer/gérer plusieurs profils enfants, chacun avec ses propres réglages
- Le solde de dirhams accumulés par enfant doit être visible et modifiable depuis cet écran

### 2. Écran de jeu (enfant)
- Sélection du profil enfant (sans code, accès libre)
- Session de **N questions** de multiplication (N défini par le parent), générées selon les paramètres définis pour cet enfant
- Chaque question a un **temps limité configurable par le parent**, affiché avec un minuteur visuel (barre ou cercle qui se vide)
- La session entière est également soumise à un **temps total configurable** ; si ce temps est dépassé avant la fin des questions, la session s'arrête et n'est pas validée en sans-faute
- Interface colorée, grandes touches/boutons, animations simples, adaptée aux enfants (police lisible, feedback visuel immédiat bonne/mauvaise réponse)
- Pour chaque question, l'enfant doit voir **10 réponses proposées sous forme de boutons cliquables** (dont une seule est correcte, les 9 autres sont des distracteurs plausibles générés aléatoirement). L'enfant répond en cliquant sur la réponse de son choix, sans avoir à taper de chiffres

### 3. Système de points et pénalités
- Réponse rapide et correcte = plus de points (ex : 3 pts si <3s, 2 pts si <6s, 1 pt sinon)
- Réponse fausse = perte d'un point + rupture de la série de bonnes réponses en cours
- **Aucune erreur tolérée** sur l'ensemble des N questions de la session pour valider la session en mode "sans faute"

### 4. Système de récompense
- Si l'enfant termine les N questions **sans aucune erreur** (sans-faute complet), dans le temps imparti : il gagne le **montant en dirhams configuré par le parent** pour ce profil
- Le montant s'accumule à chaque série réussie (visible sur le profil de l'enfant)
- Affichage clair du solde total accumulé
- Message de félicitations / animation à chaque récompense débloquée
- Si une erreur est commise, la session ne valide pas la récompense ; l'enfant est encouragé à réessayer

### 5. Stockage des données
- Utiliser le stockage disponible dans l'environnement cible pour sauvegarder les profils, paramètres, et soldes de dirhams de façon persistante (pas de perte de données en rechargeant la page)

## STYLE VISUEL
- Design ludique, coloré, pensé pour des enfants (typographie ronde et lisible, gros boutons, icônes/émojis, animations de succès)
- Responsive : doit bien fonctionner sur téléphone, tablette et ordinateur

## LIVRABLE ATTENDU
Un fichier unique et fonctionnel, prêt à l'emploi, incluant l'écran de configuration parent (protégé par code), l'écran de sélection du profil enfant, et l'écran de jeu avec minuteur, scoring, et système de récompense en dirhams.
