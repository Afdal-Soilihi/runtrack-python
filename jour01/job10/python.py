montant_investissement_initial = 10000.0
taux_rendement_annuel = 5.0
def calculer_gain_annuel(montant, taux):
    return montant * (taux / 100)
gain_annuel_initial = calculer_gain_annuel(montant_investissement_initial, taux_rendement_annuel)
print(f"Gain annuel initial : {gain_annuel_initial} euros\n")
montant_investissement_initial += 5000
taux_rendement_annuel += 2
nouveau_gain_annuel = calculer_gain_annuel(montant_investissement_initial, taux_rendement_annuel)
print(f"Nouveau gain annuel après l'augmentation du capital et du taux : {nouveau_gain_annuel} euros\n")
montant_investissement_initial -= 0.10 * montant_investissement_initial
taux_rendement_annuel -= 1
montant_final = montant_investissement_initial + nouveau_gain_annuel
print(f"Montant final de l'investissement après le retrait : {montant_final} euros")