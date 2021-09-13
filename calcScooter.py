AantalBanden = 2
BandP = float(47.98)
BandA = 15
Budget = 113

Saldo = Budget - AantalBanden * (BandP + BandA)
isReparatieBetaalbaar = Saldo >=0
print(isReparatieBetaalbaar)
print (type(isReparatieBetaalbaar))

print('Is de scooteropknapbeurt betaalbaar?')
if isReparatieBetaalbaar:
    print('Ja, want de kosten passen in het budge.t')
else:
    print('Nee, ga maar sparen voor een nieuwe scooter.')    