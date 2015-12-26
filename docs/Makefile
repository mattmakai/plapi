run:
	pelican -t theme -s settings.py -o ../site content
	cp ../site/pages/* ../site/
	rm -rf ../site/pages/

init:
	pip install -r requirements.txt
