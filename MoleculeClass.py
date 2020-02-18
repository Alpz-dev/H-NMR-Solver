class Molecule(object):

	def __init__(self, adjDict):
		if isinstance(adjDict, dict):
			self.molecule = adjDict
		else:
			return None

	#Returns True if input is Atom Class (also can check list of atoms)
	def checkAtomClass(atom):
		if isinstance(atom, list):
			for atom in set(atom):
				if not isinstance(atom, Atom):
					return False
			return True
		else:
			return isinstance(atom, Atom)

	#Adds atom to bond list in dictionary
	def makeBond(self, atom1, atom2):
		if atom1 in self.molecule and atom2 in self.molecule and checkAtomClass(list(atom1, atom2)):
			#Adds each atom to each other's bond list
			self.molecule[atom1].append(atom2)
			self.molecuel[atom2].append(atom1)
		else:	return None

	#Removes atom from bond list in dictionary
	def breakBond(self, atom1, atom2):
		if atom1 in self.molecule and atom2 in self.molecule:
			#Removes one instance of atom2 from atom1 bond list
			for atom in self.molecule[atom1]:
				if atom == atom2:
					self.molecule[atom1].remove(atom)
					break
			#Removes one instance of atom1 from atom2 bond list
			for atom in self.molecule[atom2]:
				if atom == atom1:
					self.molecule[atom2].remove(atom)
					break

	#Returns number of bonds to atom
	def getSaturation(self, atom):
		if checkAtomClass(atom) and atom in self.molecule:
			return int(len(self.molecule[atom]))
		else:	return None

	#Returns True if molecule is saturated and False otherwise
	def checkSaturation(self, atom):
		if checkAtomClass(atom) and atom in self.molecule:
			return getSaturation(atom) == atom.bondsNeeded
		else:	return None

	def getNbrH(self, atom):
		if checkAtomClass(atom) and atom in self.molecule:
			totalNbrH = 0
			for nbrAtom in set(self.molecule[atom]):
				if nbrAtom.atom == 'C':
					totalNbrH += nbrAtom.numH
			return totalNbrH
		else:	return None

	#Returns True if hydrogen count of neighbors equals nbrH needed for atom and returns False otherwise
	def checkNbrH(self, atom):
		if checkAtomClass(atom) and atom in self.molecule:
			return getNbrH(atom) == atom.nbrH
		else:	return None

	#Returns list of atoms connected to input atom
	def getBondList(self, atom):
		if atom in self.molecule:
			return self.molecule[atom]
		else:	return None

	#Returns DOU of molecule
	def getDOU(self):
		total = 1
		halogens = {'F', 'Cl', 'Br', 'I'}
		for atom in self.molecule:
			if atom.atom == 'C':
				total += 1
				total -= (key.numH/2)
			elif atom.atom == 'N':
				total += 0.5
			elif atom.atom in halogens:
				total -= 0.5
		return total 

	#Attempts to draw a molecule from the adjecency dictionary
	def draw(self):
		return self.molecule

class Atom(object):

	def __init__(self, numH, nbrH, atom = 'C', maxBonds = 4):
		self.numH = numH
		self.nbrH = nbrH
		self.atom = atom
		self.maxBonds = maxBonds
		self.bondsNeeded = maxBonds - self.numH
		self.ID = None

	def __eq__(self, otherAtom):
		return isinstance(otherAtom, Atom) and self.ID == other.ID and\
											 self.numH == other.numH and\
        									 self.atom == other.atom and\
        									 self.nbrH == other.nbrH

	def __hash__(self):
		return hash((self.numH, self.nbrH, self.atom, self.bonds, self.ID))

	def __repr__(self):
		return str(self.atom + ',' + str(self.ID))