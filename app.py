from gevent import monkey
from flask import Flask, render_template
import os

monkey.patch_all()

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='%%',
        variable_end_string='%%',
        comment_start_string='<#',
        comment_end_string='#>',
    ))

app = CustomFlask(__name__, static_folder='static')  

playlists = '"{}"'.format('", "'.join([x for x in open("playlists.txt").read().split("\n")]))

google_api_key = "AIzaSyDkzz9NxYT0beSLWdd9m8a5-lEOhBZj71M"

@app.route("/")
def index():
	return render_template('index.html', google_api_key=google_api_key, playlists=playlists)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)