YEARS = 2018 2019
TARGETS_2018 = $(shell cat targets/2018.txt)
TARGETS_2019 = $(shell cat targets/2019.txt)

.PRECIOUS: output/%.csv input/2018/%.pdf input/2019/%.pdf targets/%.txt tabula.jar

.PHONY: all clean

all: output/data.csv

clean:
	rm -f $(foreach y, $(YEARS), input/$(y)/*.pdf output/$(y)/*.csv)

output/data.csv: $(foreach y, $(YEARS), output/$(y)/data.csv)
	csvstack $^ > $@

.SECONDEXPANSION:
output/%/data.csv: output/%/dates.csv $$(foreach t, $$(TARGETS_$$*), output/$$*/$$(t).csv)
	csvstack $(filter-out $<,$^) | \
	csvjoin -c name -I --left - $< > $@

.SECONDEXPANSION:
output/%/dates.csv: input/%/$$(firstword $$(TARGETS_$$*)).pdf tabula.jar
	mkdir -p $(dir $@)
	java -jar tabula.jar -p 1-4 -c 314,447 $< | \
	python scripts/process_dates.py > $@

output/%.csv: input/%.pdf tabula.jar
	mkdir -p $(dir $@)
	java -jar tabula.jar -p 6-13 -c 362,454,529 $< | \
	python scripts/process_csv.py $* > $@

input/2019/%.pdf: targets/2019.txt
	mkdir -p $(dir $@)
	wget --no-use-server-timestamps -O $@ https://www.chicago.gov/content/dam/city/depts/dcd/tif/19reports/$*.pdf

input/2018/%.pdf: targets/2018.txt
	mkdir -p $(dir $@)
	wget --no-use-server-timestamps -O $@ https://www.chicago.gov/content/dam/city/depts/dcd/tif/18reports/$*.pdf

targets/%.txt:
	wget -O - https://www.chicago.gov/city/en/depts/dcd/supp_info/district-annual-reports--$*-.html | \
	python scripts/get_docs.py $* > $@

tabula.jar:
	wget -O $@ https://github.com/tabulapdf/tabula-java/releases/download/v1.0.2/tabula-1.0.2-jar-with-dependencies.jar
