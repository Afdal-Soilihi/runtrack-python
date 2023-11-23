# Déclaration des variables du produit
nom_produit = "Ordinateur portable"
prix_unitaire = 800.0
quantite_en_stock = 50

# Affichage initial des informations du produit
print(f"Informations du produit : {nom_produit}")
print(f"Prix unitaire : {prix_unitaire} euros")
print(f"Quantité en stock : {quantite_en_stock} unités\n")

# Ajout de produits en stock
quantite_ajoutee = int(input("Entrez la quantité de produits à ajouter en stock : "))
quantite_en_stock += quantite_ajoutee

# Mise à jour du prix unitaire après l'inflation
prix_unitaire *= 1.1  # Augmentation de 10%

# Affichage des informations mises à jour du produit
print("\nInformations mises à jour du produit après l'ajout en stock et l'inflation :")
print(f"Nom du produit : {nom_produit}")
print(f"Prix unitaire : {prix_unitaire} euros")
print(f"Quantité en stock : {quantite_en_stock} unités")