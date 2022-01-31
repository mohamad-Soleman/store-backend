from app import flask_app, db

db.create_all()
flask_app.run(host="0.0.0.0", port=12111, threaded=True)
db.drop_all()