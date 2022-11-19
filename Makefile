rouble : rouble.py
	echo "#!/bin/python3" > rouble
	cat rouble.py >> rouble
	chmod +x rouble

install : rouble
	install -Dm 744 english-words/words_alpha.txt /usr/share/rouble/words
	install -Dm 755 rouble /usr/bin/rouble

uninstall :
	rm -rf /usr/share/rouble
	rm -f /usr/bin/rouble

run : rouble.py
	python3 rouble.py

clean : 
	rm rouble
