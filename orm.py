from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, DECIMAL, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.exc import SQLAlchemyError
import uuid


from dotenv import dotenv_values

config = dotenv_values(".env")


app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = config.URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model definition
class Favourite(db.Model):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)  # Assuming SERIAL maps to an auto-incremented integer
    user_id = Column(String(255))
    cityname = Column(String(255))
    state = Column(String(255))
    country = Column(String(255))
    longitude = Column(DECIMAL(9, 6))
    latitude = Column(DECIMAL(9, 6))

    def to_dict(self):
        return {
            'id': str(self.id),  # Convert to string if needed, adjust based on actual data type
            'user_id': self.user_id,
            'cityname': self.cityname,
            'state': self.state,
            'country': self.country,
            'longitude': str(self.longitude),
            'latitude': str(self.latitude)
        }

# API endpoint to create a favorite with a provided UUID
@app.route('/favourites', methods=['POST'])
def add_favourite():
    data = request.json
    new_fav = Favourite(user_id=data['user_id'], cityname=data['cityname'], state=data['state'], country=data['country'], longitude=data['longitude'], latitude=data['latitude'])
    db.session.add(new_fav)
    db.session.commit()
    return jsonify(new_fav.to_dict()), 201

# API endpoint to retrieve a favorite by id
@app.route('/favourites', methods=['GET'])
def get_favourite():
    user_id = str(request.args.get('user_id', default = 1))
    fav = Favourite.query.filter(Favourite.user_id == user_id).all()
    r = [f.to_dict() for f in fav]
    if fav:
        return jsonify(r)
    else:
        return jsonify({"error": "Favourite not found"}), 404


# API endpoint to retrieve a favorite by id
@app.route('/deletecity', methods=['DELETE'])
def delete_favourite():
    user_id = request.args.get('user_id')
    cityname = request.args.get('cityname')
    state = request.args.get('state')

    if not all([user_id, cityname, state]):
        return jsonify({"error": "Missing parameters"}), 400

    try:
        fav = Favourite.query.filter_by(user_id=user_id, cityname=cityname, state=state).first()
        if fav:
            db.session.delete(fav)
            db.session.commit()
            return jsonify({"success": "Favourite deleted successfully"}), 200
        else:
            return jsonify({"error": "Favourite not found"}), 404
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
        
if __name__ == '__main__':
    app.run(port=9000,host="0.0.0.0")
