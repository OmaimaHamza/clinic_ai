# Clinical AI - Prédiction d'Infection (POO adaptée à l'IA)

Ce projet est un exercice d'application illustrant l'utilisation de la **Programmation Orientée Objet (POO)** dans un contexte d'Intelligence Artificielle médicale. Il met en œuvre une architecture modulaire séparant les données, le modèle, l'entraînement et la prédiction.

## Objectifs pédagogiques

*   Appliquer les concepts de la POO (Classes, Objets, Méthodes).
*   Comprendre le **Duck Typing** (Polymorphisme) en Python.
*   Séparer les responsabilités (Principe de Responsabilité Unique).
*   Structurer un projet IA de manière professionnelle.

---

## Architecture du Projet

Le projet suit l'arborescence suivante :

```text
clinical_ai/
│
├── data/
│   └── patient_data.csv          # Jeu de données (Features + Target)
│
├── core/
│   ├── __init__.py
│   ├── dataset.py                # Chargement et parsing des données
│   └── model.py                  # Le modèle mathématique (Mock)
│
├── pipeline/
│   ├── __init__.py
│   └── trainer.py                # Logique d'entraînement
│
├── app/
│   ├── __init__.py
│   └── clinical_predictor.py     # Classe de prédiction (Interface métier)
│
├── main.py                       # Point d'entrée du programme
└── README.md                     # Documentation
