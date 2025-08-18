"""
Practice Problems: Classes and Objects
=====================================

Instructions:
1. Read each problem carefully
2. Implement the solution below each problem statement
3. Test your code with the provided test cases
4. Run the file to see if your solutions work correctly

Key Concepts to Practice:
- Class definition and structure
- Constructor (__init__) method
- Instance vs class variables
- Instance methods
- String representation (__str__, __repr__)
- Input validation
- Error handling

Note: Focus on understanding why we use each concept, not just how!
"""

from datetime import datetime
from typing import Optional

# =============================================================================
# Problem 1: Library Management System
# =============================================================================

"""
Problem 1: Create a comprehensive Book class for a library system.

Requirements:
1. Class Variables:
   - library_name = "City Public Library"
   - total_books = 0 (tracks all books in the system)
   - book_id_counter = 1001 (auto-increment book IDs)

2. Instance Variables:
   - title (string): Book's title
   - author (string): Book's author
   - isbn (string): Book's ISBN number
   - book_id (int): Unique auto-generated ID
   - is_available (bool): Whether book can be borrowed (starts True)
   - borrowed_by (string or None): Who borrowed the book (starts None)
   - borrowed_date (string or None): When book was borrowed (starts None)

3. Methods:
   - __init__(title, author, isbn): Initialize the book
   - borrow_book(borrower_name): Mark book as borrowed if available
   - return_book(): Mark book as returned
   - get_book_info(): Return formatted book information
   - __str__(): Human-readable representation
   - __repr__(): Developer representation

4. Input Validation:
   - Title and author must be non-empty strings
   - ISBN must be a valid format (assume 13 digits with hyphens)
   - Borrower name must be non-empty string

Business Logic:
- Can't borrow if already borrowed
- Can't return if not borrowed
- Track borrowing date when book is borrowed
- Clear borrowing info when book is returned

Expected Output Format:
Book Info: "Book ID: 1001 | Title: 'Python Programming' | Author: 'John Doe' | Available: Yes"
Borrow Success: "✅ 'Python Programming' borrowed by Alice Johnson on 2024-01-15"
Borrow Failure: "❌ 'Python Programming' is already borrowed by Bob Smith"
"""

class Book:
    # Define class variables here
    library_name = "City Public Library"
    total_books = 0
    book_id_counter = 1001
    
    def __init__(self, title: str, author: str, isbn: str):
        """
        Initialize a new book.
        
        TODO: Implement this method
        - Validate inputs (non-empty strings)
        - Set instance variables
        - Generate unique book_id
        - Update class variables
        - Set initial availability status
        """
        if not title or not author or not isbn:
            raise ValueError("Title, author, and ISBN must be non-empty strings.")
        if len(isbn) != 17 or not all(c.isdigit() or c == '-' for c in isbn):
            raise ValueError("ISBN must be a valid format (13 digits with hyphens).")
        self.title = title
        self.author = author
        self.isbn = isbn
        self.book_id = Book.book_id_counter
        self.is_available = True
        self.borrowed_by = None
        self.borrowed_date = None
        Book.book_id_counter += 1
        Book.total_books += 1
    
    def borrow_book(self, borrower_name: str) -> str:
        """
        Borrow the book if available.
        
        TODO: Implement this method
        - Check if book is available
        - Validate borrower_name
        - Update borrowing status
        - Set borrowed_date to current date
        - Return appropriate message
        """
        if not borrower_name:
            raise ValueError("Borrower name must be a non-empty string.")
        if not self.is_available:
            return f"'{self.title}' is already borrowed by {self.borrowed_by}"
        self.is_available = False
        self.borrowed_by = borrower_name
        self.borrowed_date = datetime.now().strftime("%Y-%m-%d")
        return f"'{self.title}' borrowed by {borrower_name} on {self.borrowed_date}"
    
    def return_book(self) -> str:
        """
        Return the borrowed book.
        
        TODO: Implement this method
        - Check if book is actually borrowed
        - Clear borrowing information
        - Mark as available
        - Return appropriate message
        """
        if self.is_available:
            return f"'{self.title}' is not currently borrowed."
        self.is_available = True
        self.borrowed_by = None
        self.borrowed_date = None
        return f"'{self.title}' has been returned and is now available."
        
    
    def get_book_info(self) -> str:
        """
        Get formatted book information.
        
        TODO: Implement this method
        - Return formatted string with all book details
        - Show availability status
        - If borrowed, show who borrowed it and when
        """
        availability = "Yes" if self.is_available else "No"
        borrowed_info = f" | Borrowed by: {self.borrowed_by} on {self.borrowed_date}" if not self.is_available else ""
        return (f"Book ID: {self.book_id} | Title: '{self.title}' | Author: '{self.author}' | "
                f"Available: {availability}{borrowed_info}")
    
    def __str__(self) -> str:
        """Human-readable string representation."""
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - ID: {self.book_id} - Available: {self.is_available}"
    
    def __repr__(self) -> str:
        """Developer string representation."""
        return (f"Book(book_id={self.book_id}, title='{self.title}', author='{self.author}', "
                f"isbn='{self.isbn}', is_available={self.is_available}, "
                f"borrowed_by={self.borrowed_by}, borrowed_date={self.borrowed_date})")


