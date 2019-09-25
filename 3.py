import webbrowser as wb 
yes = ["Да","ДА","дА","да","yes"]
def open():
    url = "https://vk.com"
    vk = ["vk" , "VK" , "вк" , "ВК" , "контакт" , "Vk"]
    a = input("вы хотите открыть какой нибудь сайт? ")
    try:
        if a in vk:
            wb.open(url)
    except :
        print()
open()
ask = input("вы хотите открыть ещё какой-то сайт? ")
if ask in yes :
    def open2():
        url = "https://ru.wikipedia.org/wiki/Заглавная_страница"
        wiki = ["wiki" , "Wiki" , "вики" , "википедия" , "Вики" ]
        a2 = input("введите сайт ")
        try:
            if a2 in wiki:
                wb.open(url)
        except :
            print()
        print("завершение программы...")
    open2()
else:
    print("завершение программы...")


