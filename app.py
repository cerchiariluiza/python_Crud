from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.casa import Casas, Casa

app = Flask(__name__)
api = Api(app)

#endpoint criado por add_resource, a barra vem com ,tipo:att
api.add_resource(Hoteis, '/hoteis')
api.add_resource(Casas, '/casas')
api.add_resource(Casa, '/casas/<string:casa_id>')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    app.run(debug=False)
