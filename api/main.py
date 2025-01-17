from models.predict import count_vectorizer_predict, tfidf_vectorizer_predict

from fastapi import FastAPI, HTTPException, Request
from models.predict import count_vectorizer_predict, tfidf_vectorizer_predict

app = FastAPI()


@app.post("/predict/count_vectorizer")
async def predict_count(request: Request):
    try:
        input_text = await request.body()
        input_text = input_text.decode('utf-8')
        prediction = count_vectorizer_predict(input_text)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/predict/tfidf_vectorizer")
async def predict_tfidf(request: Request):
    try:
        input_text = await request.body()
        input_text = input_text.decode('utf-8')
        prediction = tfidf_vectorizer_predict(input_text)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
