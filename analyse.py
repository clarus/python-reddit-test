import csv

images = []

with open("images.csv", newline="") as input:
    reader = csv.reader(input)
    for row in reader:
        score, title = row
        images.append([int(score), title])

images.sort()
for image in images:
    print(image)
