from email_validator import validate_email

class Asserter:
    def assertNotNull(self, value, name):
        if not value:
            raise Exception(name +  " cannot be none!")

    def assertGreaterThanZero(self, value, name : str):
        if int(value)<=0:
            raise Exception(name + " must be greater than zero")

    def AssertValidUrl(self, value : str, name : str):
        if not value:
            raise Exception(name + " must be a valid URL!")

    def assertNotEmpty(self, value, name):
        if value==None:
            raise Exception(name + " cannot be null!")
        if len(value) == 0:
            raise Exception(name + " cannot be empty")

    def assertValidEmail(self, email : str, name : str):
        self.assertNotNull(email, name)
        try:
            validate_email(email)
        except:
            raise Exception(email + " is not a valid email address.")

        










