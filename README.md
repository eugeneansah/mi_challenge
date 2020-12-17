# mi_challenge
# Mobility Intelligence Code Challenge

# How to Run Reactjs (Docker)
* cd mi_challenge_reacjs
* docker build -t react-docker .
* docker run -p 3000:80 react-docker

# How to Run Reactjs (Development)
*  cd mi_challenge_reacjs
* npm install
* npm start

# How to Run Flask(Docker)
*   cd MI_CHALLENGE
*  docker build -t flask .
* docker run -ti -p 5000:5000 flask

# How to Run Flask(Development)
*   cd MI_CHALLENGE
*  python3 -m venv ve
* source ve/bin/activate
* pip3 install -r requirements.pip
*  export FLASK_APP=mobility.main.py
* flask run