# Test cases for Problem 1
def test_book_class():
    """Test the Book class implementation."""
    print("=== Testing Problem 1: Book Class ===")
    
    try:
        # Test book creation
        book1 = Book("Python Programming", "John Doe", "978-0-123456-78-9")
        book2 = Book("Data Structures", "Jane Smith", "978-0-987654-32-1")
        
        print("Books created successfully!")
        print(f"Total books: {Book.total_books}")
        
        # Test book info
        print(book1.get_book_info())
        print(book2.get_book_info())
        
        # Test borrowing
        print(book1.borrow_book("Alice Johnson"))
        print(book1.borrow_book("Bob Smith"))  # Should fail
        
        # Test returning
        print(book1.return_book())
        print(book1.return_book())  # Should fail
        
        # Test string representations
        print("String representation:", str(book1))
        print("Repr representation:", repr(book1))
        
    except Exception as e:
        print(f"Error testing Book class: {e}")

# Uncomment to test Problem 1
# test_book_class()


# =============================================================================
# Problem 2: Employee Management System
# =============================================================================

"""
Problem 2: Create a comprehensive Employee class for company management.

Requirements:
1. Class Variables:
   - company_name = "TechCorp Solutions"
   - total_employees = 0
   - employee_id_counter = 1000
   - departments = ["Engineering", "Marketing", "Sales", "HR", "Finance"]

2. Instance Variables:
   - name (string): Employee's full name
   - employee_id (int): Unique auto-generated ID
   - department (string): Employee's department
   - salary (float): Employee's annual salary
   - hire_date (string): Date when employee was hired
   - is_active (bool): Whether employee is currently employed
   - performance_ratings (list): list to store performance ratings

3. Methods:
   - __init__(name, department, salary): Initialize employee
   - give_raise(amount): Increase salary by given amount
   - change_department(new_department): Move to different department
   - add_performance_rating(rating): Add performance rating (1-5 scale)
   - calculate_average_rating(): Calculate average of all ratings
   - get_employee_details(): Return formatted employee information
   - terminate(): Mark employee as inactive
   - __str__() and __repr__(): String representations

4. Input Validation:
   - Name must be non-empty string
   - Department must be in allowed departments list
   - Salary must be positive number
   - Performance rating must be between 1 and 5
   - Raise amount must be positive

Business Logic:
- New employees start as active with today's hire date
- Can't give raise or change department if employee is terminated
- Performance ratings should be stored as list for history
- Average rating should handle empty ratings list gracefully

Expected Behaviors:
- Salary changes should be reflected immediately
- Department changes should validate against allowed departments
- Performance tracking should maintain history
"""

