import pytest
from CardValidity import *

l1 = ("4016870202644910", "06/21", "451", "Rama Yadav")
l2 = ("4016870202644912", "06/21", "401", "Raman Singh 3")
l3 = ("4016870202644912", "01/21", "41", "Aman Gupta")

class Test:
    def testCardNo(self):
        assert validCardNo(l1[0]) == True
        assert validCardNo(l2[0]) == False
        assert validCardNo(l3[0]) == False
    
    def testDate(self):
        assert validDate(l1[1]) == True
        assert validDate(l2[1]) == True
        assert validDate(l3[1]) == False

    def testCVV(self):
        assert validCVV(l1[2]) == True
        assert validCVV(l2[2]) == True
        assert validCVV(l3[2]) == False
    
    def testName(self):
        assert validName(l1[3]) == True
        assert validName(l2[3]) == False
        assert validName(l3[3]) == True
    
    def testCheck(self):
        assert check(*l1) == True
        assert check(*l2) == False
        assert check(*l3) == False
