# Pievieno random un string bibliotēkas.
import random
import string

'''
Uzdevums: Izveidot programmu, kas ģenerēs drošas paroles.
Programmai jāprasa lietotājam ievadīt paroles garumu,
vai izmantot lielos burtus, ciparus un speciālos simbolus.
Pēc ievades programmai jāizveido parole, kas atbilst lietotāja ievadītajiem kritērijiem.
Parolei jābūt nejauši izvēlētai no pieejamajiem simboliem.

Autors: Palmijs :))))
'''


# Ievada paroles garumu
length = int(input("Ievadiet paroles garumu: "))

uppercase = int(input("Izmantot lielos burtus?(1 = Jā, 2 = Nē): "))

numbers = int(input("Izmantot ciparus?(1 = Jā, 2 = Nē): "))

specialChar = int(input("Izmantot speciālos simbolus?(1 = Jā, 2 = Nē): "))

# Pārbauda ievadīto vērtibu special
if specialChar == 1:
    specialChar = True
elif specialChar == 2:
    specialChar = False
while specialChar != 1 and specialChar != 2:
    print("Nepareiza ievade")
    specialChar = int(input("Izmantot speciālos simbolus?(1 = Jā, 2 = Nē): "))


# Pārbauda ievadīto vērtibu numbers mainīgajam
if numbers == 1:
    numbers = True
elif numbers == 2:
    numbers = False
while numbers != 1 and numbers != 2:
    print("Nepareiza ievade")
    numbers = int(input("Izmantot ciparus?(1 = Jā, 2 = Nē): "))

# Pārbauda ievadīto vērtibu uppercase mainīgajam
if uppercase == 1:
    uppercase = True
elif uppercase == 2:
    uppercase = False
while uppercase != 1 and uppercase != 2:
    print("Nepareiza ievade")
    uppercase = int(input("Izmantot lielos burtus?(1 = Jā, 2 = Nē): "))

characters = string.ascii_lowercase # Pēc noklusējuma izmanto tikai mazos burtus

# Pārbauda vai uppercase, number un specialChar vērtibas ir True
if uppercase == True:
    characters += string.ascii_uppercase
if numbers == True:
    characters += string.digits
if specialChar == True:
    characters += string.punctuation

password = "".join(random.choice(characters) for i in range(length))
print("Izveidotā parole:", password)

# Veidoju šo lai testētu savas python spējas.