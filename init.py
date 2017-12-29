#!/usr/bin/env python3
# -*- coding: utf-8 -*-

u"""
VimScriptリポジトリの雛形を作成するスクリプト

args[1] $PLUGIN_NAME
args[2] $COMMAND_NAME
args[3] $FUNC_NAME
"""

import sys, shutil, os
from datetime import datetime

TMPL = "template"

REPLACE_PLUGIN       = "$PLUGIN_NAME"
REPLACE_COMMAND      = "$COMMAND_NAME"
REPLACE_FUNC         = "$FUNC_NAME"
REPLACE_CURRENT_DATE = "$CURRENT_DATE"

def main():
    args         = sys.argv

    if len(args) < 4:
        print("""
need arguments
args[1] $PLUGIN_NAME
args[2] $COMMAND_NAME
args[3] $FUNC_NAME
""")
        return

    plugin_name  = args[1]
    command_name = args[2]
    func_name    = args[3]

    shutil.copytree(TMPL, plugin_name)

    edit_readme(target_file_name=plugin_name + "/README.md"
            , plugin_name=plugin_name)

    edit_template(target_file_name=plugin_name + "/autoload/plugin_name.vim"
            , plugin_name=plugin_name
            , command_name=command_name
            , func_name=func_name)

    edit_template(target_file_name=plugin_name + "/doc/plugin_name.txt"
            , plugin_name=plugin_name
            , command_name=command_name
            , func_name=func_name)

    edit_template(target_file_name=plugin_name + "/plugin/plugin_name.vim"
            , plugin_name=plugin_name
            , command_name=command_name
            , func_name=func_name)

def edit_readme(target_file_name, plugin_name):
    with open(target_file_name) as infile:
        text = infile.read()

    text = text.replace(REPLACE_PLUGIN, plugin_name)

    with open(target_file_name, "w") as outfile:
        outfile.write(text)

def edit_template(target_file_name, plugin_name, command_name, func_name):
    _, ext = os.path.splitext(target_file_name)
    new_file_name = target_file_name.replace("plugin_name", plugin_name)

    os.rename(target_file_name, new_file_name)

    with open(new_file_name) as infile:
        text = infile.read()

    text = text.replace(REPLACE_PLUGIN, plugin_name)
    text = text.replace(REPLACE_COMMAND, command_name)
    text = text.replace(REPLACE_FUNC, func_name)
    now = datetime.now().strftime("%Y/%m/%d")
    text = text.replace(REPLACE_CURRENT_DATE, now)

    with open(new_file_name, "w") as outfile:
        outfile.write(text)

if __name__ == '__main__':
    main()
