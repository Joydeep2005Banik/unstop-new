n=int(input())
id=list(map(int, input().split()))

unique_id=0
for num in id:
    unique_id=unique_id ^ num

print(unique_id)