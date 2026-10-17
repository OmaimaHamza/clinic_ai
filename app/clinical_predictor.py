class ClinicalPredictor:
    def __init__(self, model):
        """
        Constructeur : reçoit un modèle déjà entraîné.
        """
        self.model = model

    def diagnosis(self, patient_data):
        """
        Reçoit les données du patient, utilise le modèle et retourne le diagnostic.
        """
        # On appelle la méthode predict() du modèle (Concept de Duck Typing)
        # On suppose que patient_data est une liste ou un array
        probabilities = self.model.predict(patient_data)
        
        results = []
        for prob in probabilities:
            if prob >= 0.5:
                results.append("Infecté")
            else:
                results.append("Sain")
        
        # Si on traite un seul patient, on retourne le premier résultat
        if len(results) == 1:
            return results[0]
        return results