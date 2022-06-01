# -O to file, -L following redirects, -C - checking if file exists & continuing if so.
DEP_FOLDER=content

spacy_dl_en_v3:
	mkdir -p ${DEP_FOLDER}
	cd ${DEP_FOLDER} && curl -O -L -C - https://github.com/explosion/spacy-models/releases/download/en_core_web_trf-3.2.0/en_core_web_trf-3.2.0-py3-none-any.whl
	cd ${DEP_FOLDER} && curl -O -L -C - https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-3.2.0/en_core_web_lg-3.2.0-py3-none-any.whl
	cd ${DEP_FOLDER} && curl -O -L -C - https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.2.0/en_core_web_md-3.2.0-py3-none-any.whl
	cd ${DEP_FOLDER} && curl -O -L -C - https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.2.0/en_core_web_sm-3.2.0-py3-none-any.whl

spacy_dl_en_v2:
	mkdir -p ${DEP_FOLDER}
	cd ${DEP_FOLDER} && curl -O -L -C - https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
	cd ${DEP_FOLDER} && curl -O -L -C - https://github.com/explosion/spacy-models/releases/download/en_core_web_md-2.3.1/en_core_web_md-2.3.1.tar.gz
	cd ${DEP_FOLDER} && curl -O -L -C - https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-2.3.1/en_core_web_lg-2.3.1-fix.tar.gz 


