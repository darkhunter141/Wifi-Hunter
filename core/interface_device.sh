ifconfig | grep -e ": " | sed -e 's/: .*//g' | sed -e 's/^/   /'