class Employee:
    company_name = "TechCorp Solutions"
    total_employees = 0
    employee_id_counter = 1000
    departments = ["Engineering", "Marketing", "Sales", "HR", "Finance"]
    
    def __init__(self, name: str, department: str, salary: float):
        """
        Initialize a new employee.
        
        TODO: Implement this method
        - Validate all inputs
        - Set instance variables
        - Generate unique employee_id
        - Set hire_date to today
        - Initialize empty performance_ratings list
        - Update class variables
        """
        if not name:
            raise ValueError("Name must be a non-empty string.")
        if department not in Employee.departments:
            raise ValueError(f"Department must be one of {Employee.departments}.")
        if salary <= 0:
            raise ValueError("Salary must be a positive number.")
        self.name = name
        self.department = department
        self.salary = salary
        self.employee_id = Employee.employee_id_counter
        self.hire_date = datetime.now().strftime("%Y-%m-%d")
        self.is_active = True
        self.performance_rating = []
        Employee.employee_id_counter += 1
        Employee.total_employees += 1
    
    def give_raise(self, amount: float) -> str:
        """
        Give the employee a salary raise.
        
        TODO: Implement this method
        - Check if employee is active
        - Validate raise amount is positive
        - Update salary
        - Return success message with new salary
        """
        if amount <= 0:
            raise ValueError("Raise amount must be a positive number.")
        if not self.is_active:
            return f"Cannot give raise to {self.name} as they are no longer active."
        self.salary += amount
        return f"{self.name} has received a raise of ${amount}. New salary: ${self.salary:.2f}"
    
    def change_department(self, new_department: str) -> str:
        """
        Transfer employee to a new department.
        
        TODO: Implement this method
        - Check if employee is active
        - Validate department exists in allowed list
        - Update department
        - Return success message
        """
        if not self.is_active:
            return f"Cannot change department for {self.name} as they are no longer active."
        if new_department not in Employee.departments:
            raise ValueError(f"Department must be one of {Employee.departments}.")
        self.department = new_department
        return f"{self.name} has been transferred to {self.department} department."
    
    def add_performance_rating(self, rating: int) -> str:
        """
        Add a performance rating for the employee.
        
        TODO: Implement this method
        - Check if employee is active
        - Validate rating is between 1 and 5
        - Add to performance_ratings list
        - Return success message
        """
        if not self.is_active:
            return f"Cannot add rating for {self.name} as they are no longer active."
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
        self.performance_rating.append(rating)
        return f"Rating {rating} added for {self.name}. Total ratings: {len(self.performance_rating)}"
    
    def calculate_average_rating(self) -> Optional[float]:
        """
        Calculate average performance rating.
        
        TODO: Implement this method
        - Handle case where no ratings exist (return None)
        - Calculate and return average of all ratings
        - Round to 2 decimal places
        """
        if not self.performance_rating:
            return None
        average = sum(self.performance_rating) / len(self.performance_rating)
        return round(average, 2)
    
    def get_employee_details(self) -> str:
        """
        Get comprehensive employee information.
        
        TODO: Implement this method
        - Return multi-line formatted string with all details
        - Include average rating if available
        - Show active/terminated status
        """
        status = "Active" if self.is_active else "Terminated"
        average_rating = self.calculate_average_rating()
        avg_rating_str = f" | Average Rating: {average_rating}" if average_rating is not None else ""
        return (f"Employee ID: {self.employee_id} | Name: {self.name} | Department: {self.department} | "
                f"Salary: ${self.salary:.2f} | Hire Date: {self.hire_date} | Status: {status}{avg_rating_str}")
    
    def terminate(self) -> str:
        """
        Terminate the employee.
        
        TODO: Implement this method
        - Mark employee as inactive
        - Return confirmation message
        """
        if not self.is_active:
            return f"{self.name} is already terminated."
        self.is_active = False
        return f"{self.name} has been terminated from the company."
    
    def __str__(self) -> str:
        """Human-readable representation."""
        return (f"{self.name} (ID: {self.employee_id}) - {self.department} Department - "
                f"Salary: ${self.salary:.2f} - Hired on: {self.hire_date} - Status: {'Active' if self.is_active else 'Terminated'}")
    
    def __repr__(self) -> str:
        """Developer representation."""
        return (f"Employee(employee_id={self.employee_id}, name='{self.name}', "
                f"department='{self.department}', salary={self.salary}, "
                f"hire_date='{self.hire_date}', is_active={self.is_active}, "
                f"performance_ratings={self.performance_rating})")


