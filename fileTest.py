from fileClass import *

p1 = System.choosePlayer(1)
p2 = System.choosePlayer(3)
intel = InteligencePlayer(p1, 200)

intel.gerarRanckAttack(p2)
print(intel.rank)
print(intel.resolverAttack(p2))

for i in System.filterItens():
    print(i.getDados())