# Classes and Objects

## 🎯 Learning Objectives
By the end of this lesson, you will understand:
- What classes and objects are and why we need them
- The difference between instance and class variables
- Python's special methods (`__init__`, `__str__`, etc.)
- Memory allocation concepts in OOP
- How to design classes for real-world problems

## 📖 Core Concepts

### What is Object-Oriented Programming (OOP)?
**Definition**: A programming paradigm that organizes code around objects and classes rather than functions and logic.

**Why OOP?**
- 🔄 **Reusability**: Write once, use many times
- 🛡️ **Maintainability**: Easier to modify and debug
- 📦 **Modularity**: Break complex problems into smaller parts
- 🎭 **Abstraction**: Hide complexity, show only what's necessary
- 🏗️ **Scalability**: Build large applications systematically

### What is a Class?
**Definition**: A blueprint or template that defines the structure and behavior of objects.

**Why Classes?**
- **Code Organization**: Group related data and functions together
- **Code Reuse**: Create multiple objects from the same template
- **Consistency**: Ensure all objects of the same type behave similarly

**Real-World Analogy**: 
- Class = House Blueprint 📋
- Object = Actual House 🏠

### What is an Object?
**Definition**: An instance of a class - a concrete entity created from the class template.

**Why Objects?**
- **Data Encapsulation**: Keep related data together
- **State Management**: Each object maintains its own state
- **Behavior Implementation**: Objects can perform actions

**Key Terms**:
- **Instance**: Another name for object
- **Instantiation**: The process of creating an object from a class

### Instance Variables vs Class Variables

| Aspect | Instance Variables | Class Variables |
|--------|-------------------|-----------------|
| **What** | Variables unique to each object | Variables shared by all objects |
| **Why** | Store object-specific data | Store data common to all instances |
| **Memory** | Each object has its own copy | Single copy shared by all objects |
| **Access** | `self.variable_name` | `ClassName.variable_name` |
| **Example** | Each person's name | All humans have 2 eyes |

### Python Special Methods (Dunder Methods)

#### `__init__` Method (Constructor)
**What**: Special method that initializes a new object when it's created
**Why**: Set up initial state and perform setup operations
**When**: Called automatically when you create an object

```python
def __init__(self, parameter1, parameter2):
    """
    Constructor method - the 'birth certificate' of an object
    - Runs automatically when object is created
    - Sets up the object's initial state
    - 'self' refers to the current instance being created
    """
```

#### `self` Parameter
**What**: Reference to the current instance of the class
**Why**: Python needs to know which object you're working with
**How**: Always the first parameter in instance methods

#### `__str__` Method (String Representation)
**What**: Defines how the object appears when printed
**Why**: Make objects human-readable for debugging
**When**: Called by `print()` and `str()` functions

#### `__repr__` Method (Developer Representation)
**What**: Defines unambiguous string representation for developers
**Why**: Helpful for debugging and development
**When**: Called by `repr()` function and in interactive shells

## 💻 Code Examples

### Basic Class Structure

```python
class Person:
    """
    A basic Person class demonstrating fundamental OOP concepts.
    
    This class shows:
    - Class definition
    - Constructor (__init__)
    - Instance variables
    - Instance methods
    - String representation
    """
    
    # Class variable - shared by all Person objects
    species = "Homo sapiens"  # All humans belong to same species
    population = 0            # Track total number of Person objects
    
    def __init__(self, name, age, email):
        """
        Constructor method - initializes a new Person object.
        
        Parameters:
        - name (str): Person's full name
        - age (int): Person's age in years
        - email (str): Person's email address
        
        This method:
        1. Sets up instance variables (unique to this person)
        2. Updates the class variable (affects all persons)
        """
        # Instance variables - unique to each person
        self.name = name        # THIS person's name
        self.age = age         # THIS person's age
        self.email = email     # THIS person's email
        self.is_active = True  # All persons start as active
        
        # Update class variable - increment total population
        Person.population += 1
    
    def introduce(self):
        """
        Instance method - makes this person introduce themselves.
        
        Returns:
        str: Formatted introduction message
        """
        return f"Hi! I'm {self.name}, {self.age} years old. Email: {self.email}"
    
    def have_birthday(self):
        """
        Instance method - increases this person's age by 1.
        
        Returns:
        str: Birthday message
        """
        self.age += 1
        return f"🎉 {self.name} is now {self.age} years old!"
    
    def deactivate(self):
        """
        Instance method - marks this person as inactive.
        """
        self.is_active = False
        return f"{self.name} has been deactivated."
    
    def __str__(self):
        """
        String representation method - for human-readable output.
        Called when using print() or str() on the object.
        """
        status = "Active" if self.is_active else "Inactive"
        return f"Person(name='{self.name}', age={self.age}, status={status})"
    
    def __repr__(self):
        """
        Official representation method - for developer debugging.
        Should be unambiguous and ideally recreate the object.
        """
        return f"Person('{self.name}', {self.age}, '{self.email}')"
    
    @classmethod
    def get_population(cls):
        """
        Class method - operates on the class itself, not instances.
        
        Why use @classmethod?
        - Access class variables
        - Alternative constructors
        - Utility methods related to the class
        
        Returns:
        int: Total number of Person objects created
        """
        return cls.population
    
    @staticmethod
    def is_adult(age):
        """
        Static method - doesn't need class or instance.
        
        Why use @staticmethod?
        - Utility functions related to the class
        - No access to self or cls needed
        - Logically belongs to the class
        
        Parameters:
        age (int): Age to check
        
        Returns:
        bool: True if age >= 18, False otherwise
        """
        return age >= 18

# Demonstration of concepts
print("=== Creating Person Objects ===")
person1 = Person("Alice Johnson", 25, "alice@email.com")
person2 = Person("Bob Smith", 17, "bob@email.com")
person3 = Person("Carol Davis", 30, "carol@email.com")

print("=== Object Information ===")
print(person1)  # Calls __str__ method
print(repr(person2))  # Calls __repr__ method

print("=== Instance Methods ===")
print(person1.introduce())
print(person1.have_birthday())
print(person2.deactivate())

print("=== Class and Static Methods ===")
print(f"Total population: {Person.get_population()}")
print(f"Is Alice an adult? {Person.is_adult(person1.age)}")
print(f"Is Bob an adult? {Person.is_adult(person2.age)}")

print("=== Class vs Instance Variables ===")
print(f"Alice's species: {person1.species}")
print(f"Bob's species: {person2.species}")
print(f"Human species: {Person.species}")
```

