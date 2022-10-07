from flask import Flask, Blueprint, request, render_template, make_response, redirect, url_for, abort, jsonify, flash, get_flashed_messages
from control.user import User
from control.plan_p import Cate
from urllib.parse import urlparse, urljoin
from flask_login import login_user, logout_user, current_user, login_required
import bcrypt

# user blueprint 생성
plan_p = Blueprint('plan', __name__)

def find():
    key = Cate.get_b_user(current_user.key)
    return key

@plan_p.route('/create', methods=['POST', 'GET'])
def plan_cate_c():
    cate = request.form.get('cate');
    user = User.get(current_user.id).key
    print(cate)
    Cate.create(user, cate)
    return redirect(url_for('plan.plan'))
    return 0

@plan_p.route('/')
def plan():
    cate = find()
    print(cate)
    return redirect(url_for('main'))