import math
import random

def uShortDown(pos, priod, scale):

	#定义并处理X轴信息
	fragment = (2 * math.pi)/pos
	ari_x = [fragment * i for i in range(pos * priod)]

	#定义并处理电压暂降需要的参数信息
	para = [scale * 1 for i in range(pos * priod)]
	start_p = 2 * pos
	end_p = 8 * pos

	for i in range(pos * priod):
		if(i > start_p and i < end_p):
			para[i] = scale * random.randint(35,50)/100.0

	#根据X轴坐标和相对应的参数生成y轴数值

	ari_y = [para[i] * math.sin(ari_x[i]) for i in range(pos * priod)]

	return [(ari_x[i], ari_y[i]) for i in range(pos * priod)]

def uShortUp(pos, priod, scale):

	#定义并处理X轴信息
	fragment = (2 * math.pi)/pos
	ari_x = [fragment * i for i in range(pos * priod)]

	#定义并处理电压暂降需要的参数信息
	para = [scale * 1 for i in range(pos * priod)]
	start_p = 2 * pos
	end_p = 8 * pos

	for i in range(pos * priod):
		if(i > start_p and i < end_p):
			para[i] = scale * random.randint(135,150)/100.0

	#根据X轴坐标和相对应的参数生成y轴数值

	ari_y = [para[i] * math.sin(ari_x[i]) for i in range(pos * priod)]

	return [(ari_x[i], ari_y[i]) for i in range(pos * priod)]

def uShortSusp(pos, priod, scale):

	#定义并处理X轴信息
	fragment = (2 * math.pi)/pos
	ari_x = [fragment * i for i in range(pos * priod)]

	#定义并处理电压暂降需要的参数信息
	para = [scale * 1 for i in range(pos * priod)]
	start_p = 2 * pos
	end_p = 8 * pos

	for i in range(pos * priod):
		if(i > start_p and i < end_p):
			para[i] = random.randint(135,150)/100.0

	#根据X轴坐标和相对应的参数生成y轴数值

	ari_y = [para[i] * math.sin(ari_x[i]) for i in range(pos * priod)]

	return [(ari_x[i], ari_y[i]) for i in range(pos * priod)]

def abnormalFreq(pos, priod, scale):

	#定义并处理X轴信息
	fragment = (2 * math.pi)/pos
	ari_x = [fragment * i for i in range(pos * priod)]

	#定义并处理电压暂降需要的参数信息
	freq_para = [1 for i in range(pos * priod)]
	start_p = 2 * pos

	for i in range(pos * priod):
		if(i > start_p):
			freq_para[i] = 2;

	#根据X轴坐标和相对应的参数生成y轴数值
	ari_y = scale * [math.sin(freq_para[i] * ari_x[i]) for i in range(pos * priod)]

	return [(ari_x[i], ari_y[i]) for i in range(pos * priod)]

def uInstantOverLoad(pos, priod, scale):

	#定义并处理X轴信息
	fragment = (2 * math.pi)/pos
	ari_x = [fragment * i for i in range(pos * priod)]

	#根据X轴坐标和相对应的参数生成y轴数值
	ari_y = [scale * math.sin(ari_x[i]) for i in range(pos * priod)]

	for i in range(10):
		if (ari_y[random.randint(2 * pos, 8 * pos)] > 0):
			ari_y[random.randint(2 * pos, 8 * pos)] = scale * random.randint(1,100)/100

	return [(ari_x[i], ari_y[i]) for i in range(pos * priod)]

def Ibump(pos, priod, scale):

	#定义并处理X轴信息
	fragment = (2 * math.pi)/pos
	ari_x = [fragment * i for i in range(pos * priod)]
	
	para = [0.2 for i in range(pos * priod)]
	part = 0.003
	for i in range(pos * priod):
		if(i < 6 * pos):
			part += 0.003
			para[i] = 1.0/(part + 1)

	#根据X轴坐标和相对应的参数生成y轴数值
	ari_y = [para[i] * scale * math.sin(ari_x[i]) for i in range(pos * priod)]

	return [(ari_x[i], ari_y[i]) for i in range(pos * priod)]