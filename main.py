from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

Streams = {
    1: {"name": "CS:2", "Streams": 15},
    2: {"name": "Dota2", "Streams": 10}
}

parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("Streams", type=int)


class Main(Resource):
    def get(self, stream_id):
        if stream_id == 0:
            return Streams
        else:
            return Streams[stream_id]

    def delete(self, stream_id):
        del Streams[stream_id]
        return Streams

    def post(self, stream_id):
        Streams[stream_id] = parser.parse_args()
        return Streams

    def put(self, stream_id):
        Streams[stream_id] = parser.parse_args()
        return Streams


api.add_resource(Main, "/api/Streams/<int:stream_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
