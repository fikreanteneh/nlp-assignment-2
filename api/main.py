from models.predict import count_vectorizer_predict, tf_idf_predict

from fastapi import FastAPI, HTTPException, Request
from models.predict import count_vectorizer_predict, tf_idf_predict

app = FastAPI()


@app.post("/predict/count")
async def predict_count(request: Request):
    try:
        input_text = await request.body()
        input_text = input_text.decode('utf-8')
        prediction = count_vectorizer_predict(input_text)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/predict/tfidf")
async def predict_tfidf(request: Request):
    try:
        input_text = await request.body()
        input_text = input_text.decode('utf-8')
        prediction = tf_idf_predict(input_text)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
