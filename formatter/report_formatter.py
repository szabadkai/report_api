import json

from dicttoxml import dicttoxml
from flask import render_template


class ReportFormatter:
    def __init__(self, report):
        self.id_ = report.id
        self.data = json.loads(report.type)

    def as_xml(self):
        return dicttoxml(self.data)

    def as_html(self, template):
        return render_template(template, **self.data)

    def as_dict(self):
        return {
            'id': self.id_, **self.data
        }
