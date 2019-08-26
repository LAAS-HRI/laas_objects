#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import argparse
from pyassimp import *

def recur_export_node(node, level = 0):
    print("  " + "\t" * level + "- " + str(node))
    export(node, str(node), file_type="obj", processing=8)
    for child in node.children:
        recur_export_node(child, level + 1)

def main(blender_file_path):
    print("Try to load blender model...")
    scene = load(blender_file_path)
    print("Scene successfuly loaded...")
    recur_export_node(scene.rootnode)
    release(scene)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert a blender file to .obj")
    parser.add_argument("blender_file_path", type=str, help="The path of the blender file to convert")
    args = parser.parse_args()
    main(args.blender_file_path)
