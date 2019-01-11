import random
from Hero_Era_Pro import PrintMsgs as PM, GetConn as Conn
from Hero_Era_Pro import Group_Builder as GB
from Hero_Era_Pro import Hero_Builder as HB
from Hero_Era_Pro import Main


class Game:
    """
    游戏主体控制类
    """
    def __init__(self):
        """
        初始化方法，初始化一个数据库连接对象
        """
        self.conn = Conn.get_conn('hero_era')
    
    def new_game(self, h_num, g_num, avg_num, r_num, c_num, game_hard):
        """
        新游戏执行操作
        :param game_hard: 游戏难度
        :param h_num: 新游戏生成英雄总数 
        :param g_num: 新游戏生成势力总数
        :param avg_num: 新游戏平均分配到各势力的英雄数
        :param r_num: 新游戏势力英雄数波动范围
        :param c_num: 新游戏玩家创建新势力最大可选择的最大英雄数
        :return: None
        """
        # 初始化数据库表
        Conn.create_hero_table(self.conn)
        Conn.create_group_table(self.conn, game_hard)
        Conn.create_den_table(self.conn)
        # 自动生成英雄和势力
        HB.auto_create_hero(self.conn, h_num)
        GB.auto_create_group(self.conn, g_num, avg_num, r_num)
        choice = int(input('1 新建英雄  2 选择势力\n'))
        if choice == 1:
            # 新建英雄
            new_hero = HB.new_hero(self.conn)
            choice_lord = int(input('是否使用新建英雄新建势力，选择是则新建英雄作为势力主公新建势力，否则新建英雄成为在野英雄：\n1 是  2 否\n'))
            if choice_lord == 1:
                # 新建势力
                GB.new_group(self.conn, new_hero, c_num)
        # 获取英雄和势力信息
        heroes = Conn.get_heroes(self.conn)
        groups = Conn.get_groups(self.conn)
        PM.print_choice_group(self.conn, groups, heroes)
        choice = input().strip()
        # 玩家扮演势力标记修改
        g_play = dict()
        g_play['g_status'] = 1
        condition = 'g_id = {}'.format(choice)
        Conn.update_data(self.conn, 'hero_group', g_play, condition)
        # 宝物数据初始化
        gems = dict()
        gems['t_group'] = 0
        gems['t_hero'] = 0
        Conn.clear_data(self.conn, 'gems', gems)
        # 纪年初始化
        years = dict()
        years['year'] = 184
        years['month'] = 1
        Conn.clear_data(self.conn, 'years', years)
        # 运行游戏主体
        Main.run(self.conn)

    def continue_game(self):
        """
        继续游戏执行操作
        :return: None
        """
        # 运行游戏主体
        Main.run(self.conn)


if __name__ == '__main__':
    print('乱世君临，等你来战！')
    start = int(input('1 初临乱世\n2 烽火再起\n3 退隐山林\n'))
    if start == 1:
        games_hard = int(input('请选择游戏难度：\n1 简单  2 普通  3 困难  4 地狱\n'))
        if games_hard == 1:
            Game().new_game(50, 5, random.randint(2, 5), random.randint(3, 5), 5, games_hard)
        elif games_hard == 2:
            Game().new_game(80, 5, random.randint(5, 10), random.randint(4, 6), 8, games_hard)
        elif games_hard == 3:
            Game().new_game(100, 5, random.randint(8, 12), random.randint(5, 8), 10, games_hard)
        elif games_hard == 4:
            Game().new_game(200, 8, random.randint(12, 20), random.randint(6, 8), 12, games_hard)
    elif start == 2:
        Game().continue_game()
    else:
        print('山高水长，江湖再见！')
