from module import *
source = 'mydata.csv'
if len(sys.argv)>1:	source = sys.argv[1]
sourceFd = open(source)
dataNp = np.array(readInput(sourceFd.readlines()))
# part1
# шаг разбиения h=(b-a)/12, где b = arg_max(data), a = arg_min(data)
# ищем макс-мин
a, b = dataNp.min(), dataNp.max()
# считаем шаг, попутно округляя до одного знака после запятой
h = round((b-a)/12,1)
# теперь выбираем отрезок [A,B] близкий к границам мин-макс, читай методу
A, B = round(a, 2), round(a+12*h, 2)
# отрезок дробим на 12 равных частичных интервалов длиной h
x = np.arange(A, B+h, h) # ndarray границ
# отдельно массив кортежей с границами индивидуальных интервалов, 12 штук
delta = []
for i in range(len(x)-1):
	delta.append((x[i],x[i+1]))
#избавляемся от потенциального треша с вещественной частью в 10 знаке после запятой
delta = [(round(each[0],2), round(each[1],2)) for each in delta]
# определяем частоты n, т.е. число элементов выборки попавших
# в каждый из частительных интервалов delta
n = np.zeros(12)
for dataI in dataNp:
	for dataJ in dataI:
		for i in range(len(delta)):
			n[i] += isFooInBar(dataJ,delta[i],i)
# относительные частоты p = ni/n
p = [ni/200 for ni in n]
#середины частичных интервалов x_middle
# x_middle = (x_i-1+x_i)/2, i=1..12
x_middle = []
for borders in delta:
	x_middle.append((borders[0]+borders[1])/2)
#и тут округлим на всякий пожарный, и для красоты)
x_middle = [round(each,2) for each in x_middle]
# построение гистограммы
plotAndSave(x_middle,p/h,h,'x','p_i/h',A,B,0,(p/h).max(),x,p/h,\
p/h,'Гистограмма','hysto.png')
#построение эфр
efr = EFR(list(p))
efr = np.array([round(each,3) for each in efr])
# print(p)
# график эфр
plotAndSave(x_middle,efr,h,'x','F_n(x)',A,B,0,efr.max(),x_middle,\
[round(each+h/2,2) for each in x_middle],efr,"График эмпирической функции распределения",'efr.png')
# среднее выборочное значение дисперсии и выборочная дисперсия
x_m = []
for i in range(len(p)):
	x_m.append(x_middle[i]*p[i])
x_m_saved = list(x_m)
x_m = round(np.array(x_m).sum(),3)
print(x_m)
x_m2 = []
for i in range(len(p)):
	x_m2.append(x_middle[i]**2*p[i])
x_m2_saved = list(x_m2)
x_m2 = round(np.array(x_m2).sum(), 3)
D = x_m2 - x_m ** 2
#доверительный интервал psi = 0.95
t =2.24
num = 200**0.5
int_bot = round(x_m - t*(sqrt(D)/num),2)
int_top = round(x_m + t*(sqrt(D)/num),2)
print(int_bot, int_top)
###
# Вывод в таблицы
#1
output_path = "out1.csv"
output_file = open(output_path, "w")
output_file.write(str(delta)+ "\n"+ str(x_middle)+"\n"+str(n)+"\n"+str(p))
output_file.close()
#2
output_path = "out2.csv"
output_file = open(output_path, "w")
output_file.write(str(x_middle)+"\n"+str(p)+"\n"+str(x_m_saved)+"\n"+str(x_m2_saved)+"\n x_m="+str(x_m)+"\n x_m2="+str(x_m2))
output_file.write("\n доверительный интервал "+str((int_bot,int_top)))
output_file.close()
