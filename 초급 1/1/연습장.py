n,c=map(int,input().split())
s=list(map(int,input().split()))
s.sort(reverse=True)
print(s[c-1])