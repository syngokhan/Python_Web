from SQL import Puppy,db

db.create_all()
sam = Puppy("Sammy",3)
frank = Puppy("Frankie",4)

print(sam.id) # None
print(frank.id) # None

#db.session.add_all([sam,frank])

db.session.add(sam)
db.session.add(frank)
db.session.commit()

print(sam.id)
print(frank.id)

my_puppy = Puppy("Rufus",5)
db.session.add(my_puppy)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)

# Select by id
print("Select ID".center(50,"-"))
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

# Filters
print("Filters".center(50,"-"))
puppy_frankie = Puppy.query.filter_by(name = "Frankie")
print(puppy_frankie.all())

# Update
print("Update".center(50,"-"))
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

# Delete
print("Delete".center(50,"-"))
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

# All of them
print("All Of Them".center(50,"-"))
all_puppies = Puppy.query.all()
print(all_puppies)