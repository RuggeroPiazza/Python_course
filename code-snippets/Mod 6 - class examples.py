# social media:
# name, last name, age, job, hobby, sport

user_1_name = "John"
user_1_last_name = "Smith"
user_1_age = 37
user_1_job = "Dev"
user_1_hobby = "gaming"
user_1_sport = "F1"

# or I can create a dictionary
user_1 = {
    'name': 'John',
    'last_name': 'Smith',
    'age': 37,
    'job': 'Dev',
    'hobby': 'gaming',
    'sport': 'F1'
}

class SocialMedia:
    def __init__(self, name, last_name, year_of_birth, job, hobby, sport):
        self.name = name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.job = job
        self.hobby = hobby
        self.sport = sport


    def create_email(self):
        return f"{self.name}.{self.last_name}@mysocialmedia.com"
    
    
    def calculate_age(self):
        return f"User {self.name} age is: {2023 - self.year_of_birth}"
    
    def __str__(self):
        return f"{self.name}, {self.last_name}"


# create an instance of the class
user1 = SocialMedia('Rug', 'Piazza', 1986, 'Dev', 'Restoration retro console', 'F1')

# print(user1)
# print(user1.name)
# print(user1.job)
# print(user1.hobby)
# print(user1.create_email())
# print(user1.calculate_age(user1.year_of_birth))
print(user1)