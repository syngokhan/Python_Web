from Relation import db,Puppy,Owner,Toy

rufus = Puppy("Rufus")
fido = Puppy("Fido")

db.session.add_all([rufus,fido])
db.session.commit()

# Check !!!
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name ="Rufus").first()
print(rufus)

# Create Owner Object
gokhan = Owner("Gokhan",rufus.id)

# Give rufus some toys

toy1 = Toy("Chew Toy",rufus.id)
toy2 = Toy("Ball", rufus.id)

db.session.add_all([gokhan,toy1,toy2])
db.session.commit()

# Grab Rufus after those additions!
rufus = Puppy.query.filter_by(name = "Rufus").first()
print(rufus)

# All Of Them Puppy features !!!
print(rufus.report_toys())