# Library Management System

A Python-based Library Management System that implements enumerations for book genres and membership levels, along with custom exception handling.

## Features

- Book management with borrowing and returning functionality
- Multiple book genres (Fiction, Non-Fiction, Science, History, Biography)
- Tiered membership system (Basic, Premium, Gold)
- Custom exception handling for various error scenarios
- Comprehensive test suite using pytest
- Automated testing with GitHub Actions

## Project Structure 
```
library-management-system/
├── library_system.py # Main implementation
├── test_library_system.py # Test suite
├── .github/
│ └── workflows/
│       └── test_library.yml # GitHub Actions workflow
└── README.md
```

## Classes and Enumerations

### Enumerations
- `BookGenre`: Defines different book categories with auto-incrementing values
  - FICTION (1)
  - NON_FICTION (2)
  - SCIENCE (3)
  - HISTORY (4)
  - BIOGRAPHY (5)

- `MembershipLevel`: Defines membership tiers with associated annual fees
  - BASIC (100)
  - PREMIUM (200)
  - GOLD (500)

### Classes
- `Book`: Manages book information and availability
- `Member`: Handles member information and fee calculation

### Custom Exceptions
- `BookNotAvailableError`: When attempting to borrow an unavailable book
- `LateReturnError`: When returning a book past its due date
- `InvalidMembershipError`: When dealing with invalid membership levels

## GitHub Actions

The project includes automated testing using GitHub Actions. Tests are automatically run on:
- Push to main branch
- Pull requests to main branch

## Usage Example

```python
from library_system import Book, BookGenre, Member, MembershipLevel
# Create a book
book = Book("1984", BookGenre.FICTION, True)
# Create a member
member = Member("Alice", MembershipLevel.PREMIUM)
# Borrow a book
try:
book.borrow()
except BookNotAvailableError:
print("Book is not available")
# Return a book
try:
book.return_book(is_late=False)
except LateReturnError:
print("Late return fee applies")
# Get membership fee
try:
fee = member.get_fee()
print(f"Annual fee: ${fee}")
except InvalidMembershipError:
print("Invalid membership level")
```