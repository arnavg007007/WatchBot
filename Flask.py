from flask import Flask, json

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@api.route('/', methods=['GET'])
def home():
  return "Hi!! Welcom to Sajal's flask first project"

if __name__ == '__main__':
    api.run()
