import os.path, subprocess, sys, random, platform, pdb, signal
from pathlib import Path
#import pdb

#pdb.set_trace()

def checkToRun():

	global flagOS, flagPlayList, musicPath, homePath
	flagOS=platform.system()
	flagPlayList=os.path.exists('playlistMP3Instrumentais.txt')
	if flagPlayList == True and sum(1 for line in open('playlistMP3Instrumentais.txt')) != 0 :
		print('Executando o script');
	else:
		print('O arquivo playlistMP3Instrumentais.txt tem que ser criado antes de executar este script.');
		print('Para verificar comando a ser executado, execute: $ head musicaDesteScript');
		sys.exit()
	if flagOS == 'Windows' :
		pass
	elif flagOS == 'Linux' :
		homePath = str(Path.home())
		musicPath = homePath+'/Music'
	else :
		print('Necessario Implementar codigo para o sistema')

def runMP3Instrumentais():
	banda='empty'
	musica='empty'
	while toPlay != 0 :
		flag='0'
		toPlayMP3InstrumentaisNowFL = open('toPlayMP3Instrumentais.txt').readline()
		open('playNowMP3Instrumentais.tmp', 'w').write(toPlayMP3InstrumentaisNowFL)
		if letra == 'sim' :
#			.split('-', 1) -> quantidade de separadores = 1
#			bandaEmusica = toPlayMP3InstrumentaisNowFL.replace('.MP3Instrumentais', '').split('-', 1)
#			...split('/')[-1].split('-') -> split com dois separadores / e -; -1 equivalente a ultima instancia.
			bandaEmusica = toPlayMP3InstrumentaisNowFL.replace('.MP3Instrumentais', '').split('/')[-1].split('-')
			print(bandaEmusica)
			print('Erro acima corrigido')
			banda = bandaEmusica[0]
			print(banda)
			musica = bandaEmusica[1].rstrip("\n\r")
			print(musica)
			print(musicPath)
			flagMusica = musica
			parenteses = '('
			if parenteses in musica :
				musica = musica.split('(')[0]
			#print(musica)
			a=0
			for root, dirs, files in os.walk(musicPath):
				for line in files:
					filePath=(root+'/'+str(line))
#					linha=line.replace(' ', '').replace("'", '')
					#print(filePath)
					#print(line)
#					print(filePath)
#					print(homePath)
#					if linha.endswith('.txt') and banda in linha and musica in linha :
#						open(homePath+'/teste2.log', 'a').writelines(filePath)
					if line.endswith('.txt') :
#						flagBandaEMusica = line.replace('.txt', '').replace('-', '').split('/')[-1].split('(')
#						flagBanda = flagBandaEMusica[1]
#						flagMusica = flagBandaEMusica[0]
#						print(flagBandaEMusica)
#						print(flagMusica)
#						print(flagBanda)
#						open(str(Path.home())+'/teste.log', 'a').writelines(filePath)
#						pass
#						if banda in flagBanda :
						if banda in line :
#							print(musica)
#							print(flagMusica)
#							pass
#							if musica in flagMusica :
							if musica in line :
#								print('oi')
#								print(filePath)
#								print(musica)
#								open(str(Path.home())+'/teste2.log', 'a').writelines(filePath)
#								print(a)
#								a += 1
#								print(banda)
#								#print(musica)
#								print(musica)
								PID=subprocess.Popen(['gedit', '-s', filePath]).pid 
