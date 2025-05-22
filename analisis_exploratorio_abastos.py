import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv("dataset_ventas_simulado.csv", parse_dates=["fecha"])

# Vista general
print("Resumen de datos:")
print(df.info())
print("\nPrimeras filas:")
print(df.head())

# Agrupación: ventas totales por tienda
ventas_tienda = df.groupby("tienda")["ventas"].sum().reset_index()
print("\nVentas totales por tienda:")
print(ventas_tienda)

# Gráfico de ventas por tienda
plt.figure(figsize=(8,5))
sns.barplot(data=ventas_tienda, x="tienda", y="ventas", palette="viridis")
plt.title("Ventas totales por tienda")
plt.ylabel("Unidades vendidas")
plt.xlabel("Tienda")
plt.tight_layout()
plt.savefig("ventas_por_tienda.png")
plt.show()

# Tendencia de ventas por fecha (todas las tiendas)
ventas_fecha = df.groupby("fecha")["ventas"].sum().reset_index()
plt.figure(figsize=(10,5))
sns.lineplot(data=ventas_fecha, x="fecha", y="ventas")
plt.title("Tendencia de ventas diarias")
plt.ylabel("Ventas totales")
plt.xlabel("Fecha")
plt.tight_layout()
plt.savefig("ventas_por_fecha.png")
plt.show()
