from fileClass import *

p1 = System.choosePlayer(3)
p2 = System.choosePlayer(4)
intel = InteligencePlayer(p1, 200)

intel.gerarRanckAttack(p2)
print(intel.rank)
print(intel.resolverAttack(p2))