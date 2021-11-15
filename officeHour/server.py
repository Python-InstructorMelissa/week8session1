from app import app
from app.controllers import public, private   # rename the imported files to what ever you name your controller files

if __name__ ==  "__main__":
    app.run(debug=True)