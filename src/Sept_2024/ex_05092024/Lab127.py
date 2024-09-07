class Son:
    gold = "1kg"

class Father(Son):
    diamond = "22karat"

class GrandFather(Father):
    btc = "1btc"

gf  = GrandFather()
print("Grandfather can access everything :", gf.btc, gf.gold, gf.diamond,sep=",")

print("-------------")

son = Son()
print("Son can only access gold :", son.gold)

print("-------------")

father = Father()
print("Father can access only son and father :", father.gold, father.diamond)

