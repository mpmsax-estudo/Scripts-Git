set -x 
#find /home/marcos/WinX/999-Backup-Nao_tem_na_HD_Externa/P/ -iname '*' | grep -v REVISTAS | grep -v Thumbs.db | grep -v txt | grep '\.' > playlist.txt; 
#find /home/marcos/Downloads/ -iname '*.mp4' >> playlist.txt;
touch ignorar.tmp;
touch played.tmp;
toPlay=$(cat toPlay.txt | wc -l);
total=$(cat playlist.txt | wc -l);
		if [ "$toPlay" == '0' ];
		then
			cat playlist.txt | sort -R > toPlay.txt;
			head -n1 toPlay.txt >> played.tmp;
			head -n1 toPlay.txt > playlist.tmp
			# echo -n "grep -v '"$(cat played.tmp)"'" > ignorar.tmp;
			cat playlist.txt | grep -v $(cat playlist.tmp) > toPlay.txt;
			break
		#elif [ "$(echo $toPlay)" == "$(echo $total)" ]
		#then
		#	rm played.tmp;
		#	rm ignorar.tmp;
		#	rm playlist.tmp;
		#	exit
		else
			# Criar arquivo
			#echo 'cat toPlay.txt | sort -R | head -n1 > playlist.tmp' > playlistEignorar.tmp
			cat toPlay.txt | sort -R > toPlay.tmp;
			cat toPlay.tmp | head -n1 > playlist.tmp; 
			# chmod 744 playlistEignorar.tmp;
			# ./playlistEignorar.tmp; # Rodar arquivo # cat playlist.txt | grep -v ... | sort -R | head -n1 > playlist.tmp
			cat playlist.tmp >> played.tmp;
			if [ "cat playlist.tmp | cut -d'/' -f8 | awk -F'.' '{print $NF}' | wc -L" -le 5 ]; 
			then
				cat toPlay.tmp | grep -v "$(cat playlist.tmp)" > toPlay.txt;
			else
				excluir=$(cat playlist.tmp | cut -d'/' -f8 | awk -F'.' '{print $NF}')
				cat toPlay.tmp | grep -v "$excluir" > toPlay.txt;
			fi
			# cp played.tmp playlist.tmp
			# echo -n "grep -v '"$(cat played.tmp)"'" > ignorar.tmp;
			# echo -n " | grep -v '"$(cat played.tmp |tail -n1)"'" >> ignorar.tmp;
			break
		fi
# for i in `ls /tmp/*.mp4`; do mplayer -xy 400 -geometry 1250:0 $i; done
# "$(playlist.tmp)" -> aceita caracteres especiais
mplayer -xy 400 -geometry 1250:0 "$(playlist.tmp)";
#head -n1 playlist.tmp >> played.txt;
#totem "$(cat playlist.tmp | head -n1 | shuf -n1)";
#xplayer $(cat playlist.tmp)
#mplayer $(cat playlist.tmp)
echo 'nao tem backup deste script';
if [ "$(cat toPlay.txt | wc -l)" == '0' ];
then
	rm played.tmp
fi

