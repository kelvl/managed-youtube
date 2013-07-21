from gevent import monkey

monkey.patch_all()

from flask import Flask
from flask import send_from_directory

app = Flask(__name__, static_folder='static')  

@app.route('/<path:filename>')  
def send_file(filename):  
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)