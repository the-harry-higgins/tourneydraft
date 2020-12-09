# TourneyDraft

## ABOUT
A game I played with family and friends that I turned into an app.

TLDR:
- Get a group of 8
- Live draft 8 teams each from the field of 64 NCAA March Madness Tournament teams
- Receive points for wins dependent on seed number and round number
- Whoever receives most points wins a portion of money
- Whoever picked overall tournament winner receives portion of money

The basic functionality is that you can create a league and add your friends to it. The league can then hold events corresponding to sports tournaments in the real world. For simplicity's sake I will only have it work for the NCAA March Madness tournament.

Once the field of 64 is determined for the tournament, your league is able to conduct a draft of the teams.
Typically this is done in modified snake fashion with 8 players where the first round is inverted for the second round and the players are reordered for the next grouping of two rounds until all 8 rounds are complete and all 64 teams have been drafted (Round ).

You then receive points for your drafted teams winning the actual games.
You receive the number value of the seed of your team plus the number value of the round of the tournament.
For example: #16 seed UMBC upsets #1 seed UVA in the first round and you receive 16 + 1 = 17 points.
This point system places a lot of value on upsets and cinderella teams, which we have anecdotally found makes the tournament even more fun to watch.

## LIVE LINK

## TECHNOLOGIES USED

### FRONTEND
  - react
  - socket.io
  - material-ui

### BACKEND
  - python
  - flask
  - flask-login
  - socket.io
  - flask-sqlalchemy
  - flask-migrate
  - alembic
  - postgresql

## FEATURES

### Highlight Feature #1
### Highlight Feature #2

## CHALLENGES FACED

## CODE SNIPPETS

# DEV STUFF

## Helpful Links
- [Team Logos](https://www.sportslogos.net/leagues/list_by_category/14/American_Colleges_-_NCAA/logos/)
- [Icon](https://www.flaticon.com/free-icon/basketball-game_77307?term=basketball&page=1&position=46&related_item_id=77307)
- [Favicon](https://favicon.io/emoji-favicons/basketball/)

## Getting started

1. Clone this repository (only this branch)

   ```bash
   git clone https://github.com/appacademy-starters/python-project-starter.git
   ```

2. Install dependencies

      ```bash
      pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt
      ```

3. Create a **.env** file based on the example with proper settings for your
   development environment
4. Setup your PostgreSQL user, password and database and make sure it matches your **.env** file

5. Get into your pipenv, migrate your database, seed your database, and run your flask app

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```

6. To run the React App in development, checkout the [README](./react-app/README.md) inside the `react-app` directory.

***
*IMPORTANT!*
   If you add any python dependencies to your pipfiles, you'll need to regenerate your requirements.txt before deployment.
   You can do this by running:

   ```bash
   pipenv lock -r > requirements.txt
   ```

*ALSO IMPORTANT!*
   psycopg2-binary MUST remain a dev dependency because you can't install it on apline-linux.
   There is a layer in the Dockerfile that will install psycopg2 (not binary) for us.
***

## Deploy to Heroku

1. Create a new project on Heroku
2. Under Resources click "Find more add-ons" and add the add on called "Heroku Postgres"
3. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)
4. Run

   ```bash
   heroku login
   ```

5. Login to the heroku container registry

   ```bash
   heroku container:login
   ```

6. Update the `REACT_APP_BASE_URL` variable in the Dockerfile.
   This should be the full URL of your Heroku app: i.e. "https://flask-react-aa.herokuapp.com"
7. Push your docker container to heroku from the root directory of your project.
   This will build the dockerfile and push the image to your heroku container registry

   ```bash
   heroku container:push web -a {NAME_OF_HEROKU_APP}
   ```

8. Release your docker container to heroku

   ```bash
   heroku container:release web -a {NAME_OF_HEROKU_APP}
   ```

9. set up your database:

   ```bash
   heroku run -a {NAME_OF_HEROKU_APP} flask db upgrade
   heroku run -a {NAME_OF_HEROKU_APP} flask seed all
   ```

10. Under Settings find "Config Vars" and add any additional/secret .env variables.

11. profit
