# URL shortner
REST API for shortening urls  
- custom hashing function to generate unique strings   
- Hash generatioin based on previous hash counter
- stores the long url mapped with hash string in the db
- redirects to original long url using the hash key as url query parameter

## Tech Stack: 
- Django Rest Framework

## To Do:  

- Migrate data base to NoSQL(MongoDB)  
- Add authentication 
- Add Caching using Redis  
- Add Custom Rate Limiter  
 
 ## API
 
 Deployed on Railway: https://web-production-c1d8.up.railway.app/api/  
 
 ## To on run  
 
 Clone the project

```bash
  git clone https://github.com/nilesh05apr/urlshortner/
```

Go to the project directory

```bash
  cd urlshortner
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python3 manage.py runserver
```
