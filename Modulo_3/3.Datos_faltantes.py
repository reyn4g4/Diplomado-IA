import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import SimpleImputer, KNNImputer, IterativeImputer

# Crear un DataFrame de ejemplo con valores faltantes

#np.random.seed(45)

data_complex = pd.DataFrame({
    'A': np.random.normal(loc=0, scale=1, size=100),  # Distribución normal
    'B': np.random.gamma(shape=2, scale=1.0, size=100),  # Distribución gamma
    'C': np.random.exponential(scale=1.0, size=100)  # Distribución exponencial
})

perc = 50

# Introducir valores faltantes
nan_indices_complex = np.random.choice(data_complex.index, size=perc, replace=False)
data_complex.loc[nan_indices_complex, 'A'] = np.nan
data_complex.loc[nan_indices_complex, 'B'] = np.nan
data_complex.loc[nan_indices_complex, 'C'] = np.nan

# Definir los imputadores
mean_imputer = SimpleImputer(strategy='mean')
median_imputer = SimpleImputer(strategy='median')
knn_imputer = KNNImputer(n_neighbors=5)
iterative_imputer = IterativeImputer(random_state=42)

# Imputar los datos con diferentes técnicas
data_complex_mean_imputed = pd.DataFrame(mean_imputer.fit_transform(data_complex), columns=data_complex.columns)

data_complex_median_imputed = pd.DataFrame(median_imputer.fit_transform(data_complex), columns=data_complex.columns)

data_complex_knn_imputed = pd.DataFrame(knn_imputer.fit_transform(data_complex), columns=data_complex.columns)

data_complex_iterative_imputed = pd.DataFrame(iterative_imputer.fit_transform(data_complex), columns=data_complex.columns)

# densidad
fig, axs = plt.subplots(1, 3, figsize=(18, 6))
columns = data_complex.columns

datasets_complex = [
    (data_complex, 'Original'),
    (data_complex_mean_imputed, 'Mean Imputed'),
    (data_complex_median_imputed, 'Median Imputed'),
    (data_complex_knn_imputed, 'KNN Imputed'),
    (data_complex_iterative_imputed, 'Iterative Imputed')
]

colors = ['blue', 'orange', 'green', 'red', 'purple']

for i, column in enumerate(columns):
    for (dataset, label), color in zip(datasets_complex, colors):
        dataset[column].plot(kind='density', ax=axs[i], label=label, color=color, alpha=0.7)
    axs[i].set_title(f'Density Plot: {column}')
    axs[i].legend()

plt.tight_layout()
plt.show()
