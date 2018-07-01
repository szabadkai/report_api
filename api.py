from flask import Flask, Response
from flask_accept import accept_fallback
from flask_restplus import Resource, Api
from flask_weasyprint import render_pdf, HTML

from config import Config
from formatter.report_formatter import ReportFormatter
from model.report import Report
from model.report import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

api = Api(app)


class ReportResource(Resource):
    @accept_fallback
    def get(self, id):
        return ReportFormatter(Report.query.get_or_404(id)).as_dict()

    @get.support('application/xml')
    def get_xml(self, id):
        return Response(ReportFormatter(Report.query.get_or_404(id)).as_xml(), mimetype='application/xml')

    @get.support('application/pdf')
    def get_pdf(self, id):
        html_render = ReportFormatter(Report.query.get_or_404(id)).as_html(template='report.html')
        return render_pdf(HTML(string=html_render))


api.add_resource(ReportResource, '/report/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
