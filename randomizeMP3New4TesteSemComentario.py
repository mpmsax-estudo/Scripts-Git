#!/usr/bin/python3.6

import os.path, subprocess, sys, random, platform, pdb, signal
from pathlib import Path
# To debug with pdb grep -v ^'#-' esseScript.py > novoScriptDebugPDB.py
#-import pdb

#-pdb.set_trace()

######################### Sort list by initial letter
######################### reduce number of code lines

# Generate playlistMP3.txt in linux Konsole
# Directories that you want
#find $HOME/Music/ -maxdepth 1 -iname *.mp3 > ~/runMP3/playlistMP3.txt;
#find $HOME/Music/claOtimasMasNaoAlcancoTonalidade/ -maxdepth 1 -iname *.mp3 >> ~/runMP3/playlistMP3.txt;
#find $HOME/Music/claMusicasInstrumentais/ -iname *.mp3 >> ~/runMP3/playlistMP3.txt;
# directoriesMP3\&Youtube.txt

# N1 to run
# Verify condition to run program

def readlines(fileName) :
	lines = open(dirToRun + fileName).readlines()

def checkToRun():
	global flagOS, flagPlayList, musicPath, homePath, dirToRun
	flagOS=platform.system()

	if flagOS == 'Windows' :
		pass
	elif flagOS == 'Linux' :
		homePath = str(Path.home())
##		print(homePath)
		dirToRun = os.path.join(homePath,"runMP3")
		if not os.path.exists(dirToRun):
			os.mkdir(dirToRun)
##		print(dirToRun)

		musicPath = homePath+'/Music'
	else :
		print('Necessario Implementar codigo para o sistema')

	flagPlayList=os.path.exists(dirToRun + '/playlistMP3.txt')
	if flagPlayList == True and sum(1 for line in open(dirToRun + '/playlistMP3.txt')) != 0 :
		print('Executando o script');
	else:
		print('O arquivo playlistMP3.txt tem que ser criado antes de executar este script.');
		print('Para verificar comando a ser executado, execute: $ head musicaDesteScript');
		sys.exit()

# N4 to run
# Run program
def runMP3():
	banda='empty'
	musica='empty'
	toPlayMP3File = '/toPlayMP3.txt'
	countToPlay=sum(1 for line in open(dirToRun + '/toPlayMP3.txt'))

#	start condition to choose list or band
	if escBanda == 's' :
		toPlayMP3File = '/toPlayMP3BandList.txt'

#		Show bands and lists to choose

#		Localizacao das listas
#		999-MusicasAnime/ = MusicasAnime\n 999-MusicasAnime/Naruto(classico) = Naruto(classico)\n \
#		999-MusicasAnime/NarutoShippuden = NarutoShippuden\n 999-MusicasAnime/Bleach = Bleach\n \
#		999-MUSICASELETRASDEMUSICA/Chronotorious = Chronotorious\n claMusicasInstrumentais\n \
#		claMusicasInstrumentais/FILMES/Back_To_The_Future = Back_To_The_Future\n \
#		claMusicasInstrumentais/Rock/(2013)UnstoppableMomentum = UnstoppableMomentum\n \
#		claMusicasInstrumentais/VA-TheMellowSoundOfJazz-RomanticJazzMoments-2013 = RomanticJazzMoments
		uniqueList = []
#		Especific lists selected
		bandasToChoose = ['MusicasAnime', 'Naruto(classico)', 'NarutoShippuden', 'Bleach', 'Chronotorious', 'claMusicasInstrumentais', \
		'Back_To_The_Future', 'UnstoppableMomentum', 'RomanticJazzMoments']
		removeList = [ '', '02.PenniesFromHeaven', '09.SmokeGetsInYourEyes', '11.SometimesImHappy', '14.HowDeepIsTheOcean', '16.Godchild', \
		'18.ItNeverEnteredInMind', '35.AStringOfPearls' ]
		bandasEmusicas = open(dirToRun + '/playlistMP3.txt').readlines()
		for line in bandasEmusicas :
			banda = line.split('/')[-1].split('-')[0]
			if banda not in uniqueList:
				if banda not in removeList:
					uniqueList.append(banda)
##		print(uniqueList)

		uniqueList.sort()
		bandasToChoose.extend(uniqueList)

		bandasEnumeracao = []

######## Between this junks - don't delete these codes
# First codes can be placed by second codes

# First codes - count number of array identity
#		for idx, line in enumerate(bandasToChoose):
#			bandasEnumeracao.append(line + ' N=' + str(idx))
# Second codes - count quantity of songs by band or list - codigo correto
		for idx, bTCline in enumerate(bandasToChoose):
			count = 0
			for root, dirs, files in os.walk(musicPath):
				for fline in files:
					if fline.endswith('.mp3') :
						filePath=(root+'/'+str(fline))
						if bandasToChoose[idx] in filePath :
							count += 1
			bandasEnumeracao.append('Qnt=' + str(count) + ' ' + bTCline + ' N=' + str(idx))
