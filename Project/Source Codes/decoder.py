# Contributed by:
# Jemish Variya - 201901112
# Nisarg Nampurkar - 201901188
# Harikrishna Patel - 201901212
# Raj Patel - 201901306
# Ashray Kothari - 201901457

# To map a ternary sequence to a integer
def invtheta(s):
    res=0
    s=s[::-1]
    for i in range(len(s)):
        if s[i]=='A':
            t = 0
        elif s[i]=='C':
            t=1
        else:
            t=2
        res+=t*3**i
    return res

# Auxilliary sequence of integers
def G(n,l,P):
    if l<n and l>=1:
        return 3**l
    G_nl = 0
    for i in range(n-1):
        P_bar_i = 3
        if P[i] == 'A' or P[i] == 'C' or P[i] == 'T':
            P_bar_i -= 1
        G_nl += P_bar_i * G(n,l-i-1,P)     
    return G_nl   

# Decodes the encoded sequence
def decodePSC(P,X):
    n=len(P)
    l=len(X)
    brk=0

    if (l<n):
        return invtheta(X)
    else:
        #find t,s
        for t in range(l):
            P_bar = ['A', 'C', 'T']
            if P[t] in P_bar:
                P_bar.remove(P[t])

            for s in range(len(P_bar)):
                temp=P[:t]+P_bar[s]
                if temp==X[:t + 1]:
                    brk=1
                    break
            if brk==1:
                break
        sum=0
        for i in range(t):
            P_bar = ['A', 'C', 'T']
            if P[i] in P_bar:
                P_bar.remove(P[i])
            sum+=len(P_bar)*G(n,l-i-1,P)

        str=''
        for i in range(t+1, l):
            str+=X[i]
            
        return sum+ s*G(n,l-t-1,P) + decodePSC(P,str)