
# Pokemon API

This project is a RESTful API built with FastAPI that provides access to Pokemon data fetched from the PokeAPI. Users can retrieve a list of Pokemon, filter them by name.


## Installation

1. Clone the repository:

   git clone https://github.com/dsilentkiller/pokemon_app.git
   cd pokemon_app  
   cd app 

2.pip install -r requirements.txt

---------------------------  database ----------------
## Troubleshooting

- If encountering database connection issues, ensure PostgreSQL is running and credentials are correct.
- Check logs for any error messages or exceptions.

## postgresql setup 
username : postgres
password : root 



## To run the project, use the following command:
uvicorn main:app --reload