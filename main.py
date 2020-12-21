'''
Created on 14 dic. 2020

@author: Ignacio
'''
import sqlite3
from sqlite3 import Error


def sql_connection(filename=":memory:"):
    try:
        con = sqlite3.connect(filename)
        print("Conectandose a ", filename)
    except Error:
        print(Error)
        con = sqlite3.connect(filename)
    finally:
        return con
