begin =0
end =1000
result=0

while begin<end:
    if begin%3==0 or begin%5==0:
        result=result+begin
    begin=begin+1
print result
