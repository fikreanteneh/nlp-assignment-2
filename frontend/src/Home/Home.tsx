import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Textarea } from "@/components/ui/textarea";
import { useState } from "react";

type ClassifyType = "count_vectorizer" | "tfidf_vectorizer" | "xlm_roberta_finetuned";

const Home = () => {

    const [news, setNews] = useState<string>("");
    const [classifyType, setClassifyType] = useState<ClassifyType>("xlm_roberta_finetuned");
    const [result, setResult] = useState<string>(" ");
    const [error, setError] = useState<string>(" ");
    const [loading, setLoading] = useState<boolean>(false);

    const onPasteNews = () => {
        setError("");
        navigator.clipboard.readText().then(
            clipText => {
                setNews(clipText);
            }
        );
    };

    const fetchResult = async (news: string, classifyType: string) => {
        const result = await fetch(
            `https://fikreanteneh-amharicnewsclassifier.hf.space/predict/${classifyType}`,
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/text'
                },
                body: news
            }
        );
        const data = await result.json();
        if (result.status !== 200) {
            throw new Error(data.detail);
        }
        return data.prediction;
    }

    const validateNews = (news: string) => {
        if (news.length < 30) {
            throw new Error("News is too short");
        }
        const totalCharCount = news.replace(/[\s.,/#!$%^&*;:{}=\-_`~()]/g, '').length;
        const amharicCharCount = news.split('').filter(char => /[\u1200-\u137F]/.test(char)).length;

        if (amharicCharCount < totalCharCount / 2) {
            throw new Error("News is not Amharic");
        }
    }
    const onClassifyNews = async () => {
        setError("");
        setLoading(true);
        try {
            validateNews(news);
            const result = await fetchResult(news, classifyType);
            setResult(result);
            // eslint-disable-next-line @typescript-eslint/no-explicit-any
        } catch (e: any) {
            setError(e.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <Card className="relative max-w-3xl border-none w-6xl" >

            <CardHeader>
                <CardTitle className="text-2xl text-center">Amharic News Classification</CardTitle>
                <CardDescription>
                    This is an Amharic News Classification App. It classifies news into 6 categories: ['ሀገር አቀፍ ዜና', 'መዝናኛ', 'ስፖርት', 'ቢዝነስ', 'አለም አቀፍ ዜና', 'ፖለቲካ'].
                    You can choose Count Vectorizer, TF IDF, or XLM RoBERTa pretrained Finetuned to classify the news. The pretrained model is expected to outperform the other two.
                </CardDescription>
            </CardHeader>

            <CardContent className="grid gap-4">
                <Tabs
                    defaultValue="xlm_roberta_finetuned"
                    className="w-full"
                    onValueChange={(value) => setClassifyType(value as ClassifyType)}
                >
                    <TabsList className="w-full">
                        <TabsTrigger value="xlm_roberta_finetuned" className="w-full">XLM RoBERTa Finetuned</TabsTrigger>
                        <TabsTrigger value="Count Vecorizer" className="w-full">Count Vecorizer</TabsTrigger>
                        <TabsTrigger value="tfidf_vectorizer" className="w-full">TF IDF</TabsTrigger>
                    </TabsList>
                </Tabs>

                <Textarea className="h-[45vh]" value={news} onChange={(e) => { setNews(e.target.value) }} />

                <div>
                    <p className="text-xl font-extrabold text-center text-green-500">{result}</p>
                    <p className="text-center text-destructive">{error}</p>
                </div>
                <div className="flex gap-2">
                    <Button className="w-full" variant={"outline"} onClick={onPasteNews}>PasteNews</Button>
                    <Button className="w-full" variant={loading ? "ghost" : "default"} onClick={onClassifyNews}>Classifiy</Button>
                </div>


            </CardContent>

            <CardFooter className="flex flex-col gap-2">
            </CardFooter>
        </Card>
    );
};

export default Home;