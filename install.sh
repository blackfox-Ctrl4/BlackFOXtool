read -p 'install BlackFox ? [y/n]:' yn
			case $yn in
			    [Yy]*) pip3 install bs4 ; pip3 install requests ; pip3 install ipwhois ; pip3 install colorama ; pip3 install ipapi ; pip3 install builtwith ; sudo apt install unzip ; unzip sqlmap.zip ; echo "[✔] Installation complete!" ; python3 blackfox.py ;;
			    [Nn]*) echo 'Installation canceled by the user, Exitting...' ; exit 1 ;;
			esac