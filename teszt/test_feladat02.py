from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestEvHanyadikNapja(TestCase):
    def test_feladat01(self):
        buvosnegyzet=[[8,1,6],[3,5,7],[4,9,2]]
        aktualis = feladatok.buvos_negyzet_e(buvosnegyzet)
        elvart = True
        self.assertEqual(elvart, aktualis,"A négyzet bűvös négyzet")
    def test_feladat02(self):
        buvosnegyzet=[[7,1,6],[3,5,7],[4,9,2]]
        aktualis = feladatok.buvos_negyzet_e(buvosnegyzet)
        elvart = False
        self.assertEqual(elvart, aktualis,"A négyzet nem bűvös négyzet")
    def test_feladat03(self):
        buvosnegyzet=[[8,2,6],[3,5,7],[4,9,2]]
        aktualis = feladatok.buvos_negyzet_e(buvosnegyzet)
        elvart = False
        self.assertEqual(elvart, aktualis,"A négyzet nem bűvös négyzet")
    def test_feladat04(self):
        buvosnegyzet=[[8,1,7],[3,5,7],[4,9,2]]
        aktualis = feladatok.buvos_negyzet_e(buvosnegyzet)
        elvart = False
        self.assertEqual(elvart, aktualis,"A négyzet nem bűvös négyzet")
    def test_feladat05(self):
        buvosnegyzet=[[8,1,6],[4,5,7],[4,9,2]]
        aktualis = feladatok.buvos_negyzet_e(buvosnegyzet)
        elvart = False
        self.assertEqual(elvart, aktualis,"A négyzet nem bűvös négyzet")
    def test_feladat06(self):
        buvosnegyzet=[[8,1,6],[3,4,7],[4,9,2]]
        aktualis = feladatok.buvos_negyzet_e(buvosnegyzet)
        elvart = False
        self.assertEqual(elvart, aktualis,"A négyzet nem bűvös négyzet")
    def test_feladat07(self):
        buvosnegyzet=[[8,1,6],[3,5,6],[4,9,2]]
        aktualis = feladatok.buvos_negyzet_e(buvosnegyzet)
        elvart = False
        self.assertEqual(elvart, aktualis,"A négyzet nem bűvös négyzet")
    def test_feladat08(self):
        buvosnegyzet=[[8,1,6],[3,5,7],[3,9,2]]
        aktualis = feladatok.buvos_negyzet_e(buvosnegyzet)
        elvart = False
        self.assertEqual(elvart, aktualis,"A négyzet nem bűvös négyzet")
    def test_feladat09(self):
        buvosnegyzet=[[8,1,6],[3,5,7],[4,10,2]]
        aktualis = feladatok.buvos_negyzet_e(buvosnegyzet)
        elvart = False
        self.assertEqual(elvart, aktualis,"A négyzet nem bűvös négyzet")
    def test_feladat10(self):
        buvosnegyzet=[[8,1,6],[3,5,7],[4,9,3]]
        aktualis = feladatok.buvos_negyzet_e(buvosnegyzet)
        elvart = False
        self.assertEqual(elvart, aktualis,"A négyzet nem bűvös négyzet")