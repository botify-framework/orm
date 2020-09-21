import inspect
import unittest


from src.masoniteorm.orm.scopes import (
    scope,
    SoftDeletesMixin,
    TimeStampsMixin,
    SoftDeleteScope,
)
from src.masoniteorm.orm.models import Model


class UserSoft(Model, SoftDeletesMixin):
    __dry__ = True


class User(Model):

    __dry__ = True


class TestMySQLGlobalScopes(unittest.TestCase):
    def test_can_use_global_scopes_on_select(self):
        sql = "SELECT * FROM `user_softs` WHERE `user_softs`.`name` = 'joe' AND `user_softs`.`deleted_at` IS NULL"
        self.assertEqual(sql, UserSoft.where("name", "joe").to_sql())

    # def test_can_use_global_scopes_on_delete(self):
    #     sql = "UPDATE `users` SET `users`.`deleted_at` = 'now' WHERE `users`.`name` = 'joe'"
    #     self.assertEqual(
    #         sql,
    #         User.apply_scope(SoftDeletes)
    #         .where("name", "joe")
    #         .delete(query=True)
    #         .to_sql(),
    #     )

    def test_can_use_global_scopes_on_time(self):
        sql = "INSERT INTO `users` (`users`.`name`, `users`.`updated_at`, `users`.`created_at`) VALUES ('Joe', 'now', 'now')"
        self.assertEqual(sql, User.create({"name": "Joe"}, query=True))

    # def test_can_use_global_scopes_on_inherit(self):
    #     sql = "SELECT * FROM `user_softs` WHERE `user_softs`.`deleted_at` IS NULL"
    #     self.assertEqual(sql, UserSoft.all(query=True))