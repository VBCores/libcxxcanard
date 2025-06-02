FORMAT = clang-format-18
TIDY = clang-tidy-18 --config-file ./.clang-tidy -p build
PROJECT_FILES = $(shell find cyphal -iname *.h -o -iname *.cpp -o -iname *.c)
SHELL = bash

.ONESHELL:
.SHELLFLAGS += -e

.PHONY: help format lint validate arduino-lib docs build

help:  ## Показать это сообщение
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

format:  ## Отформатировать код
	${FORMAT} -i $(PROJECT_FILES)

lint:  ## Запустить анализаторы и линтеры
	${TIDY} $(PROJECT_FILES)

validate: format lint

arduino-lib:  ## Собрать файлы для arduino
	python3 arduino_pack.py

docs:  ## Собрать документацию
	cd docs
	make html

host-docs:  ## <dev only> Захостить документация на 8000 порту
	cd docs/_build/html
	python3 -m http.server 8000

build:  ## <dev only> Собрать библиотку локально с compile_commands.json
	cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -S . -B build
	cmake  --build build
