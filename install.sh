read -p "install BlackFox ? [y/n]:" yn
			case $yn in
			    [Yy]*) pip3 install bs4 ; pip3 install requests ; pip3 install ipwhois ; echo "[✔] Installing ..."; clear ; python3 blackfox.py ;;
			    [Nn]*) echo "exit ... " ; exit 1 ;;
			esac
