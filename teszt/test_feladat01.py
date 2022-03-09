from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestEvHanyadikNapja(TestCase):
    def test_feladat01(self):
        ev =1
        honap=1
        nap=1
        aktualis = feladatok.ev_hanyadik_napja(ev, honap, nap)
        elvart = 1
        self.assertEqual(elvart, aktualis, str(ev)+"."+str(honap)+"."+str(nap)+". dátum esetén rosszul határozta meg, hgoy az év hanyadik napja")
    def test_feladat02(self):
        ev =2021
        honap=12
        nap=31
        aktualis = feladatok.ev_hanyadik_napja(ev, honap, nap)
        elvart = 365
        self.assertEqual(elvart, aktualis, str(ev)+"."+str(honap)+"."+str(nap)+". dátum esetén rosszul határozta meg, hgoy az év hanyadik napja")
    def test_feladat03(self):
        ev =2021
        honap=3
        nap=31
        aktualis = feladatok.ev_hanyadik_napja(ev, honap, nap)
        elvart = 90
        self.assertEqual(elvart, aktualis, str(ev)+"."+str(honap)+"."+str(nap)+". dátum esetén rosszul határozta meg, hgoy az év hanyadik napja")
    def test_feladat04(self):
        ev =2021
        honap=8
        nap=15
        aktualis = feladatok.ev_hanyadik_napja(ev, honap, nap)
        elvart = 227
        self.assertEqual(elvart, aktualis, str(ev)+"."+str(honap)+"."+str(nap)+". dátum esetén rosszul határozta meg, hgoy az év hanyadik napja")
    def test_feladat05(self):
        ev =2000
        honap=5
        nap=1
        aktualis = feladatok.ev_hanyadik_napja(ev, honap, nap)
        elvart = 222
        self.assertEqual(elvart, aktualis, str(ev)+"."+str(honap)+"."+str(nap)+". dátum esetén rosszul határozta meg, hgoy az év hanyadik napja")
    def test_feladat06(self):
        ev =1984
        honap=6
        nap=12
        aktualis = feladatok.ev_hanyadik_napja(ev, honap, nap)
        elvart = 164
        self.assertEqual(elvart, aktualis, str(ev)+"."+str(honap)+"."+str(nap)+". dátum esetén rosszul határozta meg, hgoy az év hanyadik napja")
    def test_feladat07(self):
        ev =1700
        honap=9
        nap=10
        aktualis = feladatok.ev_hanyadik_napja(ev, honap, nap)
        elvart = 253
        self.assertEqual(elvart, aktualis, str(ev)+"."+str(honap)+"."+str(nap)+". dátum esetén rosszul határozta meg, hgoy az év hanyadik napja")
    def test_feladat08(self):
        ev =2024
        honap=2
        nap=29
        aktualis = feladatok.ev_hanyadik_napja(ev, honap, nap)
        elvart = 60
        self.assertEqual(elvart, aktualis, str(ev)+"."+str(honap)+"."+str(nap)+". dátum esetén rosszul határozta meg, hgoy az év hanyadik napja")