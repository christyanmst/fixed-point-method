import calendar

x = int(input('Digite um ano para o calendário:\n'))
y = int(input('Digite um mês para o calendário:\n'))

z= calendar.month(x,y)
i = calendar.calendar(x, 2, 1, 6)

print("\nO ",y,"º mês de ",x," é:\n",z)

print("O calendário do ano de ",x, " é:\n", i) 