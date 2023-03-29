from flask import Flask
# bluprints
from . import project_detail
from . import project_edit
from . import project_join
from . import login
from . import project_open

app = Flask(__name__)

app.register_blueprint(project_detail.bp)
app.register_blueprint(project_edit.bp)
app.register_blueprint(project_join.bp)
app.register_blueprint(login.bp)
app.register_blueprint(project_open.bp)