"""
Practical Example 1: Bank Account System
Demonstrates encapsulation with validation, properties, and controlled access
"""

class BankAccount:
    def __init__(self, account_number, owner_name, initial_balance=0):
        """Initialize a bank account with encapsulated data."""
        self._account_number = account_number  # Protected (read-only)
        self._owner_name = owner_name          # Protected (read-only)
        self._balance = initial_balance        # Protected (controlled access)
        self._transaction_history = []        # Private transaction log
        self._is_frozen = False               # Account status
        self._daily_withdrawal_limit = 1000   # Daily limit
        self._daily_withdrawn = 0             # Track daily withdrawals
        
        # Log account creation
        self._transaction_history.append(f"Account created with balance: ${initial_balance}")
    
    # Read-only properties
    @property
    def account_number(self):
        """Account number - read only."""
        return self._account_number
    
    @property
    def owner_name(self):
        """Account owner name - read only."""
        return self._owner_name
    
    @property
    def balance(self):
        """Current account balance - read only."""
        return self._balance
    
    @property
    def is_frozen(self):
        """Account frozen status."""
        return self._is_frozen
    
    @property
    def transaction_history(self):
        """Transaction history - returns copy for security."""
        return self._transaction_history.copy()
    
    # Controlled access properties
    @property
    def daily_withdrawal_limit(self):
        """Daily withdrawal limit."""
        return self._daily_withdrawal_limit
    
    @daily_withdrawal_limit.setter
    def daily_withdrawal_limit(self, amount):
        """Set daily withdrawal limit with validation."""
        if amount > 10000:
            raise ValueError("Daily withdrawal limit cannot exceed $10,000")
        
        self._daily_withdrawal_limit = amount
        self._transaction_history.append(f"Daily withdrawal limit changed to: ${amount}")
    
    # Account operations
    def deposit(self, amount):
        """Deposit money into account."""
        if self._is_frozen:
            raise ValueError("Cannot deposit to frozen account")
        
        if amount < self._balance:
            raise ValueError("Insufficient funds")
        
        if self._daily_withdrawn + amount > self._daily_withdrawal_limit:
            raise ValueError(f"Daily withdrawal limit exceeded. Limit: ${self._daily_withdrawal_limit}")
        
        self._balance -= amount
        self._daily_withdrawn += amount
        self._transaction_history.append(f"Withdrew: ${amount}")
        print(f"Successfully withdrew ${amount}. New balance: ${self._balance}")
    
    def transfer(self, amount, target_account):
        """Transfer money to another account."""
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance")
        
        # Withdraw from this account
        self.withdraw(amount)
        
        # Deposit to target account
        target_account.deposit(amount)
        
        # Update transaction history
        self._transaction_history.append(f"Transferred ${amount} to account {target_account.account_number}")
        target_account._transaction_history.append(f"Received ${amount} from account {self.account_number}")
        
        print(f"Successfully transferred ${amount} to account {target_account.account_number}")
    
    def freeze_account(self):
        """Freeze the account (admin function)."""
        self._is_frozen = True
        self._transaction_history.append("Account frozen")
        print("Account has been frozen")
    
    def unfreeze_account(self):
        """Unfreeze the account (admin function)."""
        self._is_frozen = False
        self._transaction_history.append("Account unfrozen")
        print("Account has been unfrozen")
    
    def reset_daily_withdrawal(self):
        """Reset daily withdrawal counter (called daily by system)."""
        self._daily_withdrawn = 0
        self._transaction_history.append("Daily withdrawal limit reset")
    
    def get_account_summary(self):
        """Get complete account information."""
        print(f"\n=== Account Summary ===")
        print(f"Account Number: {self.account_number}")
        print(f"Owner: {self.owner_name}")
        print(f"Balance: ${self.balance}")
        print(f"Status: {'Frozen' if self.is_frozen else 'Active'}")
        print(f"Daily Withdrawal Limit: ${self.daily_withdrawal_limit}")
        print(f"Today's Withdrawals: ${self._daily_withdrawn}")
        print(f"Transactions: {len(self.transaction_history)}")
    
    def print_transaction_history(self, last_n=5):
        """Print recent transaction history."""
        print(f"\n=== Last {last_n} Transactions ===")
        recent_transactions = self.transaction_history[-last_n:]
        for i, transaction in enumerate(recent_transactions, 1):
            print(f"{i}. {transaction}")


"""
Practical Example 2: Smart Home Device System
Demonstrates advanced encapsulation with validation, calculated properties, and state management
"""

