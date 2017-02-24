import impl


class TestCreatePerson:
    """ Test a person is created in the network """

    def test_person_created_in_network(self):
        """ assert that a person is created within the network """
        try:
            n = impl.Network()
            p = n.create_person()
            n.add_person_property(p, 'name', 'p')
            assert p is n.get_person('p')
        except:
            assert False


# noinspection PyMethodMayBeStatic
class TestAddPersonProperty:
    """ Test a property is added to the person """

    def test_name_property_fails_with_non_string_value(self):
        """ asserts that a TypeError is raised if given a name property with a non-string value """
        try:
            n = impl.Network()
            p = n.create_person()
            p = n.get_person(p)
            n.add_person_property(p, 'name', 42)
            assert False
        except TypeError:
            assert True
        except:
            assert False

    def test_fails_when_name_property_already_exists(self):
        """ asserts that ValueError is raised if given a name property that already exists in the network """
        try:
            n = impl.Network()
            p1 = n.create_person()
            p2 = n.create_person()
            n.add_person_property(p1, 'name', 'foo')
            n.add_person_property(p2, 'name', 'foo')
            assert False
        except ValueError:
            assert True
        except:
            assert False

    def test_fails_when_adding_property_to_non_existing_person(self):
        """ asserts that a RuntimeError is raised if adding a property to a person not in the network """
        try:
            n = impl.Network()
            n.add_person_property('p', 'prop', 'val')
            assert False
        except RuntimeError:
            assert True
        except:
            assert False

    def test_property_is_overwritten_if_already_exists(self):
        """ asserts that the given property is overwritten with the new value if it already exists """
        try:
            n = impl.Network()
            p = n.create_person()
            n.add_person_property(p, 'name', 'p')
            n.add_person_property(p, 'name', 'p1')
            p1 = n.get_person('p1')
            assert p is p1
        except:
            assert False

    def test_valid_property_added_to_person_is_successful(self):
        """ asserts that a valid property given will be added to the person """
        try:
            n = impl.Network()
            p = n.create_person()
            n.add_person_property(p, 'name', 'p')
            p1 = n.get_person('p')
            assert p is p1
        except:
            assert False


class TestAddRelation:
    """ Test a relation is created in the network """

    def test_relation_fails_between_non_network_and_network_persons(self):
        """ asserts that a RuntimeError is raised if person1 does not exist in the network """
        try:
            n = impl.Network()
            p1 = 'p1'
            p2 = n.create_person()
            n.add_relation(p1, p2)
            assert False
        except RuntimeError:
            assert True
        except:
            assert False

    def test_relation_fails_between_network_and_non_network_persons(self):
        """ asserts that a RuntimeError is raised if person2 does not exist in the network """
        try:
            n = impl.Network()
            p1 = n.create_person()
            p2 = 'p2'
            n.add_relation(p1, p2)
            assert False
        except RuntimeError:
            assert True
        except:
            assert False

    def test_relation_fails_between_two_non_network_persons(self):
        """ asserts that a RuntimeError is raised if relation added between two people who are not in the network """
        try:
            n = impl.Network()
            p1 = 'p1'
            p2 = 'p2'
            n.add_relation(p1, p2)
            assert False
        except RuntimeError:
            assert True
        except:
            assert False

    def test_relation_fails_between_two_related_persons(self):
        """ asserts that a ValueError is raised if relation added between two people with a pre-existing relation """
        try:
            n = impl.Network()
            p1 = n.create_person()
            p2 = n.create_person()
            n.add_relation(p1, p2)
            n.add_relation(p1, p2)
        except ValueError:
            assert True
        except:
            assert False

    def test_relation_does_not_fail_if_person1_equals_person2(self):
        """ asserts that a relation can be added between a person and himself """
        try:
            n = impl.Network()
            p1 = n.create_person()
            n.add_relation(p1, p1)
            assert True
        except:
            assert False


