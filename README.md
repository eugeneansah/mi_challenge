# mi_challenge
# Mobility Intelligence Code Challenge

# How to Run Reactjs (Docker)
i.  cd mi_challenge_reacjs
ii. docker build -t react-docker .
iii. docker run -p 3000:80 react-docker

# How to Run Reactjs (Development)
i.  cd mi_challenge_reacjs
ii. npm install
iii. npm start

# How to Run Flask(Docker)
i.   cd MI_CHALLENGE
ii.  docker build -t flask .
iii. docker run -ti -p 5000:5000 flask

# How to Run Flask(Development)
i.   cd MI_CHALLENGE
ii.  python3 -m venv ve
iii. source ve/bin/activate
iii. pip3 install -r requirements.pip
iv.  export FLASK_APP=mobility.main.py
v. flask run
