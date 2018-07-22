# Simple Flask API Calculator

## API Endpoints

Domain: ```https://0pv3f7av06.execute-api.us-east-2.amazonaws.com/dev```

Endpoints: ```/divide, /multiply, /add, /subtract```

Methods: ```POST``` only

Body: Requires JSON format with a "NUMBERS" field in JSON object.

      Accepts only Integers.

      Will throw errors for div/0 & any float overflow errors.

Returns: ```{
  "message": __operationType__ results in __results__
}```