#								print(PID)
								flag='1'
								break
				if flag == '1' :
					break
		if flagPlayList == True :
			pass
		else :
			open(str(Path.home())+'/playlistMP3Instrumentais.txt', 'w').writelines('')
			for root, dirs, files in os.walk(musicPath):
				print(musicPath)
				for line in files:
					if line.endswith('.MP3Instrumentais'):
						filePath=(root+'/'+str(line))
						open(str(Path.home())+'/playlistMP3Instrumentais.txt', 'a').writelines(filePath+line+"\n")
		if flagOS == 'Windows' :
			subprocess.call('C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe /play /close "C:/Users/Student/Documents/notes/file.MP3Instrumentais"')
		elif flagOS == 'Linux' :
			subprocess.call(['mplayer', '-playlist', homePath + '/playNowMP3Instrumentais.tmp'])
				#'/home/marcospaulo/playNowMP3Instrumentais.tmp'])
		else :
			print('Necessario Implementar codigo para o sistema')
		if flag == '1' :
			os.kill(PID, signal.SIGKILL)
		with open('toPlayMP3Instrumentais.txt', 'r') as files:
			for line in files:
				if toPlayMP3InstrumentaisNowFL in line :
					with open('toPlayMP3Instrumentais.txt', 'a') as files:
						files.write(line.replace(toPlayMP3InstrumentaisNowFL, ''))
		print(homePath + '/toPlayMP3Instrumentais.txt', sum(1 for line in open(homePath + '/toPlayMP3Instrumentais.txt')))
		print(homePath + '/playedMP3Instrumentais.tmp', sum(1 for line in open(homePath + '/playedMP3Instrumentais.tmp')))
		lines = open('toPlayMP3Instrumentais.txt').readlines()
		random.shuffle(lines)
		open('toPlayMP3Instrumentais.txt', 'w').writelines(lines)
##		with open('playedMP3Instrumentais.tmp', 'r') as played:
##			lines = set(played)
#		Classificando = []
##		Cla=open('ClassificandoPlayedMP3Instrumentais.txt', 'r').readlines()
#		with open('ClassificandoPlayedMP3Instrumentais.txt', 'r') as Classificando:
#			Cla = Classificando.readlines()

		with open('playedMP3Instrumentais.tmp') as playedMP3Instrumentais, open('ClassificandoPlayedMP3Instrumentais.txt', 'a+') as ClassificandoPlayedMP3Instrumentais:
			for line in ClassificandoPlayedMP3Instrumentais:
				if not any(linePlayedMP3Instrumentais in line for linePlayedMP3Instrumentais in playedMP3Instrumentais):
					ClassificandoPlayedMP3Instrumentais.write(linePlayedMP3Instrumentais)

#		for lines in Cla:
#			if line not in lines:
#			if line in lines:
#				lines.remove(line)
#			else:
#				open('ClassificandoPlayedMP3Instrumentais.txt', 'a+').write(line + '\n')
#				with open('ClassificandoPlayedMP3Instrumentais.txt', 'a') as Classificando:
#					Classificando.append(line)

		lines = open(homePath + "/toPlayMP3Instrumentais.txt", "r").readlines()
		remove = open(homePath + "/playNowMP3Instrumentais.tmp", "r").readlines()
		remove = remove[0].rstrip("\n\r")
		with open(homePath + "/toPlayMP3Instrumentais.txt", "w") as f:
			for line in lines:
				line = line.rstrip("\n\r")
				if line != remove:
					f.write(line+'\n')

		organizar = open('ClassificandoPlayedMP3Instrumentais.txt').readlines()
		organizar.sort()
		open('ClassificandoPlayedMP3Instrumentais.txt', 'w').writelines(organizar)

def prepareToRun():
	Path(homePath + '/playedMP3Instrumentais.txt').touch()
	Path(homePath + '/toPlayMP3Instrumentais.tmp').touch()
	Path(homePath + '/toPlayMP3Instrumentais.txt').touch()
	list=[homePath + '/playedMP3Instrumentais.txt', homePath + '/toPlayMP3Instrumentais.tmp', homePath + '/toPlayMP3Instrumentais.txt']
	for valor in list:
		os.chmod(valor, 0o600);
	global toPlay, letra
	toPlay=sum(1 for line in open(homePath + '/toPlayMP3Instrumentais.txt'))
	letra=input('Letra de Musica? sim/nao\n')

def runForFirstTime ():

	if toPlay == 0 :
		lines = open('playlistMP3Instrumentais.txt').readlines()
		random.shuffle(lines)
		open(homePath + '/toPlayMP3Instrumentais.txt', 'w').writelines(lines)
		os.remove(homePath + "/playedMP3Instrumentais.tmp")
		print("File " + homePath + "/playedMP3Instrumentais.tmp Removed!")

def main():
	checkToRun()
	prepareToRun()
	runForFirstTime()
	runMP3Instrumentais()

if __name__ == '__main__':
	main()
