from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
	print('hi')
	# if request.method == 'POST':
	# 	print(request.json)
	# 	return '',200
	# else:
	# 	abort(400)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=10010)

