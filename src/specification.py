from abc import ABC, abstractmethod


class Specification(ABC):

    def __and__(self, other):
        return And(self, other)

    def __or__(self, other):
        return Or(self, other)

    def __invert__(self):
        return Invert(self)

    @abstractmethod
    def is_satisfied(self, candidate):
        raise NotImplementedError

    def remainder_unsatisfied(self, candidate):
        if self.is_satisfied(candidate):
            return None
        else:
            return self


class MultaryCompositeSpecification(Specification):
    def __init__(self, *specifications: Specification):
        self.specifications = specifications

    def is_satisfied(self, candidate):
        pass


class And(MultaryCompositeSpecification):
    def __and__(self, other):
        if isinstance(other, And):
            self.specifications += other.specifications
        else:
            self.specifications += (other,)
        return self

    def is_satisfied(self, candidate):
        satisfied = all(
            [specification.is_satisfied(candidate) for specification in self.specifications]
        )

        return satisfied


class Or(MultaryCompositeSpecification):
    def __or__(self, other):
        if isinstance(other, Or):
            self.specifications += other.specifications
        else:
            self.specifications += (other, )
        return self

    def is_satisfied(self, candidate):
        satisfied = any(
            specification.is_satisfied(candidate) for specification in self.specifications
        )
        return satisfied


class UnaryCompositeSpecification(Specification):

    def __init__(self, specification):
        self.specification = specification

    def is_satisfied(self, candidate):
        pass


class Invert(UnaryCompositeSpecification):

    def is_satisfied(self, candidate):
        return not self.specification.is_satisfied(candidate)
