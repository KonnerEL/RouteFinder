from search import *
import json
import time

source = sys.argv[1]
target = sys.argv[2]

start = time.time()

Colombia_map = UndirectedGraph(dict(eval("{'Leticia':{'Mocoa':10000000000000,'Florencia':10000000000000,'Mitu':10000000000000},'Medellin':{'Monteria':405558.1,'Cartagena':646177.8,'Bucaramanga':390330.6,'Tunja':548849.9,'Bogota':427993.9,'Manizales':200606.4,'Pereira':213371.2,'Quibdo':228218.2},'Arauca':{'Tunja':471906.6,'Yopal':406126.8,'Puerto Carreno':1361389.8},'Barranquilla':{'Santa Marta':99264.2,'Cartagena':129074.6},'Cartagena':{'Barranquilla':123536.2,'Sincelejo':180336.5,'Medellin':647341.9,'Bucaramanga':707201,'Santa Marta':227280.7,'Valledupar':421173.6,'Monteria':296802.5},'Tunja':{'Medellin':552157.8,'Bucaramanga':282920.3,'Bogota':154287.3,'Arauca':589046.3,'Yopal':222759.6,'Villavicencio':263957.9,'Manizales':422064,'Cucuta':437275.2},'Manizales':{'Medellin':199797.1,'Tunja':421876.7,'Bogota':301020.7,'Ibague':232399.6,'Pereira':55025.6},'Florencia':{'Neiva':230928.3,'Villavicencio':632216.2,'San Jose del Guaviare':488077.8,'Mitu':690828.7,'Leticia':10000000000000,'Mocoa':267250.8,'Popayan':290778.1},'Yopal':{'Tunja':219167.9,'Arauca':369991.6,'Puerto Carreno':958637.9,'Villavicencio':263791.2,'Bogota':370141},'Popayan':{'Cali':133493.3,'Ibague':396453.3,'Neiva':264524,'Florencia':290911.9,'Mocoa':277472.2,'Pasto':249538.1},'Valledupar':{'Santa Marta':253060.8,'Riohacha':193699.6,'Cucuta':683359.2,'Bucaramanga':472046.1,'Cartagena':425668.2},'Quibdo':{'Medellin':227725.8,'Pereira':330382.5,'Cali':427563},'Bogota':{'Medellin':432099.7,'Tunja':153087.7,'Manizales':302005.9,'Ibague':187865.7,'Neiva':304975.8,'Villavicencio':107180.2,'Yopal':370121.5},'Monteria':{'Medellin':406895.5,'Sincelejo':117724.5,'Cartagena':293536.1},'Inirida':{'Puerto Carreno':851475.5,'San Jose del Guaviare':961863.9,'Mitu':1201150},'San Jose del Guaviare':{'Villavicencio':288119.8,'Puerto Carreno':1046365,'Inirida':961210.7,'Mitu':242464.3,'Florencia':487876.3},'Neiva':{'Ibague':205073.9,'Bogota':304315.8,'Villavicencio':402613.2,'Florencia':231230.4,'Popayan':264782.5},'Riohacha':{'Santa Marta':171794.6,'Valledupar':194050.1},'Santa Marta':{'Barranquilla':99053.7,'Cartagena':230886.9,'Valledupar':253653.8,'Riohacha':171877.8},'Villavicencio':{'Bogota':111039.2,'Yopal':262778.1,'Puerto Carreno':762292.2,'San Jose del Guaviare':287940.2,'Florencia':635785.8,'Neiva':402444.3},'Pasto':{'Popayan':250040.5,'Mocoa':143206.5},'Cucuta':{'Valledupar':555306.2,'Bucaramanga':207482.1,'Tunja':441260.1},'Mocoa':{'Pasto':143301.3,'Popayan':277316.7,'Florencia':267280.6,'Leticia':10000000000000},'Armenia':{'Cali':179765.7,'Pereira':45179.5,'Ibague':90664.7},'Pereira':{'Quibdo':331606,'Medellin':214071.9,'Manizales':56508.4,'Ibague':130136.3,'Cali':207917.5},'Bucaramanga':{'Tunja':282709.8,'Cucuta':204624.9,'Valledupar':472647.8,'Cartagena':712297.2,'Medellin':391804.6},'Sincelejo':{'Monteria':121539.3,'Cartagena':178329.6},'Ibague':{'Neiva':206531.7,'Bogota':189608.3,'Manizales':231648.6,'Pereira':129292.2,'Armenia':90174.3,'Cali':270694.7,'Popayan':397675.6},'Cali':{'Popayan':132596.8,'Quibdo':539623.4,'Pereira':208901.1,'Armenia':181161.1,'Ibague':270969.8},'Mitu':{'Inirida':1200508.5,'San Jose del Guaviare':242455.5,'Florencia':690618.3,'Leticia':10000000000000},'Puerto Carreno':{'Arauca':1324029.9,'Yopal':957743.2,'Villavicencio':762592.3,'San Jose del Guaviare':1047018.2,'Inirida':851475.5}}")))