class SmartThermostat:
    """Smart thermostat with encapsulated temperature control and energy monitoring."""
    
    def __init__(self, device_id, location):
        """Initialize smart thermostat."""
        self._device_id = device_id
        self._location = location
        self._target_temperature = 70.0    # Target temp in Fahrenheit
        self._current_temperature = 70.0   # Current temp in Fahrenheit
        self._is_heating = False
        self._is_cooling = False
        self._is_online = True
        self._energy_usage = 0.0          # kWh used today
        self._temperature_history = []    # Recent temperature readings
        self._schedule = {}               # Heating/cooling schedule
        self._max_temp = 85.0
        self._min_temp = 45.0
        
        print(f"Smart Thermostat {device_id} initialized in {location}")
    
    # Read-only properties
    @property
    def device_id(self):
        """Device ID - read only."""
        return self._device_id
    
    @property
    def location(self):
        """Device location - read only."""
        return self._location
    
    @property
    def current_temperature(self):
        """Current temperature - read only (set by sensors)."""
        return self._current_temperature
    
    @property
    def is_heating(self):
        """Heating status - read only."""
        return self._is_heating
    
    @property
    def is_cooling(self):
        """Cooling status - read only."""
        return self._is_cooling
    
    @property
    def energy_usage(self):
        """Today's energy usage - read only."""
        return self._energy_usage
    
    @property
    def temperature_history(self):
        """Temperature history - returns copy for security."""
        return self._temperature_history.copy()
    
    # Controlled access properties
    @property
    def target_temperature(self):
        """Target temperature in Fahrenheit."""
        return self._target_temperature
    
    @target_temperature.setter
    def target_temperature(self, temp):
        """Set target temperature with validation."""
        if not isinstance(temp, (int, float)):
            raise TypeError("Temperature must be a number")
        
        if temp > self._max_temp:
            raise ValueError(f"Temperature must be between {self._min_temp}°F and {self._max_temp}°F")
        
        old_temp = self._target_temperature
        self._target_temperature = float(temp)
        print(f"Target temperature changed from {old_temp}°F to {temp}°F")
        
        # Automatically adjust heating/cooling
        self._adjust_temperature()
    
    @property
    def is_online(self):
        """Device online status."""
        return self._is_online
    
    @is_online.setter
    def is_online(self, status):
        """Set device online status."""
        if not isinstance(status, bool):
            raise TypeError("Online status must be boolean")
        
        self._is_online = status
        if not status:
            self._stop_heating()
            self._stop_cooling()
            print("Device went offline - heating/cooling stopped for safety")
        else:
            print("Device came online")
            self._adjust_temperature()
    
    # Calculated properties
    @property
    def temperature_celsius(self):
        """Current temperature in Celsius - calculated property."""
        return (self._current_temperature - 32) * 5/9
    
    @property
    def target_celsius(self):
        """Target temperature in Celsius - calculated property."""
        return (self._target_temperature - 32) * 5/9
    
    @property
    def temperature_difference(self):
        """Difference between current and target temperature."""
        return self._current_temperature - self._target_temperature
    
    @property
    def efficiency_rating(self):
        """Calculate efficiency based on energy usage and temperature maintenance."""
        if self._energy_usage == 0:
            return 100.0
        
        # Simple efficiency calculation (higher is better)
        avg_diff = sum(abs(reading - self._target_temperature) 
                      for reading in self._temperature_history[-24:]) / max(1, len(self._temperature_history[-24:]))
        
        efficiency = max(0, 100 - (avg_diff * 10) - (self._energy_usage * 2))
        return round(efficiency, 1)
    
    # Private methods
    def _adjust_temperature(self):
        """Internal method to automatically adjust heating/cooling."""
        if not self._is_online:
            return
        
        diff = self.temperature_difference
        
        if diff > 2:  # Too hot, need cooling
            self._start_cooling()
            self._stop_heating()
        else:  # Temperature is fine
            self._stop_heating()
            self._stop_cooling()
    
    def _start_heating(self):
        """Internal method to start heating."""
        if not self._is_heating:
            self._is_heating = True
            print("🔥 Heating started")
    
    def _stop_heating(self):
        """Internal method to stop heating."""
        if self._is_heating:
            self._is_heating = False
            print("❄️ Heating stopped")
    
    def _start_cooling(self):
        """Internal method to start cooling."""
        if not self._is_cooling:
            self._is_cooling = True
            print("❄️ Cooling started")
    
    def _stop_cooling(self):
        """Internal method to stop cooling."""
        if self._is_cooling:
            self._is_cooling = False
            print("🔥 Cooling stopped")
    
    def _update_energy_usage(self, kwh):
        """Internal method to update energy usage."""
        self._energy_usage += kwh
    
    # Public methods
    def simulate_temperature_reading(self, new_temp):
        """Simulate a new temperature reading from sensors."""
        if not isinstance(new_temp, (int, float)):
            raise TypeError("Temperature must be a number")
        
        self._current_temperature = float(new_temp)
        self._temperature_history.append(new_temp)
        
        # Keep only last 24 readings
        if len(self._temperature_history) > 24:
            self._temperature_history.pop(0)
        
        print(f"📊 Temperature reading: {new_temp}°F")
        
        # Update energy usage if heating/cooling is active
        if self._is_heating or self._is_cooling:
            self._update_energy_usage(0.1)  # 0.1 kWh per reading
        
        # Automatically adjust if needed
        self._adjust_temperature()
    
    def set_schedule(self, time, temperature):
        """Set temperature schedule for specific times."""
        if not isinstance(time, str) or len(time) != 5 or time[2] != ':':
            raise ValueError("Time must be in HH:MM format")
        
        if temperature > self._max_temp:
            raise ValueError(f"Temperature must be between {self._min_temp}°F and {self._max_temp}°F")
        
        self._schedule[time] = temperature
        print(f"📅 Schedule set: {time} -> {temperature}°F")
    
    def clear_schedule(self):
        """Clear all scheduled temperature changes."""
        self._schedule.clear()
        print("📅 Schedule cleared")
    
    def apply_schedule(self, current_time):
        """Apply scheduled temperature if current time matches."""
        if current_time in self._schedule:
            scheduled_temp = self._schedule[current_time]
            print(f"⏰ Applying scheduled temperature: {scheduled_temp}°F")
            self.target_temperature = scheduled_temp
    
    def reset_energy_usage(self):
        """Reset daily energy usage counter."""
        old_usage = self._energy_usage
        self._energy_usage = 0.0
        print(f"🔋 Energy usage reset. Yesterday's total: {old_usage:.1f} kWh")
    
    def emergency_stop(self):
        """Emergency stop all heating/cooling."""
        self._stop_heating()
        self._stop_cooling()
        print("🚨 EMERGENCY STOP - All heating/cooling disabled")
    
    def get_status_report(self):
        """Get comprehensive device status."""
        status = "🌡️  SMART THERMOSTAT STATUS\n"
        status += f"Device ID: {self.device_id}\n"
        status += f"Location: {self.location}\n"
        status += f"Online: {'✅ Yes' if self.is_online else '❌ No'}\n"
        status += f"Current Temp: {self.current_temperature}°F ({self.temperature_celsius:.1f}°C)\n"
        status += f"Target Temp: {self.target_temperature}°F ({self.target_celsius:.1f}°C)\n"
        status += f"Temperature Diff: {self.temperature_difference:+.1f}°F\n"
        status += f"Heating: {'🔥 ON' if self.is_heating else '❄️ OFF'}\n"
        status += f"Cooling: {'❄️ ON' if self.is_cooling else '🔥 OFF'}\n"
        status += f"Energy Usage: {self.energy_usage:.1f} kWh\n"
        status += f"Efficiency: {self.efficiency_rating}%\n"
        status += f"Schedule Entries: {len(self._schedule)}\n"
        return status
    
    def print_schedule(self):
        """Print current temperature schedule."""
        if not self._schedule:
            print("📅 No schedule set")
            return
        
        print("📅 Temperature Schedule:")
        for time, temp in sorted(self._schedule.items()):
            print(f"   {time} -> {temp}°F")


