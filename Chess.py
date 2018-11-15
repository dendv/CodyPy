# Уроки на pythontutor.ru

print("Координаты первой клетки:")
print("Столбец -", end="\t")
a = int(input())
print("Строка -", end="\t")
b = int(input())
print("Координаты второй клетки:")
print("Столбец -", end="\t")
x = int(input())
print("Строка -", end="\t")
y = int(input())
if ((a+b)%2==0 and (x+y)%2==0) or ((a+b)%2==1 and (x+y)%2==1):
	print("Клетки одного цвета.")
else:
	print("Клетки разного цвета")
