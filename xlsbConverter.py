import pandas as pd
import os

def process_xlsb(file_path):
    df = pd.read_excel(file_path, engine='pyxlsb', sheet_name='Lista com Valores')

    processed_data = []
    for index, row in df.iterrows():
        msisdn = row['MSISDN']
        iccid = row['ICCID']
        status = row['Status']
        cnpjDoCliente = row['CNPJ do Cliente']
        tempoBase = row['Tempo de Base']

        processed_row = {
            'MSISDN': msisdn,
            'ICCID': iccid,
            'Status': status,
            'CNPJ do Cliente': cnpjDoCliente,
            'Tempo de Base': tempoBase
        }
        processed_data.append(processed_row)

    processed_df = pd.DataFrame(processed_data)

    output_csv_path = 'config/reports/claro/base_claro.csv'
    processed_df.to_csv(output_csv_path, index=False)
    print(f"Dados processados salvos em {output_csv_path}")

//lê um arquivo do tipo xlsb e processa transformando-o em csv
arquivo = open("config/reports/claro/base_claro.xlsb", "r")
file_path = os.path.abspath(arquivo.name)
arquivo.close()
process_xlsb(file_path)