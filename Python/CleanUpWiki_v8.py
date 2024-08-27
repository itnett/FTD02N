python
import os
import re
import subprocess
import datetime

# Funksjon for å identifisere kjørbar kode i et kjent format
def is_executable_code_block(code_block):
    executable_patterns = {
        r'^