import pandas as pd

# Dataset y DataFrame
datos = {
    "producto": [
        "Cuaderno", "lapicera", "mochila", "Regla", "Cartuchera",
        "Calculadora", "Auriculares", "Resaltadores", "Goma", "Lapiz"
    ],
    "categoria": [
        "Libreria", "libreria", "Accesorios", " Libreria", "accesorios",
        "Tecnologia", "tecnologia", "Libreria ", "Indumentaria", " libreria "
    ],
    "precio": [2500, 800, 15000, 1200, 4500, 18000, 12500, 3200, 600, 500],
    "cantidad_vendida": [15, 25, 5, 10, 8, 3, 2, 30, 12, 50],
    "sucursal": [
        "Centro", "Centro", "Norte", "Sur", "Norte",
        "Centro", "Sur", "Centro", "Sur", "Centro"
    ],
    "forma_pago": [
        "Efectivo", "debito", "Credito", "Efectivo", "Debito",
        "credito", "Credito", "Debito", "Efectivo", "debito"
    ],
    "fecha": [
        "2024-03-01", "2024-03-01", "2024-03-02", "2024-03-02", "2024-03-03",
        "2024-03-03", "2024-03-04", "2024-03-04", "2024-03-05", "2024-03-05"
    ]
}

df = pd.DataFrame(datos)

# Normalización de categoria
reemplazos_categoria = {
    'libreria': 'Libreria',
    'accesorios': 'Accesorios',
    'tecnologia': 'Tecnologia',
    'indumentaria': 'Indumentaria'
}

df['categoria_limpia'] = (
    df['categoria']
    .str.strip()
    .str.lower()
    .replace(reemplazos_categoria)
)



# Normalización de forma_pago
df['forma_pago_lista'] = df['forma_pago'].str.strip().str.lower()

# Filtrado con condiciones
condicion_combinada = (
    (df['categoria_limpia'] == 'Libreria') &
    (df['forma_pago_lista'] == 'debito') &
    (df['cantidad_vendida'] >= 20)
)

resultado_final = df[condicion_combinada][['producto', 'precio', 'sucursal']]

print("=== RESULTADO FINAL ===")
print(resultado_final)

print("\n=== AUDITORÍA ===")
print("Tipo del objeto:", type(resultado_final))
print("Dimensiones (.shape):", resultado_final.shape)