class TestAddRelationProperty:
    """ Test a property is added to the relation """

    def test_fails_when_adding_non_boolean_to_friend_property(self):
        """ asserts that a TypeError is raised if a non-boolean value is added with a friend property"""
        try:
            n = impl.Network()
            p1 = n.create_person()
            p2 = n.create_person()
            n.add_relation(p1, p2)
            n.add_relation_property(p1, p2, 'friend', 'True')
            assert False
        except TypeError:
            assert True
        except:
            assert False

    def test_fails_when_adding_property_to_non_existing_relation(self):
        """ asserts that a RuntimeError is raised when adding a property to a non-existing relation """
        try:
            n = impl.Network()
            p1 = n.create_person()
            p2 = n.create_person()
            p3 = n.create_person()
            n.add_relation(p1, p2)
            n.add_relation_property(p1, p3, 'friend', True)
            assert False
        except RuntimeError:
            assert True
        except:
            assert False

    def test_fails_when_person1_does_not_exist(self):
        """ asserts that a RuntimeError is raised if person1 does not exist """
        try:
            n = impl.Network()
            p1 = n.create_person()
            p2 = n.create_person()
            p3 = 'p3'
            n.add_relation(p1, p2)
            n.add_relation_property(p3, p1, 'friend', True)
            assert False
        except RuntimeError:
            assert True
        except:
            assert False

    def test_fails_when_person2_does_not_exist(self):
        """ asserts that a RuntimeError is raised if person2 does not exist """
        try:
            n = impl.Network()
            p1 = n.create_person()
            p2 = n.create_person()
            p3 = 'p3'
            n.add_relation(p1, p2)
            n.add_relation_property(p1, p3, 'friend', True)
        except RuntimeError:
            assert True
        except:
            assert False

    def test_adding_relation_property_overwrites_previous_value(self):
        """ asserts that the previous value is overwritten if given a pre-existing property """
        try:
            n = impl.Network()
            p1 = n.create_person()
            p2 = n.create_person()
            p3 = n.create_person()
            n.add_relation(p1, p2)
            n.add_relation_property(p1, p2, 'friend', True)
            n.add_relation(p2, p3)
            n.add_relation_property(p2, p3, 'friend', True)
            n.add_relation_property(p2, p3, 'friend', False)
            o = n.friends_of_friends(p1)
            assert len(o) == 0
        except:
            assert False

    def test_does_not_fail_when_adding_property_to_oneself(self):
        """ asserts that a property can be added between a person and himself """
        try:
            n = impl.Network()
            p1 = n.create_person()
            n.add_relation(p1, p1)
            n.add_relation_property(p1, p1, 'tall', True)
            assert True
        except:
            assert False

    def test_does_not_fail_with_valid_parameters(self):
        """ asserts that a valid call will add a relation successfully"""
        try:
            n = impl.Network()
            p1 = n.create_person()
            p2 = n.create_person()
            n.add_relation(p1, p2)
            n.add_relation_property(p1, p2, 'friend', True)
            assert True
        except:
            assert False


class TestGetPerson:
    """ Test that a person with the given name is returned """

    def test_fails_for_non_string_names(self):
        """ asserts that a RuntimeError is raised if given name that are not strings """
        try:
            n = impl.Network()
            n.get_person(True)
            assert False
        except RuntimeError:
            assert True
        except:
            assert False

    def test_fails_for_non_existent_name(self):
        """ asserts that a RuntimeError is raised if called with a name not in the network """
        try:
            n = impl.Network()
            n.get_person('p1')
            assert False
        except RuntimeError:
            assert True
        assert False

    def test_person_requested_is_person_received(self):
        """ asserts that the person with the given name is the one that is returned """
        try:
            n = impl.Network()
            p1 = n.create_person()
            n.add_person_property(p1, 'name', 'p1')
            p2 = n.get_person('p1')
            assert p1 is p2
        except:
            assert False


class TestFriendsOfFriends:
    """ Test that a list of friends of friends of the person with the given name is returned """

    def test_fails_if_name_does_not_exist(self):
        """ asserts that a RuntimeError is raised if the given name does not exist """
        try:
            n = impl.Network()
            n.friends_of_friends('p1')
            assert False
        except RuntimeError:
            assert True
        except:
            assert False

    def test_fails_for_non_string_names(self):
        """ asserts that a TypeError is raised if given a non-string name """
        try:
            n = impl.Network()
            n.friends_of_friends(True)
            assert False
        except TypeError:
            assert True
        except:
            assert False

    def test_friends_of_friends_are_returned(self):
        """ asserts that the friends of friends of the person with the given name are returned """
        try:
            n = impl.Network()
            p1 = n.create_person()
            p2 = n.create_person()
            p3 = n.create_person()
            p4 = n.create_person()
            n.add_person_property(p1, 'name', 'p1')
            n.add_person_property(p2, 'name', 'p2')
            n.add_person_property(p3, 'name', 'p3')
            n.add_person_property(p4, 'name', 'p4')
            n.add_relation(p1, p2)
            n.add_relation(p2, p3)
            n.add_relation(p3, p4)
            n.add_relation(p3, p1)
            unknown = set(n.friends_of_friends('p2'))
            known = {p4, p1}
            assert known == unknown
        except:
            assert False

    def test_object_returned_is_a_list(self):
        """ asserts that the the returned value is an instance of a list """
        try:
            n = impl.Network()
            p1 = n.create_person()
            p2 = n.create_person()
            p3 = n.create_person()
            p4 = n.create_person()
            n.add_person_property(p1, 'name', 'p1')
            n.add_person_property(p2, 'name', 'p2')
            n.add_person_property(p3, 'name', 'p3')
            n.add_person_property(p4, 'name', 'p4')
            n.add_relation(p1, p2)
            n.add_relation(p2, p3)
            n.add_relation(p3, p4)
            n.add_relation(p3, p1)
            o = n.friends_of_friends('p2')
            assert isinstance(o, list)
        except:
            assert False


