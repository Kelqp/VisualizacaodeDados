import duckdb
conn = duckdb.connect("Inclua o nome do DB ou o caminho do arquivo")
# Imprime todas as tabelas do banco de dados
print(conn.execute("SHOW TABLES").fetchdf()['column_name'].tolist())
