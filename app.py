from flask import Flask, render_template, request, Response
from chatgpt import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET", "POST"])
def gpt_response():
    userText = request.args.get('msg')
    return str(get_response(userText))

@app.route('/sitemap.xml')
def sitemap():
    sitemap_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>http://lwandle-ai.x10.bz/</loc>
    <lastmod>2023-10-05</lastmod>
    <priority>1.0</priority>
  </url>
</urlset>'''
    return Response(sitemap_xml, mimetype='application/xml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=False)
