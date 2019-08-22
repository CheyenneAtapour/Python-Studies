# prints out my availability from schedule.txt

# unresolved issues:
	# what to do when ending time not stated?

import re

# convert a time range string to a tuple (time double, {am|pm})
# if you split a char that doesnt exist, you get the whole string
def range2tup(range):
	times = range.split("-")

	pass

# convert julian number into starting calendar date
# return a tuple (day, month, year)
def jul2date(j):
	f = j + 1401 + (((4 * j + 274277) // 146097) * 3) // 4 - 38
	e = 4 * f + 3
	g = (e % 1461) // 4
	h = 5 * g + 2
	day = (h % 153) // 5 + 1
	month = (h // 153 + 2) % 12 + 1
	year = (e // 1461) - 4716 + ((12 + 2 - month) // 12)
	return (day, month, year)

OUTLOOK = 14
WAKE = (7, 0) # tuple to store 7am ?
SLEEP = (11, 1) # 11pm

file = open("schedule.txt", "r", encoding = "utf8")
lines = file.readlines()

outarr = []

for x in range(len(lines)):
	line = lines[x].split(" ")
	parsed = 0

	# try to parse this line's priority as a pure int
	try:
		# check if the line's priority is within our outlook
		if int(line[0][1:-1], 10) <= OUTLOOK and int(line[0][1:-1], 10) >= 0: # slicing is first inclusive, last exclusive
			line.append(int(line[0][1:-1], 10))
			outarr.append(line)
			print(line)
			parsed = 1
	except:
		pass

	# need to stitch together the priority if its in the form 
	# (words words number) 
	# As in, it has spaces inside
	if parsed == 0:
		try:
			if "(" in line[0] and not ")" in line[0]:
				y = 1 
				while not ")" in line[y]:
					line[0] += line[y]
					del line[y]
				line[0] += line[y]
				del line[y] 
		except:
			pass

	# unable to parse as pure int, so manually parse
	if parsed == 0:
		try:
			priority = line[0][1:-1]
			strnum = ""
			pos = -1

			for y in range(len(priority)):
				if priority[y].isdigit():
					# if this is a second number, break
					if not pos == -1 and y > pos + 1:
						break
					pos = y
					try:
						if priority[pos-1] == "-":
							strnum += "-"
					except:
						pass
					strnum += priority[y]

			if len(strnum) >= 1 and int(strnum, 10) <= OUTLOOK and int(strnum, 10) >= 0:
				line.append(int(strnum,10))
				outarr.append(line)
				print(line)
				parsed = 1
		except:
			pass

print(" ")
print(outarr)

# outarr now contains [ ["(priority)", "description", "of", "task"] , [...] , ... , priority]

# need to consider the format of our schedule ouput and data struct
# thinking to print out every free hour. 
# also want times free, such as 
# Monday x/x/x free x xm to xxm, ... 

# get the julian number from the original file
julnum = int(lines[1].split(" ")[0], 10)
#print(jul2date(julnum))

avail = [] # want [  [[str avail],[tuple avail]]  ] 

# create availability general
for x in range(OUTLOOK): # 0 to outlook
	temp = []
	curJul = jul2date(julnum + x) # (day, month, year)
	curDate = str(curJul[0]) + "/" + str(curJul[1]) + "/" + str(curJul[2])
	temp.append(curDate)
	# a if condition else b ; "\" for linebreak 
	s = "Free: " + str(WAKE[0]) + ( "AM" if WAKE[1] == 0 else "PM" ) \
	 + " to " + (str(SLEEP[0])) + ( "PM" if SLEEP[1] == 1 else "AM" )
	temp.append(s) # temp is the [str avail]
	tupavail = [WAKE,SLEEP]
	avail.append([temp, tupavail])

print(" ")
print(avail)
print(" ")

# remove dates in which I am busy with events
# run through outarr, and change elements in avail
for x in range(len(outarr)):
	# if the element falls within our availability range, 
	# update our availability within corresponding avail array element
	# priority number in outarr corresponds to index in avail array
	# as outarr[x][-1]
	# need to parse the time range given
	# what to do with a singular time (not a range?)

	# cases:
		# xx:xx(x)m-xx:xx:(x)m
		# xx:xx(x)m - xx:xx(x)m 

		# xx:xx{ }(xm){ }-{ }xx:xx{ }(x)m
	
	# first, let's try the first case
	event = outarr[x]

	#[0-9]?[0-9].m-[0-9]?[0-9].m

	for y in range(len(event)):
		m = re.search('[0-9]?:?[0-9]:?[0-9]?[0-9]?.m-[0-9]?:?[0-9]:?[0-9]?[0-9]?.m', str(event[y]))
		if m != None: # we have found a "time range"
			print(event[y])
			#event[-1] indexes into avail array
			#avail[x][{str|tup}][pos]
			
			# if the event falls within our availability
			# we need to loop through our tuples to determine this
			# what are the cases?
				# 1. the time range falls after 1 tuple, and before the next tuple
				# 2. the time range starts after 1 tuple, and runs through other tuples
				# 3. the time range starts before a tuple, and runs past a tuple
			
			#if avail[event[-1]][1][]
			pass
