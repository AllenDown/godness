#! /usr/bin/env python
# -*- coding: utf-8 -*-


import database
import pprint

# database.delete('walden', 'sheet', {'index': 107})


sheet = database.get_sheet('walden', 'sheet')
sheet_backup = database.get_sheet('walden', 'new_sheet')


sheet_backup.delete_one({})

