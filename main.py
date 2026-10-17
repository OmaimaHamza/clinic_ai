from core.dataset import DatasetLoader
from core.model import SimpleModel
from pipeline.trainer import Trainer
from app.clinical_predictor import ClinicalPredictor

# 1. Chargement des données (depuis data/patient_data.csv)
loader = DatasetLoader("data/patient_data.csv")
X, y = loader.load_data()

print(f"Données chargées : {len(X)} patients.")

# 2. Initialisation et Entraînement
modele_ia = SimpleModel()
trainer = Trainer(modele_ia)
modele_ia_entraine = trainer.train(X, y)

# 3. Prédiction avec la classe ClinicalPredictor
predictor = ClinicalPredictor(modele_ia_entraine)

# Test avec un patient simulé (ex: 38.5°C, 90 bpm, Toux=1)
# On s'attend à ce qu'il soit "Infecté" car forte fièvre et toux
nouveau_patient = [[38.5, 90, 1]] 
diagnostic = predictor.diagnosis(nouveau_patient)

print(f"--- DIAGNOSTIC ---")
print(f"Données patient : {nouveau_patient}")
print(f"Résultat : {diagnostic}")