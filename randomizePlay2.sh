#find /home/marcospaulo/Videos/ -iname '*' | grep -v Thumbs.db | grep -v txt | grep '\.' > playlist.txt; 
touch ignorar.tmp;
touch played.tmp;
played=$(cat played.tmp | wc -l);
total=$(cat playlist.txt | wc -l);
if [ "$(echo $played)" == '0' ] 
then
	cat playlist.txt | sort -R > playlist.tmp;
	head -n1 playlist.tmp >> played.tmp;
	echo -n "grep -v '"$(cat played.tmp)"'" > ignorar.tmp;
elif [ "$(echo $played)" == "$(echo $total)" ] 
then
	rm played.tmp;
	rm ignorar.tmp;
	rm playlist.tmp;
	exit
else
	cat playlist.txt $(cat ignorar.tmp) | sort -R | head -n1 > playlist.tmp;
	echo 'cat playlist.txt |' $(cat ignorar.tmp) '| sort -R | head -n1 > playlist.tmp' > playlistEignorar.tmp
	chmod 744 playlistEignorar.tmp;
	./playlistEignorar.tmp;
	head -n1 playlist.tmp >> played.tmp;
	echo -n " | grep -v '"$(cat played.tmp |tail -n1)"'" >> ignorar.tmp;
fi
# for i in `ls /tmp/*.mp4`; do mplayer -xy 400 -geometry 1250:0 $i; done
# mplayer -xy 400 -geometry 1250:0 -playlist playlist.tmp;
#head -n1 playlist.tmp >> played.txt;
totem "$(cat playlist.tmp | head -n1 | shuf -n1)";
