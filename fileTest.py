from fileClass import *

p1 = System.choosePlayer(2)
p2 = System.choosePlayer(0)
intel = InteligencePlayer(p1, 200)

intel.gerarRanckAttack(p2)
print(intel.rank)
print(intel.resolverAttack(p2))