# Test cases for Problem 2
def test_employee_class():
    """Test the Employee class implementation."""
    print("\n=== Testing Problem 2: Employee Class ===")
    
    try:
        # Create employees
        emp1 = Employee("Alice Johnson", "Engineering", 75000)
        emp2 = Employee("Bob Smith", "Marketing", 65000)
        
        # Test operations
        print(emp1.give_raise(5000))
        print(emp1.change_department("Sales"))
        print(emp1.add_performance_rating(4))
        print(emp1.add_performance_rating(5))
        
        # Test details
        print(emp1.get_employee_details())
        print(f"Average rating: {emp1.calculate_average_rating()}")
        
        # Test termination
        print(emp2.terminate())
        print(emp2.give_raise(1000))  # Should fail
        
        print(f"Total employees: {Employee.total_employees}")
        
    except Exception as e:
        print(f"Error testing Employee class: {e}")

# Uncomment to test Problem 2
# test_employee_class()


# =============================================================================
# Problem 3: Social Media Post System
# =============================================================================

"""
Problem 3: Create a SocialMediaPost class for a social platform.

Requirements:
1. Class Variables:
   - platform_name = "PythonSocial"
   - total_posts = 0
   - post_id_counter = 10000

2. Instance Variables:
   - post_id (int): Unique auto-generated ID
   - author (string): Post author's username
   - content (string): Post content/text
   - timestamp (string): When post was created
   - likes_count (int): Number of likes (starts at 0)
   - comments (list): list to store comment strings
   - is_public (bool): Whether post is public or private
   - hashtags (list): list of hashtags extracted from content

3. Methods:
   - __init__(author, content, is_public=True): Initialize post
   - add_like(): Increment likes count
   - remove_like(): Decrement likes count (minimum 0)
   - add_comment(commenter, comment_text): Add a comment
   - edit_content(new_content): Update post content and re-extract hashtags
   - get_post_summary(): Return formatted post information
   - extract_hashtags(): Private method to find hashtags in content
   - make_private() / make_public(): Change privacy settings
   - __str__() and __repr__(): String representations

4. Business Logic:
   - Extract hashtags automatically from content (words starting with #)
   - Comments should be stored as "username: comment text"
   - Likes count cannot go below 0
   - Content editing should update hashtags
   - Posts start as public by default

5. Input Validation:
   - Author must be non-empty string without spaces (username format)
   - Content must be non-empty and max 280 characters
   - Commenter must be non-empty string
  - Comment text must be non-empty and max 100 characters

Expected Features:
- Automatic hashtag extraction (e.g., "Love #python and #coding!" -> ["#python", "#coding"])
- Comment format: "username: comment text"
- Like management with bounds checking
- Content editing with hashtag refresh
"""

