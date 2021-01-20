import random

fname = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael',
         'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer',
         'Maria', 'Adam', 'Sturt', 'Nikolson', 'Tom', 'Harry', 'Ruskin', 'Thor', 'Rocky', 'Ravid', 'David', 'Harris',
         'Eion', 'Elon', 'Mark', 'Will', 'Chris']
lname = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson',
         'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
         'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Potter', 'Jukerberg', 'Smith', 'Nebula',
         'Downy', 'Downy Jr']
street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']
fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor',
               'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg',
               'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria',
               'Winterfell', 'Braavos‎', 'Lakeview']
states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
          'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH',
          'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
class humans:
    def __init__(self,num=1):
        self.num = num

    def firstname(self):
        for name in range(self.num):
            first = random.choice(fname)
            print(first)

    def lastname(self):
        for name in range(self.num):
            last = random.choice(fname)
            print(last)

    def fullname(self):
        for name in range(self.num):
            first = random.choice(fname)
            last = random.choice(lname)
            print(f'{first} {last}')

    def profile(self):
        for i in range(self.num):
            first = random.choice(fname)
            last = random.choice(lname)
            full_name = f'{first} {last}'
            phone_num = f'+91 {random.randint(9000,9999)} {random.randint(100,999)} {random.randint(100,9999)} '
            street_num = f'{random.randint(100,999)}'
            street = f'{random.choice(street_names)}'
            cities = f'{random.choice(fake_cities)}'
            state = f'{random.choice(states)}'

            address = f'{street_num} {street} \n ST : {cities} {state}'
            email = f'{first.lower()}{last.lower()}@gmail.com'

            print(f'{first} {last} \n {address}\n{email}\n{phone_num}')

            print("*"*30)

        print("*"*30)