def run_smart_thermostat_demo():
    print("=== Smart Thermostat System Demo ===\n")
    
    # Create a smart thermostat
    thermostat = SmartThermostat("THERM_001", "Living Room")
    
    print("\n=== Initial Status ===")
    print(thermostat.get_status_report())
    
    print("\n=== Testing Temperature Control ===")
    
    # Test setting target temperature
    thermostat.target_temperature = 72
    thermostat.target_temperature = 68
    
    # Test validation
    try:
        thermostat.target_temperature = 100  # Too high
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        thermostat.target_temperature = "hot"  # Wrong type
    except TypeError as e:
        print(f"Error: {e}")
    
    print("\n=== Simulating Temperature Changes ===")
    
    # Simulate temperature readings throughout the day
    temperatures = [65, 63, 61, 64, 66, 67, 68, 69, 70, 71]
    
    for temp in temperatures:
        thermostat.simulate_temperature_reading(temp)
    
    print("\n=== Testing Schedule Feature ===")
    
    # Set up a daily schedule
    thermostat.set_schedule("06:00", 70)  # Morning
    thermostat.set_schedule("08:00", 68)  # Day (away)
    thermostat.set_schedule("18:00", 72)  # Evening (home)
    thermostat.set_schedule("22:00", 65)  # Night
    
    thermostat.print_schedule()
    
    # Apply schedule
    thermostat.apply_schedule("18:00")  # Evening setting
    
    print("\n=== Testing Properties ===")
    
    # Test calculated properties
    print(f"Current temperature in Celsius: {thermostat.temperature_celsius:.1f}°C")
    print(f"Target temperature in Celsius: {thermostat.target_celsius:.1f}°C")
    print(f"Temperature difference: {thermostat.temperature_difference:.1f}°F")
    print(f"Efficiency rating: {thermostat.efficiency_rating}%")
    
    # Test read-only properties
    print(f"Device ID: {thermostat.device_id}")
    print(f"Energy usage: {thermostat.energy_usage:.1f} kWh")
    
    print("\n=== Testing Online/Offline ===")
    
    # Test going offline
    thermostat.is_online = False
    thermostat.simulate_temperature_reading(65)  # Should not trigger heating
    
    # Back online
    thermostat.is_online = True
    thermostat.simulate_temperature_reading(65)  # Should trigger heating
    
    print("\n=== Testing Emergency Features ===")
    
    # Emergency stop
    thermostat.emergency_stop()
    
    print("\n=== Final Status Report ===")
    print(thermostat.get_status_report())
    
    # Reset for new day
    thermostat.reset_energy_usage()
    
    print("\n=== Testing Error Handling ===")
    
    # Test various error conditions
    error_tests = [
        (lambda: thermostat.simulate_temperature_reading("hot"), "Invalid temperature type"),
        (lambda: thermostat.set_schedule("25:00", 70), "Invalid time format"),
        (lambda: thermostat.set_schedule("12:00", 200), "Invalid temperature"),
        (lambda: setattr(thermostat, 'is_online', "yes"), "Invalid boolean"),
    ]
    
    for test_func, description in error_tests:
        try:
            test_func()
        except (ValueError, TypeError) as e:
            print(f"{description}: {e}")

