# Symmetric Encryption using Fernet 

Python Code for Encrypting and decrypting text

Here we use Cryptographic module Fernet

Here inside [security.py](fernet/security.py)
there is a class coonstructed for fernet you can use this inside your project

___


## Set-Up

```bash
$ pip install -r requirements.txt
```
---



## Working
```bash
$ python keygen.py

$ python encode.py

Enter the Secret Message: Fernet is really cool

$ python decode.py

Enter 1 for File input mode or skip: 1
Fernet is really cool

```

| Result | File | command|
|--------|------|--------|
|Class which has key generation,encryption,decryption functions which are made easy to handle |      [security.py](fernet/security.py)|```python security.py```|
|The key is stored in the configuration file |      [log.cfg](fernet/log.cfg)||
|Key is generated and stored inside [log.cfg](fernet/log.cfg)| [keygen.py](fernet/keygen.py)|```python keygen.py```|
|Encrypting message and stored inside [database.txt](fernet/database.txt)| [encrypt.py](fernet/encrpt.py)|```python encrpt.py```|
|Decrypt the encrpted message  stored inside [database.txt](fernet/database.txt) after collecting key| [decrypt.py](fernet/decrpt.py)|```python decrpt.py```|
|encrypted message is stored|      [database.txt](feernet/database.txt)||


---

## Task

<ul>
  <li>Adding files and image encryption</li>
</ul>

---

## Contributors


<table>
  <tr>
    <td align="center"><a href="https://github.com/Niranjanprof"><img src="https://avatars1.githubusercontent.com/u/48713926?s=400&u=a473cb9bbbc98506ae6b55ccd2b45cfdc941d517&v=4" width="100px;" alt=""/><br /><sub><b>Niranjan B(Prof Moriarty)</b></sub></a><br /><a href="https://github.com/Niranjanprof/Fernet-Class/commits?author=Niranjanprof" title="Code">💻</a> <a href="https://github.com/Niranjanprof/Fernet-Class/commits?author=Niranjanprof" title="Documentation">📖</a></td>
      </tr>

</table>

---

## License & copyright

© Niranjan B

Licensed under the [GNU GPL](LICENSE)

---

Mention This [Repo](https://github.com/Niranjanprof/Fernet-Class) while you use this in your projects :)
