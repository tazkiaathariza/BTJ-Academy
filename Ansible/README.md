# Simple Task 2

## Task

1. Membuat inventory dengan mendefinisikan daftar variables dan hosts
2. Membuat playbook dengan task menjalankan docker container yang terdapat image, port, dan environment variables

## Answer 
## No. 1 

- SSH :
    ```
    ssh tazkiaatharizadhivara@btj-academy.bangunindo.io
    ```

- Membuat file inventory
    ```
    sudo nano inventory-tazkia.yaml
    ```
- Mengisi file inventory

     ```
        all:
            vars:
                docker_tag: 0.1.0
                docker_image: inventory-tazkia
            hosts:
            btj-academy:
                ansible_host: 10.184.0.100
                ansible_user: tazkiaatharizadhivara
                docker_port: 8081
    ```

## No. 2
- Membuat file playbook :

    ```
    sudo nano playbook.yaml
    ```

- Mengisi file playbook :

    ```
    - name: Menjalankan container ubuntu Tazkia
    hosts: btj-academy
    become: true
    tasks:

        - name: Pull Docker Image
        docker_image:
            name: "{{ docker_image }}:{{ docker_tag }}"

        - name: Run Docker container
        docker_container:
            name: container-tazkia
            image: "{{ docker_image }}:{{ docker_tag }}"
            state: started
            interactive: true
            tty: true
            ports:
            - "8081:8081"
    ```


- Menjalankan

```
ansible-playbook -i inventory-tazkia.yaml playbook.yaml
```

- Output (there's an error (permission denied), i'll try it again later)

```
PLAY [Menjalankan container ubuntu Tazkia] *********************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************************
The authenticity of host '10.184.0.100 (10.184.0.100)' can't be established.
ECDSA key fingerprint is SHA256:SunjbspAHiLhNruUh9QtGdbbtrSNZluZ9lkOofSGL6o.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
fatal: [btj-academy]: UNREACHABLE! => {"changed": false, "msg": "Failed to connect to the host via ssh: Warning: Permanently added '10.184.0.100' (ECDSA) to the list of known hosts.\r\ntazkiaatharizadhivara@10.184.0.100: Permission denied (publickey).", "unreachable": true}

PLAY RECAP *****************************************************************************************************************************************************************
btj-academy                : ok=0    changed=0    unreachable=1    failed=0    skipped=0    rescued=0    ignored=0
```
