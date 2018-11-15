# Уроки на pythontutor.ru
# Напишите программу, которая считывает целое число и выводит текст,
# аналогичный приведенному в примере (пробелы важны!):
# The next number for the number 1534 is 1535.
# The previous number for the number 1534 is 1533.

for i in range(3):
	print("Введи число:", end="\t")
	n = int(input())
	print("Следующее число для числа ", n, " это ", n+1, ".", sep="")
	print("Предыдующее число для числа ", n, " это ", n-1, ".", sep="")
print("Конец!")
