from .SQLiteGrammar import SQLiteGrammar


class GrammarFactory:
    """Class for controlling the registration and creation of grammars.
    """

    grammars = {
        # Base grammars that will be used with various drivers
        "sqlite": SQLiteGrammar,
        # examples of using different versions of grammar here
    }

    @staticmethod
    def make(key):
        """Makes a specific registered grammar class from a key.

        Arguments:
            key {string} -- The key that the grammar is registered to.

        Returns:
            self
        """
        return GrammarFactory.grammars.get(key)
