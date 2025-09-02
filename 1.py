import textblob as t
print("------Welcome all to This Sentiment Analysis Page------")
user_i=input("Enter the desired passage :\n")
analysis = t.TextBlob(user_i)
print(analysis.sentiment)
polarity = analysis.sentiment.polarity
if(polarity>0):
    sentiment="Positive"
elif(polarity<0):
    sentiment="negative"
else:
    sentiment="Neutral"
print(f"The final results are here!")
print(f"The polarity of passage is : {polarity}")
print(f"The Sentiment is :{sentiment}")
