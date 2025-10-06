from flask import Flask, request, jsonify, abort
from models import Database
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
db = Database()

def paginate(query_params):
    try:
        page = int(query_params.get('page', 1))
        per_page = int(query_params.get('per_page', 10))
        if page < 1: page = 1
        if per_page < 1: per_page = 10
    except ValueError:
        page, per_page = 1, 10
    offset = (page - 1) * per_page
    return page, per_page, offset

@app.route('/artists', methods=['GET','POST'])
def artists():
    if request.method == 'GET':
        page, per_page, offset = paginate(request.args)
        rows = db.query_all('SELECT id, name FROM artists ORDER BY name LIMIT %s OFFSET %s', (per_page, offset))
        return jsonify(rows)
    else:
        data = request.get_json() or {}
        name = data.get('name')
        if not name:
            return jsonify({'error':'name required'}), 400
        new_id = db.insert('INSERT INTO artists (name) VALUES (%s)', (name,))
        return jsonify({'id': new_id, 'name': name}), 201

@app.route('/albums', methods=['GET','POST'])
def albums():
    if request.method == 'GET':
        page, per_page, offset = paginate(request.args)
        rows = db.query_all('SELECT a.id,a.title,a.year,ar.name as artist FROM albums a JOIN artists ar ON a.artist_id=ar.id ORDER BY a.title LIMIT %s OFFSET %s', (per_page, offset))
        return jsonify(rows)
    else:
        data = request.get_json() or {}
        title = data.get('title'); artist_id = data.get('artist_id'); year = data.get('year')
        if not title or not artist_id:
            return jsonify({'error':'title and artist_id required'}), 400
        new_id = db.insert('INSERT INTO albums (artist_id,title,year) VALUES (%s,%s,%s)', (artist_id,title,year))
        return jsonify({'id':new_id,'title':title,'artist_id':artist_id}),201

@app.route('/tracks', methods=['GET','POST'])
def tracks():
    if request.method == 'GET':
        q = request.args.get('q')
        page, per_page, offset = paginate(request.args)
        if q:
            like = '%%%s%%' % q
            rows = db.query_all('SELECT t.id,t.title,t.length_seconds,t.genre,a.title as album,ar.name as artist FROM tracks t LEFT JOIN albums a ON t.album_id=a.id LEFT JOIN artists ar ON a.artist_id=ar.id WHERE t.title LIKE %s OR a.title LIKE %s OR ar.name LIKE %s ORDER BY t.title LIMIT %s OFFSET %s', (like,like,like,per_page,offset))
        else:
            rows = db.query_all('SELECT t.id,t.title,t.length_seconds,t.genre,a.title as album,ar.name as artist FROM tracks t LEFT JOIN albums a ON t.album_id=a.id LEFT JOIN artists ar ON a.artist_id=ar.id ORDER BY t.title LIMIT %s OFFSET %s', (per_page,offset))
        return jsonify(rows)
    else:
        data = request.get_json() or {}
        title = data.get('title'); album_id = data.get('album_id'); length = data.get('length_seconds',0); genre = data.get('genre')
        if not title:
            return jsonify({'error':'title required'}),400
        new_id = db.insert('INSERT INTO tracks (album_id,title,length_seconds,genre) VALUES (%s,%s,%s,%s)', (album_id,title,length,genre))
        return jsonify({'id':new_id,'title':title}),201

@app.route('/playlists', methods=['GET','POST'])
def playlists():
    if request.method == 'GET':
        rows = db.query_all('SELECT id,name FROM playlists ORDER BY name')
        return jsonify(rows)
    else:
        data = request.get_json() or {}
        name = data.get('name')
        if not name:
            return jsonify({'error':'name required'}),400
        new_id = db.insert('INSERT INTO playlists (name) VALUES (%s)', (name,))
        return jsonify({'id':new_id,'name':name}),201

@app.route('/playlists/<int:pid>/tracks', methods=['POST','GET'])
def playlist_tracks(pid):
    if request.method == 'GET':
        rows = db.query_all('SELECT t.id,t.title,pt.position FROM playlist_tracks pt JOIN tracks t ON pt.track_id=t.id WHERE pt.playlist_id=%s ORDER BY pt.position', (pid,))
        return jsonify(rows)
    else:
        data = request.get_json() or {}
        track_id = data.get('track_id'); position = data.get('position',0)
        if not track_id:
            return jsonify({'error':'track_id required'}),400
        db.execute('INSERT INTO playlist_tracks (playlist_id,track_id,position) VALUES (%s,%s,%s)', (pid,track_id,position))
        return jsonify({'playlist_id':pid,'track_id':track_id}),201

@app.route('/health', methods=['GET'])
def health():
    try:
        db.ping()
        return jsonify({'status':'ok'})
    except Exception as e:
        return jsonify({'status':'error','detail':str(e)}),500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT',5000)), debug=True)