class SocialMediaPost:
   # Define class variables
   platform_name = "PythonSocial"
   total_posts = 0
   post_id_counter = 10000
   
   def __init__(self, author: str, content: str, is_public: bool = True):
       """
       Initialize a new social media post.
       
       TODO: Implement this method
       - Validate author (non-empty, no spaces)
       - Validate content (non-empty, max 280 chars)
       - Set instance variables
       - Generate unique post_id
       - Set timestamp to current datetime
       - Extract hashtags from content
       - Initialize likes_count to 0
       - Initialize empty comments list
       - Update class variables
       """
       if not author or ' ' in author:
            raise ValueError("Author must be a non-empty string without spaces.")
       if not content or len(content) > 280:
            raise ValueError("Content must be a non-empty string with max 280 characters.")
       self.author = author
       self.content = content
       self.post_id = SocialMediaPost.post_id_counter
       self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       self.likes_count = 0
       self.comments = []
       self.is_public = is_public
       self.hashtags = self._extract_hashtags(content)
       SocialMediaPost.post_id_counter += 1
       SocialMediaPost.total_posts += 1
   
   def add_like(self) -> str:
       """
       Add a like to the post.
       
       TODO: Implement this method
       - Increment likes_count
       - Return success message with new count
       """
       self.likes_count += 1
       return f"Post {self.post_id} by {self.author} now has {self.likes_count} likes."
   
   def remove_like(self) -> str:
       """
       Remove a like from the post.
       
       TODO: Implement this method
       - Decrement likes_count (minimum 0)
       - Return message with new count
       """
       self.likes_count = max(0, self.likes_count - 1)
       return f"Post {self.post_id} by {self.author} now has {self.likes_count} likes."
   
   def add_comment(self, commenter: str, comment_text: str) -> str:
       """
       Add a comment to the post.
       
       TODO: Implement this method
       - Validate commenter (non-empty string)
       - Validate comment_text (non-empty, max 100 chars)
       - Add to comments list in format "username: comment text"
       - Return success message
       """
       self.comments.append(f"{commenter}: {comment_text}")
       return f"Comment added by {commenter} on post {self.post_id}: '{comment_text}'"
   
   def edit_content(self, new_content: str) -> str:
       """
       Edit the post content.
       
       TODO: Implement this method
       - Validate new_content (same rules as __init__)
       - Update content
       - Re-extract hashtags
       - Return success message
       """
       if not new_content or len(new_content) > 280:
           raise ValueError("New content must be a non-empty string with max 280 characters.")
       self.content = new_content
       self.hashtags = self._extract_hashtags(new_content)
       return f"Post {self.post_id} content updated successfully."
   
   def _extract_hashtags(self, text: str) -> list[str]:
       """
       Private method to extract hashtags from text.
       
       TODO: Implement this method
       - Find all words starting with '#'
       - Return list of unique hashtags
       - Convert to lowercase for consistency
       - Remove duplicates
       
       Hint: Use string methods or regex to find hashtags
       """
       hashtags = set()
       words = text.split()
       for word in words:
           if word.startswith('#'):
               hashtags.add(word.lower())
       return list(hashtags)
   
   def make_private(self) -> str:
       """Make the post private."""
       self.is_public = False
       return f"Post {self.post_id} by {self.author} is now private."
   
   def make_public(self) -> str:
       """Make the post public."""
       self.is_public = True
       return f"Post {self.post_id} by {self.author} is now public."
   
   def get_post_summary(self) -> str:
       """
       Get comprehensive post information.
       
       TODO: Implement this method
       - Return multi-line formatted summary
       - Include all post details
       - Show recent comments (last 3)
       - Display hashtags
       """
       recent_comments = self.comments[-3:] if len(self.comments) > 3 else self.comments
       comments_str = "\n".join(recent_comments) if recent_comments else "No comments yet."
       hashtags_str = ", ".join(self.hashtags) if self.hashtags else "No hashtags."
       return (f"Post ID: {self.post_id} | Author: {self.author} | Timestamp: {self.timestamp}\n"
                f"Content: {self.content}\nLikes: {self.likes_count} | Public: {'Yes' if self.is_public else 'No'}\n"
                f"Hashtags: {hashtags_str}\nComments:\n{comments_str}")
   
   def __str__(self) -> str:
       """Human-readable representation."""
       return (f"Post ID: {self.post_id} | Author: {self.author} | Content: {self.content[:50]}... "
                f"| Likes: {self.likes_count} | Public: {'Yes' if self.is_public else 'No'}")
   
   def __repr__(self) -> str:
       """Developer representation."""
       return (f"SocialMediaPost(post_id={self.post_id}, author='{self.author}', "
                f"content='{self.content[:50]}...', timestamp='{self.timestamp}', "
                f"likes_count={self.likes_count}, is_public={self.is_public}, "
                f"hashtags={self.hashtags}, comments={self.comments})")


# Test cases for Problem 3
def test_social_media_post():
   """Test the SocialMediaPost class implementation."""
   print("\n=== Testing Problem 3: SocialMediaPost Class ===")
   
   try:
       # Create posts
       post1 = SocialMediaPost("alice_dev", "Learning #python and loving #coding! #webdev")
       post2 = SocialMediaPost("bob_designer", "Amazing #design inspiration today!")
       
       # Test likes
       print(post1.add_like())
       print(post1.add_like())
       print(post1.remove_like())
       
       # Test comments
       print(post1.add_comment("charlie", "Great post!"))
       print(post1.add_comment("diana", "Thanks for sharing!"))
       
       # Test content editing
       print(post1.edit_content("Updated: Learning #python and #django! #webdev #backend"))
       
       # Test privacy
       print(post2.make_private())
       
       # Show summaries
       print(post1.get_post_summary())
       print(f"Total posts on {SocialMediaPost.platform_name}: {SocialMediaPost.total_posts}")
       
   except Exception as e:
       print(f"Error testing SocialMediaPost class: {e}")

