# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
print(len(it_companies))
#2
it_companies.add('Twitter')
print(it_companies)
#3
it_companies.update(['Meta', 'ZeuZ', 'BB'])
print(it_companies)
#4
it_companies.remove('Meta')
print(it_companies)

C = A.union(B)
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))

del A
del B

print(age)
age_st = set(age)
print(age_st)

length_age = len(age)
length_age_st = len(age_st)

if length_age > length_age_st:
    print("Age list is bigger")
else:
    print("Age set is bigger")

sentence = 'I am a teacher and I love to inspire and teach people'

sentence_split = sentence.split()

unique_words = set(sentence_split)

print("Unique words: ", sentence_split)
print("Number of unique words: ", len(unique_words))