import traceback

import MySQLdb

from entity.Scoring import Scoring
from entity.User import User


class DBconnect(object):

    def findUserByName(self, username):
        db = MySQLdb.connect("localhost", "root", "root", "bysj", charset='utf8')
        cursor = db.cursor()
        users = []
        try:
            cursor.execute("select * from customer where username = '%s' " % (username,))
            results = cursor.fetchall()
            for u in results:
                user = User(u[1], u[2], u[3])
                user.ID = u[0]
                users.append(user)
                print(user)
        except:
            traceback.print_exc()
            # 如果发生异常，则回滚
            db.rollback()
        finally:
            cursor.close()
            db.close()
        return users

    def insertUser(self, user):
        db = MySQLdb.connect("localhost", "root", "root", "bysj", charset='utf8')
        cursor = db.cursor()
        flag = False
        try:
            cursor.execute("insert into customer (username, password, level) value ('%s','%s','%d')" % (
                user.username, user.password, user.level))
            db.commit()
            flag = True
        except:
            traceback.print_exc()
            # 如果发生异常，则回滚
            db.rollback()
        finally:
            cursor.close()
            db.close()
        return flag


    def findAllScoring(self):
        db = MySQLdb.connect("localhost", "root", "root", "bysj", charset='utf8')
        cursor = db.cursor()
        users_list = []
        try:
            cursor.execute("select * from scoring")
            results = cursor.fetchall()
            for u in results:
                user = Scoring(u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7],u[8])
                users_list.append(user)
                print(user)
        except:
            traceback.print_exc()
            # 如果发生异常，则回滚
            db.rollback()
        finally:
            cursor.close()
            db.close()
        return users_list

    def findAllUser(self):
        db = MySQLdb.connect("localhost", "root", "root", "bysj", charset='utf8')
        cursor = db.cursor()
        users_list = []
        try:
            cursor.execute("select * from customer")
            results = cursor.fetchall()
            for u in results:
                user = User(u[1], u[2], u[3])
                user.ID = u[0]
                users_list.append(user)
                print(user)
        except:
            traceback.print_exc()
            # 如果发生异常，则回滚
            db.rollback()
        finally:
            cursor.close()
            db.close()
        return users_list


if __name__ == '__main__':
    db = DBconnect()
    user = User("zhangsan","123456",0)
    db.insertUser(user)
    print(db.findAllUser())
