bagpack = ["food","water","wood","hp+","gun"]
da = ["da", "Da", "DA", "dA", "да", "Да", "ДА", "дА"]
import random
print(bagpack)
food = input("оставить человека без еды?: ")
if food in da :
    bagpack.pop(0)
print(bagpack)
art = input("Вы нашли артефакт,забрать его?: ")
if art in da :
    bagpack.append("art")
print(bagpack)
gyro = input("Вы нашли гироскутер,забрать?: ")
if gyro in da:
    bagpack.insert(1, "gyro")
print(bagpack)
minibag = ["bottle", "stimo"]
minibag = input("Вы нашли подсумок,забрать?: ")
if minibag in da:
    bagpack.insert(6,"minibag")
print(bagpack)
random.choise (bagpack)