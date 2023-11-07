import os


class Passport:

    def __init__(self, first_name, last_name, country, date_of_birth, num_of_passport):
        self.first_name = first_name
        self.last_name = last_name
        self.county = country
        self.date_of_birth = date_of_birth
        self.num_of_passport = num_of_passport

    def printInfo(self):
        print(f'''
Full name: {self.first_name} {self.last_name}
Date of Birth: {self.date_of_birth}
Country: {self.county}
Passport: {self.num_of_passport}''')

    def __repr__(self):
        return f'name {self.first_name} {self.last_name}, Passport {self.num_of_passport}'

class ForeignPassport(Passport):

    def __init__(self, first_name, last_name, country, date_of_birth, num_of_passport, visa):
        super().__init__(first_name, last_name, country, date_of_birth, num_of_passport)
        self.visa = visa

    def printInfo(self):
        super().printInfo()
        print(f'Visa: {self.visa}')

MFC = []
p = Passport('Ivan', 'Ivanov', 'Russia', '14.05.2006', '7743 646375')
MFC.append(p)
fp = ForeignPassport('Petr', 'Petrov', 'Russia', '25,04,1998', '2753 356735', 'China')
MFC.append(fp)
print(MFC)
for item in MFC:
    item.printInfo()

str = 'tqcrtq'
ls = [1,5,2,7,73,2,3,7]
for i in str:
    print(i)

for i in ls:
    print(i)