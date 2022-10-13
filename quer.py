import sqlite3
from sqlite3 import Error
from flask import g
from db import get_db,close_db

def nomb(dba):
    db=dba
    Data=db.execute('Select * from Gpeliculas where ID=1').fetchone()
    Data1=db.execute('Select * from Gpeliculas where ID=2').fetchone()
    Data2=db.execute('Select * from Gpeliculas where ID=3').fetchone()
    Data3=db.execute('Select * from Gpeliculas where ID=4').fetchone()
    Data4=db.execute('Select * from Gpeliculas where ID=5').fetchone()
    Data5=db.execute('Select * from Gpeliculas where ID=6').fetchone()
    Data6=db.execute('Select * from Gpeliculas where ID=7').fetchone()
    Data7=db.execute('Select * from Gpeliculas where ID=8').fetchone()
    Data8=db.execute('Select * from Gpeliculas where ID=9').fetchone()
    Data9=db.execute('Select * from Gpeliculas where ID=10').fetchone()
    Datos=[Data[1],Data1[1],Data2[1],Data3[1],Data4[1],Data5[1],Data6[1],Data7[1],Data8[1],Data9[1]]

    return Datos


def gene(dba):
    db=dba
    Data=db.execute('Select * from Gpeliculas where ID=1').fetchone()
    Data1=db.execute('Select * from Gpeliculas where ID=2').fetchone()
    Data2=db.execute('Select * from Gpeliculas where ID=3').fetchone()
    Data3=db.execute('Select * from Gpeliculas where ID=4').fetchone()
    Data4=db.execute('Select * from Gpeliculas where ID=5').fetchone()
    Data5=db.execute('Select * from Gpeliculas where ID=6').fetchone()
    Data6=db.execute('Select * from Gpeliculas where ID=7').fetchone()
    Data7=db.execute('Select * from Gpeliculas where ID=8').fetchone()
    Data8=db.execute('Select * from Gpeliculas where ID=9').fetchone()
    Data9=db.execute('Select * from Gpeliculas where ID=10').fetchone()
    Datos=[Data[3],Data1[3],Data2[3],Data3[3],Data4[3],Data5[3],Data6[3],Data7[3],Data8[3],Data9[3]]

    return Datos
