div =[];
sum=0;
for i in range(0,1000):
    if(i %3==0 or i%5==0):
        div.append(i)
print(div);
for j in div:
    sum+=j;
print(sum)