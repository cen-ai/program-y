import unittest

class LinkStoreAsserts(unittest.TestCase):

    def assert_links_storage(self, store):

        store.empty()

        store.create_link(1, "ABCEDEF", "Password123")
        store.create_link(2, "ABCEDEF", "Password123")
        store.commit()

        links = store.get_link(1)
        self.assertIsNotNone(links)
        self.assertEqual(1, len(links))
        self.assertEqual(1, links[0]['primary_user'])
        self.assertEqual("ABCEDEF", links[0]['generated_key'])
        self.assertEqual("Password123", links[0]['provided_key'])

        links = store.get_link(2)
        self.assertIsNotNone(links)
        self.assertEqual(1, len(links))
        self.assertEqual(2, links[0]['primary_user'])
        self.assertEqual("ABCEDEF", links[0]['generated_key'])
        self.assertEqual("Password123", links[0]['provided_key'])

        store.remove_link(1)
        store.commit()
        links = store.get_link(1)
        self.assertIsNotNone(links)
        self.assertEqual(0, len(links))

        links = store.get_link(2)
        self.assertIsNotNone(links)
        self.assertEqual(1, len(links))
        self.assertEqual(2, links[0]['primary_user'])
        self.assertEqual("ABCEDEF", links[0]['generated_key'])
        self.assertEqual("Password123", links[0]['provided_key'])

