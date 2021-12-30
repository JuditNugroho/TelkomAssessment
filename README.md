# TelkomAssessment
Aplikasi ini merupakan Aplikasi CLI (Command Line Tools) menggunakan bahasa pemrograman Python 3 yang digunakan untuk mengambil log file pada linux dan akan dikonversi menjadi txt atau json

# Run Program
`python3 main.py`

# Usage 
------------------------------------------CLI APP HELP TOOL-----------------------------------------<br />
Usage : mytools [Source File] [Flag Option] [command]<br />
Argument : file yang akan di konversi (Contoh: /var/log/example.log<br />
Flag Option : -t  Mengubah tipe ekstensi suatu file menjadi plaintext atau json (default : plaintext)<br />
              -o  Destinasi file output<br />
              -h  Menampilkan pesan bantu<br />
----------------------------------------EXAMPLE CODE------------------------------------------------<br />
Example 1 : (Mengkonversi menjadi file json) : mytools /var/log/nginx/error.log -t json<br />
Example 2 : (Mengkonversi menjadi file text) : mytools /var/log/nginx/error.log -t text<br />
Example 3 : (Ubah destinasi file output) : mytools /var/log/nginx/error.log -t json -o /home/a.json<br />
Example 4 : (Untuk keluar dari program) : mytools exit<br />
----------------------------------------------------------------------------------------------------<br />