# fransRecon
Script will enumerate domain name using horizontal enumeration, reverse lookup.
Each horziontal domain will then be vertically enumerated using Sublist3r.

Output can then be used for portscans etc.

*Horizontal enumeration:*
- On company registrar name
- On domain name provided

*Vertical enumeration:*
- On all the domains found during horizontal enumeration

## Usage
fransRecon.py example.com

![alt text](https://i.imgur.com/sba5giB.png "fransRecon")


Note that this could take a *long time* to run for big domains.

## Install
Should have to be run from in Sublist3r folder.
Easiest is to clone this GIT and then clone sublist3r into the same folder.
Enure you also have DIG installed.

