import csv
import json
import os
import random
from datetime import date, datetime, timedelta
from multiprocessing import Pool
from socket import gethostname

import requests
import stringcase
from dateutil.parser import isoparse
from flask import (flash, jsonify, make_response, redirect, render_template, request, send_from_directory, url_for)

from . import webhook_bp

@webhook_bp.route('/webhook', methods=['GET','POST'])
def handle_webhook():
    # Process the webhook data
    return jsonify({'status': 'success'})