class Avatar():
    
    def __init__(self,mid,left,right,go,gold,bagpack,damage,damageU):
        self.mid = False
        self.left = True
        self.right = False
        self.go = "10"
        self.gold = "500"
        self.bagpack =  ["ring","sword","hook"]
        self.damage = "50"
        self.damageU = "100"

    def stats(self):
        print("Ваша скорость:"+ self.go +" Кол-во золота:"+ self.gold + " Сила атаки:"+ self.damage + " Сила юльты:" + self.damageU ) 
        if self.left == True:
            print("Иди наверх")
        elif self.mid == True:
            print("Иди на мид")
        elif self.right == True:
            print("Тебе на нижнюю линию")
Hero = Avatar("","","","","","","","")
Hero.stats()
