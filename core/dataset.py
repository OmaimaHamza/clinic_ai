import csv
import os

class DatasetLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        """
        Charge le fichier CSV et sépare les features (X) de la cible (y).
        Retourne X (liste de listes) et y (liste de valeurs).
        """
        X = []
        y = []
        
        # Vérification de l'existence du fichier
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Le fichier {self.filepath} est introuvable.")

        with open(self.filepath, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader) # Sauter l'en-tête
            
            for row in reader:
                # On convertit les valeurs en float pour les features
                # Les 3 premières colonnes sont les features
                features = [float(val) for val in row[:3]]
                # La dernière colonne est la target (0 ou 1)
                target = int(row[3])
                
                X.append(features)
                y.append(target)
                
        return X, y