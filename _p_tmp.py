import csv,collections,re
rows=list(csv.reader(open(r"精翻_v65\09_装备附属_装饰品.csv",encoding="utf-8-sig",newline="")))
d=rows[1:]
n=sum(1 for r in d if re.search(r"~C\d\d",r[7]))
print("带色标条数",n)
print("行数分布",dict(collections.Counter(len(r[7].split("\\n")) for r in d)))
print("含装",sum(1 for r in d if "装" in r[7]))
print("空",sum(1 for r in d if r[7]==""))
print("最长行",max(sum(1 if ord(c)>=0x80 else 0.5 for c in re.sub(r"~C\d\d","",s)) for r in d for s in r[7].split("\\n") if s))
