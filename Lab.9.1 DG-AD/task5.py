#Module Code
"""Course Management Module.

Provides functions to add, remove, and retrieve course records
from an in-memory course catalog.
"""

courses = {}


def add_course(course_id, name, credits):
    """Add a new course or update an existing course in the catalog.

    Args:
        course_id (str): The unique identifier for the course (e.g., 'CS101').
        name (str): The title of the course.
        credits (int): The number of academic credits for the course.

    Returns:
        dict: The stored course dictionary containing course_id, name, and credits.
    """
    courses[course_id] = {
        "course_id": course_id,
        "name": name,
        "credits": credits,
    }
    return courses[course_id]


def remove_course(course_id):
    """Remove a course from the catalog by its course ID.

    Args:
        course_id (str): The unique identifier of the course to remove.

    Returns:
        bool: True if the course was found and removed, False otherwise.
    """
    if course_id in courses:
        del courses[course_id]
        return True
    return False


def get_course(course_id):
    """Retrieve a course record by its course ID.

    Args:
        course_id (str): The unique identifier of the course to look up.

    Returns:
        dict or None: The course dictionary if found, or None if not present.
    """
    return courses.get(course_id)