### Advanced Example: Bank Account System

```python
from datetime import datetime
from typing import List, Optional

class BankAccount:
    """
    Advanced BankAccount class demonstrating:
    - Complex instance variables
    - Input validation
    - Error handling
    - Documentation best practices
    - Type hints (modern Python)
    """
    
    # Class variables
    bank_name: str = "Python National Bank"
    interest_rate: float = 0.02  # 2% annual interest
    account_counter: int = 1000  # Starting account number
    
    def __init__(self, account_holder: str, initial_balance: float = 0.0, account_type: str = "checking"):
        """
        Initialize a new bank account.
        
        Parameters:
        account_holder (str): Name of the account owner
        initial_balance (float): Starting balance (default: 0.0)
        account_type (str): Type of account (default: "checking")
        
        Raises:
        ValueError: If initial_balance is negative
        TypeError: If account_holder is not a string
        """
        # Input validation
        if not isinstance(account_holder, str) or not account_holder.strip():
            raise TypeError("Account holder must be a non-empty string")
        
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        if account_type not in ["checking", "savings", "business"]:
            raise ValueError("Account type must be 'checking', 'savings', or 'business'")
        
        # Instance variables
        self.account_holder: str = account_holder.strip()
        self.balance: float = initial_balance
        self.account_type: str = account_type
        self.account_number: int = BankAccount.account_counter
        self.created_date: str = datetime.now().strftime("%Y-%m-%d")
        self.is_active: bool = True
        self.transaction_history: List[str] = []
        
        # Update class variable
        BankAccount.account_counter += 1
        
        # Log initial transaction
        if initial_balance > 0:
            self._log_transaction(f"Account opened with initial deposit of ${initial_balance:.2f}")
        else:
            self._log_transaction("Account opened with zero balance")
    
    def deposit(self, amount: float) -> str:
        """
        Deposit money into the account.
        
        Parameters:
        amount (float): Amount to deposit
        
        Returns:
        str: Success message with new balance
        
        Raises:
        ValueError: If amount is not positive
        RuntimeError: If account is inactive
        """
        if not self.is_active:
            raise RuntimeError("Cannot deposit to inactive account")
        
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        self._log_transaction(f"Deposited ${amount:.2f}")
        return f"✅ Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
    
    def withdraw(self, amount: float) -> str:
        """
        Withdraw money from the account.
        
        Parameters:
        amount (float): Amount to withdraw
        
        Returns:
        str: Success message with new balance
        
        Raises:
        ValueError: If amount is invalid
        RuntimeError: If insufficient funds or account inactive
        """
        if not self.is_active:
            raise RuntimeError("Cannot withdraw from inactive account")
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            raise RuntimeError(f"Insufficient funds. Balance: ${self.balance:.2f}")
        
        self.balance -= amount
        self._log_transaction(f"Withdrew ${amount:.2f}")
        return f"✅ Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
    
    def get_balance(self) -> float:
        """
        Get current account balance.
        
        Returns:
        float: Current balance
        """
        return self.balance
    
    def _log_transaction(self, description: str) -> None:
        """
        Private method to log transactions.
        
        Why private (underscore prefix)?
        - Internal implementation detail
        - Should not be called directly by external code
        - Can change without affecting public interface
        
        Parameters:
        description (str): Transaction description
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_history.append(f"[{timestamp}] {description}")
    
    def get_transaction_history(self) -> List[str]:
        """
        Get complete transaction history.
        
        Returns:
        List[str]: List of transaction records
        """
        return self.transaction_history.copy()  # Return copy to prevent external modification
    
    def close_account(self) -> str:
        """
        Close the account (deactivate).
        
        Returns:
        str: Confirmation message
        """
        self.is_active = False
        self._log_transaction("Account closed")
        return f"Account #{self.account_number} has been closed."
    
    def __str__(self) -> str:
        """Human-readable string representation."""
        status = "Active" if self.is_active else "Closed"
        return (f"BankAccount(#{self.account_number}: {self.account_holder}, "
                f"Balance: ${self.balance:.2f}, Status: {status})")
    
    def __repr__(self) -> str:
        """Developer string representation."""
        return (f"BankAccount('{self.account_holder}', {self.balance}, "
                f"'{self.account_type}')")
    
    def __eq__(self, other) -> bool:
        """
        Check equality between two accounts.
        
        Why implement __eq__?
        - Compare objects meaningfully
        - Use objects in sets and as dictionary keys
        - Enable proper testing
        """
        if not isinstance(other, BankAccount):
            return False
        return self.account_number == other.account_number

# Demonstration of advanced concepts
print("=== Advanced Bank Account Demo ===")

try:
    # Create accounts
    account1 = BankAccount("Alice Johnson", 1000.0, "checking")
    account2 = BankAccount("Bob Smith", 500.0, "savings")
    
    # Demonstrate operations
    print(account1.deposit(200.0))
    print(account1.withdraw(150.0))
    
    # Show account info
    print(account1)
    print(f"Account balance: ${account1.get_balance():.2f}")
    
    # Show transaction history
    print("\nTransaction History:")
    for transaction in account1.get_transaction_history():
        print(f"  {transaction}")
    
    # Demonstrate error handling
    try:
        account1.withdraw(2000.0)  # Should raise error
    except RuntimeError as e:
        print(f"Error: {e}")
    
except (ValueError, TypeError, RuntimeError) as e:
    print(f"Account creation failed: {e}")
```

