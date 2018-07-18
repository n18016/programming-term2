team1 = {'遠藤', '佐藤', '中村'}
team2 = {'田中', '遠藤', '中村'}
team3 = team1 | team2
team3
{'遠藤', ' 中村', '佐藤', '田中'}
team4 = team1 & team2
team4
{'遠藤', '中村'}
