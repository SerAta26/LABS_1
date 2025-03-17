memory_ = 1.44 * 1024 * 1024

page = 100
line = 50
symbol_ = 25
data_symbol = 4

book = page * line * symbol_ * data_symbol

boocks = int(memory_ // book)




print("Количество книг, помещающихся на дискету:", boocks)