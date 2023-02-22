s = "Bengaluru"
ch_to_remove = s[-1]
for i in s:
    if i==ch_to_remove:
        s=s.replace(i,'')
print(s)