# Simple Task 3

## Task

Pada example python app, tambahkan beberapa routing kemudian custom port yang di listen (Default 5000).
Buatlah satu playbook dengan beberapa task yaitu :
1. Menyalin file dari local ke server btj-academy.
2. Build docker image untuk example python app.
3. Jalankan container yang sudah di build.

## Answer

- SSH :
    ```
    ssh tazkiaatharizadhivara@btj-academy.bangunindo.io
    ```

- Clone git
    ```
    git clone https://github.com/rrw-bangunindo/btj-academy
    ```

- Buat dan edit file app.py
    ```
    sudo nano app.py
    ```

    Tambah route :
    ```
        from flask import Flask
        app = Flask(__name__)

        @app.route('/')
        def hello_world():
                return 'Hello, Tazkia!'

        @app.route('/menu')
        def menu():
                return 'Menu 1, Menu 2, Menu 3'

        @app.route('/contact')
        def menu():
                return 'Contact Me!'

        if __name__ == '__main__':
                app.run(debug=True, host='0.0.0.0', port=5099)
    ```

- Buat dan edit Dockerfile
    ```
    sudo nano Dockerfile
    ```

    Edit :
    ```
    FROM python:3.8-slim
    WORKDIR /app
    COPY . .
    RUN pip install -r requirements.txt
    CMD ["python", "app.py"]
    ```

- Buat dan edit Inventory
    ```
    sudo nano inventory.yaml
    ```

    Edit :
    ```
    all:
    vars:
        docker_tag: 0.1.0
        docker_image: inventory-app-py
    hosts:
    btj-academy:
        ansible_host: 10.184.0.100
        ansible_user: tazkiaatharizadhivara
        docker_port: 5099
    ```


- Buat dan edit Inventory
    ```
    sudo nano playbook.yaml
    ```

    Edit :
    ```
    - name: Menjalankan docker tazkia
        hosts: btj-academy
        become: true
        tasks:
        - name: copy Dockerfile
            ansible.builtin.copy:
            src: /home/tazkiaatharizadhivara/btj-academy-tazkia/Dockerfile
            dest: btj-academy-tazkia
            become: true
        - name: copy app.py
            ansible.builtin.copy:
            src: /home/tazkiaatharizadhivara/btj-academy-tazkia/app.py
            dest: btj-academy-tazkia
            become: true
        - name: copy requirements.txt
            ansible.builtin.copy:
            src: /home/tazkiaatharizadhivara/btj-academy-tazkia/requirements.txt
            dest: btj-academy-tazkia
            become: true
        - name: build docker image
            ansible.builtin.command:
            cmd: 'docker build -t app-flask:0.1.0 btj-academy-tazkia'
        - name: run docker container
            ansible.builtin.command:
            cmd: 'docker run -it -d --name tazkia-flask -p 5099:5099 app-flask:0.1.0'
    ```


Menjalankan

```
ansible-playbook -i inventory.yaml playbook.yaml
```