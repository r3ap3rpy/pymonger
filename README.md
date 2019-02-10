# Welcome

This repository helps you get started with the [pymongo](https://pypi.org/project/pymongo/) module of python.
Also teaches you to configure and install [mongodb](https://www.mongodb.com/) on ubuntu.

Install mongodb.

```bash
apt-get update && apt-get upgrade && apt-get install mongodb
```

Configure mongo config.

Got to 
```bash 
vi /etc/mongodb.conf
```

Replace "bind_ip = 127.0.0.1" with "bind_ip = 0.0.0.0" and uncomment the line "port = 27017"
Finally restart the mongodb.

```bash
/etc/init.d/mongodb restart
```
Install python module.

```python
pip install pymongo
```
