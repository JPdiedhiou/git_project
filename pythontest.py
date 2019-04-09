n=int(input("Entrer le nombre de valeur à entrer:"))
a=[]
for i in range(0,n):
        elem=int(input("Entrer une valeur: "))
        a.append(elem)
avg=sum(a)/n
print("La moyenne des valeurs est", round(avg,2))
