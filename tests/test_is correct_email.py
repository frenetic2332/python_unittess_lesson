from unittest import TestCase
from functions.is_correcr_email import is_correct_email



class IsCorrectEmailFunctionTestCase(TestCase):
    def test_email_1_is_true(self):
        email1 = is_correct_email("monrealstedio@gmail.com")
        self.assertTrue(email1)

    def test_email_2_is_true(self):
        email2 = is_correct_email("ss@gmail.com")
        self.assertTrue(email2)

    def test_email_3_is_flase(self):
        email3 = is_correct_email("s@d@gmail.com")
        self.assertFalse(email3)

    def test_email_4_is_flase(self):
        email4 = is_correct_email("aidana.yahoo.com")
        self.assertFalse(email4)

