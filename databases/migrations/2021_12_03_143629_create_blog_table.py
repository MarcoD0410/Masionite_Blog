"""CreateBlogTable Migration."""

from masoniteorm.migrations import Migration


class CreateBlogTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("blog") as table:
            table.increments("id")
            table.string("subject")
            table.string("details")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("blog")
