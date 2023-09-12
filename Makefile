FORMAT = clang-format-18
TIDY = clang-tidy-18
PROJECT_FILES = $(shell find cyphal -iname *.h -o -iname *.cpp -o -iname *.c)
SHELL = bash

.PHONY: help format lint validate arduino-lib

help:  ## Показать это сообщение
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

format:  ## Отформатировать код
	${FORMAT} -i $(PROJECT_FILES)

lint:  ## Запустить анализаторы и линтеры
	${TIDY} $(PROJECT_FILES)

validate: format lint

arduino-lib:  ## Собрать файлы для arduino
	python3 arduino_pack.py
