import unittest

import mock
from traits.api import Float, HasTraits, Property

from trait_documenter.trait_documenter import (
    is_class_trait, TraitDocumenter)


class Dummy(HasTraits):

    trait_1 = Float

    trait_2 = Property(
        Float,
        depends_on='trait_1')

    not_trait = 2


class TestTraitDocumenter(unittest.TestCase):

    def test_is_class_trait(self):
        self.assertTrue(is_class_trait('trait_1', Dummy))
        self.assertTrue(is_class_trait('trait_2', Dummy))
        self.assertFalse(is_class_trait('not_trait', Dummy))
        self.assertFalse(is_class_trait('__dict__', object))

    def test_get_simple_trait_definition(self):
        documenter = TraitDocumenter(mock.Mock(), 'test')
        documenter.parent = Dummy
        documenter.object_name = 'trait_1'
        definition = documenter.get_trait_definition()
        self.assertEqual(definition, 'Float')

    def test_get_multi_line_trait_definition(self):
        documenter = TraitDocumenter(mock.Mock(), 'test')
        documenter.parent = Dummy
        documenter.object_name = 'trait_2'
        definition = documenter.get_trait_definition()
        self.assertEqual(definition, "Property(Float,depends_on='trait_1')")


if __name__ == '__main__':
    unittest.main()
