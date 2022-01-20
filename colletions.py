news_articles = [{'id':143,'title':'Happy New Year','date':'01-01-2022','description':'2022 for klu','type':'general'},
                 {'id':123,'title':'radhe shyam','date':'14-01-2022','description':'releasing','type':'movie'},
                 {'id':122,'title':'rrr','date':'07-01-2022','description':'releasing date','type':'movies'},
                 {'id':114,'title':'omicron','date':'02-01-2022','description':' pandamic situation','type':'pharmacy'},
                 {'id':146,'title':'india won match','date':'03-01-2022','description':'india on by england','type':'sports'}
                 ]
print(type(news_articles),len(news_articles))
for na in news_articles:
    if na.get('id') == 123:
        print(na.get('type'))
        print(na.get('date'))
        print(na.get('title'))



