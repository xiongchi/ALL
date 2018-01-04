from flask import Blueprint

main = Blueprint('drawPhoto', __name__)
from da.main import drawPhoto
from da.main import epsPng
from da.main import monitor
from da.main import changesize
from da.main import codeincsv
