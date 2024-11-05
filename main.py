num1=[7,5,3]
num2=[8,5,3]
k=map(lambda x,y:x*y,num1,num2)
print(list(k))









#ziptwoelementsoftwolists
s1={5,4,7}
s2={'b','a','c'}
s3=list(zip(s1,s2))
print(s3)







#zip into dictionary
stocks=['reliance','infosys','tcs']
prices=[2570,4569,7990]
new_dict={stocks:prices for stocks,prices in zip(stocks,prices)}
print(new_dict)