Colombia_map.locations = dict(eval("{'Leticia' : (-70.0708,-4.0047),'Medellin' : (-75.57483,6.24475),'Arauca' : (-70.76167,7.09028),'Barranquilla' : (-74.79639,10.96389),'Cartagena' : (-75.52528,10.42361),'Tunja' : (-73.36139,5.54028),'Manizales' : (-75.48472,5.06611),'Florencia' : (-75.61167,1.61417),'Yopal' : (-72.39056,5.33056),'Popayan' : (-76.60028,2.45917),'Valledupar' : (-73.25972,10.46028),'Quibdo' : (-76.65819,5.69228),'Bogota' : (-74.08083,4.59889),'Monteria' : (-75.88556,8.75972),'Inirida' : (-67.92,3.87),'San Jose del Guaviare' : (-72.6459,2.5729),'Neiva' : (-75.2875,2.9275),'Riohacha' : (-72.90694,11.54417),'Santa Marta' : (-74.20167,11.23611),'Villavicencio' : (-73.62944,4.1425),'Pasto' : (-77.27472,1.21),'Cucuta' : (-72.50472,7.9075),'Mocoa' : (-76.6466,1.1493),'Armenia' : (-75.6725,4.53889),'Pereira' : (-75.69456,4.81428),'San Andres' : (-81.7,12.58333),'Bucaramanga' : (-73.11611,7.11861),'Sincelejo' : (-75.39583,9.29944),'Ibague' : (-75.20056,4.43778),'Cali' : (-76.51972,3.44),'Mitu' : (-70.1733,1.1983),'Puerto Carreno' : (-68.1638,6.0681)}"))

graph = {}
expandedNodes = 0
totalNodes = 1
Colombia_problem = GraphProblem(source, target, Colombia_map)
nodeFinal = (astar_search((Colombia_problem)))

end = time.time()
spentTime = end - start

solu = nodeFinal[0].solution()
graph = nodeFinal[1]
expandedNodes = nodeFinal[2]
totalNodes = nodeFinal[3]

estadistic = []
esH = []
esG = []
esDistance = []
k={}
g = []
k["origen"]=source
k["destino"]=solu[0]
k["peso"] =(str(Colombia_map.get(source,solu[0])))
esDistance.append(k)

for i in range(len(solu)-1):
    k={}
    k["origen"]=solu[i]
    k["destino"]=solu[i+1]
    k["peso"] =(str(Colombia_map.get(solu[i],solu[i+1])))
    esDistance.append(k)

k={}
k["name"]=source
k["h"]=str(Colombia_problem.h(source))
esH.append(k)
for i in range(len(solu)):
  k={}
  k["name"]=solu[i]
  k["h"]=str(Colombia_problem.h(solu[i]))  
  esH.append(k) 

for i in nodeFinal[0].path():
  k={}
  g.append(i.state+"-"+str(i.path_cost))
  k["name"] = i.state
  k["g"] = str(i.path_cost)
  esG.append(k)

estadistic.append(esDistance)
estadistic.append(esH)
estadistic.append(esG)
estadistic.append(totalNodes)
estadistic.append(expandedNodes)
estadistic.append(spentTime)

with open('route.json', 'w') as outfile:
    json.dump(solu, outfile) 
with open('data.json', 'w') as outfile:
    json.dump(graph, outfile)

with open('estadistic.json', 'w') as outfile:
    json.dump(estadistic, outfile) 