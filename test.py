N, M = input().strip().split()
N, M = int(N), int(M)
U=int((N-1)/2)
X=1

for i in range (U):
   print((".|."*X).center(M,'-'))
   X+=2
    
print('WELCOME'.center(M,'-'))

X-=2
for i in range (U):
   print((".|."*X).center(M,'-'))
   X-=2
