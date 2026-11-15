import json,os,urllib.request as u
U=os.environ["MAKEFUN_ENV_URL"]
def P(p,b):return json.load(u.urlopen(U+p,json.dumps(b).encode()))
VL=(0,100,320,330,500,900,0);MT=1000000
ND=(33,31,18,14,-14,-18,-31,-33);BD=(15,17,-15,-17);RD=(1,-1,16,-16);KD=RD+BD;DT=(0,0,ND,BD,RD,BD+RD,KD)
CM={0:13,7:14,4:12,112:7,119:11,116:3}
B=[0]*128;S=1;C=0;K=[0,0]
def F(f):
 global B,S,C,K
 B=[0]*128;S=1;C=0;K=[0,0];a=f.split();s=112
 for ch in a[0]:
  if ch=="/":s-=24
  elif ch.isdigit():s+=int(ch)
  else:
   p="PNBRQK".index(ch.upper())+1;p=-p if ch.islower() else p;B[s]=p
   if abs(p)==6:K[0 if p>0 else 1]=s
   s+=1
 S=1 if a[1]=="w" else -1;C=sum({"K":1,"Q":2,"k":4,"q":8}.get(c,0)for c in a[2])
def A(s,w):
 for o in(15,17):
  t=s-o*w
  if not t&136 and B[t]==w:return 1
 for ds,pt,ry in((ND,2,0),(KD,6,0),(BD,3,1),(RD,4,1)):
  for d in ds:
   t=s+d
   while not t&136:
    p=B[t]
    if p==w*pt or p==w*5 and pt!=2:return 1
    if p or not ry:break
    t+=d
 return 0
def G(cp):
 m=[]
 def pm(t):[m.append(s|t<<7|x<<14)for x in(5,4,3,2)]
 for s in range(128):
  if s&136:continue
  p=B[s]
  if p*S<=0:continue
  a=abs(p);r=s>>4
  if a==1:
   d=16*S;pr=r==(6 if S>0 else 1);t=s+d
   if not t&136 and B[t]==0:
    if pr:pm(t)
    elif not cp:m.append(s|t<<7);m.append(s|(s+2*d)<<7)if r==(1 if S>0 else 6)and B[s+2*d]==0 else 0
   for t in(s+d-1,s+d+1):
    if not t&136 and B[t]and B[t]*S<0:
     if pr:pm(t)
     else:m.append(s|t<<7)
  else:
   ds=DT[a]
   for d in ds:
    t=s+d
    while not t&136:
     q=B[t]
     if q==0:
      if not cp:m.append(s|t<<7)
     else:
      if q*S<0:m.append(s|t<<7)
      break
     if a%4==2:break
     t+=d
 if not cp:
  for b,k,t,r,e,a in((1,4,6,7,(5,6),(4,5,6)),(2,4,2,0,(3,2,1),(4,5,3)))if S>0 else((4,116,118,119,(117,118),(116,117,118)),(8,116,114,112,(115,114,113),(116,115,114))):
   if C&b and B[r]==4*S and all(B[x]==0 for x in e)and not any(A(x,-S)for x in a):m.append(k|t<<7)
 return m
def M(m):
 global S,C
 f=m&127;t=m>>7&127;p=m>>14&7;pc=B[f];cp=B[t];u=[pc,cp,C,K[0],K[1]];C&=CM.get(f,15)&CM.get(t,15);B[f]=0;B[t]=S*p if p else pc
 if abs(pc)==6 and abs(t-f)==2:B[t-1 if t>f else t+1]=B[t+1 if t>f else t-2];B[t+1 if t>f else t-2]=0
 if abs(pc)==6:K[0 if S>0 else 1]=t
 S=-S;return u
def UM(m,u):
 global S,C
 f=m&127;t=m>>7&127;pc,cp,C,K[0],K[1]=u;B[f]=pc;B[t]=cp
 if abs(pc)==6 and abs(t-f)==2:B[t+1 if t>f else t-2]=B[t-1 if t>f else t+1];B[t-1 if t>f else t+1]=0
 S=-S
def EV():
 w=b=0
 for s in range(128):
  if s&136:continue
  p=B[s]
  if not p:continue
  a=abs(p);r=s>>4;f=s&7;c=min(f,7-f)+min(r,7-r);v=VL[a]
  if a==1:v+=10*(r if p>0 else 7-r)
  elif a==2:v+=8*c
  elif a==3:v+=5*c
  elif a==6:v+=-6*c
  if p>0:w+=v
  else:b+=v
 return(w-b)*S
class X(Exception):pass
N=0;L=40000;KL=[[0,0]for _ in range(128)]
def O(ms,pl):
 ms.sort(key=lambda m:(10000+VL[abs(B[m>>7&127])])if B[m>>7&127]else(9000 if m==KL[pl][0]else 8000 if m==KL[pl][1]else 0),reverse=True)
def R(d,a,b,pl):
 global N
 N+=1
 if N>L:raise X
 if d<=0:
  st=EV();a=max(a,st)
  if st>=b:return b
  if pl>48:return a
 ms=G(not A(K[(1-S)//2],-S))if d<=0 else G(False)
 O(ms,pl);bv=-MT;al=a
 for m in ms:
  u=M(m)
  if A(K[(1+S)//2],S):UM(m,u);continue
  v=-R(d-1 if d>0 else 0,-b,-al,pl+1);UM(m,u)
  if v>bv:bv=v
  if v>al:al=v
  if al>=b:
   t=m>>7&127
   if not B[t]:KL[pl][1]=KL[pl][0];KL[pl][0]=m
   break
 if d<=0:return al
 if bv==-MT:return-MT+pl if A(K[(1-S)//2],-S) else 0
 return bv
def RT():
 ms=G(False);O(ms,0);best=0;d=1
 while d<40:
  try:
   bv=-MT;bm=0
   for m in ms:
    u=M(m)
    if A(K[(1+S)//2],S):UM(m,u);continue
    v=-R(d-1,-MT,MT,1);UM(m,u)
    if v>bv:bv=v;bm=m
   if bm:best=bm;ms.remove(bm);ms.insert(0,bm)
   d+=1
  except X:break
 return best
def MU(m):
 a=lambda s:"abcdefgh"[s&7]+str((s>>4)+1)
 return a(m&127)+a(m>>7&127)+("nbrq"[(m>>14&7)-2]if m>>14 else"")
while True:
 g=P("/game",{})
 if g["status"]=="done":break
 F(g["fen"])
 while g["status"]=="your_move":
  N=0;m=RT();lm=g["legal_moves"];mv=MU(m)if m else lm[0]
  if mv not in lm:mv=lm[0]
  g=P("/move",{"game":g["game"],"move":mv})
  if g["status"]=="your_move":F(g["fen"])
