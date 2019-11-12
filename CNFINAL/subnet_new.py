import sys

(addrString,cidrString)= sys.argv[1].split("/")
addr=addrString.split(".")
cidr=int(cidrString)
mask=[0,0,0,0]
for i in range(cidr):
    mask[i//8]=mask[i//8]+(1 << (7-i%8))

net=[]
for i in range(4):
    net.append(int(addr[i]) & mask[i])

broad=list(net)
brange = 32-cidr
for i in range(brange):
    broad[3 - i//8] = broad[3 - i//8] +(1 << (i%8))

num_subnet=int(sys.argv[2]) 
max = int((broad[3] + 1) / num_subnet)
ll=[]
ul=[]
for i in range(num_subnet):
    ll.append(0)
    ul.append(0)

n_max=0;
max1=int(max)
for i in range(num_subnet):
    n_max=n_max+max
    ll[i]=n_max-max1
    ul[i]=n_max-1

lb=[]
ub=[]
for i in range(3):
    lb.append(0)
    ub.append(0)

for i in range(3):
    lb[i]=broad[i]
    ub[i]=broad[i]

print("Address:",addrString)
ip=addrString.split(".")
print ("Address in bits:",'{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])))
print("Netmask:",".".join(map(str,mask)))
print ("Netmask in bits:",'{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(mask[0]),int(mask[1]),int(mask[2]),int(mask[3])))
print("Network",".".join(map(str,net)))
print("Broadcast",".".join(map(str,broad)))
print("SUBNETS: ")
for i in range(num_subnet):
    print("Subnet",i,".".join(map(str,lb)),".",ll[i],"--->",".".join(map(str,ub)),".",ul[i])


# pythonn subnet.py 192.168.10.1/26 4(no. of subnets)
