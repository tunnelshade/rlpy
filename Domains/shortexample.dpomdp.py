agents: 2 
discount: 1.0
values: reward
states: s0 s1     
start exclude: s0
actions: 
agent1-a1 a12 a13
2
observations: 
2
hear-left hear-right
T: * : 
uniform
T: a12 1 : s2 : 
0.4 0.6
T: 1 2 :
0.2 0.8
0.6 0.5
T: * * : * : * : 0.5
T: 1 1 : 0 : 1 : 0.33333
T: 1 1 : 0 : 0 : 0.66666
T: 1 : 0 : 
0.123 0.876
T: 0 0 : 0 : 
0.11111 0.88888
T: 2 :
identity 
T: 3 :
0.2222 0.2233
0.2244 0.2255
O: * * :
uniform
O: a12 1 : state-one : * * : 0.002
O: a12 1 : state-one : 0 hear-left : 0.7225
O: 0 0 : * : * : 0.9
O: 0 1 : s2 : 0 hear-right : 0.1275
O: 0 1 : 0 : 1 hear-left : 0.1275
O: 1 0 : 1 : * hear-right : 0.0225
O: 1 1 : 1 : 1 * : 0.7225
O: 2 0 : 0 : 0 hear-right  : 0.1275
O: 2 1 : 0 : 0 0 : 0.1275
O: 2 1 : 1 : * : 0.0225
O: * 1 :
uniform
O: a12 1 : s2 : 
0.1 0.1 0.1 0.6 
O: 1 2 :
0.1 0.8 0.05 0.05
0.6 0.3 0.06 0.04
R: * : 1 : 3 :
4.3 34.2 253 12
R: * : s2 : 
4.3 34.2 253 12
5.3 2352 2.3 1.2
R: a12 0 : * : * : * : -2
R: 0 0 : 0 : * : * : -50
R: 0 1: 1 : * : * : +20
R: 0 2: 1 : * : * : 20
R: 1 0: 0 : * : * : -100
R: 1 1: 1 : * : * : -10
R: 1 2: 0 : * : * : -101
R: 2 0: 1 : * : * : -101
R: 2 1 : 1 : * : * : 9