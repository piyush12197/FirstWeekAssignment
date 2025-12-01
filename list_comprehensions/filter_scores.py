scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}

result = {name: score for name, score in scores.items() if score > 80}
print(result)
