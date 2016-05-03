from unittest import TestCase
from molecupy.atomic import Atom

class AtomTest(TestCase):

    def check_valid_atom(self, atom):
        self.assertIsInstance(atom, Atom)
        self.assertIsInstance(atom.x, float)
        self.assertIsInstance(atom.y, float)
        self.assertIsInstance(atom.z, float)
        self.assertIsInstance(atom.element, str)
        self.assertRegex(str(atom), r"<Atom \([a-zA-Z]{1,2}\)>")



class AtomCreationTests(AtomTest):

    def test_can_create_atom(self):
        atom = Atom(1.0, 2.0, 3.0, "C")
        self.check_valid_atom(atom)


    def test_coordinates_must_be_floats(self):
        with self.assertRaises(TypeError):
            atom = Atom("1", 2.0, 3.0, "C")
        with self.assertRaises(TypeError):
            atom = Atom(1.0, "2", 3.0, "C")
        with self.assertRaises(TypeError):
            atom = Atom(1.0, 2.0, "3", "C")
