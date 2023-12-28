# Contributed by:
# Jemish Variya - 201901112
# Nisarg Nampurkar - 201901188
# Harikrishna Patel - 201901212
# Raj Patel - 201901306
# Ashray Kothari - 201901457

# Auxilliary sequence of integers
def G(n,l,P):
    if l<n and l>=1:
        return 3**l
    G_nl = 0
    for i in range(0,n-1):
        P_bar = "ACT"
        if P[i] in P_bar:
            P_bar = P_bar.replace(P[i],'')
        G_nl += len(P_bar) * G(n,l-i-1,P)     
    return G_nl   

# To map a integer to a ternary representation 
def theta(y,l):
    res=''
    while y!=0:
        t=y%3
        if t==0:
            res+='A'
        elif t==1:
            res+='C'
        else:
            res+='T'
        y=y//3
    res=res[::-1]
    diff=l-len(res)
    return diff*'A'+res

# Encodes the sequence 
# l: length of the sequence 
# x: integer we want to encode
def encode(P, l, x):
    n = len(P)
    if l >= n:
        t = 0
        P_bar = "ACT"
        if P[t] in P_bar:
            P_bar = P_bar.replace(P[t],'')
     
        while x >= len(P_bar) * G(n,l-t-1,P):
            x -= len(P_bar) * G(n,l-t-1,P)
            t += 1
            P_bar = "ACT"
            if P[t] in P_bar:
                P_bar = P_bar.replace(P[t],'')
                
        a = x // G(n,l-t-1,P)
        b = x % G(n,l-t-1,P)     
        return P[0:t] + P_bar[a] + encode(P,l-t-1,b)   
    else:
        return theta(x,l)