import json

from dicttoxml import dicttoxml
from flask import Flask, Response, render_template
from flask_accept import accept
from flask_restplus import Resource, Api
from flask_weasyprint import render_pdf

from config import Config
from model.report import Report, db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

api = Api(app)


class HelloWorldResource(Resource):
    @accept('application/json')
    def get(self, id):
        return json.loads(Report.query.get(id).type)

    @get.support('application/xml')
    def get_xml(self, id):
        return Response(dicttoxml(json.loads(Report.query.get(id).type)), mimetype='application/xml')

    @get.support('application/pdf')
    def get_pdf(self, id):
        report = json.loads(Report.query.get(id).type)
        rendered = render_template("report.html", **report)
        return render_pdf(rendered, download_filename='report.pdf')


api.add_resource(HelloWorldResource, '/report/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
