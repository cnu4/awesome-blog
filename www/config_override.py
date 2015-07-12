#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Override configurations.
'''
import sae.const
__author__ = 'fang'

configs = {
    'db': {
        'host': sae.const.MYSQL_HOST,
        'port': int(sae.const.MYSQL_PORT),
        'user': sae.const.MYSQL_USER,
        'password': sae.const.MYSQL_PASS,
        'database': sae.const.MYSQL_DB
    },
}