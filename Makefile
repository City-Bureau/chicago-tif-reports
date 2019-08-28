TARGETS = $(shell cat targets.txt)

.PRECIOUS: output/data.csv output/%.csv input/%.pdf targets.txt tabula.jar

.PHONY: all clean

all: output/data.csv

clean:
	rm -f input/*.pdf output/*.csv


output/data.csv: output/dates.csv $(foreach t, $(TARGETS), output/$(t).csv)
	csvstack $(filter-out $<,$^) | \
	csvjoin -c name -I --left - $< > $@

output/dates.csv: input/$(firstword $(TARGETS)).pdf tabula.jar
	java -jar tabula.jar -p 1-4 -c 314,447 $< | \
	python scripts/process_dates.py > $@

output/%.csv: input/%.pdf tabula.jar
	java -jar tabula.jar -p 6-13 -c 362,454,529 $< | \
	python scripts/process_csv.py $* > $@

input/%.pdf: targets.txt
	wget --no-use-server-timestamps -O $@ https://www.chicago.gov/content/dam/city/depts/dcd/tif/18reports/$*.pdf

targets.txt:
	wget -O - https://www.chicago.gov/city/en/depts/dcd/supp_info/district-annual-reports--2018-.html | \
	python scripts/get_docs.py > $@

tabula.jar:
	wget -O $@ https://github.com/tabulapdf/tabula-java/releases/download/v1.0.2/tabula-1.0.2-jar-with-dependencies.jar
