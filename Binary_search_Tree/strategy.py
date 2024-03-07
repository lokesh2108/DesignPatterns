from abc import ABC, abstractmethod

# define Strategy as abstract base class
class Strategy(ABC):
    @abstractmethod
    def apply_strategy(self, student):
        pass

# define different strategies
class RedIdStrategy(Strategy):
    def apply_strategy(self, student):
        return student.red_id

class LastNameFirstNameStrategy(Strategy):
    def apply_strategy(self, student):
        return (student.last_name, student.first_name)

class RoundedGpaRedIdStrategy(Strategy):
    def apply_strategy(self, student):
        return (round(student.gpa), student.red_id)