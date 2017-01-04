from flask import Flask, request, session, render_template, jsonify;
from flaskext.mysql import MySQL;
import json;

app = Flask(__name__);
mysql = MySQL();

app.config['MYSQL_DATABASE_USER'] = 'root';
app.config['MYSQL_DATABASE_PASSWORD'] = 'akekdk1';
app.config['MYSQL_DATABASE_DB'] = 'miboard';

mysql.init_app(app);
cursor = mysql.connect().cursor();

@app.route("/")
def helloworld():
	return "HelloWorld";

@app.route("/login", methods=['POST'])
def login():
	if request.form:
		content = [item for item in request.form]
		print "Content:", ''.join(content)
	else:
		content = request.get_json(force=True)
		print "Content:", content

	temp = json.dumps(content)
	data = json.loads(temp)
	print data["id"]

	if data["id"] == 'a' and data["password"] == 'a':
		return jsonify({'result_code':'200'}), 200
	if data["id"] == 'a' and data["password"] != 'a':
		return jsonify({'result_code':'405'}), 405
	else:
		return jsonify({'result_code':'404'}), 404


@app.route("/login/member", methods=['GET', 'POST'])
def members():
	
	cursor.execute("SELECT * FROM miboard_member")

	result = []
	columns = tuple( d[0] for d in cursor.description)

	for row in cursor:
		result.append(dict(zip(columns, row)))

	return json.dumps(result);

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=5009);