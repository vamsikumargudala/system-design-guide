# 02. Encapsulation in Object-Oriented Programming

## Table of Contents
1. [What is Encapsulation?](#what-is-encapsulation)
2. [Why Do We Need Encapsulation?](#why-do-we-need-encapsulation)
3. [Access Modifiers in Python](#access-modifiers-in-python)
4. [Implementing Encapsulation](#implementing-encapsulation)
5. [Getters and Setters](#getters-and-setters)
6. [Python Properties (@property)](#python-properties-property)
7. [Real-World Examples](#real-world-examples)
8. [Benefits of Encapsulation](#benefits-of-encapsulation)
9. [Best Practices](#best-practices)
10. [Common Mistakes](#common-mistakes)
11. [Practice Problems](#practice-problems)

## What is Encapsulation?

**Encapsulation** is one of the four fundamental principles of Object-Oriented Programming (OOP). It refers to:

1. **Bundling data and methods** that operate on that data into a single unit (class)
2. **Restricting direct access** to some of an object's components (data hiding)
3. **Providing controlled access** through public methods

### Real-World Analogy
Think of a **car**:
- The engine, transmission, and other internal components are hidden under the hood
- You interact with the car through a controlled interface: steering wheel, pedals, gear shift
- You don't need to know how the engine works to drive the car
- The manufacturer can change the internal engine design without changing how you drive

Similarly, encapsulation protects your object's internal data and provides a controlled interface for interaction.

### Key Concepts
```python
# Encapsulation combines:
# 1. Data (attributes)
# 2. Methods that operate on that data
# 3. Access control (who can use what)

class BankAccount:
    def __init__(self, account_number, initial_balance):
        # Public attribute (accessible from outside)
        self.account_number = account_number
        
        # Private attribute (internal use only)
        self.__balance = initial_balance
        self.__transaction_history = []
    
    # Public method (controlled interface)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__add_transaction(f"Deposited ${amount}")
            return True
        return False
    
    # Private method (internal implementation)
    def __add_transaction(self, description):
        self.__transaction_history.append(description)
```

## Why Do We Need Encapsulation?

### 1. **Data Protection and Integrity**
```python
# WITHOUT encapsulation - Direct access (PROBLEMATIC)
class BankAccountBad:
    def __init__(self, balance):
        self.balance = balance  # Anyone can modify this directly!

# Problems that can occur:
account = BankAccountBad(1000)
account.balance = -5000      # Negative balance allowed!
account.balance = "invalid"  # Wrong data type allowed!
account.balance = None       # Null values allowed!
```

```python
# WITH encapsulation - Controlled access (SECURE)
class BankAccountGood:
    def __init__(self, initial_balance):
        self.__balance = 0  # Private attribute
        if self.__is_valid_amount(initial_balance):
            self.__balance = initial_balance
    
    def __is_valid_amount(self, amount):
        return isinstance(amount, (int, float)) and amount >= 0
    
    def deposit(self, amount):
        if self.__is_valid_amount(amount):
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid deposit amount"
    
    def get_balance(self):
        return self.__balance
    
    # Controlled withdrawal with business logic
    def withdraw(self, amount):
        if not self.__is_valid_amount(amount):
            return "Invalid withdrawal amount"
        
        if amount > self.__balance:
            return "Insufficient funds"
        
        self.__balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.__balance}"

# Now the data is protected
account = BankAccountGood(1000)
print(account.deposit(500))     # Works: Deposited $500. New balance: $1500
print(account.withdraw(200))    # Works: Withdrew $200. New balance: $1300
print(account.withdraw(2000))   # Protected: Insufficient funds

# Direct access is prevented
# account.__balance = -1000     # Won't work - attribute is private
```

### 2. **Maintainability and Evolution**
```python
# Internal implementation can change without affecting external code
class Student:
    def __init__(self, name):
        self.name = name
        # Initially store grades as a simple list
        self.__grades = []
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
    
    def get_average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)

# Later, we can change internal implementation without breaking existing code
class StudentImproved:
    def __init__(self, name):
        self.name = name
        # Changed to dictionary for more detailed tracking
        self.__grades = {}  # {subject: [grades]}
        self.__weighted_grades = {}  # {subject: weight}
    
    def add_grade(self, grade, subject="General", weight=1.0):
        if 0 <= grade <= 100:
            if subject not in self.__grades:
                self.__grades[subject] = []
                self.__weighted_grades[subject] = weight
            self.__grades[subject].append(grade)
    
    def get_average(self):
        # More complex calculation, but same interface
        if not self.__grades:
            return 0
        
        total_weighted_score = 0
        total_weight = 0
        
        for subject, grades in self.__grades.items():
            subject_avg = sum(grades) / len(grades)
            weight = self.__weighted_grades[subject]
            total_weighted_score += subject_avg * weight
            total_weight += weight
        
        return total_weighted_score / total_weight if total_weight > 0 else 0

# External code using the class doesn't need to change
student = StudentImproved("Alice")
student.add_grade(95)
student.add_grade(87)
print(f"Average: {student.get_average()}")  # Still works the same way
```

## Access Modifiers in Python

Python uses naming conventions to indicate the intended access level of attributes and methods:

### 1. **Public** (No prefix)
- Accessible from anywhere
- Part of the class's public interface
- Standard way to expose functionality

```python
class Car:
    def __init__(self, brand, model):
        # Public attributes
        self.brand = brand      # Anyone can access and modify
        self.model = model      # Part of public interface
        self.year = 2024        # Default value, publicly accessible
    
    # Public methods
    def start_engine(self):     # Anyone can call this
        return f"{self.brand} {self.model} engine started!"
    
    def get_info(self):         # Public interface method
        return f"{self.year} {self.brand} {self.model}"

# Usage - Direct access is expected and allowed
car = Car("Toyota", "Camry")
print(car.brand)            # Toyota - Direct access OK
car.year = 2025             # Direct modification OK
print(car.start_engine())   # Toyota Camry engine started!
print(car.get_info())       # 2025 Toyota Camry
```

### 2. **Protected** (Single underscore `_`)
- Intended for internal use within the class and its subclasses
- Convention: "Internal implementation, use at your own risk"
- Still accessible from outside, but discouraged

```python
class Vehicle:
    def __init__(self, vin_number):
        # Public attribute
        self.brand = "Generic"
        
        # Protected attributes (for internal/subclass use)
        self._vin_number = vin_number       # Internal identifier
        self._maintenance_log = []          # Internal tracking
        self._engine_hours = 0              # Internal metrics
    
    # Protected methods (for internal/subclass use)
    def _log_maintenance(self, action):
        """Internal method to log maintenance actions."""
        self._maintenance_log.append({
            'action': action,
            'engine_hours': self._engine_hours,
            'timestamp': 'current_time'  # Simplified
        })
    
    def _update_engine_hours(self, hours):
        """Internal method to update engine hours."""
        if hours > 0:
            self._engine_hours += hours
    
    # Public interface that uses protected methods
    def drive(self, hours):
        """Public method using internal protected methods."""
        if hours > 0:
            self._update_engine_hours(hours)
            print(f"Drove for {hours} hours. Total engine hours: {self._engine_hours}")
    
    def service(self, service_type):
        """Public method using internal protected methods."""
        self._log_maintenance(service_type)
        print(f"Service completed: {service_type}")
        print(f"Total maintenance records: {len(self._maintenance_log)}")

class Car(Vehicle):  # Subclass can access protected members
    def __init__(self, vin_number, model):
        super().__init__(vin_number)
        self.model = model
    
    def get_diagnostic_info(self):
        """Subclass accessing protected attributes."""
        return {
            'vin': self._vin_number,           # OK - subclass access
            'engine_hours': self._engine_hours, # OK - subclass access
            'maintenance_count': len(self._maintenance_log)  # OK
        }
    
    def reset_engine_hours(self):
        """Subclass using protected method."""
        self._log_maintenance("Engine hour reset")  # OK - protected method
        self._engine_hours = 0  # OK - direct protected access

# Usage
car = Car("1HGCM82633A123456", "Honda Civic")
car.drive(5)        # Public method
car.service("Oil change")  # Public method

# Protected access (discouraged but possible)
print(f"VIN: {car._vin_number}")  # Works, but not recommended
diagnostic = car.get_diagnostic_info()  # Proper way through public interface
print(diagnostic)
```

### 3. **Private** (Double underscore `__`)
- Name mangling - Python changes the name internally
- Strongest form of encapsulation in Python
- Cannot be accessed directly from outside the class

```python
class SecureBankAccount:
    def __init__(self, account_number, pin, initial_balance):
        # Public attributes
        self.account_holder = "Anonymous"
        self.account_type = "Checking"
        
        # Protected attributes (internal use)
        self._account_number = account_number
        self._created_date = "2024-01-01"  # Simplified
        
        # Private attributes (heavily protected)
        self.__pin = pin                    # PIN should never be directly accessible
        self.__balance = initial_balance    # Balance requires validation
        self.__transaction_log = []         # Internal security logging
        self.__failed_attempts = 0          # Security tracking
        self.__is_locked = False            # Account lock status
    
    # Private methods (internal implementation only)
    def __validate_pin(self, entered_pin):
        """Private method to validate PIN."""
        if self.__is_locked:
            return False, "Account is locked"
        
        if entered_pin == self.__pin:
            self.__failed_attempts = 0  # Reset on success
            return True, "PIN validated"
        else:
            self.__failed_attempts += 1
            if self.__failed_attempts >= 3:
                self.__is_locked = True
                self.__log_security_event("Account locked due to failed PIN attempts")
                return False, "Account locked due to multiple failed attempts"
            return False, f"Invalid PIN. {3 - self.__failed_attempts} attempts remaining"
    
    def __log_security_event(self, event):
        """Private method for security logging."""
        self.__transaction_log.append({
            'type': 'SECURITY',
            'event': event,
            'timestamp': 'current_time',  # Simplified
            'balance_after': self.__balance
        })
    
    def __log_transaction(self, transaction_type, amount):
        """Private method for transaction logging."""
        self.__transaction_log.append({
            'type': transaction_type,
            'amount': amount,
            'timestamp': 'current_time',  # Simplified
            'balance_after': self.__balance
        })
    
    # Public interface methods
    def check_balance(self, pin):
        """Public method to check balance with PIN validation."""
        is_valid, message = self.__validate_pin(pin)
        if is_valid:
            return f"Current balance: ${self.__balance}"
        return message
    
    def deposit(self, amount, pin):
        """Public method to deposit money."""
        is_valid, message = self.__validate_pin(pin)
        if not is_valid:
            return message
        
        if amount <= 0:
            return "Deposit amount must be positive"
        
        self.__balance += amount
        self.__log_transaction("DEPOSIT", amount)
        return f"Deposited ${amount}. New balance: ${self.__balance}"
    
    def withdraw(self, amount, pin):
        """Public method to withdraw money."""
        is_valid, message = self.__validate_pin(pin)
        if not is_valid:
            return message
        
        if amount <= 0:
            return "Withdrawal amount must be positive"
        
        if amount > self.__balance:
            return "Insufficient funds"
        
        self.__balance -= amount
        self.__log_transaction("WITHDRAWAL", amount)
        return f"Withdrew ${amount}. New balance: ${self.__balance}"
    
    def change_pin(self, old_pin, new_pin):
        """Public method to change PIN."""
        is_valid, message = self.__validate_pin(old_pin)
        if not is_valid:
            return message
        
        if len(str(new_pin)) != 4:
            return "PIN must be 4 digits"
        
        self.__pin = new_pin
        self.__log_security_event("PIN changed")
        return "PIN changed successfully"
    
    def unlock_account(self, master_key):
        """Public method to unlock account (admin function)."""
        if master_key == "MASTER_2024":  # Simplified master key
            self.__is_locked = False
            self.__failed_attempts = 0
            self.__log_security_event("Account unlocked by administrator")
            return "Account unlocked successfully"
        return "Invalid master key"
    
    def get_account_status(self):
        """Public method to get account status."""
        return {
            'account_number': self._account_number,
            'account_holder': self.account_holder,
            'account_type': self.account_type,
            'is_locked': self.__is_locked,
            'failed_attempts': self.__failed_attempts
        }

# Usage examples
account = SecureBankAccount("ACC12345", 1234, 1000)

# Public interface works
print(account.check_balance(1234))      # Current balance: $1000
print(account.deposit(500, 1234))       # Deposited $500. New balance: $1500
print(account.withdraw(200, 1234))      # Withdrew $200. New balance: $1300

# PIN protection works
print(account.withdraw(100, 9999))      # Invalid PIN. 2 attempts remaining
print(account.withdraw(100, 8888))      # Invalid PIN. 1 attempts remaining
print(account.withdraw(100, 7777))      # Account locked due to multiple failed attempts

# Private attributes cannot be accessed directly
# print(account.__pin)          # AttributeError: 'SecureBankAccount' object has no attribute '__pin'
# print(account.__balance)      # AttributeError: 'SecureBankAccount' object has no attribute '__balance'

# Even with name mangling, they're still not easily accessible
# print(account._SecureBankAccount__pin)  # Would work but violates encapsulation

# Protected attributes can be accessed (but shouldn't be)
print(f"Account Number: {account._account_number}")  # Works but discouraged

# Public attributes can be freely accessed
account.account_holder = "John Doe"
print(f"Account Holder: {account.account_holder}")

# Account unlock demo
print(account.unlock_account("MASTER_2024"))  # Account unlocked successfully
print(account.check_balance(1234))            # Now works again
```

### Access Levels Summary Table

| Access Level | Naming | External Access | Subclass Access | Intended Use |
|--------------|--------|----------------|-----------------|--------------|
| **Public** | `attribute` | ✅ Direct | ✅ Direct | Public API/Interface |
| **Protected** | `_attribute` | ⚠️ Discouraged | ✅ Direct | Internal/Subclass use |
| **Private** | `__attribute` | ❌ Name mangled | ❌ Name mangled | Internal implementation only |

## Implementing Encapsulation

Let's look at a comprehensive example that demonstrates proper encapsulation implementation:

### Complete Example: Smart Home Device

```python
import datetime
from typing import List, Dict, Any

class SmartDevice:
    """Base class for smart home devices demonstrating encapsulation principles."""
    
    def __init__(self, device_id: str, device_name: str):
        # Public attributes (part of the device interface)
        self.device_id = device_id
        self.device_name = device_name
        self.manufacturer = "SmartHome Inc."
        
        # Protected attributes (for subclass use)
        self._firmware_version = "1.0.0"
        self._last_update = datetime.datetime.now()
        self._status_log = []
        
        # Private attributes (internal implementation)
        self.__is_online = True
        self.__power_consumption = 0.0  # watts
        self.__error_count = 0
        self.__security_token = self.__generate_token()
    
    # Private methods (internal implementation)
    def __generate_token(self) -> str:
        """Generate security token for device authentication."""
        import hashlib
        raw_token = f"{self.device_id}_{self.device_name}_{datetime.datetime.now()}"
        return hashlib.md5(raw_token.encode()).hexdigest()[:16]
    
    def __log_status_change(self, status: str, details: str = ""):
        """Internal method to log status changes."""
        log_entry = {
            'timestamp': datetime.datetime.now(),
            'status': status,
            'details': details,
            'error_count': self.__error_count
        }
        self._status_log.append(log_entry)
        
        # Keep only last 100 log entries to manage memory
        if len(self._status_log) > 100:
            self._status_log = self._status_log[-100:]
    
    def __validate_security_token(self, token: str) -> bool:
        """Validate security token for sensitive operations."""
        return token == self.__security_token
    
    # Protected methods (for subclass use)
    def _update_power_consumption(self, watts: float):
        """Update power consumption - for subclass use."""
        if watts >= 0:
            self.__power_consumption = watts
            self.__log_status_change("POWER_UPDATE", f"Power: {watts}W")
    
    def _report_error(self, error_message: str):
        """Report error - for subclass use."""
        self.__error_count += 1
        self.__log_status_change("ERROR", error_message)
        
        if self.__error_count >= 5:
            self.__is_online = False
            self.__log_status_change("OFFLINE", "Too many errors")
    
    def _reset_error_count(self):
        """Reset error count - for subclass use."""
        self.__error_count = 0
        if not self.__is_online:
            self.__is_online = True
            self.__log_status_change("ONLINE", "Errors cleared")
    
    # Public interface methods
    def get_device_info(self) -> Dict[str, Any]:
        """Get basic device information."""
        return {
            'id': self.device_id,
            'name': self.device_name,
            'manufacturer': self.manufacturer,
            'firmware': self._firmware_version,
            'online': self.__is_online,
            'power_consumption': self.__power_consumption,
            'error_count': self.__error_count
        }
    
    def is_online(self) -> bool:
        """Check if device is online."""
        return self.__is_online
    
    def get_power_consumption(self) -> float:
        """Get current power consumption."""
        return self.__power_consumption
    
    def restart_device(self, security_token: str) -> str:
        """Restart device (requires security token)."""
        if not self.__validate_security_token(security_token):
            return "Invalid security token"
        
        self._reset_error_count()
        self.__log_status_change("RESTART", "Device restarted")
        return "Device restarted successfully"
    
    def get_security_token(self) -> str:
        """Get security token for privileged operations."""
        return self.__security_token
    
    def get_status_summary(self) -> str:
        """Get a summary of device status."""
        status = "Online" if self.__is_online else "Offline"
        return f"{self.device_name} ({self.device_id}): {status}, Power: {self.__power_consumption}W, Errors: {self.__error_count}"

# Specific device implementation using encapsulation
class SmartLight(SmartDevice):
    """Smart light implementation demonstrating inheritance with encapsulation."""
    
    def __init__(self, device_id: str, device_name: str):
        super().__init__(device_id, device_name)
        
        # Public attributes specific to lights
        self.light_type = "LED"
        self.max_brightness = 100
        
        # Protected attributes for subclass use
        self._color_temperature_range = (2700, 6500)  # Kelvin
        self._brightness_step = 5
        
        # Private attributes specific to light functionality
        self.__brightness = 0           # 0-100
        self.__color_temperature = 3000 # Kelvin
        self.__is_on = False
        self.__total_runtime_hours = 0.0
        
        # Initial power consumption
        self._update_power_consumption(0.0)
    
    # Private methods specific to light
    def __calculate_power_consumption(self):
        """Calculate power consumption based on brightness."""
        if not self.__is_on:
            return 0.0
        
        # LED light: 10W max, scales with brightness
        base_power = 10.0  # watts at 100% brightness
        actual_power = (self.__brightness / 100.0) * base_power
        return round(actual_power, 2)
    
    def __validate_brightness(self, brightness: int) -> bool:
        """Validate brightness value."""
        return isinstance(brightness, int) and 0 <= brightness <= 100
    
    def __validate_color_temperature(self, kelvin: int) -> bool:
        """Validate color temperature."""
        min_temp, max_temp = self._color_temperature_range
        return isinstance(kelvin, int) and min_temp <= kelvin <= max_temp
    
    # Public interface methods for light control
    def turn_on(self) -> str:
        """Turn the light on."""
        if self.__is_on:
            return f"{self.device_name} is already on"
        
        self.__is_on = True
        if self.__brightness == 0:
            self.__brightness = 50  # Default brightness
        
        power = self.__calculate_power_consumption()
        self._update_power_consumption(power)
        return f"{self.device_name} turned on at {self.__brightness}% brightness"
    
    def turn_off(self) -> str:
        """Turn the light off."""
        if not self.__is_on:
            return f"{self.device_name} is already off"
        
        self.__is_on = False
        self._update_power_consumption(0.0)
        return f"{self.device_name} turned off"
    
    def set_brightness(self, brightness: int) -> str:
        """Set light brightness with validation."""
        if not self.__validate_brightness(brightness):
            self._report_error(f"Invalid brightness: {brightness}")
            return f"Invalid brightness. Must be 0-100"
        
        self.__brightness = brightness
        
        if brightness == 0:
            self.__is_on = False
        elif not self.__is_on:
            self.__is_on = True
        
        power = self.__calculate_power_consumption()
        self._update_power_consumption(power)
        
        return f"{self.device_name} brightness set to {brightness}%"
    
    def set_color_temperature(self, kelvin: int) -> str:
        """Set color temperature with validation."""
        if not self.__validate_color_temperature(kelvin):
            min_temp, max_temp = self._color_temperature_range
            self._report_error(f"Invalid color temperature: {kelvin}K")
            return f"Invalid color temperature. Must be {min_temp}K-{max_temp}K"
        
        self.__color_temperature = kelvin
        return f"{self.device_name} color temperature set to {kelvin}K"
    
    def get_light_status(self) -> Dict[str, Any]:
        """Get comprehensive light status."""
        base_status = self.get_device_info()
        light_status = {
            'is_on': self.__is_on,
            'brightness': self.__brightness,
            'color_temperature': self.__color_temperature,
            'light_type': self.light_type,
            'runtime_hours': self.__total_runtime_hours
        }
        return {**base_status, **light_status}
    
    def dim_light(self, steps: int = 1) -> str:
        """Dim the light by specified steps."""
        if not self.__is_on:
            return f"{self.device_name} is off. Turn it on first."
        
        new_brightness = max(0, self.__brightness - (steps * self._brightness_step))
        return self.set_brightness(new_brightness)
    
    def brighten_light(self, steps: int = 1) -> str:
        """Brighten the light by specified steps."""
        if not self.__is_on:
            return f"{self.device_name} is off. Turn it on first."
        
        new_brightness = min(100, self.__brightness + (steps * self._brightness_step))
        return self.set_brightness(new_brightness)

# Usage demonstration
def demonstrate_encapsulation():
    """Demonstrate encapsulation with the smart light."""
    print("=== Smart Light Encapsulation Demo ===\n")
    
    # Create a smart light
    living_room_light = SmartLight("LIGHT_001", "Living Room Light")
    
    # Public interface usage (CORRECT WAY)
    print("1. Using Public Interface:")
    print(living_room_light.turn_on())
    print(living_room_light.set_brightness(75))
    print(living_room_light.set_color_temperature(4000))
    print(f"Status: {living_room_light.get_status_summary()}")
    print()
    
    # Demonstrate validation
    print("2. Input Validation:")
    print(living_room_light.set_brightness(150))      # Invalid - too high
    print(living_room_light.set_color_temperature(10000))  # Invalid - too high
    print()
    
    # Show device information
    print("3. Device Information:")
    device_info = living_room_light.get_device_info()
    for key, value in device_info.items():
        print(f"   {key}: {value}")
    print()
    
    # Light-specific information
    print("4. Light-specific Status:")
    light_status = living_room_light.get_light_status()
    light_specific = ['is_on', 'brightness', 'color_temperature', 'light_type']
    for key in light_specific:
        if key in light_status:
            print(f"   {key}: {light_status[key]}")
    print()
    
    # Demonstrate security token usage
    print("5. Security Operations:")
    token = living_room_light.get_security_token()
    print(f"Security token obtained: {token[:8]}...")
    print(living_room_light.restart_device(token))
    print(living_room_light.restart_device("invalid_token"))
    print()
    
    # Show what happens when we try to access private attributes
    print("6. Encapsulation Protection:")
    try:
        # This will fail - private attribute
        brightness = living_room_light.__brightness
        print(f"Private brightness: {brightness}")
    except AttributeError as e:
        print(f"✓ Private attribute protected: {e}")
    
    try:
        # This will fail - private method
        living_room_light.__calculate_power_consumption()
    except AttributeError as e:
        print(f"✓ Private method protected: {e}")
    
    # Protected attributes are accessible but discouraged
    print(f"⚠ Protected attribute (discouraged): {living_room_light._firmware_version}")
    
    # Public attributes are freely accessible
    print(f"✓ Public attribute access: {living_room_light.device_name}")
    print()

if __name__ == "__main__":
    demonstrate_encapsulation()
```

## Getters and Setters

### Traditional Getter/Setter Pattern

While Python favors properties (covered in the next section), understanding traditional getters and setters is important:

Getters and Setters are methods that control how you access and modify private attributes.

- Getter: A method to GET (read) a private attribute
- Setter: A method to SET (write) a private attribute

#### Why Use Them?
Instead of direct access, we use getters/setters to:

- Validate data before storing it
- Control access to sensitive data
- Add logic when getting/setting values

```python
class Temperature:
    """Temperature class using traditional getter/setter pattern."""
    
    def __init__(self, celsius=0):
        self.__celsius = 0  # Private attribute
        self.set_celsius(celsius)  # Use setter for validation
    
    # Getter methods
    def get_celsius(self):
        """Get temperature in Celsius."""
        return self.__celsius
    
    def get_fahrenheit(self):
        """Get temperature in Fahrenheit."""
        return (self.__celsius * 9/5) + 32
    
    def get_kelvin(self):
        """Get temperature in Kelvin."""
        return self.__celsius + 273.15
    
    # Setter methods with validation
    def set_celsius(self, celsius):
        """Set temperature in Celsius with validation."""
        if not isinstance(celsius, (int, float)):
            raise TypeError("Temperature must be a number")
        
        if celsius < -273.15:  # Absolute zero
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        
        self.__celsius = celsius
    
    def set_fahrenheit(self, fahrenheit):
        """Set temperature using Fahrenheit."""
        celsius = (fahrenheit - 32) * 5/9
        self.set_celsius(celsius)  # Reuse validation
    
    def set_kelvin(self, kelvin):
        """Set temperature using Kelvin."""
        celsius = kelvin - 273.15
        self.set_celsius(celsius)  # Reuse validation
    
    def __str__(self):
        return f"{self.__celsius}°C ({self.get_fahrenheit():.1f}°F, {self.get_kelvin():.1f}°K"

# Usage
temp = Temperature(25)
print(temp.get_celsius())    # 25
print(temp.get_fahrenheit()) # 77.0
temp.set_fahrenheit(100)
print(temp.get_celsius())    # 37.78
```

## Python Properties (@property)

Properties provide a more Pythonic way to implement getters and setters: (Python provides a cleaner syntax using @property:)

```python
class Circle:
    def __init__(self, radius):
        self._radius = 0
        self.radius = radius  # Use setter for validation
    
    @property
    def radius(self):
        """Get radius."""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Set radius with validation."""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self):
        """Calculated property - read-only."""
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self):
        """Another calculated property."""
        return 2 * 3.14159 * self._radius

# Usage - looks like simple attributes
circle = Circle(5)
print(circle.radius)        # 5
print(circle.area)          # 78.54
circle.radius = 10          # Uses setter
print(circle.area)          # 314.16
# circle.area = 100         # Error: can't set attribute
```

## Real-World Examples

### Example 1: E-commerce Product

```python
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self._sku = self._generate_sku()
        self.__price = 0
        self.__stock = 0
        self.__sales_count = 0
        
        self.price = price    # Use setter
        self.stock = stock    # Use setter
    
    def _generate_sku(self):
        import random
        return f"SKU{random.randint(10000, 99999)}"
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be positive")
        self.__price = value
    
    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self.__stock = value
    
    @property
    def total_revenue(self):
        return self.__sales_count * self.__price
    
    def sell(self, quantity):
        if quantity > self.__stock:
            raise ValueError("Insufficient stock")
        self.__stock -= quantity
        self.__sales_count += quantity
        return self.__price * quantity

# Usage
product = Product("Laptop", 999.99, 50)
print(f"Price: ${product.price}")
print(f"Revenue: ${product.total_revenue}")
sale_amount = product.sell(5)
print(f"Sold for: ${sale_amount}")
```

### Example 2: User Account System

```python
class UserAccount:
    def __init__(self, username, email):
        self.username = username
        self.__email = ""
        self.__is_active = True
        self.__login_attempts = 0
        
        self.email = email  # Use setter for validation
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value.split("@")[-1]:
            raise ValueError("Invalid email format")
        self.__email = value
    
    @property
    def is_active(self):
        return self.__is_active
    
    def login(self, password):
        # Simplified password check
        if password == "correct_password":
            self.__login_attempts = 0
            return "Login successful"
        
        self.__login_attempts += 1
        if self.__login_attempts >= 3:
            self.__is_active = False
            return "Account locked"
        return f"Invalid password. {3 - self.__login_attempts} attempts left"
    
    def unlock_account(self, admin_code):
        if admin_code == "ADMIN123":
            self.__is_active = True
            self.__login_attempts = 0
            return "Account unlocked"
        return "Invalid admin code"
```

## Benefits of Encapsulation

1. **Data Protection**: Prevents invalid data states
2. **Maintainability**: Change implementation without breaking code
3. **Security**: Hide sensitive implementation details
4. **Validation**: Ensure data integrity through controlled access
5. **Debugging**: Easier to track where data changes occur

## Best Practices

### Do's:
- Use properties instead of traditional getters/setters
- Validate input in setters
- Keep private attributes truly private
- Provide clear public interfaces
- Use meaningful method names

### Don'ts:
- Don't access private attributes directly
- Don't create unnecessary getters/setters for simple attributes
- Don't make everything private - use appropriate access levels
- Don't forget to validate inputs

## Common Mistakes

```python
# ❌ Bad: No validation
class BadExample:
    def __init__(self, value):
        self.value = value  # No validation

# ❌ Bad: Unnecessary getters/setters
class OverEngineered:
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):  # Unnecessary for simple attribute
        return self.__name
    
    def set_name(self, name):  # Unnecessary complexity
        self.__name = name

# ✅ Good: Simple and clean
class GoodExample:
    def __init__(self, name, age):
        self.name = name  # Simple public attribute
        self.__age = 0
        self.age = age    # Use property for validation
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a positive integer")
        self.__age = value
```

## Practice Problems

### Basic Problems

**Problem 1: Student Grade Manager**
Create a `Student` class with:
- Private attributes: `name`, `grades` (list), `student_id`
- Methods: `add_grade()`, `get_average()`, `get_letter_grade()`
- Properties: `name` (read-only), `grade_count` (read-only)

**Problem 2: Banking System**
Build a `BankAccount` class with:
- Private balance and account number
- Methods: `deposit()`, `withdraw()`, `get_balance()`
- Validation: No negative deposits/withdrawals, sufficient funds

**Problem 3: Temperature Converter**
Create a `Temperature` class that:
- Stores temperature in Celsius internally
- Properties for Celsius, Fahrenheit, and Kelvin
- Validates temperature isn't below absolute zero

### Intermediate Problems

**Problem 4: Product Inventory**
Design a `Product` class with:
- Private price and stock attributes
- Properties with validation (price > 0, stock >= 0)
- Methods: `apply_discount()`, `restock()`, `purchase()`
- Read-only property for `total_value`

**Problem 5: User Authentication**
Build a `UserAccount` class with:
- Private password (hashed)
- Login attempt tracking
- Account locking after 3 failed attempts
- Methods: `login()`, `change_password()`, `unlock_account()`

### Advanced Problems

**Problem 6: Smart Device Controller**
Create a base `SmartDevice` class with:
- Protected attributes for device status
- Private security token system
- Public interface for device control
- Subclass it as `SmartThermostat` with temperature control

**Learning Objectives:**
- Understand the three pillars of encapsulation
- Master Python's naming conventions for access control  
- Implement proper validation in setters
- Use properties effectively
- Build secure, maintainable class interfaces

**Next Topic:** After mastering encapsulation, we'll explore **Inheritance** - how classes can extend and specialize other classes while maintaining encapsulation principles!