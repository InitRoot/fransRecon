# fransRecon
Script will enumerate domain name using horizontal enumeration, reverse lookup.
Each horziontal domain will then be vertically enumerated using Sublist3r.

Output can then be used for portscans etc.

### Horizontal enumeration:
- On company registrar name
- On domain name provided

### Vertical enumeration:
- On all the domains found during horizontal enumeration

## Usage
fransRecon.py example.com

![alt text](https://i.imgur.com/sba5giB.png "fransRecon")


Note that this could take a *long time* to run for big domains.

## Install
Should have to be run from in Sublist3r folder.
Easiest is to clone this GIT and then clone sublist3r into the same folder.
Enure you also have DIG installed.

The folder structure is as follow once installed:
```
 ✘ ⚡ root@pentest  ~/Tools/fransRecon  ls -la
total 96
drwxr-xr-x  4 root root  4096 May 27 18:29 .
drwxr-xr-x 14 root root  4096 May 26 12:48 ..
-rwxr--r--  1 root root  5545 May 26 22:17 fransRecon.py
drwxr-xr-x  2 root root  4096 May 26 21:00 subbrute
drwxr-xr-x  3 root root  4096 May 26 21:00 Sublist3r
-rwxr-xr-x  1 root root 36120 May 26 21:00 sublist3r.py
-rw-r--r--  1 root root 36642 May 26 21:00 sublist3r.pyc
```

