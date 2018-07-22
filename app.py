from flask import Flask, request,jsonify
from flask_restful import Resource, Api
import re
import math
from functools import reduce

# Instantiating Flask app and API
app = Flask(__name__)
api = Api(app)

# Takes JSON request with "numbers" converts it to an array and checks to see if there are only numbers
# Returns a str -> float number list for numbers to be calculated on
# If not it returns back an error
def json_numbers_validation():
    json_data = request.get_json(force=True)
    if "NUMBERS" not in json_data:
        return False, 'Make sure the body contains a NUMBERS field. Please try again.'
    number_string = str(json_data["NUMBERS"])
    number_list = re.split(',|\s', number_string)
    number_list = filter(None, number_list)

    if (all (i.isdigit() for i in number_list)) == False:
        return False,"Hey, seems like you used either a non-comma or non-numeric value. Please try again."
    else:
        float_list = [float(i) for i in number_list]
        return True, float_list

# Multiply class unpacks return variables from json_numbers_validation()
# Performs calculation if the numbers were valid, checks for any overflow errors
# Then return response as string
class Multiply(Resource):
    def post(self):
        is_valid, validation_return_body = json_numbers_validation()
        if is_valid == False:
            return  validation_return_body
        else:
            float_list = validation_return_body
            result = reduce((lambda x,y: x * y), float_list)
            if math.isinf(result):
                return jsonify({"message": "Woah those were those large numbers, looks like we had an overflow error! Try again with smaller/less numbers." })
            return jsonify({"message": "Multiplication results in: {}".format(result)})

# Divide class/resource is similar to multiply except there has been an added div/0 error check
class Divide(Resource):
    def post(self):
        is_valid, validation_return_body = json_numbers_validation()
        if is_valid == False:
            return  validation_return_body
        else:
            float_list = validation_return_body
            if (0 in float_list):
                return jsonify({"message": "Hey come on man we know you can't divide by zero! Please try again."})
            result = reduce((lambda x,y: x / y), float_list)

            return jsonify({"message": "Division results in: {}".format(result)})

# Similar to Multiply Resource
class Add(Resource):
    def post(self):
        is_valid, validation_return_body = json_numbers_validation()
        if is_valid == False:
            return  validation_return_body
        else:
            float_list = validation_return_body
            result = reduce((lambda x,y: x + y), float_list)
            if math.isinf(result):
                return jsonify({"message": "Woah those were those large numbers, looks like we had an overflow error! Try again with smaller/less numbers"})
            return jsonify({"message": "Addition results in: {}".format(result)})

# Similar to Multiply Resource
class Subtract(Resource):
    def post(self):
        is_valid, validation_return_body = json_numbers_validation()
        if is_valid == False:
            return  validation_return_body
        else:
            float_list = validation_return_body
            result = reduce((lambda x,y: x - y), float_list)
            if math.isinf(result):
                return jsonify({"message": "Woah those were those large numbers, looks like we had an overflow error! Try again with smaller/less numbers"})
            return jsonify({"message": "Subtraction results in: {}".format(result)})

# Adding resources to the API
api.add_resource(Multiply,'/multiply')
api.add_resource(Divide,'/divide')
api.add_resource(Add,'/add')
api.add_resource(Subtract,'/subtract')

# Run the app when ready
if __name__ == '__main__':
    app.run(debug=False)
