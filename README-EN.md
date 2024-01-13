<img src=https://img.shields.io/badge/python-3.10-violet> <img src=https://img.shields.io/badge/style-black-green>
> [!Note]
>As of 13.01.24 Api that allowed to generate recipes is not working, when api will function again this note will disappear
# Neuro-cook-API 
## Description
This repository is an API for generating recipes using GPT. 
The API also provides the ability to create posts with recipes, add comments to them and create a user.
## Technologies used
The API was developed using the following technologies:
- Programming Language: Python 3.10
- Framework: FastApi
- Database: PostgreSQL
- Caching: Redis
- ## How to use
1. Install the required dependencies by running the command:
   ```
   pip install -r requirements.txt
   ```
2. Start the API server, run the command:
   ```
   uvicorn app.main:app
   ```
   or
   ```
   uvicorn app.main:app --reload --port 8080
   ```

3. To access Swagger, go to http://127.0.0.1:8080/docs#/
  ![изображение](https://github.com/ded2322/Neuro-cook-API/assets/151318767/56fa6e4d-22a8-45bb-8415-640faaecef1d)
  ![изображение](https://github.com/ded2322/Neuro-cook-API/assets/151318767/86fd7ea2-e54e-4942-bd36-1742417ccf6c)
  Swagger
## Sample Queries
- Retrieve all recipes:
  ```http
  GET /recipes/
  ```
- Retrieving a specific recipe:
  ```http
  GET /recipes/1
  ```
- Adding a new recipe:
  ```http
  POST /recipes/add_recipe
  ```
  ```json
  {
    "name_recipe": string,
    "text_post": "string",
    "text_preview": "string"
  }
  ```
- Data update:
  ```http.
  PUT /user/change?new_name=s
  ```
It was only at the moment of the gh push that I realized that I needed to send the data via json 😅 
- Recipe generation
  ```http
  POST /generate
  ```
  ```json
  {
  "food": "string"
  }
  ```
**Note:** Before using the API, make sure you have alemdic data migration and redis configured
