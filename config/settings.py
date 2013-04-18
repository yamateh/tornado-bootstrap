import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_PATH, '..'))

port = 8080
static_path = "%s/static" % PROJECT_ROOT
template_path = "%s/templates" % PROJECT_ROOT
cookie_secret = "ctMgP6m2TA+1p/NhyTSBWwcQ0TKR9U1fsOWdt6SQvVI="
login_url = "/login"
#define a log file... optionally just use the string 'db' to log it to mongo
#log = "%s/tmp/log/application.log" % PROJECT_ROOT
log = 'logs/access.log'

MONGO = {
    'port': 27017,
    'host': '127.0.0.1',
    'user': '',
    'password': '',
    'database': 'bootstrap',
}

TEST_MONGO  = {
    'port': 27017,
    'host': '127.0.0.1',
    'user': '',
    'password': '',
    'database': 'test_bootstrap'
}
