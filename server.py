from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
app = Flask(__name__)

densities = {
    'sand':1540,
    'cement':1600,
    'aggregate':1750,
}

with open("estimator.bin", 'rb') as f:
    model = pickle.load(f)

@app.route("/")
def index():
    return render_template("client.html")


@app.route('/concrete_strength')
def concrete_strength():
    cement_mass = request.args.get("cement")
    sand_mass = request.args.get("sand")
    aggregate_mass = request.args.get("aggregate")
    feature_set = np.array([cement_mass,0,0,186.4,0,aggregate_mass,sand_mass,28])
    results = model.predict([feature_set])
    strength = results[0]
    return str(strength)

@app.route('/densities')
def component_densities():
    return jsonify(densities)