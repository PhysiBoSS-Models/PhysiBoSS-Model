VERSION := $(shell grep . VERSION.txt | cut -f1 -d:)

# sample projects 	
list-projects:
	@echo "Sample projects: template_BM"
	@echo ""
	
template_BM:
	cp ./sample_projects_intracellular/boolean/template_BM/custom_modules/* ./custom_modules/
	rm -fr main.cpp README.md model.yml
	cp ./sample_projects_intracellular/boolean/template_BM/main.cpp ./main.cpp
 	cp ./sample_projects_intracellular/boolean/template_BM/README.md ./README.md
	cp ./sample_projects_intracellular/boolean/template_BM/model.yml ./model.yml
	cp ./sample_projects_intracellular/boolean/template_BM/Makefile .
	rm -fr config/*
	cp -r ./sample_projects_intracellular/boolean/template_BM/config/* ./config/
	mkdir ./scripts/
	cp ./sample_projects_intracellular/boolean/template_BM/scripts/* ./scripts/

# upgrade rules 

SOURCE := PhysiCell_upgrade.zip 
get-upgrade: 
	@echo $$(curl https://raw.githubusercontent.com/MathCancer/PhysiCell/master/VERSION.txt) > VER.txt 
	@echo https://github.com/MathCancer/PhysiCell/releases/download/$$(grep . VER.txt)/PhysiCell_V.$$(grep . VER.txt).zip > DL_FILE.txt 
	rm -f VER.txt
	$$(curl -L $$(grep . DL_FILE.txt) --output PhysiCell_upgrade.zip)
	rm -f DL_FILE.txt 

PhysiCell_upgrade.zip: 
	make get-upgrade 

upgrade: $(SOURCE)
	unzip $(SOURCE) PhysiCell/VERSION.txt
	mv -f PhysiCell/VERSION.txt . 
	unzip $(SOURCE) PhysiCell/core/* 
	cp -r PhysiCell/core/* core 
	unzip $(SOURCE) PhysiCell/modules/* 
	cp -r PhysiCell/modules/* modules 
	unzip $(SOURCE) PhysiCell/sample_projects/* 
	cp -r PhysiCell/sample_projects/* sample_projects 
	unzip $(SOURCE) PhysiCell/BioFVM/* 
	cp -r PhysiCell/BioFVM/* BioFVM
	unzip $(SOURCE) PhysiCell/documentation/User_Guide.pdf
	mv -f PhysiCell/documentation/User_Guide.pdf documentation
	rm -f -r PhysiCell
	rm -f $(SOURCE) 

# use: make save PROJ=your_project_name
PROJ := my_project

save: 
	echo "Saving project as $(PROJ) ... "
	mkdir -p ./user_projects
	mkdir -p ./user_projects/$(PROJ)
	mkdir -p ./user_projects/$(PROJ)/custom_modules
	mkdir -p ./user_projects/$(PROJ)/config 
	cp main.cpp ./user_projects/$(PROJ)
	cp Makefile ./user_projects/$(PROJ)
	cp VERSION.txt ./user_projects/$(PROJ)
	cp -r ./config/* ./user_projects/$(PROJ)/config
	cp -r ./custom_modules/* ./user_projects/$(PROJ)/custom_modules

load: 
	echo "Loading project from $(PROJ) ... "
	cp ./user_projects/$(PROJ)/main.cpp .
	cp ./user_projects/$(PROJ)/Makefile .
	cp -r ./user_projects/$(PROJ)/config/* ./config/ 
	cp -r ./user_projects/$(PROJ)/custom_modules/* ./custom_modules/ 

pack:
	@echo " "
	@echo "Preparing project $(PROJ) for sharing ... "
	@echo " " 
	cd ./user_projects && zip -r $(PROJ).zip $(PROJ)
	@echo " "
	@echo "Share ./user_projects/$(PROJ).zip ... "
	@echo "Other users can unzip $(PROJ).zip in their ./user_projects, compile, and run."
	@echo " " 

unpack:
	@echo " "
	@echo "Preparing shared project $(PROJ).zip for use ... "
	@echo " " 
	cd ./user_projects && unzip $(PROJ).zip 
	@echo " "
	@echo "Load this project via make load PROJ=$(PROJ) ... "
	@echo " " 	

list-user-projects:
	@echo "user projects::"
	@cd ./user_projects && ls -dt1 * | grep . | sed 's!empty.txt!!'
