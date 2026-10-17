class SimpleModel:
    def __init__(self):
        self.is_trained = False
        # Ajustement des poids pour être plus sensible aux symptômes
        # Température, Pouls, Toux
        self.weights = [1.5, 0.05, 2.0] 
        self.bias = -60.0 # Biais très négatif pour que le patient "sain" reste sain

    def fit(self, X, y):
        print("Modèle en cours d'entraînement...")
        self.is_trained = True

    def predict(self, X):
        if not self.is_trained:
            raise Exception("Le modèle doit être entraîné avant de prédire.")
        
        probabilities = []
        for row in X:
            # Calcul du score
            score = (row[0] * self.weights[0]) + \
                    (row[1] * self.weights[1]) + \
                    (row[2] * self.weights[2]) + self.bias
            
            # Fonction Sigmoïde (pour avoir une proba entre 0 et 1)
            prob = 1 / (1 + pow(2.718, -score)) 
            probabilities.append(prob)
            
        return probabilities