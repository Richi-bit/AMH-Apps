import math
import numpy as np
import pandas as pd

namino = float(input("Ingrese el nivel del namino en metros: "))
ei = float(input("Ingrese el nivel del namo: "))
namo = ei
mi = float(input("Ingrese el mes inicial: "))
mf = int(input("Ingrese la cantidad de meses de simulación: "))
i = 1
efn = 0
matriz = []

while i <= 2 * mf:
	if i % 2 == 1:
		if ei > namo:
			dif = ei - namo
			ei = namo
			print("Se superó el nivel del NAMO." + "\n")
			if dif >= 30:
				print("Riesgo de desbordamiento." + "\n")
		if i == 1:
			ef = namino
		else:
			ei = efn

		if mi == 1:
			xi = 400
		elif mi == 2:
			xi = 370
		elif mi == 3:
			xi = 360
		elif mi == 4:
			xi = 370
		elif mi == 5:
			xi = 400
		elif mi == 6:
			xi = 420
		elif mi == 7:
			xi = 580
		elif mi == 8:
			xi = 820
		elif mi == 9:
			xi = 1850
		elif mi == 10:
			xi = 1100
		elif mi == 11:
			xi = 420
		elif mi == 12:
			xi = 390
		vll = 0
		veva = 0
		vinf = 0	

		h = ei - ef

		Ai = -0.00000000011242133210*ei**6 + 0.00000032867408242011*ei**5 - 0.00039904098985664300*ei**4 + 0.25752569396893200000*ei**3 - 93.17322452375990000000*ei**2 + 17918.34678822460000000000*ei - 1430967.15209796000000000000

		Vi = -0.00000000188998886593*ei**6 + 0.00000552509629311165*ei**5 - 0.00671575787830005000*ei**4 + 4.34536181124196000000*ei**3 - 1578.59855589843000000000*ei**2 + 305268.07772519100000000000*ei - 24546945.05418570000000000000

		if h >= 85:
			Si = 490
		elif 63 <= h < 85:
			Si = 490 * math.sqrt(h/85)
		elif h < 63:
			Si = 0

		Pi = vll - veva - vinf

		vf = Vi + xi - Si + Pi

		er = -0.00000000000000000300*vf**6 + 0.00000000000003641386*vf**5 - 0.00000000017231570203*vf**4 + 0.00000039955084270293*vf**3 - 0.00047175884348860100*vf**2 + 0.29053131259024700000*vf + 419.87258508292100000000

		if er < ei:
			hf = er - namino
		else:
			hf = namo - namino

		Af = -0.00000000011242133210*er**6 + 0.00000032867408242011*er**5 - 0.00039904098985664300*er**4 + 0.25752569396893200000*er**3 - 93.17322452375990000000*er**2 + 17918.34678822460000000000*er - 1430967.15209796000000000000

		hprom = (h + hf) / 2

		Aprom = (Ai + Af) / 2

		i = i + 1

	if i % 2 == 0:
		if ei > namo:
			dif = ei - namo
			ei = namo
			print("Se superó el nivel del NAMO." + "\n")
			if dif >= 30:
				print("Riesgo de desbordamiento." + "\n")
		if i == 2:
			ef = namino
		else:
			ef = er

		if mi == 1:
			xi = 400
			hp = 0.046
			evap = 0.059
		elif mi == 2:
			xi = 370
			hp = 0.046
			evap = 0.067
		elif mi == 3:
			xi = 360
			hp = 0.034
			evap = 0.117
		elif mi == 4:
			xi = 370
			hp = 0.008
			evap = 0.133
		elif mi == 5:
			xi = 400
			hp = 0.076
			evap = 0.161
		elif mi == 6:
			xi = 420
			hp = 0.494
			evap = 0.138
		elif mi == 7:
			xi = 580
			hp = 0.377
			evap = 0.119
		elif mi == 8:
			xi = 820
			hp = 0.255
			evap = 0.114
		elif mi == 9:
			xi = 1850
			hp = 0.288
			evap = 0.086
		elif mi == 10:
			xi = 1100
			hp = 0.195
			evap = 0.086
		elif mi == 11:
			xi = 420
			hp = 0.078
			evap = 0.062
		elif mi  == 12:
			xi = 390
			hp = 0.07
			evap = 0.065

		vll = Aprom * hp
		veva = hp * evap

		h = ei - namino

		Ai = -0.00000000011242133210*ei**6 + 0.00000032867408242011*ei**5 - 0.00039904098985664300*ei**4 + 0.25752569396893200000*ei**3 - 93.17322452375990000000*ei**2 + 17918.34678822460000000000*ei - 1430967.15209796000000000000

		Vi = -0.00000000188998886593*ei**6 + 0.00000552509629311165*ei**5 - 0.00671575787830005000*ei**4 + 4.34536181124196000000*ei**3 - 1578.59855589843000000000*ei**2 + 305268.07772519100000000000*ei - 24546945.05418570000000000000

		if h >= 85:
			Si = 490
		elif 63 <= h < 85:
			Si = 490 * math.sqrt(h/85)
		elif h < 63:
			Si = 0

		Pi = vll - veva - vinf

		vf = Vi + xi - Si + Pi

		er = -0.00000000000000000300*vf**6 + 0.00000000000003641386*vf**5 - 0.00000000017231570203*vf**4 + 0.00000039955084270293*vf**3 - 0.00047175884348860100*vf**2 + 0.29053131259024700000*vf + 419.87258508292100000000

		if er < ei:
			hf = er - namino
		else:
			hf = namo - namino

		Af = -0.00000000011242133210*er**6 + 0.00000032867408242011*er**5 - 0.00039904098985664300*er**4 + 0.25752569396893200000*er**3 - 93.17322452375990000000*er**2 + 17918.34678822460000000000*er - 1430967.15209796000000000000
		
		hprom = (h + hf) / 2

		Aprom = (Ai + Af) / 2

		efn = er

		agg = [ei, h, Ai, Vi, xi, Si, vll, veva, vinf, Pi, vf, er, hf, Af, hprom, Aprom]
		matriz.append(agg)
		print(str(agg) + "\n")
		i = i + 1
		if mi >= 12:
			mi = 1
		else:
			mi = mi + 1		
