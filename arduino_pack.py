import re
import pathlib

DIR = pathlib.Path(__file__).parent.resolve()
SRC_DIR = DIR / 'cyphal'


def subdir_names(dir_):
    for subdir in [d for d in dir_.iterdir() if d.is_dir()]:
        yield subdir.name
        yield from subdir_names(subdir)


SUBDIRS = tuple(subdir_names(SRC_DIR))
print(f"Known first-party: {SUBDIRS}\n")

OUT_H = DIR / 'src' / 'cyphal.h'
OUT_CPP = DIR / 'src' / 'cyphal.cpp'

TARGET_FILES = []
with open(DIR / 'arduino_list.txt', 'r') as arduino_list:
    for line in arduino_list:
        if not line:
            continue
        TARGET_FILES.append(SRC_DIR / pathlib.Path(line.strip(' \n\r\t')))
print(f"Processing files: {[f.name for f in TARGET_FILES]}\n")

REMOVE_TEMPLATES = [re.compile(reg) for reg in (
    r"^#pragma.*",
    *(f"^#include (<|\"){inner_include}/.*(>|\").*"
      for inner_include in SUBDIRS + (SRC_DIR.name,)),
    *(f"^#include (<|\")(../)*{inner_file.name}(>|\").*"
      for inner_file in TARGET_FILES),
    r"^#include (<|\")(../)*FDCAN_generic.h(>|\").*"
)]


def matches(line_):
    for template in REMOVE_TEMPLATES:
        if template.match(line_):
            return True
    return False


processed = []


def process_file(path):
    if path in processed:
        return
    processed.append(path)
    with open(path, 'r') as file:
        for line_ in file:
            if matches(line_):
                continue
            yield line_


with open(OUT_H, 'w+t') as out_h, open(OUT_CPP, 'w+t') as out_cpp:
    out_cpp.write('#include "cyphal.h"\n')
    out_h.write("""
#undef Error_Handler
#undef Error_Handler()
""")

    out_h.write('#define STM32_G\n')
    out_h.write('#define HAL_FDCAN_MODULE_ENABLED\n')

    for target_file in TARGET_FILES:
        print(f"Processing {target_file}")
        for line in process_file(target_file):
            out_h.write(line)
        
        if target_file.suffix != '.h':
            continue
        impl_file = target_file.parent / (target_file.stem + '.cpp')
        if not impl_file.exists():
            continue
        print(f"Processing {impl_file}")
        for line in process_file(impl_file):
            out_cpp.write(line)
