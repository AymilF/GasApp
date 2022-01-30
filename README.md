# README

This repository make use of Redis and RQ for asynchronously executing
long running tasks in Plotly Dash in order to display custom list of Gas Station
prices, exposed by on French [Open Data Plateform](https://www.data.gouv.fr/fr/datasets/prix-des-carburants-en-france/).  

Have a look at a running example [here](http://gas.emilienfoissotte.fr)

Examples adapted from :
 * https://github.com/tcbegley/dash-rq-demo
 * https://trstringer.com/logging-flask-gunicorn-the-manageable-way/
 * https://trstringer.com/python-flask-debug-docker-compose/
 * https://pythonspeed.com/articles/activate-virtualenv-dockerfile/

Need improvements : 
 [ ] Implement a Redis Job queue for parsing task
 [ ] Implement a map view with openable link to add a station to database
 [ ] Need a dash layout to filter stations by Gas, with a Selector on location