## 🔍 Memory Concepts Explained

### Object Memory Allocation

```python
class MemoryDemo:
    class_var = "Shared by all"
    
    def __init__(self, instance_data):
        self.instance_var = instance_data

# Create objects
obj1 = MemoryDemo("Object 1 data")
obj2 = MemoryDemo("Object 2 data")

print("=== Memory Addresses ===")
print(f"obj1 memory location: {id(obj1)}")              # Different
print(f"obj2 memory location: {id(obj2)}")              # Different

print(f"obj1.instance_var location: {id(obj1.instance_var)}")  # Different
print(f"obj2.instance_var location: {id(obj2.instance_var)}")  # Different

print(f"obj1.class_var location: {id(obj1.class_var)}")        # Same
print(f"obj2.class_var location: {id(obj2.class_var)}")        # Same
print(f"MemoryDemo.class_var location: {id(MemoryDemo.class_var)}")  # Same
```

**Key Memory Concepts**:
- **Instance Variables**: Each object gets its own memory space
- **Class Variables**: All objects share the same memory location
- **Object Identity**: Each object has a unique memory address (`id()`)

## 🎯 Real-World Applications

### 1. **User Management System**
```python
class User:
    total_users = 0
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = True
        self.created_at = datetime.now()
        User.total_users += 1
```

### 2. **E-commerce Product Catalog**
```python
class Product:
    def __init__(self, name, price, category, stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
        self.reviews = []
```

### 3. **File Management System**
```python
class File:
    def __init__(self, filename, size, file_type):
        self.filename = filename
        self.size = size
        self.file_type = file_type
        self.created_at = datetime.now()
        self.is_deleted = False
```

## 💡 Best Practices

1. **Naming Conventions**:
   - Classes: `PascalCase` (e.g., `BankAccount`)
   - Variables/Methods: `snake_case` (e.g., `account_number`)
   - Constants: `UPPER_CASE` (e.g., `MAX_BALANCE`)

2. **Documentation**:
   - Always include class docstrings
   - Document method parameters and return values
   - Use type hints for better code clarity

3. **Initialization**:
   - Validate input parameters in `__init__`
   - Set sensible default values
   - Initialize all instance variables

4. **Method Design**:
   - Keep methods focused on single responsibility
   - Use descriptive method names
   - Handle edge cases and errors

## 🔗 Connection to System Design

Classes and objects are fundamental building blocks for:
- **Microservices**: Each service as a class with specific responsibilities
- **API Design**: Resources modeled as classes
- **Database Design**: Tables mapped to classes (ORM)
- **Caching Systems**: Cache entries as objects
- **Message Queues**: Messages as objects with metadata

## 📝 Key Takeaways

1. **Classes are templates**, objects are instances created from those templates
2. **`__init__` initializes objects** when they're created
3. **`self` refers to the current instance** in methods
4. **Instance variables are unique** to each object
5. **Class variables are shared** among all instances
6. **Special methods** (`__str__`, `__repr__`) make objects more usable
7. **Proper error handling** makes classes robust and reliable
8. **Documentation and type hints** make code maintainable

---
**Next**: [Encapsulation - Data Hiding and Access Control](../02-encapsulation/)
**Practice**: Complete the exercises in `practice-problems.py`