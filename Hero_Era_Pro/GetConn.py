# -*- coding:utf-8 -*-

import configparser
import pymysql


def get_conn(db):
    """
    获取配置文件的内容来创建数据库连接
    @ cp 读取配置文件
    @ host 数据库地址
    @ port 数据库端口
    @ user 数据库用户名
    @ passwd 数据库密码
    @ charset 数据库编码
    @ conn 创建数据库连接
    :param db: 需要连接的数据库名称
    :return: conn 数据库连接
    """
    # 分别从配置文件中读入mysql配置信息
    cp = configparser.ConfigParser()
    cp.read('./conf.cfg', encoding='utf-8')
    host = cp.get('MYSQL_DB', 'host')
    port = int(cp.get('MYSQL_DB', 'port'))
    user = cp.get('MYSQL_DB', 'user')
    passwd = cp.get('MYSQL_DB', 'passwd')
    charset = cp.get('MYSQL_DB', 'charset')
    # 异常控制
    try:
        # 创建数据库连接
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
        # 返回数据库连接对象
        return conn
    except Exception as e:
        print(e)


def create_hero_table(conn):
    """
    重建英雄数据表
    用于新游戏时，清空上一场游戏数据内容，重新生成英雄数据表
    :param conn: 数据库连接对象
    :return: None
    """
    # 获取数据库操作游标
    cursor = conn.cursor()
    # SQL删除英雄表
    drop_sql = 'DROP TABLE IF EXISTS heroes;'
    # SQL创建英雄表
    create_sql = '''
        CREATE TABLE heroes (
            h_id INT(10) NOT NULL AUTO_INCREMENT COMMENT '英雄ID',
            h_group INT(10) DEFAULT 0 COMMENT '所属势力ID',
            h_name VARCHAR(10) COLLATE utf8_bin DEFAULT NULL COMMENT '英雄姓名',
            h_gender VARCHAR(10) COLLATE utf8_bin DEFAULT NULL COMMENT '英雄性别',
            h_age INT(10) DEFAULT NULL COMMENT '英雄年龄',
            h_identity VARCHAR(10) COLLATE utf8_bin DEFAULT NULL COMMENT '英雄身份',
            h_lead INT(10) DEFAULT NULL COMMENT '英雄统率',
            h_force INT(10) DEFAULT NULL COMMENT '英雄武力',
            h_brain INT(10) DEFAULT NULL COMMENT '英雄智力',
            h_politics INT(10) DEFAULT NULL COMMENT '英雄政治',
            h_charm INT(10) DEFAULT NULL COMMENT '英雄魅力',
            h_status INT(10) DEFAULT 1 COMMENT '英雄状态',
            PRIMARY KEY (h_id),
            KEY (h_group)
        ) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    '''
    try:
        # 执行SQL
        cursor.execute(drop_sql)
        cursor.execute(create_sql)
    except Exception as e:
        print(e)
        # 事务回滚
        conn.rollback()
        
        
def create_den_table(conn):
    """
    重建据点数据表
    用于新游戏时，清空上一场游戏数据内容，重新生成据点数据表
    :param conn: 数据库连接对象
    :return: None
    """
    # 获取数据库操作游标
    cursor = conn.cursor()
    # SQL删除据点表
    drop_sql = 'DROP TABLE IF EXISTS den;'
    # SQL创建据点表
    create_sql = '''
        CREATE TABLE den (
            d_id INT(10) NOT NULL AUTO_INCREMENT COMMENT '据点ID',
            d_group INT(10) COMMENT '所属势力ID',
            d_name VARCHAR(10) COLLATE utf8_bin DEFAULT NULL COMMENT '据点名称',
            d_corps INT(10) NOT NULL COMMENT '据点兵种',
            d_ranker INT(100) NOT NULL COMMENT '据点兵力',
            d_gold INT(100) NOT NULL COMMENT '据点黄金',
            d_rations INT(100) NOT NULL COMMENT '据点粮草',
            d_gem INT(10) NOT NULL COMMENT '据点宝物',
            PRIMARY KEY (d_id),
            KEY (d_group)
        ) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    '''
    try:
        # 执行SQL
        cursor.execute(drop_sql)
        cursor.execute(create_sql)
    except Exception as e:
        print(e)
        # 事务回滚
        conn.rollback()
        

