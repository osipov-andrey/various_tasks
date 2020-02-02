import unittest
import re
from phone_numbers import parse, get_patterns, format_phones


class PhoneNumbersTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.test_phones = [
            '28-49-5-123-45-67',
            '87544456789',
            '+28 (495) 123 45 56',
            '875-(29)-123456',
        ]
        self.test_masks = [
            '+875 (29) 1XXXXX - Atlantis MythCell',
            '+875 (44) 4XXXXX - Atlantis MobTelecom',
            '+28 (495) XXXXXXX - ElDorado GoldLine',
        ]
        self.res_phones = [
            '284951234567',
            '87544456789',
            '284951234556',
            '87529123456'
        ]
        self.res_masks = [
            ['+875 (29) 1XXXXX', 'Atlantis MythCell'],
            ['+875 (44) 4XXXXX', 'Atlantis MobTelecom'],
            ['+28 (495) XXXXXXX', 'ElDorado GoldLine']
        ]
        self.res_patterns = {
            re.compile('(875)(29)(1\\d\\d\\d\\d\\d)'): 'Atlantis MythCell',
            re.compile('(875)(44)(4\\d\\d\\d\\d\\d)'): 'Atlantis MobTelecom',
            re.compile('(28)(495)(\\d\\d\\d\\d\\d\\d\\d)'): 'ElDorado GoldLine'
        }
        self.sample_result = [
            '+28 (495) 1234567 - ElDorado GoldLine',
            '+875 (44) 456789 - Atlantis MobTelecom',
            '+28 (495) 1234556 - ElDorado GoldLine',
            '+875 (29) 123456 - Atlantis MythCell',
        ]
        super(PhoneNumbersTest, self).__init__(*args, **kwargs)

    def test_parse(self):
        self.assertEqual(parse(self.test_phones, self.test_masks), (self.res_phones, self.res_masks))

    def test_get_patterns(self):
        self.assertEqual(get_patterns(self.res_masks), self.res_patterns)

    def test_format_phones(self):
        for phone in self.res_phones:
            self.assertIn(format_phones(phone, self.res_patterns), self.sample_result)


if __name__ == '__main__':
    unittest.main()
