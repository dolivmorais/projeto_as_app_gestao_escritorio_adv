import pandas as pd
import sqlite3

# Criando o Conn
conn = sqlite3.connect('sistema.db')

# Criando o Cursor
c = conn.cursor()

# Criando a Tabela
c.execute("""create table if not exists processos(
          'No Processo' numeber,
          'EMpresa' text,
          'Tipo' text,
          'Açãoo' text,
          'Vara' text,
          'Fase' text,
          'Instancia' text,
          'Data Inicio' text,
          'Data Final' text,
          'Processo Concluído' number,
          'Processo Vencido' number,
          'Advogado' text
          'Cliente' text
          'CPF Cliente' text
          'Descrição' text)""")

c.execute("""create table if not exists advogados(
          'Advogado' text,
          'OAB' numeber,
          'CPF' text)""")

df_adv = pd.read_sql("select * from advogados", conn)
df_proc = pd.read_sql("select * from processos", conn)

conn.commit()
conn.close