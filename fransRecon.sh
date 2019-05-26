#!/bin/bash
# Put all the domain names in domains.txt, one per line
# then run in the terminal. It will portscan and will output the results
# in the results.txt.
# 
# Created by InitRoot (Frans Hendrik Botes)

#!/bin/bash
#Just my intro art

base64 -d <<<"IF9fX18gIF9fX18gICBf
XyAgIF9fIF8gIF9fX18g
ICAgX19fXyAgX19fXyAg
X19fICBfXyAgIF9fIF8g
CiggIF9fKSggIF8gXCAv
IF9cICggICggXC8gX19f
KSAgKCAgXyBcKCAgX18p
LyBfXykvICBcICggICgg
XAogKSBfKSAgKSAgIC8v
ICAgIFwvICAgIC9cX19f
IFwgICApICAgLyApIF8p
KCAoX18oICBPICkvICAg
IC8KKF9fKSAgKF9fXF8p
XF8vXF8vXF8pX18pKF9f
X18vICAoX19cXykoX19f
XylcX19fKVxfXy8gXF8p
X18p" 
echo ""
echo "Now enumerating the results file... "
echo "Please wait to complete."
#remove previous results files
rm results.txt
#start reading the data
filename=$1
while read line; do
	# get the IP address
	IP=$(dig +short $line)
	# do quick portscan if IP address is not empty
	if [ -z "$IP" ]
	then
		portscan="No IP"
	else
		portscan=$(masscan --rate=16000 -p80,53,443,445,8000-9000 $IP | grep -o -P '(?<=port ).*(?=/)')
	fi
	#screen output
	echo $line": "$IP
	echo "Ports open: "$portscan
	echo  $line": "$IP "| Ports open: "$portscan >> results.txt
done < $filename


