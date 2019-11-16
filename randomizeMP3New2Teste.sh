#!/usr/bin/bash

######################### CRIAR NOVO SCRIPT ? PARA MP4 ##########################
#find /home/marcospaulo/Music/999-Youtube/ -iname '*.mp4' > playlistMP4.txt
#cat playlistMP4.txt | sort -R > /tmp/playlistMP4.tmp
#cp /tmp/playlistMP4.tmp playlistMP4.txt



# Nao pode-se utilizar nomes de musica:
# com mais de um "-" hyphen 
# com "´" ou "'" apostrofe - erro: letra de musica nao carrega

# Debug
set -x 

# renomearMP3.sh - Necessario retirar "'" e espacos, para esse script funcionar sem erro

#find /home/marcospaulo/Music/ -maxdepth 1 -iname *.mp3 > playlistMP3.txt;
#find /home/marcospaulo/Music/ -iname *.mp3 | grep -v Pornografica > playlistMP3.txt;
#find /home/marcospaulo/Music/MusicasInstrumentais/ -iname *.mp3 >> playlistMP3.txt;
# directoriesMP3\&Youtube.txt

# De: http://ubuntuhandbook.org/index.php/2013/08/install-smplayer-ubuntu-linux-mint-ppa/
# Install smplayer on Linux Mint
#sudo add-apt-repository ppa:rvm/smplayer
#sudo apt install smplayer
#sudo apt install mplayer

#:: Mplayer error
	#mplayer: could not connect to socket
	#mplayer: No such file or directory
	#Failed to open LIRC support. You will not be able to use your remote control.
#:: How to fix Failed to open LIRC support
	#Add ‘nolirc=yes’ in your own Mplayer config file:
	#cd
	#echo "nolirc=yes" >> .mplayer/config

# Filtrar Generos Classificados
# cat ClassificandoPlayedMP3.txt | awk -F' ' '{print $NF}' | grep -v .mp3 | sort | uniq -c;

# Adicionar espacos no nome das musicas para procura-las
#cat playlistMP3.txt | awk -F'/' '{print $NF}' | sed 's/\([^[:blank:]]\)\([[:upper:]]\)/\1 \2/g' | sed 's/- / - /g' | sed 's/&/ &/g' | sed 's/K IS S/KISS/g' | sed 's/L MF AO/LMFAO/g' | sed 's/A CD C/ACDC/g' | sed 's/E MF/EMF/g' | sed 's/AS/A S/g' | sed 's/AG/A G/g' | sed 's/AD/A D/g' | sed 's/AL/A L/g' | sed 's/AC/A C/g' | sed 's/ SZ /SZ/g' | sed 's/A CDC/ACDC/g' | sed 's/R PM/RPM/g' | sed 's/AW/A W/g' | sed 's/IM/I M/g' | sed 's/AB/A B/g' | sed 's/IC/I C/g' | sed 's/R EM/REM/g' | sed 's/ID/I D/g' | sed 's/ MØ/MØ/g' | sed 's/AT/A T/g' | sed 's/Z Z/ZZ/g' | sed 's/NI/N I/g' | sed 's/C P/CP/g' | sed 's/Z Z/ZZ/g' | sed 's/IP/I P/g' | sed 's/BL/B L/g' | sed 's/I NX S/INXS/g' | sed 's/IG/I G/g' | sed 's/AM/A M/g' | sed 's/DO A/DOA/g' | sed 's/OQ/O Q/g' | sed 's/IF/I F/g' | sed 's/AP/A P/g' | sed 's/IB/I B/g' | sed 's/C OM - PR OB LE MA - Pitbull - Give Me Everything( Ft. Ne - Yo, Afrojack, Nayer).mp3/COM-PROBLEMA - Pitbull - Give Me Everything(Ft.Ne-Yo,Afrojack,Nayer).mp3/g' | sed 's/Fromthe Inside/From The Inside/g' | sed 's/Windof/Wind Of/g' | sed 's/Puddleof/Puddle Of/g' | sed 's/( / (/g' | sed 's/Sir Mix - A - Lot/SirMix-A-Lot/g' | sed 's/Quedalivre/Queda Livre/g' | sed 's/N I B/NIB/g'

#grep MusicasInstrumentais toPlayMP3.txt > toPlayMP3Instrumentais.txt

#### if instrumentais do
#cp toPlayMP3.txt toPlayMP3.bkp
#cp toPlayMP3Instrumentais.txt toPlayMP3.txt

