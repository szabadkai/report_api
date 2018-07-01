from unittest import TestCase, main

import requests

import api


class TestFlaskApi(TestCase):
    def setUp(self):
        """To run these, you will need to run the actual app"""
        self.app = api.app.test_client()

    def test_swager_ui(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code, "Root route returns 200")

    def test_report_default_accepts_content_type_is_json(self):
        response = requests.get('http://localhost:5000/report/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("content-type", response.headers)
        self.assertEqual("application/json", response.headers.get('content-type'))

    def test_invalid_id_returns_404(self):
        response = requests.get('http://localhost:5000/report/9999999')
        self.assertEqual(response.status_code, 404)

    def test_report_xml_accepts_response_content_type_is_xml(self):
        response = requests.get('http://localhost:5000/report/1', headers={'Accept': 'application/xml'})
        self.assertEqual(response.status_code, 200)
        self.assertIn("content-type", response.headers)
        self.assertEqual("application/xml; charset=utf-8", response.headers.get('content-type'))

    def test_report_pdf_accepts_response_content_type_is_pdf(self):
        response = requests.get('http://localhost:5000/report/1', headers={'Accept': 'application/pdf'})
        self.assertEqual(response.status_code, 200)
        self.assertIn("content-type", response.headers)
        self.assertEqual("application/pdf", response.headers.get('content-type'))


if __name__ == "__main__":
    main()
