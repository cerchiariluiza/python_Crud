from flask_restful import Resource, reqparse

class Casas(Resource):
    def get(self):
        return{'casas': casas}

class Casa(Resource):
    def get(self, casa_id):
        for casa in casas:
            if casa['casa_id'] == casa_id:
                return casa
            return {'message: casa não found'}, 404
    def post(self, casa_id):
        argumentes =reqparse.RequestParser()
        argumentes.add_argument('casa_nome')
        argumentes.add_argument('estrelas')
        argumentes.add_argument('cidade')

        dades =argumentes.parse_args()

        nova_casa = {
        'casa_id':casa_id,
        'casa_nome':dades['casa_nome'],
        'estrelas':dades['estrelas'],
        'cidade':dades['cidade'],

        }
        casas.append(nova_casa)
        return nova_casa, 200
casas = [
    {
    'casa_id': 'alpha',
    'casa_nome': 'nome_alpha',
    'estrelas': '4.5',
    'cidade': 'fn'
    },
    {
    'casa_id': 'beta',
    'casa_nome': 'nome_beta',
    'estrelas': '4.3',
    'cidade': 'rj'
    },
    {
    'casa_id': 'other',
    'casa_nome': 'nome_other',
    'estrelas': '4.2',
    'cidade': 'sp'
    }

]
