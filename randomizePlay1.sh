#find /home/marcospaulo/Videos/ -iname '*' | grep -v Thumbs.db | grep -v txt | grep '\.' > playlist.txt; 
# for i in `ls /tmp/*.mp4`; do mplayer -xy 400 -geometry 1250:0 $i; done
# mplayer -xy 400 -geometry 1250:0 -playlist playlist.tmp;
smplayer "$(cat playlist.txt | sort -R | shuf -n1)"
