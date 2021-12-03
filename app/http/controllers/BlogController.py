""" A BlogController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Blog import Blog

class BlogController(Controller):
    """Class Docstring Description
    """

    def __init__(self, request: Request):
        self.request = request


    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", BlogController)
        """
        id = self.request.param("id")
        return Blog.find(id)

        pass

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", TodoController)
        """
        return Blog.all()

        pass

    def create(self):
        subject = self.request.input("subject")
        details = self.request.input("details")
        blog = Blog.create({"subject": subject, "details": details})
        return blog

        pass

    

    def update(self):
        subject = self.request.input("subject")
        details = self.request.input("details")
        id = self.request.param("id")
        Blog.where("id", id).update({"subject": subject, "details": details})
        return Blog.where("id", id).get()

        pass

    def destroy(self):
        id = self.request.param("id")
        blog = Blog.where("id", id).get()
        Blog.where("id", id).delete()
        return blog

        pass