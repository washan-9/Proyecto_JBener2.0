import csv
import os

CSV_PATH = '../datos_csv/mis_finanzas_2026.csv'
SQL_OUT_PATH = '../supabase/insert_data.sql'
USER_ID = '36b73ee2-e715-46f7-b63a-4afe892b3262'

def escape_sql(val):
    if not val or val.strip() == '':
        return 'NULL'
    # Escape single quotes
    safe_val = val.strip().replace("'", "''")
    return f"'{safe_val}'"

def generate_sql():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(script_dir, CSV_PATH)
    sql_file = os.path.join(script_dir, SQL_OUT_PATH)

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader) # skip header
        
        with open(sql_file, 'w', encoding='utf-8') as out:
            out.write("-- SCRIPT DE MIGRACIÓN DE DATOS CSV\n")
            out.write(f"-- Para el usuario con ID: {USER_ID}\n\n")
            
            for row in reader:
                if not row or not ''.join(row).strip(): continue # Skip empty rows
                
                # Columnas del CSV:
                # 0:Fecha, 1:Categoria, 2:Descripción, 3:Monto, 4:Tipo, 5:SUNAT, 6:Descripcion, 7:Fecha_Devolucion
                
                fecha = escape_sql(row[0])
                categoria = escape_sql(row[1])
                monto = row[3] if row[3].strip() else '0.0'
                tipo = escape_sql(row[4])
                sunat = escape_sql(row[5]) if len(row) > 5 else "NULL"
                descripcion = escape_sql(row[6]) if len(row) > 6 else "NULL"
                fecha_devolucion = escape_sql(row[7]) if len(row) > 7 and row[7].strip() else "NULL"
                
                out.write(f"INSERT INTO public.transacciones (user_id, fecha, categoria, monto, tipo, sunat, descripcion, fecha_devolucion)\n")
                out.write(f"VALUES ('{USER_ID}', {fecha}, {categoria}, {monto}, {tipo}, {sunat}, {descripcion}, {fecha_devolucion});\n")

    print(f"Genarado exitosamente: {sql_file}")

if __name__ == '__main__':
    generate_sql()
