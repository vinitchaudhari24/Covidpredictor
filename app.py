from flask import Flask, render_template, request, url_for, session, redirect
import pickle 
from sqlite3 import *


app = Flask(__name__)
app.secret_key = "vinit12"




@app.route("/")
def home():
	if "username" in session:
		return render_template("home.html", name=session["username"])
	else:
		return redirect(url_for("signup"))

@app.route("/signup",methods=["GET", "POST"])
def signup():
	if request.method == "POST":
		un = request.form["un"]
		pw1 = request.form["pw1"]
		pw2 = request.form["pw2"]
		if pw1 == pw2:
			con = None
			try:
				con = connect("user.db")
				cursor = con.cursor()
				sql = "insert into data values('%s', '%s')"
				cursor.execute(sql%(un, pw1))
				con.commit()
				return redirect(url_for("login"))
			except Exception as e:
				con.rollback()
				return render_template("signup.html", msg="Already a user ?")
			finally:
				if con is not None:
					con.close()
		else:
			return render_template("signup.html", msg="passwords did not match")
	else:
		return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		un = request.form["un"]
		pw = request.form["pw"]
		con = None
		try:
			con = connect("user.db")
			cursor = con.cursor()
			sql = ("select * from data where username = '%s' and password = '%s'")
			cursor.execute(sql%(un, pw))
			data = cursor.fetchall()
			if len(data) == 0:
				return render_template("login.html", msg = "Username or Password incorrect")
			else:
				session["username"] = un
				return redirect(url_for("find_out"))
		except Exception as e:
			return render_template("login.html", msg = e)
		finally:
			if con is not None:
				con.close()
	else:
		return render_template("login.html")
	
@app.route("/find_out")
def find_out():
	r1 =  request.args.get("r1")
	if r1 == "no":
		co = 0
	else:
		co = 1 
	r2 = request.args.get("r2")
	if r2 == "no":
		ma = 0
	else:
		ma = 1 
	r3 = request.args.get("r3")
	if r3 == "no":
		t = 0
	else:
		t = 1 
	r4 = request.args.get("r4")
	if r4 == "no":
		st = 0
	else:
		st = 1 
	r5 = request.args.get("r5")
	if r5 == "no":
		rn = 0
	else:
		rn = 1  
	r6 = request.args.get("r6")
	if r6 == "no":
		sn = 0
	else:
		sn = 1 
	r7 = request.args.get("r7")
	if r7 == "no":
		fe = 0
	else:
		fe = 1 
	r8 = request.args.get("r8")
	if r8 == "no":
		na = 0
	else:
		na = 1 
	r9 = request.args.get("r9")
	if r9 == "no":
		vo = 0
	else:
		vo = 1 
	r10 = request.args.get("r10")
	if r10 == "no":
		di = 0
	else:
		di = 1 
	r11 = request.args.get("r11")
	if r11 == "no":
		sb = 0
	else:
		sb = 1 
	r12 = request.args.get("r12")
	if r12 == "no":
		db = 0
	else:
		db = 1 
	r13 = request.args.get("r13")
	if r13 == "no":
		lt = 0
	else:
		lt = 1 
	r14 = request.args.get("r14")
	if r14 == "no":
		ls = 0
	else:
		ls = 1 
	r15 = request.args.get("r15")
	if r15 == "no":
		tc = 0
	else:
		tc = 1 
	r16 = request.args.get("r16")
	if r16 == "no":
		ie = 0
	else:
		ie = 1 
	r17 = request.args.get("r17")
	if r17 == "no":
		im = 0
	else:
		im = 1 
	r18 = request.args.get("r18")
	if r18 == "no":
		iie = 0
	else:
		iie = 1 
	r19 = request.args.get("r19")
	if r19 == "no":
		sn = 0
	else:
		sn = 1 
	r20 =  request.args.get("r20")
	if r20 == "no":
		pe = 0
	else:
		pe = 1

	data = [[co, ma, t, st, rn, sn, fe, na, vo, di, sb, db, lt, ls, tc, ie, im, iie, sn, pe]]
	with open("covid.model", "rb") as f:
		model = pickle.load(f)
	
	res = model.predict(data)
	return render_template("home.html", msg=res)

	

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)


 