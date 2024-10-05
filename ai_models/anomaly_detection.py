
from sklearn.ensemble import IsolationForest
import numpy as np
import pickle

# Sample data for training
data = np.array([[22.1, 55.3, 45],
                 [23.4, 60.2, 48],
                 [22.5, 58.5, 50],
                 [23.0, 57.1, 47],
                 [21.8, 59.0, 42]])

# Train the Isolation Forest model
model = IsolationForest(contamination=0.1)
model.fit(data)

# Save the model
with open('models/isolation_forest.pkl', 'wb') as f:
    pickle.dump(model, f)
