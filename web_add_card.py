# coding:utf-8
import re
import sys
import subprocess
from Reader import Reader
reader = Reader()

reload(sys)
sys.setdefaultencoding('utf-8')

# set flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
        title = "NFC Reader/Writer WEB"
        # index.html をレンダリングする
        return render_template('index.html', title=title)

@app.route('/read', methods=['GET', 'POST'])
def read():
	res = subprocess.call('sudo systemctl stop musiccards.service', shell=True)
	print (res)
	title = "NFC Reader/Writer WEB"
	try:
		plist = reader.readCard()
	except ValueError:
		plist =  "thin card in maybe notdata"
	# read.html をレンダリングする
	return render_template('read.html', plist=plist, title=title)

# /post にアクセスしたときの処理
@app.route('/post', methods=['GET', 'POST'])
def post():
	title = "NFC Reader/Writer WEB"
	if request.method == 'POST':
		# リクエストフォームから「プレイリスト」を取得して
		plist = request.form['plist']
		#プレイリストを書き込み
		reader.writeCard(plist)
		# index.html をレンダリングする
		return redirect(url_for('read'))
	else:
		# エラーなどでリダイレクトしたい場合はこんな感じで
		return redirect(url_for('index'))

@app.route('/end', methods=['GET', 'POST'])
def end():
	res = subprocess.call('sudo systemctl restart musiccards.service', shell=True)
	print (res)
	return redirect(url_for('index'))
        #func = request.environ.get('werkzeug.server.shutdown')
	#if func is None:
	#	raise RuntimeError('Not running with the Werkzeug Server')
	#func()
	#return 'Server shutting down...'

if __name__ == '__main__':
	app.run(host='0.0.0.0')
