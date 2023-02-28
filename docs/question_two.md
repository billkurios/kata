### Question 2
Swagger definition of the Flask API endpoint implement in Question 1.
In the project, the auto generated file is [here](https://github.com/billkurios/kata/blob/master/docs/swagger.json).
Below it's the swagger content file in yaml format.

```yaml
info:
  contact:
    url: https://github.com/billkurios
  license:
    name: MIT
    url: https://opensource.org/license/mit/
  title: Properties Portfolio APIs Docs
  version: 0.0.1
servers:
  - description: Test Server (Local)
    url: http://127.0.0.1:3000
tags:
  - name: Properties
    description: Endpoints related to properties portfolio
paths:
  /api/manager/properties:
    get:
      description: Get a list of properties linked to the given manager.
      responses:
        '200':
          description: Should return a list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Property'
        '400':
          description: Manager Identifier
        '404':
          description: manager_id don't exist
openapi: 3.0.0
components:
  schemas:
    Property:
      type: object
      properties:
        type:
          type: string
          maxLength: 100
        location:
          type: string
          maxLength: 100
        number_bedrooms:
          type: integer
        price:
          type: integer
        id:
          type: integer
      required:
        - location
        - number_bedrooms
        - price
        - type
```

[Question 1](question_one.md)

[Back to Questions](../README.md)