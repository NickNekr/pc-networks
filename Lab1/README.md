# Lab1

Для начала установим VMWare и образ EVE-NG, а также образы Cisco Switch и Cisco Router.

## Топология
Я построил такую топологию сети:
![telegram-cloud-document-2-5438442883327744100](https://github.com/NickNekr/pc-networks/assets/87271224/3ac5bf62-3e99-4693-aa9e-6202451a3b49)


## Настройки узлов
### S0
```plaintext
vlan 10,20
exit
spanning-tree vlan 10,20 root primary
interface range Gi0/0-2
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 10,20
exit
exit
```
### S1
```plaintext
vlan 10,20
exit
interface Gi0/2
switchport mode access
switchport access vlan 10
exit
interface range Gi0/0-1
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 10,20
exit
exit
```

### S2
```plaintext
vlan 10,20
exit
interface Gi0/2
switchport mode access
switchport access vlan 20
exit
interface range Gi0/0-1
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 10,20
exit
exit
```

### Router
```plaintext
interface Gi0/0
no shutdown
exit
interface Gi0/0.1
encapsulation dot1q 10
ip address 10.0.10.1 255.255.255.0
exit
interface Gi0/0.2
encapsulation dot1q 20
ip address 10.0.20.1 255.255.255.0
exit
```

### Client1
```plaintext
ip 10.0.10.2/24 10.0.10.1
```

### Client2
```plaintext
ip 10.0.20.2/24 10.0.20.1
```

## Пункты задания:
### 1 пункт
Построенная топология соответствует заданному.

### 2 пункт
Каждый из клиентов находится в своем VLAN.

### 3 пункт (STP)
3.1) Взглянем на spanning-tree коммутатора ядра сети:

![telegram-cloud-document-2-5438442883327744254](https://github.com/NickNekr/pc-networks/assets/87271224/195284ec-f168-4a19-b138-13cca201988b)

3.2) На spanning-tree одного из коммутаторов доступа:

![telegram-cloud-document-2-5438442883327744251](https://github.com/NickNekr/pc-networks/assets/87271224/6d559021-d686-432f-83eb-dea9cdad146c)

Видно, что соответствует требованиям.

### 4 пункт (Ping)
После настройки клиентов попробуем поотравлять друг другу ping'и.

**Client1 -> Client2**:

![telegram-cloud-document-2-5438442883327744105](https://github.com/NickNekr/pc-networks/assets/87271224/d80164fd-99af-4e3d-bcc7-a078047a3ffe)


**Client2 -> Client1**:

![telegram-cloud-document-2-5438442883327744106](https://github.com/NickNekr/pc-networks/assets/87271224/00612022-5c7c-4cc9-b2db-763a3d9194ee)

Видно, что клиенты могу отправлять друг другу пинги.

### 5 пункт (EVE-NG)

Работа выполнена в EVE-NG + VMWare.

### Отказоустойчивость

Предлагается поочереди отключать соединения между парами коммутаторов и проверять доступность на клиентах с помощью пингов.

#### 1 случай

![telegram-cloud-document-2-5438442883327744338](https://github.com/NickNekr/pc-networks/assets/87271224/4fe6bda7-2090-4c82-a920-60a4e5e8591b)

**Client1 -> Client2**:

![telegram-cloud-document-2-5438442883327744109](https://github.com/NickNekr/pc-networks/assets/87271224/8d850ffb-8d1a-4a24-aeec-3b71d4e8bbe6)

**Client2 -> Client1**:

![telegram-cloud-document-2-5438442883327744111](https://github.com/NickNekr/pc-networks/assets/87271224/5998c7ba-e821-4bd2-8e9a-6e3ea6e8a27d)

Видно, что клиенты могу отправлять друг другу пинги.

#### Случай 2

![telegram-cloud-document-2-5438442883327744151](https://github.com/NickNekr/pc-networks/assets/87271224/131f6d06-523e-4c9e-b192-4e62a57c50c5)

**Client1 -> Client2**:

![telegram-cloud-document-2-5438442883327744148](https://github.com/NickNekr/pc-networks/assets/87271224/ef96dd11-a335-41c3-9dba-e6836f93f54a)

**Client2 -> Client1**:

![telegram-cloud-document-2-5438442883327744150](https://github.com/NickNekr/pc-networks/assets/87271224/d53d8220-b86e-4233-b651-b1bc13792da1)

Видно, что клиенты могу отправлять друг другу пинги.

#### Случай 3 

![telegram-cloud-document-2-5438442883327744167](https://github.com/NickNekr/pc-networks/assets/87271224/f54c4f11-d27e-4abd-9661-87e70950bba3)

**Client1 -> Client2**:

![telegram-cloud-document-2-5438442883327744169](https://github.com/NickNekr/pc-networks/assets/87271224/c8331dc0-3390-4f02-90c8-0d0e8b584c78)

**Client2 -> Client1**:

![telegram-cloud-document-2-5438442883327744171](https://github.com/NickNekr/pc-networks/assets/87271224/84426056-5a70-41c8-9d82-137b0c02ad00)

Видно, что клиенты могу отправлять друг другу пинги.
