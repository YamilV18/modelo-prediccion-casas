---

## 🚀 **Instrucciones de Ejecución**

### 1. 📦 Requisitos previos
Antes de ejecutar el proyecto, asegúrate de tener instalado:

- **Python 3.9 o superior**
- **Conexión a Internet** (para descargar las librerías necesarias)
- **Sistema operativo Windows** (el archivo `.bat` está diseñado para este entorno)

Puedes comprobar tu versión de Python ejecutando:
```bash
python --version
```

### 2. ⚙️ Archivos del proyecto

| Archivo   | Descripción |
|-----------|---------------|
| algoritmo.py |	Contiene el código principal del modelo: lectura de datos, entrenamiento de la red neuronal y la interfaz gráfica. |
| SaratogaHouses.csv	| Dataset utilizado para el entrenamiento del modelo. |
| run.bat	Script | automatizado que instala dependencias, configura el entorno virtual y ejecuta el modelo. |
| modelo_casas.h5	| (Se genera automáticamente) Modelo entrenado guardado en formato HDF5. |
| README.md	| Este archivo con las instrucciones de uso. |

### 3. ▶️ Ejecución automática con run.bat

💡 Recomendado: Siempre utiliza este método.

1. Haz doble clic en el archivo run.bat.

2. El script verificará:
- Que Python esté instalado.
- Que se cree (si no existe) un entorno virtual.
- Que se instalen todas las dependencias necesarias (tensorflow, scikit-learn, pandas, etc.).

3. Luego ejecutará automáticamente el archivo algoritmo.py.

Una vez finalizado el entrenamiento del modelo, aparecerá una ventana interactiva donde podrás probar predicciones.

### 4. 🧩 Uso de la interfaz gráfica

Al finalizar el entrenamiento, se abrirá una ventana con los campos correspondientes:

- Los valores numéricos (como tamaño del terreno, área habitable o número de habitaciones) deben ser números válidos.
- Los campos categóricos (como tipo de calefacción o combustible) se seleccionan desde un menú desplegable.
- Los campos de tipo “Sí/No” aparecen como casillas de verificación.

Después de introducir los datos, presiona el botón "Predecir Precio" y se mostrará el resultado.

### 5. 🛠️ Solución de problemas
| Problema | Posible causa |	Solución |
|----------|---------------|-----------|
| Python no está instalado	| Python no se encuentra en el PATH	| Instálelo desde python.org y marque “Add to PATH” durante la instalación. |
| Error de librerías	| Falta una dependencia	| Ejecuta nuevamente run.bat para reinstalar dependencias. |
| La ventana no aparece	| Error al finalizar el entrenamiento	| Verifica que no haya errores en consola y que el archivo CSV esté correctamente formateado. |
### 6. 📂 Estructura del proyecto
#### 📁 proyecto_modelo_casas/
#### │
#### ├── algoritmo.py
#### ├── SaratogaHouses.csv
#### ├── run.bat
#### ├── README.md
#### └── modelo_casas.h5     ← (se genera automáticamente)

### 7. 👨‍💻 Autor

#### Desarrollado por:
Yamil Valente Quispe Cuellar
#### 📅 Versión: Octubre 2025
