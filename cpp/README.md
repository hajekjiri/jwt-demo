# C++ demo
---

## Requirements

Install OpenSSL library:
```console
jwt@demo:~$ sudo apt-get install libssl-dev
```
Download include libraries from [Thalhammer's jwt-cpp](https://github.com/Thalhammer/jwt-cpp/tree/master/include) repository  and put them in "include" folder in following fashion:
```console
├── include
│   ├── base.h
│   ├── jwt.h
│   └── picojson.h
```

## Start with JWT
Use make to compile:
```console
jwt@demo:~$ make compile
```

Or to run the program:
```console
jwt@demo:~$ make run
```