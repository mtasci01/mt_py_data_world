from fastapi import FastAPI, HTTPException

from mt_py_data_world_service import MtPyDataWorldService

app = FastAPI()

service = MtPyDataWorldService()

@app.get("/online_dating_sim")
def runOnlineDating():
    return service.runOnlineDatingSim()

@app.get("/search_engine")
def runSearch(q = None):
    if q is None:
        raise HTTPException(status_code=400, detail="q is null")
    return service.runSearchEngine(q)

@app.get("/weather_predictor")
def runWeatherPredictor(m = None):
    return service.runWeatherPredictor(m)

