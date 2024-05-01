from flask import Flask,request,render_template
import config 
from project.utils import Sales_Prediction
import numpy as np 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Saurabh_335@localhost:3306/sales_prediction'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Saurabh_335@localhost:3306/sales_prediction'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class UserInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_weight = db.Column(db.Float)
    item_visibility = db.Column(db.Float)
    item_mrp = db.Column(db.Float)
    outlet_type = db.Column(db.String(50))
    outlet_location_type = db.Column(db.String(50))
    item_fat_content = db.Column(db.String(50))
    item_type = db.Column(db.String(50))
    predicted_sales = db.Column(db.Float)


@app.route("/")
def get_home():
    return render_template("home.html")

@app.route("/Information")
def html():
    return render_template("index.html")


@app.route("/predict_sales",methods = ["POST","GET"])
def get_sales():
    if request.method == "POST":
        data = request.form
        print("User Input Data  ",data)
        Item_Weight = float(data["Item_Weight"])
        Item_Visibility = float(data["Item_Visibility"])
        Item_MRP = float(data["Item_MRP"])
        Outlet_Type = data["Outlet_Type"]
        Outlet_Location_Type = data["Outlet_Location_Type"]
        Item_Fat_Content = data["Item_Fat_Content"]
        Item_Type = data["Item_Type"]


        sales_obj = Sales_Prediction(Item_Weight,Item_Visibility,Item_MRP,Outlet_Type,Outlet_Location_Type,Item_Fat_Content,Item_Type)
        sales = sales_obj.Get_Sales()

        user_input = UserInput(
            item_weight=Item_Weight,
            item_visibility=Item_Visibility,
            item_mrp=Item_MRP,
            outlet_type=Outlet_Type,
            outlet_location_type=Outlet_Location_Type,
            item_fat_content=Item_Fat_Content,
            item_type=Item_Type,
            predicted_sales=sales[0]  
        )
        db.session.add(user_input)
        db.session.commit()

        return render_template("result.html", 
                               Item_Weight=Item_Weight,
                               Item_Visibility=Item_Visibility,
                               Item_MRP=Item_MRP,
                               Outlet_Type=Outlet_Type,
                               Outlet_Location_Type=Outlet_Location_Type,
                               Item_Fat_Content=Item_Fat_Content,
                               Item_Type=Item_Type,
                               predicted_sales=sales[0])



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER, debug=False)
