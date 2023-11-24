This generates a sql query from provided text in natural language using
gpt3.5/4 and runs the same on a provided database uri

this works with any database, i have tried
imdb-movie.sqlite from kaggle (https://www.kaggle.com/code/priy998/imdb-sqlite/)
uri is
sqlite:///imdb-movie.sqlite

I also got the omdb movies database imported into a hosted postgres db
on Neon service (https://github.com/df7cb/omdb-postgresql was used for getting the required sql files and then imported into the db with psql command) , the current version uses the same reference as the default uri.

uri from the neon service is 
postgresql+psycopg2://username:password@ep-floral-frog-97311990-pooler.ap-southeast-1.aws.neon.tech/omdb?sslmode=require&options=endpoint%3Dep%2Dfloral%2Dfrog%2D97311990%2Dpooler


I tried implementing the same using ctransformers based local quantized llama and nsql llms, but the results proved to be inaccurate and in some situations irrelevant.

gpt3.5 isn't the best, but the sanest option at this point.

pip install -r requirements.txt --user

streamlit is optional, but it seemed good enough for getting an interface going and hosting the solution, plus i like the way i works with github 

in case you want to try the free version without using openai api_key,
you can just use the llm 


you can access a live version by running it from
codespaces  using the following commands


Setup:
pip install -r requirements.txt --user


streamlit run text-to-sql.py --server.enableCORS false --server.enableXsrfProtection false