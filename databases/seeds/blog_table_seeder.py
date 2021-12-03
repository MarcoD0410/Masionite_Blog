"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog

class BlogTableSeeder(Seeder):
    def run(self):
        Blog.create({"subject": "games", "details": "RPG"})
        Blog.create({"subject": "computer", "details": "Pc"})
        Blog.create({"subject": "marvel", "details": "Spider-man"})
