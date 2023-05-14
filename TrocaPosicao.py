import csv

with open('arquivo1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    with open('arquivo_saida.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=';')
        writer.writerow(['Nome do repositorio', 'Projeto', 'Tribo', 'Squad'])
        
        for row in reader:
            projeto = row[1]
            tribo = row[2]
            squad = row[3]
            nome_do_repositorio = row[0]
            linha_para_gravar = f"{nome_do_repositorio};{projeto};{tribo};{squad}"
            writer.writerow([linha_para_gravar])
