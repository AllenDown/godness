#! /usr/bin/env python
# -*- coding: utf-8 -*-


import pymongo


def get_sheet(base, sheet):
    client = pymongo.MongoClient('localhost', 27017)
    base = client[base]
    sheet = base[sheet]
    return sheet


def delete(base, sheet, condition=None):
    sheet = get_sheet(base, sheet)
    sheet.delete_one(condition)


def insert_one(base, sheet, document):
    sheet = get_sheet(base, sheet)
    sheet.insert_one(document)


def insert_many(base, sheet, documents):
    sheet = get_sheet(base, sheet)
    sheet.insert_many(documents)


def find_one(base, sheet, condition=None):
    sheet = get_sheet(base, sheet)
    return sheet.find_one(condition)


def find(base, sheet, condition=None):
    sheet = get_sheet(base, sheet)
    return sheet.find(condition)

