import os.path, subprocess, sys, random, platform, pdb, signal
from pathlib import Path
#import pdb

#pdb.set_trace()

def checkToRun():

	global flagOS, flagPlayList, musicPath, homePath
	flagOS=platform.system()
	flagPlayList=os.path.exists('playlistMP3.txt')
	if flagPlayList == True and sum(1 for line in open('playlistMP3.txt')) != 0 :
		print('Executando o script');
	else:
		print('O arquivo playlistMP3.txt tem que ser criado antes de executar este script.');
		print('Para verificar comando a ser executado, execute: $ head musicaDesteScript');
		sys.exit()
	if flagOS == 'Windows' :
		pass
	elif flagOS == 'Linux' :
		homePath = str(Path.home())
		musicPath = homePath+'/Music'
	else :
		print('Necessario Implementar codigo para o sistema')

def runMP3():
	banda='empty'
	musica='empty'
	while toPlay != 0 :
		flag='0'
		toPlayMP3NowFL = open('toPlayMP3.txt').readline()
		open('playNowMP3.tmp', 'w').write(toPlayMP3NowFL)

		if letra == 'sim' :
#			.split('-', 1) -> quantidade de separadores = 1
#			bandaEmusica = toPlayMP3NowFL.replace('.mp3', '').split('-', 1)
#			...split('/')[-1].split('-') -> split com dois separadores / e -; -1 equivalente a ultima instancia.
			bandaEmusica = toPlayMP3NowFL.replace('.mp3', '').split('/')[-1].split('-')
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
			open(str(Path.home())+'/playlistMP3.txt', 'w').writelines('')
			for root, dirs, files in os.walk(musicPath):
				print(musicPath)
				for line in files:
					if line.endswith('.mp3'):
						filePath=(root+'/'+str(line))
						open(str(Path.home())+'/playlistMP3.txt', 'a').writelines(filePath+line+"\n")
		if flagOS == 'Windows' :
			subprocess.call('C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe /play /close "C:/Users/Student/Documents/notes/file.mp3"')
		elif flagOS == 'Linux' :
			subprocess.call(['mplayer', '-playlist', homePath + '/playNowMP3.tmp'])
				#'/home/marcospaulo/playNowMP3.tmp'])
		else :
			print('Necessario Implementar codigo para o sistema')
		if flag == '1' :
			os.kill(PID, signal.SIGKILL)
		with open('toPlayMP3.txt', 'r') as files:
			for line in files:
				if toPlayMP3NowFL in line :
					with open('toPlayMP3.txt', 'a') as files:
						files.write(line.replace(toPlayMP3NowFL, ''))
		print(homePath + '/toPlayMP3.txt', sum(1 for line in open(homePath + '/toPlayMP3.txt')))
		print(homePath + '/playedMP3.tmp', sum(1 for line in open(homePath + '/playedMP3.tmp')))
		lines = open('toPlayMP3.txt').readlines()
		random.shuffle(lines)
		open('toPlayMP3.txt', 'w').writelines(lines)
##		with open('playedMP3.tmp', 'r') as played:
##			lines = set(played)
#		Classificando = []
##		Cla=open('ClassificandoPlayedMP3.txt', 'r').readlines()
#		with open('ClassificandoPlayedMP3.txt', 'r') as Classificando:
#			Cla = Classificando.readlines()

		with open('playedMP3.tmp') as playedMP3, open('ClassificandoPlayedMP3.txt', 'a+') as ClassificandoPlayedMP3:
			for line in ClassificandoPlayedMP3:
				if not any(linePlayedMP3 in line for linePlayedMP3 in playedMP3):
					ClassificandoPlayedMP3.write(linePlayedMP3)

#		for lines in Cla:
#			if line not in lines:
#			if line in lines:
#				lines.remove(line)
#			else:
#				open('ClassificandoPlayedMP3.txt', 'a+').write(line + '\n')
#				with open('ClassificandoPlayedMP3.txt', 'a') as Classificando:
#					Classificando.append(line)

#		Deleta musica jah tocada
		lines = open(homePath + "/toPlayMP3.txt", "r").readlines()
		remove = open(homePath + "/playNowMP3.tmp", "r").readlines()
		remove = remove[0].rstrip("\n\r")
		with open(homePath + "/toPlayMP3.txt", "w") as f:
			for line in lines:
				line = line.rstrip("\n\r")
				if line != remove:
					f.write(line+'\n')

		organizar = open('ClassificandoPlayedMP3.txt').readlines()
		organizar.sort()
		open('ClassificandoPlayedMP3.txt', 'w').writelines(organizar)

def prepareToRun():
	Path(homePath + '/playedMP3.txt').touch()
	Path(homePath + '/toPlayMP3.tmp').touch()
	Path(homePath + '/toPlayMP3.txt').touch()
	list=[homePath + '/playedMP3.txt', homePath + '/toPlayMP3.tmp', homePath + '/toPlayMP3.txt']
	for valor in list:
		os.chmod(valor, 0o600);
	global toPlay, letra
	toPlay=sum(1 for line in open(homePath + '/toPlayMP3.txt'))
	letra=input('Letra de Musica? sim/nao\n')

def runForFirstTime ():

	if toPlay == 0 :
		lines = open('playlistMP3.txt').readlines()
		random.shuffle(lines)
		open(homePath + '/toPlayMP3.txt', 'w').writelines(lines)
		os.remove(homePath + "/playedMP3.tmp")
		print("File " + homePath + "/playedMP3.tmp Removed!")

def main():
	checkToRun()
	prepareToRun()
	runForFirstTime()
	runMP3()

if __name__ == '__main__':
	main()
