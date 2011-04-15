# Copyright (C) 2011 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details. 

from nose.tools import *
from tests import prepare_database, with_database
from acoustid.api import serialize_json, serialize_xml


def test_serialize_json():
    data = {'status': 'ok', 'artists': [{'name': 'Jean Michel Jarre', 'year': 1948, 'cities': ['Paris', 'Lyon']}]}
    resp = serialize_json(data)
    assert_equals('text/json', resp.content_type)
    expected = '''{"status": "ok", "artists": [{"cities": ["Paris", "Lyon"], "name": "Jean Michel Jarre", "year": 1948}]}'''
    assert_equals(expected, resp.data)


def test_serialize_xml():
    data = {'status': 'ok', 'artists': [{'name': 'Jean Michel Jarre', 'year': 1948, 'cities': ['Paris', 'Lyon']}]}
    resp = serialize_xml(data)
    assert_equals('text/xml', resp.content_type)
    expected = '''<?xml version='1.0' encoding='UTF-8'?>\n<response><status>ok</status><artists><artist><cities><city>Paris</city><city>Lyon</city></cities><name>Jean Michel Jarre</name><year>1948</year></artist></artists></response>'''
    assert_equals(expected, resp.data)


#@with_database
#def test_lookup_account_id_by_apikey(conn):
#    id = lookup_account_id_by_apikey(conn, 'userkey')
#    assert_equals(1, id)
#    id = lookup_account_id_by_apikey(conn, 'foooo')
#    assert_equals(None, id)
