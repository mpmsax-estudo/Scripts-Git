#!/bin/python

import os.path, subprocess, sys, random, platform
from pathlib import Path

#OBS:   O QUE ESTA COMENTADO JAH FOI CODIFICADO EM PYTHON
#       CONTINUAR CODIFICACAO PARA PYTHON

# os.path.exists -> check if file exists; sum (...) count total lines of file;
def checkToRun():
	flagOS=platform.system() # verifica o sistema operacional. Ex: Linux
	flagPlayList=os.path.exists('playlistMP3.txt')
	if flagPlayList == True and sum(1 for line in open('playlistMP3.txt')) != 0 :
	    print('Executando o script');
	else:
	    print('O arquivo playlistMP3.txt tem que ser criado antes de executar este script.');
	    print('Para verificar comando a ser executado, execute: $ head musicaDesteScript');
	    sys.exit()	
	return flagOS,flagPlayList


### PARA USAR ###
# Abrir programa
###subprocess.call('gedit')
#subprocess.call(['mplayer', '-playlist', '/home/marcospaulo/playNowMP3.tmp'])


def runMP3():
	while toPlay != 0 :
		with open('toPlayMP3.txt') as files:
	        toPlayMP3NowFL = files.readline() # Ler primeira linha
		with open('playNowMP3.tmp', 'w') as line:
		    line.write(toPlayMP3NowFL) # sobrescrever arquivo e inserir uma linha
		if letra == 0 :
			bandaEmusica = toPlayMP3NowFL.replace('.mp3', '').split('/')[-1].split('-')
			banda = bandaEmusica[0]
			musica = bandaEmusica[1]
			flagMusica = musica
			parenteses = '('
			if parenteses in musica :
#			if [ "$musica | grep -o '('" == '(' ]; then
				musica = musica.split('(')[0]
#				musica=$(echo $musica | awk -F'(' '{print $1}');
		#dir_path = '/home/marcospaulo/Music'

		if flagOS == 'Windows' :
			#home = str(Path.home())+'/Music/'
		elif flagOS == 'Linux' :
			dir_path = str(Path.home())+'/Music/'
		else :
			print('Necessario Implementar codigo para o sistema')
		dir_path = str(Path.home())+'/Music'
		if flagPlayList == True :
			pass
		else
			open(str(Path.home())+'/playlistMP3.txt', 'w').writelines('')
			for root, dirs, files in os.walk(dir_path):
			    for line in files:
			        if line.endswith('.mp3'):
			            filePath=(root+'/'+str(line))
			            open(str(Path.home())+'/playlistMP3.txt', 'a').writelines(filePath+line+"\n")
		for root, dirs, files in os.walk(dir_path):
		    for line in files:
		#        musica = file.endswith('.mp3')
		        #if musica : 
		        if line.endswith('.txt'):
		            if banda in line :
		                if musica in line :
		                    filePath=(root+'/'+str(line))
		                    #print(teste)
		                    #subprocess.call(['gedit', teste])
		                    PID=subprocess.Popen(['gedit', '-s', filePath]).pid # Carrega letra de Musica
		#                        '/home/marcospaulo/playNowMP3.tmp'])
		                    flag='1'
		    if flag == '1' :
		        break
		if flagOS == 'Windows' :
			subprocess.call('C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe /play /close "C:/Users/Student/Documents/notes/file.mp3"')
		elif flagOS == 'Linux' :
			subprocess.call(['mplayer', '-playlist', '/home/marcospaulo/playNowMP3.tmp'])
		else :
			print('Necessario Implementar codigo para o sistema')
		os.kill(PID, signal.SIGKILL) # Mata PID da letra de Musica
		with open('toPlayMP3.txt', 'a') as files:
			for line in files:
		        if toPlayMP3NowFL in line :
		            files.write(line.replace('toPlayMP3NowFL', ''))
		print('toPlayMP3.txt', sum(1 for line in open('toPlayMP3.txt')))
		print('playedMP3.tmp', sum(1 for line in open('playedMP3.tmp')))
		lines = open('toPlayMP3.txt').readlines()
		random.shuffle(lines)
		open('toPlayMP3.txt', 'w').writelines(lines)
		with open('playedMP3.tmp', 'r') as played:
		    lines = set(played)  # all lines, as a set, with newlines
		Classificando = []
		with open('ClassificandoPlayedMP3.txt', 'r') as Classificando:
		    for line in Classificando:
		        if line in lines:
		            # present in both files, remove from `lines` to find extra lines in a
		            lines.remove(line)
		        else:
		            # extra line in b
		            Classificando.append(line)
		lines = open('ClassificandoPlayedMP3.txt')
		organizar = lines.readlines()
		open('ClassificandoPlayedMP3.txt', 'w').writelines(organizar)

#cat playedMP3.tmp ClassificandoPlayedMP3.txt | sort -u > ClassificandoPlayedMP3.txt
#Bash
#whileDo () {
#	while [ "$toPlay" != '0' ]; do
#		head -n1 toPlayMP3.txt > playNowMP3.tmp;
#		if [ "$letra" -eq 0 ]; then
#			bandaEmusica=$(cat playNowMP3.tmp | awk -F'/' '{print $5}' | sed 's/.mp3//g');
#			musica = musica=$(echo $bandaEmusica | awk -F'-' '{print $2}');
#			banda=$(echo $bandaEmusica | awk -F'-' '{print $1}');
#			flagMusica=$(echo $musica)'empty';
#			if [ "$musica | grep -o '('" == '(' ]; then
#				musica=$(echo $musica | awk -F'(' '{print $1}');
#			fi

#dir_path = os.path.dirname(os.path.realpath(__file__)) 
			#lyric=$(find Music/ -iname "*$musica*$banda*" | head -n1)'empty';
			#if
			#if [ "$flagMusica" != 'empty' ] && [ "$lyric" != 'empty' ]; then
			#	gedit $(echo $lyric | sed 's/empty//g')  &
			#fi
		#fi
		#mplayer -playlist playNowMP3.tmp;
		#cat toPlayMP3.txt | grep -v "$(cat playNowMP3.tmp | awk -F'/' '{print $NF}')" | sort -R > /tmp/toPlayMP3.tmp;
		#cp /tmp/toPlayMP3.tmp toPlayMP3.txt;
		#cat playNowMP3.tmp >> playedMP3.tmp;
		#toPlay=$(cat toPlayMP3.txt | wc -l);
		#wc -l toPlayMP3.txt playedMP3.tmp;
		#cat playedMP3.tmp ClassificandoPlayedMP3.txt | sort -u > /tmp/toOrderMP3Classificados.tmp;
#		cp /tmp/toOrderMP3Classificados.tmp ClassificandoPlayedMP3.txt;
#	done
#}



def prepareToRun():

	#Bash
	touch playedMP3.tmp toPlayMP3.txt /tmp/toPlayMP3.tmp;

	chmod 744 toPlayMP3.txt /tmp/toPlayMP3.tmp;

	toPlay=$(cat toPlayMP3.txt | wc -l);

	echo 'Digite se quer letra de musica: 0 para sim';
	read letra;

def runForFirstTime ():
	#Bash
	if [ "$toPlay" -eq 0 ]; then
		cat playlistMP3.txt | sort -R > toPlayMP3.txt;
		cp playedMP3.tmp playedMP3Old.tmp;
		rm playedMP3.tmp;
		toPlay=$(cat toPlayMP3.txt | wc -l);
	fi

def main():
    checkToRun()
    print('asdfasdf')
    prepareToRun()
    runForFirstTime()
    runMP3()

#whileDo # Chamar funcao

if __name__ == '__main__':
	main()
