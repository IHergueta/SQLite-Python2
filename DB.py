'''
Created on 14 dic. 2020

@author: Ignacio
'''
import sqlite3
from main import sql_connection

con = sql_connection("mi_erp.db")

cur = con.cursor()

try:

    cur.execute("create table productos(id integer PRIMARY KEY, nombre text, precioventa real, preciocoste real, stockactual integer)")

    con.commit()

    print("La tabla productos se ha creado")

except sqlite3.OperationalError:
    print("No se ha podido crear")

try:

    cur.execute("create table stock(id integer PRIMARY KEY, cdgproducto integer, almacen text, stock integer, FOREIGN KEY(cdgproducto) REFERENCES productos(id))")

    con.commit()

    print("La tabla stock se ha creado")

except sqlite3.OperationalError:
    print("No se ha podido crear")

try:

    cur.execute("create table ventas(id integer PRIMARY KEY, cdgproducto integer, cantidad integer, ciudad text,importe real, precio real, FOREIGN KEY(cdgproducto) REFERENCES productos(id))")

    con.commit()

    print("La tabla ventas se ha creado")

except sqlite3.OperationalError:
    print("No se ha podido crear")

try:

    cur.execute("Insert into productos Values(1,'Fifa',55,30,3)")
    cur.execute("Insert into productos Values(2,'The Last of us',40,10,7)")
    cur.execute("Insert into productos Values(3,'Maincra',30,7,3)")
    cur.execute("Insert into productos Values(4,'God of war',10,50,8)")

    con.commit()

    print("Productos insertados correctamente")

except sqlite3.DatabaseError:

    print("No se ha isertado correctamente")

try:

    cur.execute("Insert into ventas Values(1,1,100,'Huelva',NULL,15)")
    cur.execute("Insert into ventas Values(2,1,100,'Sevilla',NULL,15)")
    cur.execute("Insert into ventas Values(3,2,100,'Sevilla',NULL,18)")
    cur.execute("Insert into ventas Values(4,2,100,'Sevilla',NULL,18)")
    cur.execute("Insert into ventas Values(5,2,100,'Huelva',NULL,18)")
    cur.execute("Insert into ventas Values(6,3,100,'Sevilla',NULL,21)")
    cur.execute("Insert into ventas Values(7,3,100,'Cordoba',NULL,21)")
    cur.execute("Insert into ventas Values(8,4,100,'Sevilla',NULL,24)")
    cur.execute("Insert into ventas Values(9,4,100,'Huelva',NULL,24)")
    cur.execute("Insert into ventas Values(10,4,100,'Cordoba',NULL,24)")

    con.commit()

    print("Ventas insertados correctamente")

except sqlite3.DatabaseError:

    print("No se ha isertado correctamente")

try:

    cur.execute("update ventas set importe=(cantidad*precio)")

    con.commit()

    print("Importe actualizado correctamente")

except sqlite3.DatabaseError:

    print("No se ha actualizado correctamente")

try:

    cur.execute("Select sum((cantidad*precio) ) from ventas where ciudad = 'Huelva'")

    resH = cur.fetchall()

    con.commit()

    print("Importe total Huelva -> ",resH)

except sqlite3.DatabaseError:

    print("Algo ha ido mal")

try:

    cur.execute("Select sum((cantidad*precio) ) from ventas where ciudad = 'Sevilla'")

    resS = cur.fetchall()

    con.commit()

    print("Importe total Sevilla -> ",resS)

except sqlite3.DatabaseError:

    print("Algo ha ido mal")