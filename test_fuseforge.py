# test_fuseforge.py
"""
Tests for FuseForge module.
"""

import unittest
from fuseforge import FuseForge

class TestFuseForge(unittest.TestCase):
    """Test cases for FuseForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FuseForge()
        self.assertIsInstance(instance, FuseForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FuseForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
