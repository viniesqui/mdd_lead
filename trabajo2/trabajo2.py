# Import necessary libraries
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split, GridSearchCV
import pandas as pd
import joblib

# 1. Leer el dataset
df = pd.read_csv("C:\\Users\\vinie\\Downloads\\toyota_price.csv", delimiter=';', decimal='.') 

# 2. Preprocesamiento

df = df.dropna()  # Se eliminan los NaN
# Convierte las variables de object a categórica
df['modelo'] = df['modelo'].astype('category')
df['transmision'] = df['transmision'].astype('category')
df['tipo_combustible'] = df['tipo_combustible'].astype('category')
# Recodifica las categorías usando números
df["modelo"] = df["modelo"].cat.codes
df['transmision'] = df['transmision'].cat.codes
df['tipo_combustible'] = df['tipo_combustible'].cat.codes

y = df['precio'] #queremos predecir el precio basado en las otras variables
X = df.drop('precio', axis=1)

# Dividimos el entrenamiento y las pruebas
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


# 3. Pipeline
# Primero standarizamos los datos despus le tiramos un RandomForestRegressor a travez de un pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', RandomForestRegressor())
])


# 4. Hiperparametros
#se usan dos hiperparametros para el RandomForestRegressor. En esos vamos a probar diferentes valores para encontrar el mejor modelo
parameters = {
    'regressor__n_estimators': [50, 100, 200],
    'regressor__max_depth': [None, 10, 20, 30],
}

# El gridsearch busca el mejor modelo en base a los hiperparametros que estan en el diccionario de arriba
grid_search = GridSearchCV(pipeline, parameters, cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train)

# 5. Entrenamiento
# El modelo en realidad se entreto en el fit del gridsearch entonces aqui solo vamos a predecir
y_pred = grid_search.predict(X_test)

# 6. Metricas
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
print('R-squared:', r2_score(y_test, y_pred))

# 7. Serializacion del modelo
joblib.dump(grid_search, 'modelo_1_precios_toyotas.pkl')