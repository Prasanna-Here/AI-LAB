from textblob import TextBlob

user_input=input("Enter input: ")
analysis=TextBlob(user_input)
polarity=analysis.sentiment.polarity

if polarity>0:
    sentiment="Positive"
elif polarity==0:
    sentiment="Neutral"
else:
    sentiment="Negative"

print(f"Polarity Score: {polarity}")
print(f"\nSentiment: {sentiment}")