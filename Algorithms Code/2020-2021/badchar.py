def make_bad_match_table(pattern):
    length=len(pattern)
    table={}
    for i in range(length):
        c=pattern[i]
        if i== length-1:
            table[c]=length
        else:
            table[c]=length-i-1
    return table

def boyer_mooree(pattern,text):
    match_table=[]
    patternlength=len(pattern)
    textlength=len(text)
    assert patternlength<=textlength
    table=make_bad_match_table(pattern)
    index=patternlength-1
    pattern_index=patternlength-1
    i=0
    while index+i<textlength:
        if pattern[pattern_index]==text[index]:
            if pattern_index==0:
                match_table.append(index)
                pattern_index=patternlength-1
                index+=(patternlength*2-1)
                i=0
            else:
                pattern_index-=1
                index-=1
                i+=1
        else:
            index+=table.get(text[index+i],patternlength)+i
            pattern_index=patternlength-1
            i=0
    return match_table
text="WELCOMETOTEAMMAST"
pattern="TEAMMAST"
match_table=boyer_mooree(pattern,text)
print("pattern occurs at index = ", match_table)
# print(make_bad_match_table(pattern))