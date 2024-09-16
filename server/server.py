import flask

app = flask.Flask(__name__)

@app.route("/")
def serve_home_page():
    return flask.render_template_string(
        open('index.html').read()
    )

@app.route("/table")
def serve_table():
    email = flask.request.query_string.decode("utf-8")
    table = [line.split(",") for line in open(f"db/{email}.csv").readlines()]
    html = "<table border='1'>"
    html += "<thead><tr>" + "".join(f"<th>{header}</th>" for e in table[0]) + "<tr><thead>"
    html += "<tbody>" + "".join([
        "".join([f"<td>{e}</td>" for e in row])
        for row in table
    ]) + "</tbody>"
    html += "</table>"
    
    html = f"""
    <html>
    <head>
        <title>CSV Table</title>
    </head>
    <body>
        <h1>Data ^_^</h1>
        {html}
    </body>
    </html>
    """

    return flask.render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
