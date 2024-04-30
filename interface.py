from flask import Flask,request,render_template
import config 
from project.utils import Sales_Prediction
import numpy as np 


app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return '', 404



app = Flask(__name__)
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
        Item_Weight = eval(data["Item_Weight"])
        Item_Visibility = eval(data["Item_Visibility"])
        Item_MRP = eval(data["Item_MRP"])
        Outlet_Type = data["Outlet_Type"]
        Outlet_Location_Type = data["Outlet_Location_Type"]
        Item_Fat_Content = data["Item_Fat_Content"]
        Item_Type = data["Item_Type"]

        sales_obj = Sales_Prediction(Item_Weight,Item_Visibility,Item_MRP,Outlet_Type,Outlet_Location_Type,Item_Fat_Content,Item_Type)
        sales = sales_obj.Get_Sales()
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
