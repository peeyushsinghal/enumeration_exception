import enum
class Book:
    def __init__(self, year, genre, is_available) -> None:
        self.year = year
        self.genre = genre
        self.is_available = is_available
        # self.is_late = False

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return 
        else:
            raise BookNotAvailableError
    
    def return_book(self, is_late= False):
        if is_late:
            raise LateReturnError
        else:
            self.is_available = True
        
class BookGenre(enum.Enum):
    FICTION = enum.auto()
    NON_FICTION = enum.auto()
    SCIENCE = enum.auto()
    HISTORY = enum.auto()
    BIOGRAPHY = enum.auto()

class MembershipLevel(enum.Enum):
    BASIC = 100
    PREMIUM = 200
    GOLD = 500
    

class BookNotAvailableError(Exception):
    pass

class LateReturnError(Exception):
    pass

class InvalidMembershipError(Exception):
    pass

class Member:
    def __init__(self, name, membership_level) -> None:
        self.name = name
        self.membership_level = membership_level
    
    def get_fee(self):
        # if isinstance(MembershipLevel(self.membership_level).value, int):
        #     return MembershipLevel(self.membership_level).value
        # else:
        #     raise InvalidMembershipError
        
        try:
            return MembershipLevel(self.membership_level).value
        except:
            raise InvalidMembershipError