# Uncomment to test Problem 3
test_social_media_post()


# =============================================================================
# Challenge Problem: University Course Management
# =============================================================================

"""
Challenge Problem: Create a comprehensive Course class for university management.

This is an advanced problem that combines all concepts from this lesson.

Requirements:
1. Class Variables:
  - university_name = "Python University"
  - total_courses = 0
  - course_code_counter = 1000
  - valid_departments = ["CS", "EE", "MATH", "PHYS", "CHEM"]
  - semester_options = ["Fall", "Spring", "Summer"]

2. Instance Variables:
  - course_code (string): Auto-generated (e.g., "CS1001", "MATH1002")
  - title (string): Course title
  - department (string): Department code
  - credits (int): Number of credit hours
  - instructor (string): Instructor name
  - semester (string): Current semester
  - year (int): Academic year
  - max_capacity (int): Maximum students allowed
  - enrolled_students (list): list of enrolled student names
  - waitlist (list): list of waitlisted student names
  - prerequisites (list): list of prerequisite course codes

3. Advanced Methods:
  - __init__(): Initialize with full validation
  - enroll_student(student_name): Enroll if space available, otherwise waitlist
  - drop_student(student_name): Remove from enrolled or waitlist
  - add_prerequisite(course_code): Add prerequisite course
  - check_enrollment_status(student_name): Return enrollment status
  - get_available_spots(): Calculate remaining capacity
  - promote_from_waitlist(): Move first waitlisted student to enrolled
  - get_course_statistics(): Return detailed course stats
  - is_full(): Check if course is at capacity
  - get_class_roster(): Return formatted list of enrolled students
  - __str__(), __repr__(): Professional representations

4. Complex Business Logic:
  - Course codes format: DEPARTMENT + auto-incremented number
  - Students enroll if space available, otherwise go to waitlist
  - Dropping students should promote from waitlist automatically
  - Prerequisites should be stored and validated
  - Comprehensive error handling and validation

5. Input Validation:
  - All string inputs must be non-empty
  - Department must be in valid_departments
  - Credits must be 1-6 range
  - Semester must be in semester_options
  - Year must be reasonable (current year ± 2)
  - Max capacity must be positive
  - Student names must be unique (no duplicates)

Expected Advanced Features:
- Automatic waitlist management
- Smart course code generation
- Comprehensive statistics reporting
- Professional string representations
- Robust error handling
"""

