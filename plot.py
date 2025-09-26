import matplotlip.pyplot as plt 
x =["saturday","sunday","monday","tuesday","wednesday","thursday","friday"]
y =[40,35,30,25,20,18,17]

plt.plot(x,y,marker="o",linestyle="-",color="blue")
plt.title("temperature variation over a week") 
plt.xlabel("days of the week")
plt.ylabel("temperature in degree celsius")
plt.show() 
