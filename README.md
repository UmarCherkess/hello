# Лабораторная работа
## *Практические задачи* 
![пингвин](https://avatars.mds.yandex.net/i?id=478feae407a42dfab539a10f8c2fb1a1-5192432-images-thumbs&n=13)
### *Цель работы:*
* Изучить основные команды комнадной строки Linux
* Закрепить полученные знания при решении практических задач

ЗАДАНИЕ 1 - root@d4e8f3ca43df:~# cd /home
root@d4e8f3ca43df:/home# ls -F --color 
temp1/  temp2/  test/  user/  user1/  user2/  user3/
root@d4e8f3ca43df:/home# mkdir umar1
root@d4e8f3ca43df:/home# ls -F --color
temp1/  temp2/  test/  umar1/  user/  user1/  user2/  user3/

ЗАДАНИЕ 2 - root@d4e8f3ca43df:/home# rmdir umar1
root@d4e8f3ca43df:/home# ls -F --color
temp1/  temp2/  test/  user/  user1/  user2/  user3/

ЗАДАНИЕ 3 - root@d4e8f3ca43df:~# uname -a
Linux d4e8f3ca43df 4.19.0-16-amd64 #1 SMP Debian 4.19.181-1 (2021-03-19) x86_64 x86_64 x86_64 GNU/Linux

ЗАДАНИЕ 4 - root@d4e8f3ca43df:~# uname -s
Linux

ЗАДАНИЕ 5 - root@d4e8f3ca43df:~# uname -r
4.19.0-16-amd64

ЗАДАНИЕ 6 - root@d4e8f3ca43df:~# date
Fri Oct 15 12:46:03 UTC 2021

ЗАДАНИЕ 7 - root@d4e8f3ca43df:~# cal
    October 2021      
Su Mo Tu We Th Fr Sa  
                1  2  
 3  4  5  6  7  8  9  
10 11 12 13 14 15 16  
17 18 19 20 21 22 23  
24 25 26 27 28 29 30  
31                  

Задание - 8 &&

Задание - 9 clear

Задание 10 - команда pwd

Задание 11 - root@d4e8f3ca43df:/home# cd user

Задание 12 - root@d4e8f3ca43df:~# ls
curutum  test  test1  umar
root@d4e8f3ca43df:~# ls -R
.:
curutum  test  test1  umar

./curutum:
dele

./curutum/dele:

./test:
1.txt  subtest  subtest1

./test/1.txt:

./test/subtest:

./test/subtest1:

./test1:
subtest2

./test1/subtest2:

./umar:
subumar

./umar/subumar:

ЗАДАНИЕ 13 - root@d4e8f3ca43df:/# ls -a
.   .dockerenv  bin   classics  etc   lib    lib64   media  my_bin  proc  run   srv       sys  txt.txt  var
..  alenamas    boot  dev       home  lib32  libx32  mnt    opt     root  sbin  sumbulov  tmp  usr      w_gromov

ЗАДАНИЕ 14 - root@d4e8f3ca43df:/ ls -l
total 80
drwxr-xr-x   2 root root 4096 Sep 29 13:41 alenamas
lrwxrwxrwx   1 root root    7 Aug 27 07:16 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 15  2020 boot
drwxr-xr-x   2 root root 4096 Sep 28 09:50 classics
drwxr-xr-x   5 root root  360 Sep 29 13:07 dev
drwxr-xr-x   1 root root 4096 Oct 15 12:19 etc
drwxr-xr-x   1 root root 4096 Oct 15 12:51 home
lrwxrwxrwx   1 root root    7 Aug 27 07:16 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Aug 27 07:16 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Aug 27 07:16 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Aug 27 07:16 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4096 Aug 27 07:16 media
drwxr-xr-x   2 root root 4096 Aug 27 07:16 mnt
drwxr-xr-x   2 root root 4096 Sep 13 14:58 my_bin
drwxr-xr-x   2 root root 4096 Aug 27 07:16 opt
dr-xr-xr-x 358 root root    0 Sep 29 13:07 proc
drwx------   1 root root 4096 Oct 15 12:42 root
drwxr-xr-x   5 root root 4096 Aug 27 07:27 run
lrwxrwxrwx   1 root root    8 Aug 27 07:16 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Aug 27 07:16 srv
drwxr-xr-x   2 root root 4096 Sep 13 14:50 sumbulov
dr-xr-xr-x  13 root root    0 Sep  7 08:54 sys
drwxrwxrwt   1 root root 4096 Oct 15 12:35 tmp
-rwxrwxrwx   1 root root    0 Oct  6 12:42 txt.txt
drwxr-xr-x   1 root root 4096 Aug 27 07:16 usr
drwxr-xr-x   1 root root 4096 Aug 27 07:27 var
drwxrwxrwx   2 root root 4096 Oct 12 12:45 w_gromov

ЗАДАНИЕ 15 - root@d4e8f3ca43df:/ ls -F
alenamas/  boot/      dev/  home/  lib32@  libx32@  mnt/     opt/   root/  sbin@  sumbulov/  tmp/      usr/  w_gromov/
bin@       classics/  etc/  lib@   lib64@  media/   my_bin/  proc/  run/   srv/   sys/       txt.txt*  var/

Задание 16 - root@d4e8f3ca43df:/# cd classics
root@d4e8f3ca43df:/classics# 

ЗАДАНИЕ 17 - root@d4e8f3ca43df:/# cd etc
root@d4e8f3ca43df:/etc# cd X11
root@d4e8f3ca43df:/etc/X11# 

ЗАДАНИЕ 18 - root@d4e8f3ca43df:~# pwd
/root

ЗАДАНИЕ 19 - root@d4e8f3ca43df:~cd /
root@d4e8f3ca43df:/# cd etc
root@d4e8f3ca43df:/etc#

ЗАДАНИЕ 20 - root@d4e8f3ca43df:/etc# cd group
bash: cd: group: Not a directory

ЗАДАНИЕ 21 - less passwd&&group

ЗАДАНИЕ 22 - root@d4e8f3ca43df:/etc# head -n 5 passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync

ЗАДАНИЕ 23 - root@d4e8f3ca43df:/etc# head -n 3 passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin

ЗАДАНИЕ 24 - root@d4e8f3ca43df:/etc# wc passwd
  33   38 1561 passwd
  
ЗАДАНИЕ 25 - root@d4e8f3ca43df:/# cd student
root@d4e8f3ca43df:/student#

ЗАДАНИЕ 26 - root@d4e8f3ca43df:/student# touch file1
root@d4e8f3ca43df:/student# touch file2
root@d4e8f3ca43df:/student# touch file3
root@d4e8f3ca43df:/student# ls
file1  file2  file3

ЗАДАНИЕ 27 - root@d4e8f3ca43df:/student# mkdir dir1
root@d4e8f3ca43df:/student# mkdir dir2
root@d4e8f3ca43df:/student# mkdir dir3
root@d4e8f3ca43df:/student# ls
dir1  dir2  dir3  file1  file2  file3

ЗАДАНИЕ 28 - root@d4e8f3ca43df:/student# cp file1 dir1
root@d4e8f3ca43df:/student# tree
bash: tree: command not found
root@d4e8f3ca43df:/student# cd dir1
root@d4e8f3ca43df:/student/dir1# ls
file1

ЗАДАНИЕ 29 - root@d4e8f3ca43df:/etc# cp ssh ../dir2/

ЗАДАНИЕ 30 - root@d4e8f3ca43df:/student/dir3# mkdir vegetables 
root@d4e8f3ca43df:/student/dir3# ls
vegetables

ЗАДАНИЕ 31 - root@d4e8f3ca43df:/student/dir2/ssh# mv sshd_config /student/dir3/vegetables
root@d4e8f3ca43df:/student/dir3/vegetables# ls 
sshd_config
