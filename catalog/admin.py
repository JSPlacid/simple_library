from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

"""Minimal registration of Models.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
"""

class BooksInline(admin. StackedInline):
    model = Book
    extra = 0

#admin.site.register(Author)
#Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = [('first_name', 'last_name'), 'date_of_birth', 'date_of_death']

    inlines = [BooksInline]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# add book instance inline pattern
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

#admin.site.register(Book)
# Register the Admin classes for Book using the decorator

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Administration object for Book models.
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of book instances in book view (inlines)
    """
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availabilty', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

admin.site.register(Genre)
admin.site.register(Language)