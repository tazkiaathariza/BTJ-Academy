# Simple Task (DOCKER)

## 1. Buatlah image dari aplikasi sederhana yang sudah dibuat
IMAGE ID = 7de1fb9af381

## 2. Jalankan image tersebut sebagai container dan berjalan pada port 8081


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
