from math import exp
u = []

for x in range(248):
    if x <= 124:
        u.append((1/(1+exp((x/5)-10))/2)+0.5)
        #print(f"x={x} : u={(1/(1+exp((x/5)-10))/2)+0.5}")
    else:
        u.append(1-((1/(1+exp((x/5)-30)))/2))
        #print(f"x={x} : u={1-((1/(1+exp((x/5)-30)))/2)}")
u=u+[1]*10
u = [1]*60+[0.5]*160+[1]*50

v = [1]*30+[0.3]*2500+[1]*100