from flask import Blueprint

dataService = Blueprint('dataService', __name__)
from . import hqService
from . import dpredis