def create_group_table(conn, game_hard):
    """
    重建势力数据表
    用于新游戏时，清空上一场游戏数据内容，重新生成势力数据表
    :param game_hard: 游戏难度等级
    :param conn: 数据库连接对象
    :return: None
    """
    # 数据库操作游标
    cursor = conn.cursor()
    # SQL删除势力表
    drop_sql = 'DROP TABLE IF EXISTS hero_group;'
    # SQL创建势力表
    create_sql = '''
        CREATE TABLE hero_group (
            g_id INT(10) NOT NULL AUTO_INCREMENT COMMENT '势力ID',
            g_lord INT(10) DEFAULT NULL COMMENT '势力主公ID',
            g_name VARCHAR(10) COLLATE utf8_bin DEFAULT NULL COMMENT '势力名',
            g_economy INT(10) NOT NULL DEFAULT '{0}' COMMENT '势力经济',
            g_farming INT(10) NOT NULL DEFAULT '{0}' COMMENT '势力农业',
            g_military INT(10) NOT NULL DEFAULT '{0}' COMMENT '势力军事',
            g_science INT(10) NOT NULL DEFAULT '{0}' COMMENT '势力科技',
            g_morale INT(10) NOT NULL DEFAULT '{1}' COMMENT '势力民心',
            g_gold INT(100) NOT NULL DEFAULT '{2}' COMMENT '势力黄金',
            g_rations INT(100) NOT NULL DEFAULT '{3}' COMMENT '势力粮草',
            g_corps INT(10) NOT NULL DEFAULT '1' COMMENT '势力兵种',
            g_experience INT(10) NOT NULL DEFAULT '10' COMMENT '势力兵种经验',
            g_ranker INT(100) NOT NULL DEFAULT '{4}' COMMENT '势力兵力',
            g_populace INT(100) NOT NULL DEFAULT '{5}' COMMENT '势力人口',
            g_status INT(10) NOT NULL DEFAULT '0' COMMENT '势力状态',
            PRIMARY KEY (g_id),
            KEY (g_lord)
        ) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    '''.format(50*game_hard, 50, 2000*game_hard, 10000*game_hard, 1000*game_hard*game_hard, 50000*game_hard)
    try:
        # 执行SQL
        cursor.execute(drop_sql)
        cursor.execute(create_sql)
    except Exception as e:
        print(e)
        # 事务回滚
        conn.rollback()


def clear_data(conn, t_name, data):
    """
    初始化指定数据表中数据
    :param data: 初始化数据字典
    :param t_name: 操作表名称
    :param conn: 数据库连接对象
    :return: None
    """
    sets = ''
    # 数据库操作游标
    cursor = conn.cursor()
    for key, value in data.items():
        sets = '{0}{1}={2},'.format(sets, key, value)
    # SQL更新数据库信息
    sql = 'update {0} set {1}'.format(t_name, sets[:-1])
    try:
        # 执行SQL并提交事务
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        # 事务回滚
        conn.rollback()
   
        
def insert_data(conn, t_name, data):
    """
    向数据库中插入数据
    @ conn 接收由get_conn()返回的conn这个数据库连接
    @ cursor 数据库操作游标，用于数据库操作
    @ keys 拼接SQL语句，值是student字典中所有的key
    @ values 拼接SQL语句，值是student字典中所有的value
    @ sql 拼接需要执行的SQL语句
    :param data: 插入数据字典
    :param t_name: 操作表名称
    :param conn: 数据库连接对象
    :return: None
    """
    keys = ''
    values = ''
    cursor = conn.cursor()
    # 遍历字典中所有的key和value并分别接收拼接
    for key, value in data.items():
        keys = keys + '{},'.format(key)
        values = values + '"{}",'.format(value)
    sql = 'INSERT INTO {0}({1}) VALUES({2})'.format(t_name, keys[:-1], values[:-1])
    # 异常控制
    try:
        # 执行SQL语句并提交事务
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        # 事务回滚
        conn.rollback()


def update_data(conn, t_name, data, condition):
    """
    向数据库中更新数据
    @ conn 接收由get_conn()返回的conn这个数据库连接
    @ cursor 数据库操作游标，用于数据库操作
    @ sets 接收拼接的更新对象和数据
    @ sql 拼接需要执行的SQL语句
    :param condition: 操作表条件
    :param data: 更新数据字典
    :param t_name: 操作表名称
    :param conn: 数据库连接对象
    :return: None
    """
    sets = ''
    cursor = conn.cursor()
    # 遍历字典中所有的key和value并分别接收拼接
    for key, value in data.items():
        sets = '{0}{1}={2},'.format(sets, key, value)
    sql = 'UPDATE {0} SET {1} where {2}'.format(t_name, sets[:-1], condition)
    # 异常控制
    try:
        # 执行SQL语句并提交事务
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        # 事务回滚
        conn.rollback()


def get_heroes(conn):
    """
    从数据库中获取英雄信息
    :param conn: 数据库连接对象
    :return: heroes 英雄信息字典
    """
    heroes = dict()
    # 数据库操作游标
    cursor = conn.cursor()
    # SQL查询语句
    sql = 'select * from {};'.format('heroes')
    try:
        # 执行SQL
        cursor.execute(sql)
        # 获取查询结果
        rows = cursor.fetchall()
        # 遍历结果，并将对应信息存储为字典
        for row in rows:
            heroes[row[0]] = {
                'h_id': row[0],
                'h_group': row[1],
                'h_name': row[2],
                'h_gender': row[3],
                'h_age': row[4],
                'h_identity': row[5],
                'h_lead': row[6],
                'h_force': row[7],
                'h_brain': row[8],
                'h_politics': row[9],
                'h_charm': row[10],
                'h_status': row[11]
            }
        return heroes
    except Exception as e:
        print(e)


