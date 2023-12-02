# Simple Task (DOCKER)

## 1. Buatlah image dari aplikasi sederhana yang sudah dibuat
Membuat Dockfile dengan vim, kemudian build menjadi image. Hasilnya adalah sebagai berikut:

IMAGE ID = 7de1fb9af381

REPOSITORY dan TAG = none

Proses:

- SSH
- vim Dockerfile
- Isi file :

  FROM python:3.8-slim
  
  LABEL Name="Tazkia BTJ Academy Python App"
  
  LABEL Version="0.1.0"

  RUN apt-get update && \
    apt-get install -y git
  
  RUN git clone https://github.com/tazkiaathariza/BTJ-Academy.git .
  
  CMD ["python", "WhatToGetDone_Tazkia.py"]
  
- docker build -t tazkiapythonapp .
- docker images

## 2. Jalankan image tersebut sebagai container dan berjalan pada port 8081
Membuat container dengan docker run. Hasilnya adalah sebagai berikut:

Container ID = f133ce1ee1b1

IMAGE = 7de1fb9af381

COMMAND = "python3"

NAME = tazkia

Proses pembuatan :
- docker run -it -d --name tazkia 7de1fb9af381

## 3. Berapakah IP docker container whoami?
Berdasarkan docker inspeck, IP whoami adalah :

  "IPAddress": "172.17.0.2",
  
  "IPPrefixLen": 16,
  
  "IPv6Gateway": "",
  
  "MacAddress": "02:42:ac:11:00:02",
  
  
## 4. Apa isi dari file yang tersembunyi dari docker container whoami? Clue: Volume Mounting
Berdasarkan docker inspeck, mounts whoami adalah :

"Mounts": [
            {
            
                "Type": "bind",
                "Source": "/home/local/.docker",
                "Destination": "/tmp/system",
                "Mode": "",
                "RW": true,
                "Propagation": "rprivate"
            }
        ],

## 5. Image apa yang digunakan pada docker container whoami?
Berdasarkan docker inspect, image pada whoami adalah :

"Image": "sha256:f3464846ab67b3dfbe1cf9b7ee41d28634cb7ed23780c1d4197ff849d5e62f7a",