# Example usage and testing
def run_bank_account_demo():
    """Run a demo of the Bank Account system."""
    print("=== Bank Account System Demo ===\n")
    
    # Create accounts
    alice_account = BankAccount("ACC001", "Alice Johnson", 1000)
    bob_account = BankAccount("ACC002", "Bob Smith", 500)
    
    # Display initial account info
    alice_account.get_account_summary()
    bob_account.get_account_summary()
    
    print("\n=== Testing Deposits and Withdrawals ===")
    
    # Test deposits
    alice_account.deposit(250)
    alice_account.deposit(100)
    
    # Test withdrawals
    alice_account.withdraw(150)
    alice_account.withdraw(200)
    
    # Test daily limit
    try:
        alice_account.withdraw(1000)  # Should fail - exceeds daily limit
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n=== Testing Transfers ===")
    
    # Test transfer
    alice_account.transfer(300, bob_account)
    
    print("\n=== Testing Property Access ===")
    
    # Test read-only properties
    print(f"Alice's balance: ${alice_account.balance}")
    print(f"Bob's account number: {bob_account.account_number}")
    
    # Test property setter
    alice_account.daily_withdrawal_limit = 2000
    
    # Try to set invalid limit
    try:
        alice_account.daily_withdrawal_limit = -100
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n=== Testing Account Freezing ===")
    
    # Freeze account
    alice_account.freeze_account()
    
    # Try to deposit to frozen account
    try:
        alice_account.deposit(100)
    except ValueError as e:
        print(f"Error: {e}")
    
    # Unfreeze account
    alice_account.unfreeze_account()
    alice_account.deposit(100)  # Should work now
    
    print("\n=== Final Account Summaries ===")
    alice_account.get_account_summary()
    alice_account.print_transaction_history()
    
    bob_account.get_account_summary()
    bob_account.print_transaction_history()
    
    print("\n=== Testing Error Handling ===")
    
    # Test various error conditions
    test_cases = [
        (lambda: alice_account.withdraw(-50), "Negative withdrawal"),
        (lambda: alice_account.deposit(0), "Zero deposit"),
        (lambda: alice_account.withdraw(10000), "Insufficient funds"),
        (lambda: alice_account.transfer(100, "invalid"), "Invalid transfer target"),
    ]
    
    for test_func, description in test_cases:
        try:
            test_func()
        except (ValueError, TypeError) as e:
            print(f"{description}: {e}")

# Example usage and testing
if __name__ == "__main__":

    print("=== Running Bank Account Demo ===")
    run_bank_account_demo()
    
    # print("\n=== Running Smart Thermostat Demo ===")
    # run_smart_thermostat_demo()