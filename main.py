from fastapi import FastAPI
import pandas as pd 

app5 = FastAPI()

df2 = pd.read_csv("signatures.tsv", sep="\t") 

@app5.get("/")
async def root(patient_id): 
    return df2[df2.iloc[:, 0].str.contains(patient_id)].to_json(orient="index")   # Input examples: NSCLC1155  NSCLC825 
