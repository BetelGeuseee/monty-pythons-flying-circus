import mymodules
#from mymodules import Car

ans=mymodules.person['name']
print(ans)

carOne=mymodules.Car("Ferrari",300)
carTwo=mymodules.Car("Lamborghini",500)

carOne.display()
carTwo.display()