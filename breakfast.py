'''Breakfast'''



def makebreakfast(name, ingredients = input(" Enter extra ingridients") ):
    #ingredients = input(" Enter extra ingridients")
    print("Get the ingredients ")
    print("prepare the ingredients for mixing ")
    print("mix the ingredients ")
    print("Heat the pan")
    print("pour ingredients into the heated pan")
    print("Flip on to the other side")
    if ingredients == "":
        breakfast = "--yummy " + name + "--"
    else:
        breakfast = "--yummy " + name + " with " + ingredients + "--"
    return breakfast

print(makebreakfast('egg'))
#print(makebreakfast('pancake'))

