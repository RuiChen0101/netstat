.PHONY: directories clean

all: directories src/ui/mainwindows.py

src/ui/mainwindows.py: src/ui/mainui.ui
	pyuic5 ./src/ui/mainui.ui -o ./src/ui/mainwindow.py

directories:

clean:

stat:
	wc src/*
