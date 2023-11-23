# Programme affichant l'alphabet à l'envers dans le terminal

# Début de la boucle de Z à A
for lettre in range(ord('Z'), ord('A')-1, -1):
    print(chr(lettre), end=' ')

# Saut de ligne à la fin
print()