import jsonlines



colums = []
with jsonlines.open('train.jsonl') as table_file:
    for obj in table_file:
        # print(obj["sql"]["sel"])
        colums.append(obj["sql"]["sel"])
print(len(colums))