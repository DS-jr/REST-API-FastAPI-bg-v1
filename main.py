from fastapi import FastAPI
import pandas as pd 

app5 = FastAPI()

df2 = pd.read_csv("signatures.tsv", sep="\t") 

@app5.get("/")
async def root(patient_id): 
    return df2[df2.iloc[:, 0].str.contains(patient_id)].to_json(orient="index")     # Add a ?JSON-fy function  ***Check FastAPI or Pandas, so the output is strictly in JSON format


#input_name = input("Enter the patient's name (from index column in 'signatures.tsv' file): ") # Input example: NSCLC1155  NSCLC825 
#	return {"message2": "You are always in the optimal place with the optimal LESSONS selected specifically for your max self-dev"} 



