import os
import random
import bluepy # 要インストール

COCOA_UUID = "0000fd6f-0000-1000-8000-00805f9b34fb"

while True:
	scanner = bluepy.btle.Scanner(0)
	devices = scanner.scan(3.0) # 引数はスキャンする秒数
	print('Scanning...')
	for device in devices:
		for (adtype, desc, value) in device.getScanData():
			if value == COCOA_UUID and device.rssi > -40: # 受信範囲の設定（40を大きくすると範囲が広くなる）
				print('Device found!')
				num = random.randrange(6)
				if num == 0:
					os.system("omxplayer daikiti.mp4")
				elif num == 1:
					os.system("omxplayer tyuukiti.mp4")
				elif num == 2:
					os.system("omxplayer syoukiti.mp4")
				elif num == 3:
					os.system("omxplayer kiti.mp4")
				elif num == 4:
					os.system("omxplayer kyou.mp4")
				elif num == 5:
					os.system("omxplayer daikyou.mp4")
