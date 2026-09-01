"""Unit Tests for Authentication and RBAC Security."""
import unittest
from app.core.security import Security
from app.services.auth_service import AuthService

class TestAuthSecurity(unittest.TestCase):
    def test_password_hashing_and_verification(self):
        pwd = "EnterpriseSecurePass2026!"
        h = Security.hash_password(pwd)
        self.assertIn(":", h)
        self.assertTrue(Security.verify_password(pwd, h))
        self.assertFalse(Security.verify_password("WrongPass", h))

    def test_jwt_token_generation_and_decoding(self):
        token = Security.generate_token("u100", "testuser", "ANALYST")
        self.assertIn(".", token)
        payload = Security.decode_token(token)
        self.assertIsNotNone(payload)
        self.assertEqual(payload["username"], "testuser")
        self.assertEqual(payload["role"], "ANALYST")

    def test_permission_hierarchy(self):
        self.assertTrue(Security.check_permission("ADMIN", "VIEWER"))
        self.assertTrue(Security.check_permission("ADMIN", "ANALYST"))
        self.assertTrue(Security.check_permission("ADMIN", "ADMIN"))
        self.assertTrue(Security.check_permission("ANALYST", "VIEWER"))
        self.assertFalse(Security.check_permission("ANALYST", "ADMIN"))
        self.assertFalse(Security.check_permission("VIEWER", "ANALYST"))

    def test_demo_logins(self):
        admin_res = AuthService.authenticate_user("admin", "AdminPass2026!")
        self.assertEqual(admin_res["user"]["role"], "ADMIN")
        analyst_res = AuthService.authenticate_user("analyst", "AnalystPass2026!")
        self.assertEqual(analyst_res["user"]["role"], "ANALYST")
        viewer_res = AuthService.authenticate_user("viewer", "ViewerPass2026!")
        self.assertEqual(viewer_res["user"]["role"], "VIEWER")

if __name__ == "__main__":
    unittest.main()
