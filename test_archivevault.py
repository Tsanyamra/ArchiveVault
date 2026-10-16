# test_archivevault.py
"""
Tests for ArchiveVault module.
"""

import unittest
from archivevault import ArchiveVault

class TestArchiveVault(unittest.TestCase):
    """Test cases for ArchiveVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArchiveVault()
        self.assertIsInstance(instance, ArchiveVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArchiveVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
