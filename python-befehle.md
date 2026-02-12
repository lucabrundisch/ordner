# Python Befehlsübersicht


## Grundsyntax

print("Hallo Welt")	# Ausgabe


## Variablen & Datentypen

x = 5			# Integer
pi = 3.14		# Float
name = "Max"		# String
ist_wahr = True		# Boolean
type(x)			# Typ anzeigen


## Rechenoperatoren

+	# Addition
-	# Subtraktion
*	# Multiplikation
/	# Division
//	# Ganzzahl-Division
%	# Modulo
**	# Potenz


## Strings

text = "Hallo"
text.lower()
text.upper()
text.strip()
len(test)


#String Verbindungen

name = "Max"
print("Hallo "+ name)
print(f"Hallo {name}")


## Listen

liste = [1,2,3]
liste.append(4)
liste.remove(2)
liste[0]		# Zugriff
len(liste)


## Bedingungen

if x > 10:
	print("größer als 10")
elif x == 10:
	print("gleich 10")
else:
	print("kleiner als 10")

== != > < >= <=		# Vergleichsoperatoren


## Schleife

# While-Schleife
while x < 5:
	x += 1

# For-Schleife
for i in range(5):
	print(i)

# Element-For-Schleife
for element in liste:
	print(element)


## Funktionen
def begruessung(name):
	return f"Hallo {name}"

print(begruessung("Anna")) 


## Dictionaries

person = {
	"name": "Max",
	"alter": 25
}

person["name"]
person.keys()
person.values()


## Fehlerbehandlung

try:
	x = 10 / 0
except ZeroDivisionError:
	print("Division durch 0!")


## Dateien lesen & schreiben

# lesen
with open("datei.txt", "r") as f:
	inhalt = f.read()

# schreiben
with open("datei.txt", "w") as f:
	f.write("Hallo")


## Module importieren

import math
math.sqrt(16)

from random import randint
randint(1,10)


## Built-in Funktionen

print()
len()
type()
input()
range()
int()
float()
str()
list()
