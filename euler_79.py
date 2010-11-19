#!/usr/bin/env python
s = set()

f = open('keylog.txt')
for i in f:
	for j in i[0], i[1], i[2]:
		s.add(int(j))

l = list(s)

def all_perms(l):
	if len(l) <=1:
		yield l
	else:
		for perm in all_perms(l[1:]):
			for i in range(len(perm)+1):
				yield perm[:i] + l[0:1] + perm[i:]
k = []
for i in open('keylog.txt'):
	k.append([int(j) for j in i[0], i[1], i[2]])

for i in all_perms(l):
	n = 0
	for j in k:
		a = i.index(j[0])
		b = i.index(j[1])
		c = i.index(j[2])
		if not a < b < c:
			break
		else:
			n+=1
		if n == len(k):
			print i