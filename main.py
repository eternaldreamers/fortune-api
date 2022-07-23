# from flask import Flask
# from flask_migrate import Migrate
# # from waitress import serve

# # from src.controllers import app, db

# # migrate = Migrate(app, db)

# if __name__ == "__main__":
#     serve(app, host="0.0.0.0", port=5000)


from src import Bootsrap

boot = Bootsrap()
if __name__ == '__main__':
    boot.run()