set -x 
#find /home/marcospaulo/Videos/ -iname '*' | grep -v REVISTAS | grep -v Thumbs.db | grep -v txt | grep '\.' > playlist.txt; 
#find /home/marcos/Downloads/ | grep '\.' >> playlist.txt;
touch ignorar.tmp;
touch played.tmp;
played=$(cat played.tmp | wc -l);
total=$(cat playlist.txt | wc -l);
		if [ "$(echo $played)" == '0' ];
		then
			cat playlist.txt | sort -R > playlist.tmp;
			head -n1 playlist.tmp >> played.tmp;
			cp played.tmp playlist.tmp
			# echo -n "grep -v '"$(cat played.tmp)"'" > ignorar.tmp;
			cat playlist.txt | grep -v $(cat playlist.tmp) > toPlay.txt;
			break
		elif [ "$(echo $played)" == "$(echo $total)" ]
		then
			rm played.tmp;
			rm ignorar.tmp;
			rm playlist.tmp;
			exit
		else
			# Criar arquivo
			#echo 'cat toPlay.txt | sort -R | head -n1 > playlist.tmp' > playlistEignorar.tmp
			cat toPlay.txt | sort -R | head -n1 > playlist.tmp; 
			chmod 744 playlistEignorar.tmp;
			# ./playlistEignorar.tmp; # Rodar arquivo # cat playlist.txt | grep -v ... | sort -R | head -n1 > playlist.tmp
			head -n1 playlist.tmp >> played.tmp;
			cp played.tmp playlist.tmp
			# echo -n "grep -v '"$(cat played.tmp)"'" > ignorar.tmp;
			# echo -n " | grep -v '"$(cat played.tmp |tail -n1)"'" >> ignorar.tmp;
			chmod 744 toPlay.txt;
			cat toPlay.txt | grep -v $(cat playlist.tmp) > toPlay.tmp;
			chmod 744 toPlay.tmp;
			cp toPlay.tmp toPlay.txt;
			break
		fi
# for i in `ls /tmp/*.mp4`; do mplayer -xy 400 -geometry 1250:0 $i; done
# mplayer -xy 400 -geometry 1250:0 -playlist playlist.tmp;
#head -n1 playlist.tmp >> played.txt;
#totem "$(cat playlist.tmp | head -n1 | shuf -n1)";
xplayer $(cat playlist.tmp)
echo 'nao tem backup deste script';
if [ "$(cat toPlay.txt | wc -l)" == '0' ]
then
	rm played.tmp
fi

