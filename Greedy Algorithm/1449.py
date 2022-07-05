# S3 수리공 항승

leaks, tapeLen = map(int, input().split())
leaksList = list(map(int, input().split()))
leaksList.sort()

needTape = 1
start = leaksList[0]
end = start + tapeLen - 0.5

for i in leaksList:
    if end >= i:
        continue
    else:
        needTape += 1
        end = i + tapeLen - 0.5
    
print(needTape)