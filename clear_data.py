from models import Session, Scholarship

session = Session()
session.query(Scholarship).delete()
session.commit()

print("Old data cleared successfully!")