########
		print(bandasEnumeracao)

		qualBanda=input('Qual banda ou lista? Digitar apenas os numeros separados por espacos.\n')

#		caracteresInvalidos
		invalido='abcdefghijklmnopqrstuvwxyz'
		for i in invalido :
			if i in qualBanda :
				print('Musica escolhida invalida, necessario valores numericos separados por espacos')
				sys.exit()

		qualBanda = (qualBanda.split(' '))

#		Generate file with all possible songs (PS: Some songs aren't on playlistMP3.txt)
		open(dirToRun + toPlayMP3File, 'w').writelines('')
		for root, dirs, files in os.walk(musicPath):
			for line in files:
				filePath=(root+'/'+str(line))
				if line.endswith('.mp3') :
					open(dirToRun + toPlayMP3File, 'a').writelines(filePath+'\n')

		bandasEmusicas = open(dirToRun + toPlayMP3File).readlines()
##		print(bandasEmusicas)

#		Generate file: band or list choosen
### 	Debug - copy file without the inicial grep -v ^'##' esseScript.py > novoScriptDebug.py
##		toPlayMP3BandList = []
		open(dirToRun + toPlayMP3File, 'w').writelines('')
		for line in bandasEmusicas :
			for x in qualBanda :
				if bandasToChoose[int(x)] in line :
					open(dirToRun + toPlayMP3File, 'a').writelines(line)

		organizar = open(dirToRun + toPlayMP3File).readlines()
		random.shuffle(organizar)
		open(dirToRun + toPlayMP3File, 'w').writelines(organizar)

#		count quantity of songs to play
		countToPlay=sum(1 for line in open(dirToRun + toPlayMP3File))

#	Condition to execute program, until the last song
	while countToPlay != 0 :
		flag='0'
		toPlayMP3NowFL = open(dirToRun + toPlayMP3File).readline()
		open(dirToRun + '/playNowMP3.tmp', 'w').write(toPlayMP3NowFL)
		print(toPlayMP3NowFL)

#		Condition to open lyrics of songs for each playing
		if letra == 's' :
			bandasEmusicas = toPlayMP3NowFL.replace('.mp3', '').split('/')[-1].split('-')
			print(bandasEmusicas)
			print('Erro acima corrigido')
			banda = bandasEmusicas[0]
##			print(banda)
			musica = bandasEmusicas[1].rstrip("\n\r")
##			print(musica)
##			print(musicPath)
			parenteses = '('
			if parenteses in musica :
				musica = musica.split('(')[0]
##			print(musica)
			a=0
			for root, dirs, files in os.walk(musicPath):
				for line in files:
					filePath=(root+'/'+str(line))
##					print(filePath)
##					print(line)
					if line.endswith('.txt') :
						if banda in line :
							if musica in line :
								PID=subprocess.Popen(['gedit', '-s', filePath]).pid
##								print('PID letra de musica: ' + PID)
								flag='1'
								break
				if flag == '1' :
					break
#		Condition: if song list exists
		if flagPlayList == True :
			pass

#		Condition: if song list doesn't exist
		else :
			open(dirToRun+'/playlistMP3.txt', 'w').writelines('')
			for root, dirs, files in os.walk(musicPath):
				print(musicPath)
				for line in files:
					if line.endswith('.mp3'):
						filePath=(root+'/'+str(line))
						open(dirToRun+'/playlistMP3.txt', 'a').writelines(filePath+line+"\n")
#		if operational system is Windows
		if flagOS == 'Windows' :
			subprocess.call('C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe /play /close "C:/Users/Student/Documents/notes/file.mp3"')
#		if operational system is Linux
		elif flagOS == 'Linux' :
			subprocess.call(['mplayer', '-playlist', dirToRun + '/playNowMP3.tmp'])
		else :
#		For other Operational Systems
			print('Necessario Implementar codigo para o sistema')
		if flag == '1' :
			os.kill(PID, signal.SIGKILL)

#		Remove played song from file list
		with open(dirToRun + toPlayMP3File, 'r') as files:
			for line in files:
				if toPlayMP3NowFL in line :
					with open(dirToRun + toPlayMP3File, 'a') as files:
						files.write(line.replace(toPlayMP3NowFL, ''))
		lines = open(dirToRun + toPlayMP3File).readlines()
		random.shuffle(lines)
		open(dirToRun + toPlayMP3File, 'w').writelines(lines)

