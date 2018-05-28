# -*- coding: UTF-8 -*-
__Author__ = "Sky Huang"

import os
import sys

from mekk.xmind import XMindDocument

print(sys.path)

proDir = os.path.split(os.path.realpath(__file__))[0]
OUTPUT = os.path.join(proDir, "test_manual.xmind")


def parse_and_print(OUTPUT):
    xmind = XMindDocument.open(OUTPUT)

    sheet = xmind.get_first_sheet()
    print("Sheet title: ", sheet.get_title())

    root = sheet.get_root_topic()
    print("Root title: ", root.get_title())
    print("Root note: ", root.get_note())

    for topic in root.get_subtopics():
        print("* ", topic.get_title())
        print("   label: ", topic.get_label())
        print("   link: ", topic.get_link())
        print("   markers: ", list(topic.get_markers()))
        # topic.get_subtopics()

        # legend = sheet.get_legend()


if __name__ == "__main__":
    parse_and_print(OUTPUT)
