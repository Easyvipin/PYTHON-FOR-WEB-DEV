#Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = { }
for each in dic1 :
    dic4.update({each : dic1[each]})

for each in dic2 :
    dic4.update({each : dic2[each]})
    
for each in dic3 :
    dic4.update({each : dic3[each]})

print(dic4)

#alternative method
for each in (dic1 , dic2 , dic3 ) :
    print(each)
#dic4.update(each)
#will do the same thing