######## NAO ESTA PRONTO
##		with open('playedMP3.tmp', 'r') as played:
##			lines = set(played)
#		Classificando = []
##		Cla=open('ClassificandoPlayedMP3.txt', 'r').readlines()
#		with open('ClassificandoPlayedMP3.txt', 'r') as Classificando:
#			Cla = Classificando.readlines()
######## programando para classificar musicas
#/*
#		playedMP3 = open(dirToRun + '/playedMP3.tmp').readlines()
#		Path(dirToRun + '/ClassificandoPlayedMP3.txt').touch()
#		ClassificandoPlayedMP3 = open(dirToRun + '/ClassificandoPlayedMP3.txt').readlines()
		countPlayed=sum(1 for line in open(dirToRun + '/playedMP3.tmp'))
#		if countPlayed != 0 :
#			with open(dirToRun + '/playedMP3.tmp') as playedMP3, open('ClassificandoPlayedMP3.txt', 'a+') as ClassificandoPlayedMP3:
#				for claLine in ClassificandoPlayedMP3 :
#					if not any(linePlayedMP3 in line for line in playedMP3):
#						ClassificandoPlayedMP3.(linePlayedMP3)
#						*/
#		for lines in Cla:
#			if line not in lines:
#			if line in lines:
#				lines.remove(line)
#			else:
#				open('ClassificandoPlayedMP3.txt', 'a+').write(line + '\n')
#				with open('ClassificandoPlayedMP3.txt', 'a') as Classificando:
#					Classificando.append(line)
######## NAO ESTA PRONTO - FINAL

#		Delete played song
		lines = open(dirToRun + toPlayMP3File, "r").readlines()
		remove = open(dirToRun + "/playNowMP3.tmp", "r").readlines()
		print(remove)
		remove = remove[0].rstrip("\n\r")
		with open(dirToRun + toPlayMP3File, "w") as f:
			for line in lines:
				line = line.rstrip("\n\r")
				if line != remove:
					f.write(line+'\n')

######## NAO ESTA PRONTO
#		organizar = open('ClassificandoPlayedMP3.txt').readlines()
#		organizar.sort()
#		open('ClassificandoPlayedMP3.txt', 'w').writelines(organizar)
######## NAO ESTA PRONTO - FINAL

		print(dirToRun + '/toPlayMP3.txt', sum(1 for line in open(dirToRun + '/toPlayMP3.txt')))
		print(dirToRun + '/playedMP3.tmp: ', countPlayed)
		print(dirToRun + '/toPlayMP3BandList.txt', sum(1 for line in open(dirToRun + '/toPlayMP3BandList.txt')))

		countToPlay=sum(1 for line in open(dirToRun + toPlayMP3File))

		if countToPlay == 0 and escBanda == 's' :
			print('Arquivo toPlayMP3BandList.txt esta vazio, saindo do programa.')
			sys.exit()
		if countToPlay == 0 and escBanda != 's' :
			print('Arquivo toPlayMP3.txt esta vazio, saindo do programa.')
			sys.exit()

# N2 to run
def prepareToRun():
	Path(dirToRun + '/playedMP3.txt').touch()
	Path(dirToRun + '/toPlayMP3.tmp').touch()
	Path(dirToRun + '/toPlayMP3.txt').touch()
	Path(dirToRun + '/toPlayMP3BandList.txt').touch()
	Path(dirToRun + '/playedMP3.tmp').touch()
	Path(dirToRun + '/playNowMP3.tmp').touch()
	list=[dirToRun + '/playedMP3.txt', dirToRun + '/toPlayMP3.tmp', dirToRun + '/toPlayMP3.txt', dirToRun + '/toPlayMP3BandList.txt']
	for valor in list:
		os.chmod(valor, 0o600);
	global countToPlay, letra, escBanda, qualBanda
	countToPlay=sum(1 for line in open(dirToRun + '/toPlayMP3.txt'))
	letra=input('Letra de Musica? s/n\n')
	escBanda=input('Escolher banda ou lista? s/n\n')

# N3 to run
def runForFirstTime ():
	if countToPlay == 0 :
		lines = open(dirToRun + '/playlistMP3.txt').readlines()
		random.shuffle(lines)
		open(dirToRun + '/toPlayMP3.txt', 'w').writelines(lines)

		lines = open(dirToRun + '/toPlayMP3BandList.txt').readlines()
		random.shuffle(lines)
		open(dirToRun + '/toPlayMP3BandList.txt', 'w').writelines(lines)

		Path(dirToRun + '/playedMP3.tmp').touch()
		os.remove(dirToRun + "/playedMP3.tmp")
		print("File " + dirToRun + "/playedMP3.tmp Removed!")

	else :
		pass

def main():
	checkToRun()
	prepareToRun()
	runForFirstTime()
	runMP3()

if __name__ == '__main__':
	main()
