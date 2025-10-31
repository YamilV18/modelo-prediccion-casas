import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

data = pd.read_csv("SaratogaHouses.csv")

# Variables predictoras y variable objetivo
X = data.drop("price", axis=1)
y = data["price"]

# Variables categóricas
categorical_cols = ["heating", "fuel", "sewer", "waterfront", "newConstruction", "centralAir"]

# Convertir variables categóricas a numéricas (Yes/No -> 1/0)
for col in ["waterfront", "newConstruction", "centralAir"]:
    X[col] = X[col].map({"Yes": 1, "No": 0})

# Variables categóricas con múltiples categorías (One-hot encoding)
X = pd.get_dummies(X, columns=["heating", "fuel", "sewer"], drop_first=True)

# Escalamiento
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Separar datos
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')

print("\nEntrenando el modelo... 🔁")
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=500, verbose=1)
print("\n✅ Entrenamiento finalizado")

# Guardar modelo
model.save("modelo_casas.h5")
print("💾 Modelo guardado como modelo_casas.h5\n")


root = tk.Tk()
root.title("🏡 Predicción de Precio de Casa")
root.geometry("800x400")
root.resizable(False, False)

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill="both", expand=True)

# Validación para solo números
def validar_numero(texto):
    return texto == "" or texto.replace('.', '', 1).isdigit()

vcmd = (root.register(validar_numero), '%P')

# Campos numéricos (izquierda)
left_frame = tk.Frame(main_frame)
left_frame.grid(row=0, column=0, padx=20, pady=10, sticky="n")

# Campos categóricos y booleanos (derecha)
right_frame = tk.Frame(main_frame)
right_frame.grid(row=0, column=1, padx=20, pady=10, sticky="n")

# ====== CAMPOS NUMÉRICOS ======
entries = {}
fields = {
    "lotSize": "Tamaño del terreno (acres)",
    "age": "Antigüedad (años)",
    "landValue": "Valor del terreno ($)",
    "livingArea": "Área habitable (pies²)",
    "pctCollege": "% de residentes con estudios universitarios",
    "bedrooms": "Número de dormitorios",
    "fireplaces": "Número de chimeneas",
    "bathrooms": "Número de baños",
    "rooms": "Número total de habitaciones"
}

for i, (key, label) in enumerate(fields.items()):
    tk.Label(left_frame, text=label, anchor="w").grid(row=i, column=0, sticky="w", pady=5)
    entry = tk.Entry(left_frame, validate="key", validatecommand=vcmd)
    entry.grid(row=i, column=1, pady=5)
    entries[key] = entry

# ====== CAMPOS CATEGÓRICOS ======
tk.Label(right_frame, text="Tipo de calefacción").grid(row=0, column=0, sticky="w", pady=5)
heating_cb = ttk.Combobox(right_frame, values=["electric", "hot water/steam", "hot air"], state="readonly")
heating_cb.grid(row=0, column=1, pady=5)
heating_cb.set("electric")

tk.Label(right_frame, text="Tipo de combustible").grid(row=1, column=0, sticky="w", pady=5)
fuel_cb = ttk.Combobox(right_frame, values=["electric", "gas", "oil"], state="readonly")
fuel_cb.grid(row=1, column=1, pady=5)
fuel_cb.set("gas")

tk.Label(right_frame, text="Tipo de alcantarillado").grid(row=2, column=0, sticky="w", pady=5)
sewer_cb = ttk.Combobox(right_frame, values=["septic", "public/commercial", "none"], state="readonly")
sewer_cb.grid(row=2, column=1, pady=5)
sewer_cb.set("septic")

# ====== CHECKBOX ======
bool_vars = {}
bool_fields = {
    "waterfront": "¿Frente al agua?",
    "newConstruction": "¿Construcción nueva?",
    "centralAir": "¿Aire acondicionado central?"
}

for i, (key, label) in enumerate(bool_fields.items(), start=3):
    var = tk.IntVar()
    chk = tk.Checkbutton(right_frame, text=label, variable=var)
    chk.grid(row=i, column=0, columnspan=2, sticky="w", pady=5)
    bool_vars[key] = var


# ====== FUNCIÓN DE PREDICCIÓN ======
def predecir():
    try:
        data_input = {key: float(entries[key].get()) for key in entries}
        data_input.update({
            "heating": heating_cb.get(),
            "fuel": fuel_cb.get(),
            "sewer": sewer_cb.get(),
            "waterfront": bool_vars["waterfront"].get(),
            "newConstruction": bool_vars["newConstruction"].get(),
            "centralAir": bool_vars["centralAir"].get()
        })

        df = pd.DataFrame([data_input])

        # Transformaciones igual que el entrenamiento
        for col in ["waterfront", "newConstruction", "centralAir"]:
            df[col] = df[col].map({1: 1, 0: 0})

        df = pd.get_dummies(df, columns=["heating", "fuel", "sewer"], drop_first=True)

        # Alinear columnas
        for col in set(X.columns) - set(df.columns):
            df[col] = 0
        df = df[X.columns]

        df_scaled = scaler.transform(df)
        pred = model.predict(df_scaled)[0][0]
        messagebox.showinfo("Predicción", f"💰 Precio estimado: ${pred:,.2f}")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese solo valores numéricos válidos.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Botón de predicción
predict_btn = tk.Button(main_frame, text="🔮 Predecir Precio", command=predecir, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
predict_btn.grid(row=1, column=0, columnspan=2, pady=20)

root.mainloop()
