import csv


file = 'DigiDB_digimonlist.csv'

# with open('DigiDB_digimonlist.csv', 'r') as file:
#     # Ler o arquivo CSV
#     reader = csv.DictReader(file)
    
#     # Inicializar variáveis
#     total_hp = 0
#     count = 0
    
#     # Calcular a média de Lv50 HP
#     for row in reader:
#         total_hp += int(row['Lv 50 HP'])
#         count += 1
        
#     avg_hp = total_hp / count
    
#     # Exibir a média de Lv50 HP
#     print(f"A média de Lv50 HP é: {avg_hp}")

################## organizando os digimons por Lv50 Atk
   
   
    # Abrir o arquivo CSV
#     with open('DigiDB_digimonlist.csv', 'r') as file:
#     # Ler o arquivo CSV
#      reader = csv.DictReader(file)
    
#     # Ordenar os Digimons por Lv50 Atk
#      sorted_digimons = sorted(reader, key=lambda x: int(x['Lv50 Atk']))
    
#     # Exibir os Digimons ordenados
#      print("Digimons ordenados por Lv50 Atk:")
#      for digimon in sorted_digimons:
#         print(digimon)

# ################## organizando os digimons por critérios

# import csv

# Abrir o arquivo CSV
with open('DigiDB_digimonlist.csv', 'r') as file:
    # Ler o arquivo CSV
    reader = csv.DictReader(file)
    
    # Filtrar os Digimons
    filtered_digimons = []
    for row in reader:
        if row['Type'] == 'Virus' and row['Attribute'] == 'Fire':
            filtered_digimons.append(row)
            
    # Exibir os Digimons filtrados
    print("Digimons filtrados:")
    for digimon in filtered_digimons:
        print(digimon)