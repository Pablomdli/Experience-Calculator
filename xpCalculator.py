import sys

# Verificación de argumentos
if len(sys.argv) < 3:
    print("Error: Se requieren dos argumentos: nivel inicial y nivel final.")
    sys.exit(1)

# Obtiene los niveles desde los argumentos
start_level = int(sys.argv[1])
end_level = int(sys.argv[2])

# Configuración de cálculo
by_level_estimate = True  # True para imprimir detalles por nivel, False para omitir

# Cálculos iniciales
current_level = start_level
exp_start = start_level * start_level * 100  # Experiencia inicial

# Cálculos por nivel
prev_level_exp = (start_level - 1) * (start_level - 1) * 100  # EXP del nivel anterior
output = []  # Lista para almacenar resultados y luego imprimirlos
while current_level <= end_level:
    level_exp = current_level * current_level * 100  # EXP total del nivel actual
    exp_needed = level_exp - prev_level_exp  # EXP necesaria para subir de nivel
    prev_level_exp = level_exp  # Actualiza la EXP previa para el siguiente ciclo
    avg_games_needed = round(exp_needed / 75)  # Promedio de partidas requeridas (50% winrate)
    
    if by_level_estimate:
        output.append(f"Nivel: {current_level} | EXP total: {level_exp} | EXP necesaria: {exp_needed} | Partidas promedio: {avg_games_needed}")
    
    current_level += 1

# Cálculos totales
current_level -= 1  # Corrige el nivel final tras el ciclo
exp_end = current_level * current_level * 100  # EXP total al nivel objetivo
total_exp_needed = exp_end - exp_start  # Diferencia de EXP total
avg_games_total = round(total_exp_needed / 75)  # Partidas promedio totales
time_estimate_hours = round(avg_games_total * 0.025)  # Tiempo estimado en horas (90 segundos por partida)
min_games = round(total_exp_needed / 100)  # Partidas mínimas (100 EXP por partida)
max_games = round(total_exp_needed / 50)  # Partidas máximas (50 EXP por partida)

# Resultados finales
output.append(f"EXP total necesaria para niveles {start_level}-{end_level}: {total_exp_needed}")
output.append(f"Partidas promedio estimadas: {avg_games_total}")
output.append(f"Partidas mínimas: {min_games} | Partidas máximas: {max_games}")
output.append(f"Tiempo estimado (horas, 90 seg/partida, 50% winrate): {time_estimate_hours}")

# Imprime los resultados en una salida adecuada para PHP
print("\n".join(output))