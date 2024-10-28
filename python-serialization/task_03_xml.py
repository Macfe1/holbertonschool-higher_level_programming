#!/usr/bin/python3
"""
This module provides functionality for serializing
and deserializing Python dictionaries
to and from XML format.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file."""

    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)

    tree = ET.ElementTree(root)
    with open(filename, "wb") as xml_File:
        tree.write(xml_File)


def deserialize_from_xml(filename):
    """Deserialize an XML file back into a Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}

    for item in root:
        dictionary[item.tag] = item.text

    return dictionary
