import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import sys
import time
# чтение данных из файла в виде строк в list
def readInput(lines):
	data = []
	for line in lines:
		numsOfCurrentLine = line.split(" ")
		numsOfCurrentLine = [float(num) for num in numsOfCurrentLine]
		data.append(numsOfCurrentLine)
	return data
#костыль для проверки принадлежности множеству foo in bar
def isFooInBar(foo,bar,i):
	if (i == 11 ) and (foo>=bar[1]) or (i==0) and (foo<=bar[0]):
		return True
	else:
		return (foo >= bar[0]) and (foo<= bar[1])
#построение и сохранение в файл
def plotAndSave(x,h,w,xlabel,ylabel,xleft,xright,ybot,ytop,xticks,xticks2,yticks,title,outName,show = None):
	fig = plt.figure(figsize=(16, 9), dpi=100)
	ax = plt.subplot(111)
	plt.axis([xleft, xright, ybot, ytop])
	plt.bar(x, height = h, width = w)
	ax.xaxis.grid(True), ax.yaxis.grid(True)
	plt.xlabel(xlabel), plt.ylabel(ylabel)
	#костыль для замены шкалы оси, в эфр надо для сдвига на h/2
	plt.xticks(xticks,xticks2)
	plt.yticks(yticks)
	plt.title(title)
	plt.savefig(outName)
	if show:
		plt.show()
#эфр
def EFR(nx):
	for i in range(1,len(nx)):
		nx[i]+=nx[i-1]
	return nx
