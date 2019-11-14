ls /home/marcos/WinX/999-Backup-Não_tem_na_HD_Externa/Series/BRASILEIRAS/ > /tmp/teste;
ls /home/marcos/WinX/999-Backup-Não_tem_na_HD_Externa/Series/EXTRANGEIRAS/ >> /tmp/teste;
ls /home/marcos/Downloads/adicionar\ no\ p/ >> /tmp/teste;
cat /tmp/teste|sort -R|head -n1;