class Course:
   university_name = "Python University"
   total_courses = 0
   course_code_counter = 1000
   valid_departments = ["CS", "EE", "MATH", "PHYS", "CHEM"]
   semester_options = ["Fall", "Spring", "Summer"]
   
   def __init__(self, title: str, department: str, credits: int, 
                instructor: str, semester: str, year: int, max_capacity: int):
       """
       Initialize a comprehensive university course.
       
       This is the most complex constructor in our exercises.
       TODO: Implement with full validation and setup
       """
       if not title or not isinstance(title, str):
           raise ValueError("Title must be a non-empty string.")
       if department not in Course.valid_departments:
           raise ValueError(f"Department must be one of {Course.valid_departments}.")
       if not isinstance(credits, int) or not (1 <= credits <= 6):
           raise ValueError("Credits must be an integer between 1 and 6.")
       if instructor and not isinstance(instructor, str):
           raise ValueError("Instructor must be a non-empty string.")
       if semester not in Course.semester_options:
           raise ValueError(f"Semester must be one of {Course.semester_options}.")
       if not isinstance(year, int) or not (datetime.now().year - 2 <= year <= datetime.now().year + 2):
           raise ValueError("Year must be within 2 years of the current year.")
       if not isinstance(max_capacity, int) or max_capacity <= 0:
           raise ValueError("Max capacity must be a positive integer.")
       self.title = title
       self.department = department
       self.credits = credits
       self.instructor = instructor
       self.semester = semester
       self.year = year
       self.max_capacity = max_capacity
       self.course_code = f"{department}{Course.course_code_counter}"
       self.enrolled_students = []
       self.waitlist = []
       self.prerequisites = []
       Course.total_courses += 1
       Course.course_code_counter += 1
   
   def enroll_student(self, student_name: str) -> str:
       """
       Enroll student or add to waitlist.
       
       TODO: Complex enrollment logic
       - Check if student already enrolled/waitlisted
       - Add to enrolled if space available
       - Add to waitlist if course is full
       - Return appropriate message
       """
       # Your implementation here
       pass
   
   def drop_student(self, student_name: str) -> str:
       """
       Drop student and manage waitlist.
       
       TODO: Complex drop logic
       - Remove from enrolled or waitlist
       - If removed from enrolled, promote from waitlist
       - Return appropriate message
       """
       # Your implementation here
       pass
   
   def add_prerequisite(self, course_code: str) -> str:
       """Add a prerequisite course."""
       # Your implementation here
       pass
   
   def check_enrollment_status(self, student_name: str) -> str:
       """Check if student is enrolled, waitlisted, or not registered."""
       # Your implementation here
       pass
   
   def get_available_spots(self) -> int:
       """Calculate remaining capacity."""
       # Your implementation here
       pass
   
   def promote_from_waitlist(self) -> Optional[str]:
       """Move first waitlisted student to enrolled."""
       # Your implementation here
       pass
   
   def get_course_statistics(self) -> str:
       """Return comprehensive course statistics."""
       # Your implementation here
       pass
   
   def is_full(self) -> bool:
       """Check if course is at maximum capacity."""
       # Your implementation here
       pass
   
   def get_class_roster(self) -> str:
       """Return formatted list of enrolled students."""
       # Your implementation here
       pass
   
   def __str__(self) -> str:
       """Professional human-readable representation."""
       # Your implementation here
       pass
   
   def __repr__(self) -> str:
       """Complete developer representation."""
       # Your implementation here
       pass


# Test cases for Challenge Problem
def test_course_class():
   """Test the advanced Course class implementation."""
   print("\n=== Testing Challenge Problem: Course Class ===")
   
   try:
       # Create courses
       course1 = Course("Introduction to Python", "CS", 3, "Dr. Smith", "Fall", 2024, 25)
       course2 = Course("Calculus I", "MATH", 4, "Prof. Johnson", "Spring", 2024, 30)
       
       # Test enrollments
       students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
       for student in students:
           print(course1.enroll_student(student))
       
       # Test waitlist and capacity
       print(f"Available spots: {course1.get_available_spots()}")
       print(course1.enroll_student("Frank"))  # Should go to waitlist if full
       
       # Test dropping and promotion
       print(course1.drop_student("Alice"))  # Should promote from waitlist
       
       # Test statistics
       print(course1.get_course_statistics())
       print(course1.get_class_roster())
       
       print(f"Total courses: {Course.total_courses}")
       
   except Exception as e:
       print(f"Error testing Course class: {e}")

# Uncomment to test Challenge Problem
# test_course_class()


# =============================================================================
# Main Execution
# =============================================================================

if __name__ == "__main__":
   """
   Main execution block for testing all problems.
   
   Uncomment the test functions you want to run:
   """
   
   print("🎓 Classes and Objects - Practice Problems")
   print("=" * 50)
   
   # Uncomment to test specific problems:
   # test_book_class()           # Problem 1
   # test_employee_class()       # Problem 2  
   # test_social_media_post()    # Problem 3
   # test_course_class()         # Challenge Problem
   
   # Or run all tests:
   print("To run tests, uncomment the test function calls in the main block!")
   print("\nAvailable tests:")
   print("- test_book_class()           # Library Management")
   print("- test_employee_class()       # Employee Management") 
   print("- test_social_media_post()    # Social Media Platform")
   print("- test_course_class()         # University Course System (Challenge)")
   
   print(f"\n📚 Ready to practice? Start with Problem 1!")
   print("💡 Remember: Focus on understanding WHY we use each concept!")