def get_group_hero(conn, g_id):
    """
    获取势力所属英雄ID列表
    :param conn: 数据库连接对象
    :param g_id: 势力ID
    :return: group_hero
    """
    group_hero = list()
    # 数据库操作游标
    cursor = conn.cursor()
    sql = 'select {0} from {1} where {2} = {3}'.format('h_id', 'heroes', 'h_group', g_id)
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            group_hero.append(row[0])
        return group_hero
    except Exception as e:
        print(e)


def get_groups(conn):
    """
    获取所有势力ID列表及势力信息
    :param conn: 数据库连接对象
    :return: groups [group_list, {g_id: {k: v}}]
    """
    # 数据库操作游标
    cursor = conn.cursor()
    # 存储所有势力内容
    groups = dict()
    sql = 'select * from {}'.format('hero_group')
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            groups[row[0]] = {
                'g_id': row[0],
                'g_lord': row[1],
                'g_name': row[2],
                'g_economy': row[3],
                'g_farming': row[4],
                'g_military': row[5],
                'g_science': row[6],
                'g_morale': row[7],
                'g_gold': row[8],
                'g_rations': row[9],
                'g_corps': row[10],
                'g_experience': row[11],
                'g_ranker': row[12],
                'g_populace': row[13],
                'g_status': row[14]
            }
        return groups
    except Exception as e:
        print(e)


def get_ranker(conn):
    """
    获取兵种信息
    :param conn: 数据库连接对象
    :return: ranker {r_id: {k: v}}
    """
    cursor = conn.cursor()
    ranker = dict()
    sql = 'select * from {}'.format('ranker')
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            ranker[row[0]] = {
                'r_id': row[0],
                'r_name': row[1],
                'r_force': row[2],
                'r_defense': row[3],
                'r_level': row[4]
            }
        return ranker
    except Exception as e:
        print(e)


def get_gems(conn):
    """
    获取宝物信息
    :param conn: 数据库连接对象
    :return: gems
    """
    gems = dict()
    cursor = conn.cursor()
    sql = 'select * from {}'.format('gems')
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            gems[row[0]] = {
                't_id': row[0],
                't_name': row[1],
                't_lead': row[2],
                't_force': row[3],
                't_brain': row[4],
                't_politics': row[5],
                't_charm': row[6],
                't_group': row[7],
                't_hero': row[8],
                't_level': row[9]
            }
        return gems
    except Exception as e:
        print(e)


def get_group_gem(conn, g_id):
    """
    获取指定势力的宝物ID列表
    :param g_id: 
    :param conn: 
    :return: group_gem
    """
    group_gem = list()
    cursor = conn.cursor()
    sql = 'select {0} from {1} where {2} = {3}'.format('t_id', 'gems', 't_group', g_id)
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            group_gem.append(row[0])
        return group_gem
    except Exception as e:
        print(e)


def get_years(conn):
    """
    获取当前游戏时间
    :param conn: 数据库连接对象
    :return: years
    """
    cursor = conn.cursor()
    sql = 'select * from {}'.format('years')
    try:
        cursor.execute(sql)
        row = cursor.fetchone()
        years = [row[0], row[1]]
        return years
    except Exception as e:
        print(e)


def find_recluse(conn):
    """
    获取在野英雄ID列表
    :param conn: 
    :return: recluses [type:list]
    """
    recluses = list()
    cursor = conn.cursor()
    sql = 'select {0} from {1} where {2} = 1'.format('h_id', 'heroes', 'h_status')
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            recluses.append(row[0])
        return recluses
    except Exception as e:
        print(e)


def find_treasure(conn):
    """
    获取在野宝物ID列表
    :param conn: 
    :return: treasures [type:list]
    """
    treasures = list()
    cursor = conn.cursor()
    sql = ' select {0} from {1} where {2} = 0'.format('t_id', 'gems', 't_group')
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            treasures.append(row[0])
        return treasures
    except Exception as e:
        print(e)


def get_level_ranker(conn, level):
    """
    获取不同等级的兵种ID列表
    :param level: 
    :param conn: 
    :return: level_ranker [type:list]
    """
    level_ranker = list()
    cursor = conn.cursor()
    sql = 'select {0} from {1} where {2} = {3}'.format('r_id', 'ranker', 'r_level', level)
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            level_ranker.append(row[0])
        return level_ranker
    except Exception as e:
        print(e)
