import re

def newvalue(source_1, source_2, destination, operator):
	if source_1 in values:
		if source_2 == None or source_2.isdigit() or source_2 in values :
			if operator == "NOT":
				values[destination] = (~values[source_1]) & 65535
			elif operator == "LSHIFT":
				values[destination] = (values[source_1] << int(source_2) ) & 65535
			elif operator == "RSHIFT":
				values[destination] = values[source_1] >> int(source_2)
			elif operator == "OR":
				values[destination] = values[source_1] | values[source_2]
			elif operator == "AND":
				values[destination] = values[source_1] & values[source_2]
			elif operator == "SET":
				values[destination] = values[source_1]
			if destination in pending_gates:
				for infos in pending_gates.pop(destination):
					newvalue(infos[0], infos[1], infos[2], infos[3])
		else:
			if source_2 in pending_gates:
				pending_gates[source_2].append((source_1, source_2, destination, operator))
			else:
				pending_gates[source_2] = [(source_1, source_2, destination, operator)]
	else:
		if source_1 in pending_gates:
			pending_gates[source_1].append((source_1, source_2, destination, operator))
		else:
			pending_gates[source_1] = [(source_1, source_2, destination, operator)]			

valuesRegex = re.compile("[a-z0-9]{1,}")
operatorRegex = re.compile("[A-Z]{2,}")
f = open("input.txt")
line = f.readline()
values = {}
pending_gates = {}

while line != '':
	wires = valuesRegex.findall(line)
	print wires
	if len(wires) == 2:
		if "NOT" in line:
			newvalue(wires[0], None, wires[1], "NOT")
		else:
			if wires[0].isdigit():				
				values[wires[1]] = int(wires[0])
				if wires[1] in pending_gates:
					for infos in pending_gates.pop(wires[1]):
						newvalue(infos[0], infos[1], infos[2], infos[3])
			else:
				newvalue(wires[0], None, wires[1], "SET")
	else:
		if "LSHIFT" in line:
			newvalue(wires[0], wires[1], wires[2], "LSHIFT")
		elif "RSHIFT" in line:
			newvalue(wires[0], wires[1], wires[2], "RSHIFT")
		elif "OR" in line:
			newvalue(wires[0], wires[1], wires[2], "OR")
		elif "AND" in line:
			newvalue(wires[0], wires[1], wires[2], "AND")
	line = f.readline()
print values
print "Result: " + str(values["a"])