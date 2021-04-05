import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import pandas as pd
df = pd.read_excel('Dataset.xlsx')
import json
import re
d={}
def Output(user_input):
  user_input=user_input.lower()
  user_input= re.sub(r'[^\w\s]', '',user_input)
  user_input=user_input.strip()

  stop_words = set(stopwords.words('english')) 
  ignore_words=['today','tomorrow','yesterday','last week','last saturday','very','keenly','keen','with','flying','colours','']
  dont_ignore_words=['i love you','i miss you','i miss her','i miss him','i love him','i love her','i hate him','i hate her','nobody loves me','am ill','is ill','what to do','hello khushi','how are you','not happy','will you be my gf','will you be my girlfriend']
  
  if user_input not in dont_ignore_words:
    word_tokens = word_tokenize(user_input) 
    filtered_sentence = [w for w in word_tokens if w not in stop_words and w not in ignore_words] 
    user_input=' '.join(map(str, filtered_sentence))
  
  for i in range(len(df)):
      if df.loc[i, "User Input"]==user_input or str(df.loc[i, "User Input"]) in user_input:
        d['Khushi']=df.loc[i, "Khushi Output"]
        d['Emotion']=df.loc[i, "Emotion"]
  json_object = json.dumps(d)  
  return json.loads(json_object)
from flask import Flask,jsonify,request
from flask_restful import Resource,Api
app = Flask(__name__)
api=Api(app)
@app.route("/")
def home():
     return jsonify({"about":"Welcome to Khushi App"});
name=''
class Khushi(Resource):
    def get(self,name):
        return Output(name)

api.add_resource(Khushi,'/Name/<string:name>')

if __name__=="__main__":
    app.run(debug=True)