if [ -f playlistMP3.txt ] && [ "$(cat playlistMP3.txt | wc -l)" != '0' ]; then 
	echo 'Executando o script'; 
else
	echo 'O arquivo playlistMP3.txt tem que ser criado antes de executar este script.'
	echo 'Para verificar comando a ser executado, execute: $ head nomeDesteScript';
	exit
fi

#checkToPlayMP3 () {
#	if [ "$toPlay" != '0' ]; then
#		for i in "toPlayMP3.txt"; do
			
#		done
#	else
#		echo 'Ocorreu algum erro';
#	fi
#}

whileDo () {
	while [ "$toPlay" != '0' ]; do
		head -n1 toPlayMP3.txt > playNowMP3.tmp;
		if [ "$letra" -eq 0 ]; then
			bandaEmusica=$(cat playNowMP3.tmp | awk -F'/' '{print $5}' | sed 's/.mp3//g');
			nome=$(echo $bandaEmusica | awk -F'-' '{print $2}');
			banda=$(echo $bandaEmusica | awk -F'-' '{print $1}');
			flagParenteses=$(echo $nome | awk -F'(' '{print $1}')'empty';
			flagNome=$(echo $nome)'empty';
			#lyric=$(find Music/ -iname "*$nome*$banda*" | head -n1)'empty';
			#if [ "$lyric | grep -o '('" == '(' ]; then
 			#if [ "$nome | grep -o '('" == '\(' ]; then
 			if [ "$flagParenteses" != 'empty' ]; then
				nome=$(echo $nome | awk -F'(' '{print $1}');
				#lyric=$(find Music/ -iname "*$nome*$banda*" | head -n1)'empty';
			fi
			lyric=$(find Music/ -iname "*$nome*$banda*" | grep '.txt' | head -n1)'empty';
			if [ "$flagNome" != 'empty' ] && [ "$lyric" != 'empty' ]; then
				gedit "$(echo $lyric | sed 's/empty//g')"  &
				PID=$!
			fi
		fi
		#if [ "$letra" -ne 0 ] || [ "$flagNome" == 'empty' ] || [ "$lyric" == 'empty' ]; then
		wc -l toPlayMP3.txt playedMP3.tmp;
		# "$(playNowMP3.tmp)" -> jeito de evitar erros com caracteres especiais.
		mplayer "$(cat playNowMP3.tmp)";
		kill $PID;
		#fi
	 	#totem "$(cat playNowMP3.tmp | head -n1 | shuf -n1)";
		#mplayer -xy 400 -geometry 1250:0 "$(cat playNowMP3.tmp)"
		#xplayer $(cat playNowMP3.tmp)
		cat toPlayMP3.txt | grep -v "$(cat playNowMP3.tmp | awk -F'/' '{print $NF}')" | sort -R > /tmp/toPlayMP3.tmp;
		cp /tmp/toPlayMP3.tmp toPlayMP3.txt;
		cat playNowMP3.tmp >> playedMP3.tmp;
		toPlay=$(cat toPlayMP3.txt | wc -l);
		wc -l toPlayMP3.txt playedMP3.tmp;
		cat playedMP3.tmp ClassificandoPlayedMP3.txt | sort -u > /tmp/toOrderMP3Classificados.tmp;
		cp /tmp/toOrderMP3Classificados.tmp ClassificandoPlayedMP3.txt;
	done
}

touch playedMP3.tmp toPlayMP3.txt /tmp/toPlayMP3.tmp;

chmod 744 toPlayMP3.txt /tmp/toPlayMP3.tmp;

toPlay=$(cat toPlayMP3.txt | wc -l);
#total=$(cat playlistMP3.txt | wc -l);
#letra='1';

echo 'Digite se quer letra de musica: 0 para sim';
read letra;

if [ "$toPlay" -eq 0 ]; then
	cat playlistMP3.txt | sort -R > toPlayMP3.txt;
	cp playedMP3.tmp playedMP3Old.tmp;
	rm playedMP3.tmp;
	toPlay=$(cat toPlayMP3.txt | wc -l);
#else
#	cat toPlayMP3.txt | sort -R > /tmp/toPlayMP3.tmp;
#	cp /tmp/toPlayMP3.tmp toPlayMP3.txt;
fi

# checkToPlayMP3

whileDo # Chamar funcao

