import os.path, subprocess, sys, random, platform, pdb, signal
from pathlib import Path
# To debug with pdb grep -v ^'#-' esseScript.py > novoScriptDebugPDB.py
#-import pdb

#-pdb.set_trace()

# N1 to run
# Verify condition to run program
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
	if escBanda == 'sim' :
		toPlayMP3File = '/toPlayMP3BandList.txt'

#		Show bands and lists to choose
		uniqueList = []
		removeList = [ '', '02.PenniesFromHeaven', '09.SmokeGetsInYourEyes', '11.SometimesImHappy', '14.HowDeepIsTheOcean', '16.Godchild', \
		'18.ItNeverEnteredInMind', '35.AStringOfPearls' ]
		bandasEmusicas = open(dirToRun + '/playlistMP3.txt').readlines()
		for line in bandasEmusicas :
			banda = line.split('/')[-1].split('-')[0]
			if banda not in uniqueList:
				if banda not in removeList:
					uniqueList.append(banda)
		uniqueList.sort()
		print(uniqueList)
#		Listas especificas selecionadas
		print(' 999-MusicasAnime/ = MusicasAnime\n 999-MusicasAnime/Naruto(classico) = Naruto(classico)\n \
999-MusicasAnime/NarutoShippuden = NarutoShippuden\n 999-MusicasAnime/Bleach = Bleach\n \
999-MUSICASELETRASDEMUSICA/Chronotorious = Chronotorious\n claMusicasInstrumentais\n \
claMusicasInstrumentais/FILMES/Back_To_The_Future = Back_To_The_Future\n \
claMusicasInstrumentais/Rock/(2013)UnstoppableMomentum = UnstoppableMomentum\n \
claMusicasInstrumentais/VA-TheMellowSoundOfJazz-RomanticJazzMoments-2013 = RomanticJazzMoments')

		qualBanda=input('Qual banda ou lista?\n')

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
			if qualBanda in line :
				open(dirToRun + toPlayMP3File, 'a').writelines(line)
##					toPlayMP3BandList.append(line)
##			print(toPlayMP3BandList)
		organizar = open(dirToRun + toPlayMP3File).readlines()
		random.shuffle(organizar)
		open(dirToRun + toPlayMP3File, 'w').writelines(organizar)

#		contar quantidade de musicas a tocar
		countToPlay=sum(1 for line in open(dirToRun + toPlayMP3File))

#	Condicao para executar programa ate a ultima musica
	while countToPlay != 0 :
		flag='0'
		toPlayMP3NowFL = open(dirToRun + toPlayMP3File).readline()
		open(dirToRun + '/playNowMP3.tmp', 'w').write(toPlayMP3NowFL)
		print(toPlayMP3NowFL)
#		Condicao de exibir letras de musica
		if letra == 'sim' :
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
#		Condition: if music list exists
		if flagPlayList == True :
			pass

#		Condition: if music list don't exist
		else :
			open(dirToRun+'/playlistMP3.txt', 'w').writelines('')
			for root, dirs, files in os.walk(musicPath):
				print(musicPath)
				for line in files:
					if line.endswith('.mp3'):
						filePath=(root+'/'+str(line))
						open(dirToRun+'/playlistMP3.txt', 'a').writelines(filePath+line+"\n")
		if flagOS == 'Windows' :
			subprocess.call('C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe /play /close "C:/Users/Student/Documents/notes/file.mp3"')
		elif flagOS == 'Linux' :
			subprocess.call(['mplayer', '-playlist', dirToRun + '/playNowMP3.tmp'])
				#'/home/marcospaulo/playNowMP3.tmp'])
		else :
			print('Necessario Implementar codigo para o sistema')
		if flag == '1' :
			os.kill(PID, signal.SIGKILL)
		with open(dirToRun + toPlayMP3File, 'r') as files:
			for line in files:
				if toPlayMP3NowFL in line :
					with open(dirToRun + toPlayMP3File, 'a') as files:
						files.write(line.replace(toPlayMP3NowFL, ''))
		lines = open(dirToRun + toPlayMP3File).readlines()
		random.shuffle(lines)
		open(dirToRun + toPlayMP3File, 'w').writelines(lines)
##		with open('playedMP3.tmp', 'r') as played:
##			lines = set(played)
#		Classificando = []
##		Cla=open('ClassificandoPlayedMP3.txt', 'r').readlines()
#		with open('ClassificandoPlayedMP3.txt', 'r') as Classificando:
#			Cla = Classificando.readlines()

		countPlayed=sum(1 for line in open(dirToRun + '/playedMP3.tmp'))
		if countPlayed != 0 :
			with open(dirToRun + '/playedMP3.tmp') as playedMP3, open('ClassificandoPlayedMP3.txt', 'a+') as ClassificandoPlayedMP3:
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
		lines = open(dirToRun + toPlayMP3File, "r").readlines()
		remove = open(dirToRun + "/playNowMP3.tmp", "r").readlines()
		print(remove)
		remove = remove[0].rstrip("\n\r")
		with open(dirToRun + toPlayMP3File, "w") as f:
			for line in lines:
				line = line.rstrip("\n\r")
				if line != remove:
					f.write(line+'\n')

		organizar = open('ClassificandoPlayedMP3.txt').readlines()
		organizar.sort()
		open('ClassificandoPlayedMP3.txt', 'w').writelines(organizar)

		print(dirToRun + '/toPlayMP3.txt', sum(1 for line in open(dirToRun + '/toPlayMP3.txt')))
		print(dirToRun + '/playedMP3.tmp', sum(1 for line in open(dirToRun + '/playedMP3.tmp')))
		print(dirToRun + '/toPlayMP3BandList.txt', sum(1 for line in open(dirToRun + '/toPlayMP3BandList.txt')))

		countToPlay=sum(1 for line in open(dirToRun + toPlayMP3File))

		if countToPlay == 0 and escBanda == 'sim' :
			print('Arquivo toPlayMP3BandList.txt esta vazio, saindo do programa.')
			sys.exit()
		if countToPlay == 0 and escBanda != 'sim' :
			print('Arquivo toPlayMP3.txt esta vazio, saindo do programa.')
			sys.exit()

# N2 a executar
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
#	toPlay=sum(1 for line in open(dirToRun + '/toPlayMP3.txt'))
	countToPlay=sum(1 for line in open(dirToRun + '/toPlayMP3.txt'))
	letra=input('Letra de Musica? sim/nao\n')
	escBanda=input('Qual banda ou lista? sim/nao\n')

# N3 a executar
# executar pela primeira vez
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