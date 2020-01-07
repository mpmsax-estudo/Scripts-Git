ls /home/marcospaulo/Music/3-LetrasDeMusica | grep txt > teste.txt;
for i in $(cat teste.txt); do
	nome=$(echo $i | awk -F'(' '{print $2}' | awk -F')' '{print $1}');
	banda=$(echo $i | awk -F'(' '{print $1}');
	mp3=$(find Music/ -maxdepth 1 -iname "*$banda*$nome*" | grep '.mp3' | head -n1)'empty';
	if [ "$mp3" != 'empty' ]; then
		echo $banda $nome;
	fi;
done
