from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# 데이터 저장소
data = {
    "records": [],
    "goal": 8
}

