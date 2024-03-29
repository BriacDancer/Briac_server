from flask import Flask, render_template, Response
from camera import Camera

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\R\N'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
	return Response(gen(Camera()),
				mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ =='__main__':
	app.run(host='0.0.0.0', debug=True)
