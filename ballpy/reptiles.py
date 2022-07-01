from flask import (Blueprint, jsonify,render_template,request ,redirect)
from . import models

bp = Blueprint('reptiles', __name__, url_prefix="/reptiles")




@bp.route('/', methods=['GET', 'POST']) 
def index(): 
    if request.method == 'POST':
        common_name = request.form['common_name']
        scientific_name = request.form['scientific_name']
        conservation_status = request.form["conservation_status"]
        native_habitat = request.form["native_habitat"]
        fun_fact = request.form["fun_fact"]

        new_reptile = models.Reptile(common_name=common_name,scientific_name=scientific_name,conservation_status=conservation_status,native_habitat=native_habitat,fun_fact=fun_fact)
        models.db.session.add(new_reptile)
        models.db.session.commit()

        return "Reptile Posted!"

    results = models.Reptile.query.all()

    return jsonify([results.to_json() for reptile in results])

@bp.route('/<int:id>')
def show(id): 
    reptile = models.Reptile.query.filter_by(id=id).first()
    reptile_dict = {
        'Common Name': reptile.common_name,
        "Scientific Name": reptile.scientific_name,
        "conservation_status":  reptile.conservation_status,
        "native_habitat":  reptile.native_habitat,
        "fun_fact":  reptile.fun_fact,
    }

    return reptile_dict
