"""Regression checks for the publication UTF-8 guard (standard library only)."""
from pathlib import Path
import json
import tempfile
import unittest
from check_text_encoding import check

class EncodingGuardTests(unittest.TestCase):
    def scan(self, data, name='PUBLICATION_INDEX.json'):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)/name
            p.write_bytes(data)
            return check(Path(tmp))

    def test_correct_bilingual_titles(self):
        data = {'title': 'Colbourn\u2013Dinitz\u2013Rosa',
                'description': 'art\u00edculos: demostraci\u00f3n \u2014 versi\u00f3n 1.0'}
        self.assertEqual(self.scan(json.dumps(data, ensure_ascii=False).encode())['status'], 'PASS')

    def test_three_reported_corruptions(self):
        samples = [('PUBLICATION_INDEX.json', 'Colbourn\u2013Dinitz\u2013Rosa'),
                   ('BILINGUAL_PARITY.json', 'art\u00edculos, demostraci\u00f3n'),
                   ('EDITORIAL_REPORT.md', '\u2014')]
        for name, text in samples:
            corrupted = text.encode('utf-8').decode('cp1252')
            with self.subTest(name=name), self.assertRaises(ValueError):
                data = json.dumps({'text': corrupted}, ensure_ascii=False) if name.endswith('.json') else corrupted
                self.scan(data.encode('utf-8'), name)

    def test_escaped_json_corruption(self):
        corrupted = 'demostraci\u00f3n'.encode('utf-8').decode('cp1252')
        with self.assertRaises(ValueError):
            self.scan(json.dumps({'text': corrupted}, ensure_ascii=True).encode('ascii'))

    def test_invalid_utf8(self):
        with self.assertRaises(ValueError):
            self.scan(b'\xff', 'README.md')

if __name__ == '__main__':
    unittest.main()
