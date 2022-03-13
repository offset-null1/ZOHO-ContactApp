from app.controller.auth import SignupApi, LoginApi
from app.controller.contact import ContactApi
from app_init import api,app
 
@app.errorhandler(Exception)
def server_error(err):
    """Function for unhandled exceptions.

        Keyword arguments:
        err -- error code
    """
    app.logger.exception(err)
    return {'error': f"Something went wrong: {err.__class__.__name__}"}, 500


"""
Api routes.
"""
api.add_resource(SignupApi, '/signup')
api.add_resource(LoginApi, '/login')
api.add_resource(ContactApi, '/contact')


if __name__ == "__main__":
    app.run(debug=True,threaded=True)