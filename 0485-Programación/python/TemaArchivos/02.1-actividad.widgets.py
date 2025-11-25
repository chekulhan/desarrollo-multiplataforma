# --- Widgets Factory Production Log ---

# production_log.txt: Incluir estos datos en un fichero, sin #
# son datos diarias de widgets producidos

#Widgets Produced per Day (header row)
# 45
# 52
# 76
# 48
# 60

# El resultado deberia ser algo asi:
# Produced: 45, Bonus: 0
# Produced: 52, Bonus: 5.2
# ...

# leer widgets log
with open("production_log.txt", "w") as f_in: 
    lines = f_in.readlines()

# 2. Calcular pago (10% bonus por >50 widgets)
overtime_report = []
for line in lines:
    produced = int(line.strip())
    if produced > 50:
        bonus = produced * 0.12
    else:
        bonus = 0
    overtime_report.append(f"Produced: {produced}, Bonus: {bonus}")  

#  Producir informe final
with open("overtime_report.txt") as f_out:
        f_out.write() 

print("Overtime report generado con {contar} lineas.") 


# COMO un gerente de la fabrica de WIDGETS
# QUIERO saber el total de widgets producidos
# Para tener un informe relevante y actual para la toma de decisiones