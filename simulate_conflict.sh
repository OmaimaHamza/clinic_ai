#!/usr/bin/env bash
# Simule le conflit (étapes 07-08) : à lancer DANS votre dépôt cloné, branche preproduction à jour.
set -e
git checkout preproduction && git pull
echo "Ligne de départ : version=1.0" > conflit.txt
git add conflit.txt && git commit -m "chore: fichier de base pour le conflit" && git push

git checkout -b feature/membre-a preproduction
echo "Ligne de départ : version=2.0 (membre A)" > conflit.txt
git commit -am "feat: membre A modifie la ligne" && git push -u origin feature/membre-a

git checkout -b feature/membre-b preproduction
echo "Ligne de départ : version=3.0 (membre B)" > conflit.txt
git commit -am "feat: membre B modifie la même ligne" && git push -u origin feature/membre-b

echo "Conflit prêt. Fusionnez membre-a via PR, puis suivez le guide pour membre-b."
