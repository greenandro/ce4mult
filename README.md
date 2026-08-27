# ✖️ Les Tables Magiques

Application web d'entraînement aux **tables de multiplication** pour enfants, avec espace parent
protégé par code, minuteurs, système de points et **récompenses en dirhams**.

👉 **Application en ligne : https://VOTRE-COMPTE.github.io/multiplication/**
*(remplacez `VOTRE-COMPTE` par votre pseudo GitHub une fois le dépôt publié)*

Tout tient dans un seul fichier autonome : [`index.html`](index.html) — aucune installation,
aucun serveur, aucune dépendance.

## Fonctionnalités

**Espace parent** (code secret : `8213`)
- Plusieurs profils enfants (prénom, avatar), chacun avec ses propres réglages
- Intervalle de nombres (ex. de 1 à 10) et tables à travailler (1 à 12, plusieurs possibles)
- Temps accordé par question (en secondes)
- Temps total accordé pour la session (minutes + secondes)
- Nombre de questions de la session
- Nombre de réponses proposées par question (de 2 à 12)
- Montant de la récompense en dirhams pour chaque série réussie sans faute
- Solde de dirhams visible et modifiable
- Export / import des données en JSON (sauvegarde ou transfert d'appareil)

**Écran enfant** (accès libre, sans code)
- Sélection du profil, puis session de N questions
- **Plusieurs réponses proposées** par question (10 par défaut, réglable de 2 à 12) — l'enfant clique, il n'a rien à taper
- Minuteur circulaire par question + minuteur de session ; le dépassement du temps total
  arrête la session et annule le sans-faute
- Points : 3 pts si la réponse est donnée en moins de 3 s, 2 pts en moins de 6 s, 1 pt sinon ;
  une erreur coûte 1 point et casse la série
- Récompense versée uniquement si la session est **entièrement sans faute** dans le temps imparti
- Animations, confettis, sons de réussite, retour visuel immédiat
- Responsive : téléphone, tablette, ordinateur

## Données

Tout est enregistré dans le `localStorage` du navigateur (clé `tables-magiques-v1`) :
profils, réglages et soldes survivent au rechargement de la page. Les données restent
**sur l'appareil** — rien n'est envoyé sur le réseau. Un même enfant sur deux appareils
a donc deux soldes distincts ; utilisez l'export/import pour les transférer.

## Publier / mettre à jour

Le site est publié par GitHub Pages via le workflow [`.github/workflows/pages.yml`](.github/workflows/pages.yml) :
chaque `git push` sur `main` redéploie automatiquement la racine du dépôt.

Activation, une seule fois : **Settings → Pages → Build and deployment → Source : GitHub Actions**.

## En local

Ouvrez simplement `index.html` dans un navigateur (double-clic), ou :

```bash
python -m http.server 8000   # puis http://localhost:8000
```

## Personnalisation

Le code secret parent est défini en haut du script de `index.html` :

```js
const CODE_PARENT = '8213';
```

Le cahier des charges d'origine se trouve dans [`prompt-application-multiplication.md`](prompt-application-multiplication.md).
