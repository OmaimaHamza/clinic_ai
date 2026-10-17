class Trainer:
    def __init__(self, model):
        self.model = model

    def train(self, X_train, y_train):
        # Logique d'entraînement séparée de la prédiction
        self.model.fit(X_train, y_train)
        return self.model