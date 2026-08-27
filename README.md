# ✖️ Les Tables Magiques

Application web d'entraînement aux **tables de multiplication** pour enfants, avec espace parent
protégé par code, minuteurs, système de points et **récompenses en dirhams**.

👉 **Application en ligne : https://VOTRE-COMPTE.github.io/multiplication/**
*(remplacez `VOTRE-COMPTE` par votre pseudo GitHub une fois le dépôt publié)*

L'interface tient dans un seul fichier autonome : [`index.html`](index.html). L'application est
aussi une **PWA installable** sur téléphone et tablette, et fonctionne ensuite **hors connexion**.

## Fonctionnalités

**Espace parent** (code secret : `8213`)
- Autant de profils enfants que nécessaire (prénom, avatar), **chacun avec ses propres réglages** ;
  bouton « ⧉ Dupliquer » pour créer un frère ou une sœur avec les mêmes réglages
- Intervalle de nombres (ex. de 1 à 10) et tables à travailler (1 à 12, plusieurs possibles)
- Temps accordé par question (en secondes)
- Temps total accordé pour la session (minutes + secondes)
- Nombre de questions de la session
- Nombre de réponses proposées par question (de 2 à 12)
- Durée de la pause après une erreur, pendant laquelle la bonne réponse reste affichée (0 à 10 s)
- Montant de la récompense en dirhams pour chaque série réussie sans faute
- **Abandons accordés par jour** (1 par défaut, 0 pour interdire complètement de quitter une partie)
- **Seuil de réactivation** du bouton « Quitter » (75 % de bonnes réponses par défaut) ;
  état du jour visible, avec un bouton de remise à zéro
- Solde de dirhams visible et modifiable
- Export / import des données en JSON (sauvegarde ou transfert d'appareil)

**Écran enfant** (accès libre, sans code)
- Sélection du profil, puis session de N questions
- **Plusieurs réponses proposées** par question (10 par défaut, réglable de 2 à 12) — l'enfant clique, il n'a rien à taper
- Minuteur circulaire par question + minuteur de session ; le dépassement du temps total
  arrête la session et annule le sans-faute
- Points : 3 pts si la réponse est donnée en moins de 3 s, 2 pts en moins de 6 s, 1 pt sinon ;
  une erreur coûte 1 point et casse la série
- Après une erreur ou un temps écoulé, la bonne réponse s'affiche en vert pendant la durée réglée par le parent
- Récompense versée si la session est **entièrement sans faute** dans le temps imparti
- **Bouton « Quitter »** : disponible une fois par jour (par défaut). Une fois utilisé, il
  **disparaît** pour les sessions suivantes, et n'est **réactivé qu'en dépassant 75 %** de bonnes
  réponses sur une session (seuil réglable). La session reste de toute façon bornée par le temps total.
- En fin de session, **récapitulatif « À revoir »** des multiplications ratées : le calcul, la bonne
  réponse en vert et la réponse donnée barrée en rouge (ou « pas de réponse » si le temps a expiré)
- Animations, confettis, sons de réussite, retour visuel immédiat
- Responsive : téléphone, tablette, ordinateur

## Installer sur mobile

Ouvrez l'adresse du site dans le navigateur du téléphone, puis :

- **Android (Chrome, Edge, Samsung Internet)** : bouton **« 📲 Installer l'appli »** sur l'écran
  d'accueil de l'application (ou menu ⋮ → « Installer l'application »).
- **iPhone / iPad (Safari)** : bouton **Partager** → **« Sur l'écran d'accueil »**. Le bouton
  d'installation de l'application rappelle la manipulation.
- **Ordinateur (Chrome, Edge)** : icône d'installation dans la barre d'adresse.

L'application s'ouvre alors en plein écran avec sa propre icône, et démarre **sans connexion** :
le service worker ([`sw.js`](sw.js)) met en cache l'interface et les icônes.
Fichiers concernés : [`manifest.webmanifest`](manifest.webmanifest), [`sw.js`](sw.js) et le dossier
`icons/` (régénérable avec `python tools/make-icons.py`, nécessite Pillow).

> ⚠️ L'installation exige **HTTPS** : elle fonctionne depuis l'adresse GitHub Pages, mais pas en
> ouvrant `index.html` en local (`file://`), où le bouton d'installation reste masqué.

## Données

Tout est enregistré dans le `localStorage` du navigateur (clé `tables-magiques-v1`) :
profils, réglages et soldes survivent au rechargement de la page. Les données restent
**sur l'appareil** — rien n'est envoyé sur le réseau. Un même enfant sur deux appareils
a donc deux soldes distincts ; utilisez l'export/import pour les transférer.

## Publier / mettre à jour

Le site est publié par GitHub Pages via le workflow [`.github/workflows/pages.yml`](.github/workflows/pages.yml) :
chaque `git push` sur `main` redéploie automatiquement la racine du dépôt.

Activation, une seule fois : **Settings → Pages → Build and deployment → Source : GitHub Actions**.

Après une modification de l'application, incrémentez `VERSION` dans [`sw.js`](sw.js) : les appareils
déjà installés récupèrent ainsi la nouvelle version au lancement suivant.

## En local

Ouvrez simplement `index.html` dans un navigateur (double-clic), ou, pour tester la partie PWA :

```bash
python -m http.server 8000   # puis http://localhost:8000
```

## Personnalisation

Le code secret parent est défini en haut du script de `index.html` :

```js
const CODE_PARENT = '8213';
```

Le cahier des charges d'origine se trouve dans [`prompt-application-multiplication.md`](prompt-application-multiplication.md).
