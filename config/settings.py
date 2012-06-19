import os
app_path = os.getcwd()

port = 8080
static_path = "%s/static" % app_path
cookie_secret = "ctMgP6m2TA+1p/NhyTSBWwcQ0TKR9U1fsOWdt6SQvVI="
login_url = "/login"
#define a log file... optionally just use the string 'db' to log it to mongo
#log = "%s/tmp/log/application.log" % app_path
log = 'db'

MONGO = {
    'port': 27017,
    'host': '127.0.0.1',
    'user': '',
    'password': '',
    'database': 'bootstrap',
    'test_database': 'test_bootstrap'
}