from unittest import TestCase

import api
from formatter import report_formatter


class StubReport:
    id = 1
    type = '{"organization": "Levi and co"}'


class TestFormatter(TestCase):
    def setUp(self):
        self.app = api.app.test_client()
        self.formatter = report_formatter.ReportFormatter(StubReport())

    def test_dict_format(self):
        self.assertDictEqual({"organization": "Levi and co", "id": 1}, self.formatter.as_dict(),
                             "Test dictionary format")

    def test_xml_format(self):
        self.assertEqual(
            b'<?xml version="1.0" encoding="UTF-8" ?><root><organization type="str">Levi and co</organization></root>',
            self.formatter.as_xml(), "Test XML format")

    def test_html_format(self):
        with api.app.app_context():
            self.assertIn("Levi and co", self.formatter.as_html('report.html'), "Test HTML format")
