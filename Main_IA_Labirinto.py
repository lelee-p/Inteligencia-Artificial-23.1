from Agentes_IA_Labirinto import AgentDFS, AgentEsperto
from Labirinto_IA import Labirinto

nlin = 10
ncol = 10

l1 = Labirinto(nlin,ncol,0.25,[0,0],[nlin-1,ncol-1]) #define labirinto
ag = AgentEsperto(l1,type='AStar')
caminho = ag.act()
print(caminho)