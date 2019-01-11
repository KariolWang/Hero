from Hero_Era_Pro import PrintMsgs as PM, GetConn as Conn
from Hero_Era_Pro import MainAI
from Hero_Era_Pro import Manage_Group as MG


def run(conn):
    """
    游戏运行主体
    :param conn: 数据库连接对象
    :return: None
    """
    # 获取游戏纪年
    years = Conn.get_years(conn)
    # 年标记
    year = years[0]
    # 回合标记
    time = years[1]
    # 玩家势力信息字典
    group = dict()
    print('\n{0}恭迎主公！{1}\n'.format('-'*70, '-'*70))
    while True:
        print('*' * 150)
        # 月标记
        month = 12 if time % 12 == 0 else time % 12
        # 获取所有势力信息
        groups = Conn.get_groups(conn)
        # 获取所有英雄信息
        heroes = Conn.get_heroes(conn)
        # 获取所有宝物信息
        gems = Conn.get_gems(conn)
        # 获取所有兵种信息
        ranker = Conn.get_ranker(conn)
        # 取出标记为玩家的势力信息
        for k, v in groups.items():
            if v.get('g_status') == 1:
                group = groups.get(k)
        PM.print_group_info(group, ranker, year, month)
        g_id = group.get('g_id')
        # 获取玩家势力中英雄ID列表
        group_hero = Conn.get_group_hero(conn, g_id)
        # 游戏纪年更新
        now_years = dict()
        now_years['year'] = year
        now_years['month'] = month
        Conn.clear_data(conn, 'years', now_years)
        start = int(input('新的一月，请主公决策：\n1 势力朝会  2 退隐山林\n'))
        if start != 1:
            print('\n{0}恭送主公！{1}\n'.format('-'*70, '-'*70))
            exit()
        # 循环，直到势力所有英雄都有了任务或选择了退朝，执行任务
        while True:
            # 主命令
            # 内政：经济 农业 军事 科技 民心
            # 军政：募兵 训练 巡逻 征讨
            # 英雄：寻访 
            #      官职：擢升 罢黜
            #      赏罚：赏赐 罚没
            # 市场：粮草交易：买进 卖出
            #      宝物交易：收购 贩卖
            # 情报：势力 英雄 宝物 兵种
            # 退朝
            main_order = int(input('请下达命令：1 内政  2 军政  3 英雄  4 市场  5 情报  0 退朝\n'))
            if main_order not in [1, 2, 3, 4, 5]:
                break
            # 内政命令
            if main_order == 1:
                # 次命令
                # 经济 农业 军事 科技 民心
                manage_order = int(input('请选择内政策略：1 经济  2 农业  3 军事  4 科技  5 民心  0 取消\n'))
                if manage_order not in [1, 2, 3, 4, 5]:
                    continue
                # 执行听候差遣的英雄列表
                c_hero = choice_executor(group_hero, heroes)
                hero_id = c_hero[0]
                check = int(input('任务需要经费黄金{}两，是否执行：\n1 是  2 否\n'.format(50*len(hero_id))))
                # 经济
                if manage_order == 1:
                    if check == 1:
                        # 执行经济开发操作
                        group = MG.get_economy(conn, group, heroes, hero_id, check)
                # 农业
                elif manage_order == 2:
                    if check == 1:
                        # 执行农业开发操作
                        group = MG.get_farming(conn, group, heroes, hero_id, check)
                # 军事
                elif manage_order == 3:
                    if check == 1:
                        # 执行军事提升操作
                        group = MG.get_military(conn, group, heroes, hero_id, check)
                # 科技
                elif manage_order == 4:
                    if check == 1:
                        # 执行科技提升操作
                        group = MG.get_science(conn, group, heroes, hero_id, check)
                # 民心
                else:
                    if check == 1:
                        # 执行民心提升操作
                        group = MG.get_morale(conn, group, heroes, hero_id, check)
                group_hero = c_hero[1]
                # 势力英雄都执行任务后自动结束本回合
                if len(group_hero) == 0:
                    print('谨遵圣谕，臣等告退！')
                    break
            # 军政命令
            elif main_order == 2:
                # 次命令
                # 募兵 训练 巡逻 征讨
                manage_order = int(input('请选择军政策略：1 募兵  2 训练  3 巡逻  4 征讨  0 取消\n'))
                if manage_order not in [1, 2, 3, 4]:
                    continue
                # 执行听候差遣的英雄列表
                c_hero = choice_executor(group_hero, heroes)
                hero_id = c_hero[0]
                # 募兵
                if manage_order == 1:
                    # 计算最大招募兵力数
                    max_ranker = round(group.get('g_populace')/50)
                    new_ranker = int(input('当前最大可招募兵力为{}，请输入本次招募兵力数：\n'.format(max_ranker)))
                    check = int(input('是否确认招募新兵{}人：\n1 是  2 否\n'.format(new_ranker)))
                    if check == 1:
                        # 执行士兵招募操作
                        group = MG.get_ranker(conn, group, heroes, hero_id, max_ranker, new_ranker, check)
                    else:
                        continue
                # 训练
                elif manage_order == 2:
                    check = int(input('请指定训练内容：\n1 变更兵种  2 常规训练  3 强化训练\n'))
                    if check not in [1, 2, 3]:
                        check = 2
                    if check == 1:
                        exp = group.get('g_experience')
                        level = (1 if exp < 50 else 2 if exp < 200 else 3 if exp < 450 else 4 if exp < 950 else 5)
                        level_ranker = Conn.get_level_ranker(conn, level)
                        PM.print_corps_info(level_ranker, ranker)
                        choice = int(input('请指定变更兵种ID：'))
                        if choice not in level_ranker:
                            continue
                        MG.change_corps(conn, group, ranker, choice)
                    elif check == 2:
                        t_type = 1  # 常规训练
                        group = MG.train_corps(conn, group, heroes, hero_id, t_type)
                    else:
                        t_type = 2  # 强化训练
                        group = MG.train_corps(conn, group, heroes, hero_id, t_type)
                        
                # 巡逻
                elif manage_order == 3:
                    p_group = MG.patrol_group(conn, group, heroes, hero_id)
                    group = p_group[0]
                    r_type = p_group[1]
                    if r_type == 2:     # 讨贼巡逻，发现贼寇探子，完成讨贼
                        spy = MG.find_spy(group)
                        group = MG.fight_enemy(conn, group, heroes, hero_id, spy)
                    elif r_type == 3:   # 据点巡逻，发现贼寇据点
                        MG.find_den(conn, group, ranker)
                # 征讨
                else:
                    print('征讨胜利')
                group_hero = c_hero[1]
                # 势力英雄都执行任务后自动结束本回合
                if len(group_hero) == 0:
                    print('谨遵圣谕，臣等告退！')
                    break
            # 英雄命令
            elif main_order == 3:
                # 次命令
                # 寻访
                # 官职：擢升 罢黜
                # 赏罚：赏赐 罚没
                manage_order = int(input('请选择执行内容：1 寻访  2 官职  3 赏罚  0 取消\n'))
                if manage_order not in [1, 2, 3]:
                    continue
                # 寻访
                if manage_order == 1:
                    # 执行听候差遣的英雄列表
                    c_hero = choice_executor(group_hero, heroes)
                    hero_id = c_hero[0]
                    group_hero = c_hero[1]
                    group = MG.find_recluse_treasure(conn, group, heroes, hero_id, gems)
                # 官职
                elif manage_order == 2:
                    group_heroes = Conn.get_group_hero(conn, group.get('g_id'))
                    PM.print_group_hero(group_heroes, heroes)
                    h_id = int(input().strip())
                    key_order = int(input('请选择任免：1 擢升  2 罢黜  0 取消\n'))
                    if key_order == 1:
                        print('擢升了官职')
                    elif key_order == 2:
                        print('罢黜了官职')
                    else:
                        continue
                # 赏罚
                else:
                    key_order = int(input('请选择赏罚：1 赏赐  2 罚没  0 取消\n'))
                    if key_order == 1:
                        # 获取玩家势力中宝物ID列表
                        group_gem = Conn.get_group_gem(conn, group.get('g_id'))
                        if len(group_gem) > 0:
                            group_heroes = Conn.get_group_hero(conn, group.get('g_id'))
                            PM.print_group_hero(group_heroes, heroes)
                            h_id = int(input().strip())
                            group_gem = [t_id for t_id in group_gem if gems.get(t_id).get('t_hero') == 0]
                            PM.print_choice_gem(group_gem, gems, heroes)
                            t_id = int(input('请输入赏赐宝物ID：\n'))
                            heroes = MG.rewards_hero(conn, group, gems, t_id, heroes, h_id, 1)
                    elif key_order == 2:
                        # 获取玩家势力中宝物ID列表
                        group_gem = Conn.get_group_gem(conn, group.get('g_id'))
                        if len(group_gem) > 0:
                            group_gem = [t_id for t_id in group_gem if gems.get(t_id).get('t_hero') != 0]
                            if len(group_gem) == 0:
                                print('无持有宝物的英雄！')
                                continue
                            PM.print_choice_gem(group_gem, gems, heroes)
                            t_id = int(input('请输入收回宝物ID：\n'))
                            heroes = MG.rewards_hero(conn, group, gems, t_id, heroes, gems.get(t_id).get('t_hero'), 2)
                    else:
                        continue
                # 势力英雄都执行任务后自动结束本回合
                if len(group_hero) == 0:
                    print('谨遵圣谕，臣等告退！')
                    break
            # 市场命令
            elif main_order == 4:
                # 次命令
                # 粮草交易：买进 卖出
                # 宝物交易：收购 贩卖
                manage_order = int(input('请选择交易内容：1 粮草交易  2 宝物交易  0 取消\n'))
                if manage_order not in [1, 2]:
                    continue
                # 执行听候差遣的英雄列表
                c_hero = choice_executor(group_hero, heroes)
                hero_id = c_hero[0]
                # 粮草交易
                if manage_order == 1:
                    key_order = int(input('请选择交易类型：1 买进  2 卖出  0 取消\n'))
                    if key_order == 1:
                        print('买进了粮草')
                    elif key_order == 2:
                        print('卖出了粮草')
                    else:
                        continue
                # 宝物交易
                else:
                    key_order = int(input('请选择交易类型：1 收购  2 贩卖  0 取消\n'))
                    if key_order == 1:
                        print('收购了宝物')
                    elif key_order == 2:
                        print('贩卖了宝物')
                    else:
                        continue
                group_hero = c_hero[1]
                # 势力英雄都执行任务后自动结束本回合
                if len(group_hero) == 0:
                    print('谨遵圣谕，臣等告退！')
                    break
            # 情报命令
            else:
                # 次命令
                # 势力 英雄 宝物 兵种
                query_order = int(input('请选择情报内容：1 势力一览  2 英雄一览  3 宝物一览  4 兵种一览\n'))
                if query_order not in [1, 2, 3, 4]:
                    continue
                # 势力情报
                if query_order == 1:
                    PM.print_groups_info(groups, conn, heroes)
                # 英雄情报
                elif query_order == 2:
                    PM.print_heroes_info(groups, heroes)
                # 宝物情报
                elif query_order == 3:
                    PM.print_gems_info(groups, gems, heroes)
                # 兵种情报
                else:
                    level_ranker = ranker.keys()
                    PM.print_corps_info(level_ranker, ranker)
                # 势力英雄都执行任务后自动结束本回合
                if len(group_hero) == 0:
                    print('谨遵圣谕，臣等告退！')
                    break
        # 每月势力人口增加
        group = MG.get_populace(conn, group)
        # 每月势力粮草消耗
        group = MG.eat_rations(conn, group, heroes, ranker)
        # 对势力现状评定，有几率触发特殊事件
        MG.check_group(conn, group, heroes, gems)
        # 每三个回合即每个季度执行
        if time % 3 == 0:
            # 发放军饷
            group = MG.pay_provisions(conn, group, heroes, ranker)
            # 势力黄金收入
            group = MG.get_gold(conn, group)
            # 势力粮草收入
            group = MG.get_rations(conn, group)
        # 每12个回合及每年执行
        if time % 12 == 0:
            # 游戏纪年增加
            year += 1
            hero = dict()
            # 所有英雄年龄增加
            for h_id in heroes.keys():
                hero['h_age'] = heroes.get(h_id).get('h_age') + 1
                # 如果英雄年龄增加后超过70岁，则英雄状态变更为死亡
                if hero.get('h_age') > 70:
                    hero['h_status'] = 0
                    hero['h_group'] = 0
                    print('{0}{1}年岁已高，不幸病逝！'.format(
                        groups.get(heroes.get(h_id).get('h_group')).get('g_name'), heroes.get(h_id).get('h_name'))
                    )
                condition = 'h_id = {}'.format(h_id)
                Conn.update_data(conn, 'heroes', hero, condition)
        # 电脑势力执行任务
        MainAI.run(conn, time)
        time += 1


def choice_executor(group_hero, heroes):
    c_hero = list()
    PM.print_group_hero(group_hero, heroes)
    # 将输入的字符串以空格且分为str_list列表，使用list(map(int, str_list))将str_list转换为int_list
    hero_id = list(map(int, input().strip().split(' ')))
    for h_id in hero_id:
        try:
            group_hero.remove(h_id)
        except Exception as e:
            print('所选英雄ID{}不存在！'.format(h_id), e)
            hero_id.remove(h_id)
    c_hero.append(hero_id)
    c_hero.append(group_hero)
    return c_hero
