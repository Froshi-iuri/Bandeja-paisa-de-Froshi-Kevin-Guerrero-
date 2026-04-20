print("Restaurante super basico, no lleva while, así que \n termina con el primer pedido")
restaurant_info = ("Restaurante Froshiru", "Calle 15N 57-2")

menu_tags = {"Jugos", "Comidas", "Postres"}

items = {
    1: "Jugo de Mora",
    2: "Bandeja Paisa",
    3: "Ajiaco"
}

log = []

log.append("Programa iniciado, creo")

print(f"--- BIENVENIDO A {restaurant_info[0]} ---")
print(f"Direccion: {restaurant_info[1]}")
print("")

print("Categorias:")
for tag in menu_tags:
    print(f"- {tag}")

print("\nPlatos disponibles:")
for id, name in items.items():
    print(f"{id}. {name}")

user_order = input("\n¿Que desea ordenar? (Escriba el nombre): ")

log.append(f"orden del usuario: {user_order}")

print(f"\nListo, su {user_order} estara en un momento.")

print("\nHistorial de lo que sucede:")
for event in log:
    print(f"> {event}")
    