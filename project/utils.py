import pickle
import json
import numpy as np
import config

class Sales_Prediction():
    def __init__( self,Item_Weight ,Item_Visibility ,Item_MRP ,Outlet_Type ,Outlet_Location_Type ,Item_Fat_Content , Item_Type):
        self.Item_Weight = Item_Weight
        self.Item_Visibility = Item_Visibility
        self.Item_MRP = Item_MRP
        self.Outlet_Type = "Outlet_Type_" + Outlet_Type
        self.Outlet_Location_Type = "Outlet_Location_Type_" + Outlet_Location_Type
        self.Item_Fat_Content = "Item_Fat_Content_" + Item_Fat_Content
        self.Item_Type = "Item_Type_" + Item_Type


    def Model(self):
        with open(config.model_path,"rb")as file:
            self.model = pickle.load(file)
        with open(config.json_path,"r")as file:
            self.json_data = json.load(file)


    def Get_Sales(self):
        self.Model()
        test_array = np.zeros(len(self.json_data["columns"]))
        test_array[0] = self.Item_Weight
        test_array[1] = self.Item_Visibility
        test_array[2] = self.Item_MRP

        index_Outlet_Type1 = self.json_data["columns"].index(self.Outlet_Type)
        test_array[index_Outlet_Type1] = 1

    
        index_Outlet_Location_Type1 = self.json_data["columns"].index(self.Outlet_Location_Type)
        test_array[index_Outlet_Location_Type1] = 1

        
        index_Item_Fat_Content1 = self.json_data["columns"].index(self.Item_Fat_Content)
        test_array[index_Item_Fat_Content1]=1

        
        index_Item_Type = self.json_data["columns"].index(self.Item_Type)
        test_array[index_Item_Type] = 1

        predict_sales = self.model.predict([test_array])
        return predict_sales