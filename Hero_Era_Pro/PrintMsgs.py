from Hero_Era_Pro import GetConn as Conn


def print_group_info(group, ranker, year, month):
    print('{0}年{1}月'.format(year, month))
    print('势力：{0:<6}\t经济：{1:<4}\t农业：{2:<4}\t军事：{3:<4}\t科技：{4:<4}\t民心：{5:<4}\t黄金：{6:<8}\t 粮草：{7:<8}\t'
          '兵力：{8:<8}\t兵种：{9:<6}\t人口：{10:<8}'.format(
            group.get('g_name'), group.get('g_economy'), group.get('g_farming'), group.get('g_military'),
            group.get('g_science'), group.get('g_morale'), group.get('g_gold'), group.get('g_rations'),
            group.get('g_ranker'), ranker.get(group.get('g_corps')).get('r_name'), group.get('g_populace'))
          )


def print_groups_info(groups, conn, heroes):
    print('{0:<12}\t{1:<10}\t{2:<4}\t{3:<4}\t{4:<4}\t{5:<4}\t{6:<4}\t{7:<8}\t{8:<8}\t{9:<8}\t{10:<8}\t{11:<4}'.format(
        '全势力', '主公', '经济', '农业', '军事', '科技', '民心', '黄金', '粮草', '人口', '兵力', '英雄数')
    )
    for g_id in groups.keys():
        print('{0:<12}\t{1:<10}\t{2:<4}\t{3:<4}\t{4:<4}\t{5:<4}\t{6:<4}\t{7:<8}\t{8:<8}\t{9:<8}\t{10:<8}\t{11:<4}'.format(
            groups.get(g_id).get('g_name'), heroes.get(groups.get(g_id).get('g_lord')).get('h_name'),
            groups.get(g_id).get('g_economy'), groups.get(g_id).get('g_farming'),
            groups.get(g_id).get('g_military'), groups.get(g_id).get('g_science'),
            groups.get(g_id).get('g_morale'), groups.get(g_id).get('g_gold'),
            groups.get(g_id).get('g_rations'), groups.get(g_id).get('g_populace'),
            groups.get(g_id).get('g_ranker'), len(Conn.get_group_hero(conn, g_id)))
        )


def print_heroes_info(groups, heroes):
    print('{0:<10}\t{1:<6}\t{2:<6}\t{3:<6}\t{4:<6}\t{5:<6}\t{6:<6}\t{7:<6}\t{8:<6}\t{9:<6}'.format(
        '姓名', '性别', '年龄', '身份', '统率', '武力', '智力', '政治', '魅力', '所属')
    )
    for h_id in heroes.keys():
        print('{0:<10}\t{1:<6}\t{2:<6}\t{3:<6}\t{4:<6}\t{5:<6}\t{6:<6}\t{7:<6}\t{8:<6}\t{9:<6}'.format(
            heroes.get(h_id).get('h_name'), heroes.get(h_id).get('h_gender'), heroes.get(h_id).get('h_age'),
            heroes.get(h_id).get('h_identity'), heroes.get(h_id).get('h_lead'), heroes.get(h_id).get('h_force'),
            heroes.get(h_id).get('h_brain'), heroes.get(h_id).get('h_politics'), heroes.get(h_id).get('h_charm'),
            groups.get(heroes.get(h_id).get('h_group')).get('g_name') if groups.get(heroes.get(h_id).get('h_group')) is not None else '无')
        )


def print_group_hero(group_hero, heroes):
    print('请指定英雄ID\n{0:<6}\t{1:<10}\t{2:<6}\t{3:<6}\t{4:<6}\t{5:<6}\t{6:<6}\t{7:<6}\t{8:<6}\t{9:<6}'.format(
        'ID', '姓名', '性别', '年龄', '身份', '统率', '武力', '智力', '政治', '魅力')
    )
    for h_id in group_hero:
        print('{0:<6}\t{1:<10}\t{2:<6}\t{3:<6}\t{4:<6}\t{5:<6}\t{6:<6}\t{7:<6}\t{8:<6}\t{9:<6}'.format(
            h_id, heroes.get(h_id).get('h_name'), heroes.get(h_id).get('h_gender'), heroes.get(h_id).get('h_age'),
            heroes.get(h_id).get('h_identity'), heroes.get(h_id).get('h_lead'), heroes.get(h_id).get('h_force'),
            heroes.get(h_id).get('h_brain'), heroes.get(h_id).get('h_politics'),
            heroes.get(h_id).get('h_charm'))
        )


def print_choice_group(conn, groups, heroes):
    print('请选择扮演势力ID：')
    print('{0:<4}\t{1:<12}\t{2:<10}\t{3:<6}'.format('ID', '名称', '主公', '英雄数'))
    # 列出所有势力基本信息
    for g_id in groups.keys():
        print('{0:<4}\t{1:<12}\t{2:<10}\t{3:<6}'.format(
            g_id, groups.get(g_id).get('g_name'),
            heroes.get(groups.get(g_id).get('g_lord')).get('h_name'),
            len(Conn.get_group_hero(conn, g_id)))
        )


def print_gems_info(groups, gems, heroes):
    print('{0:<4}\t{1:<12}\t{2:^8}\t{3:^8}\t{4:^8}\t{5:^8}\t{6:^8}\t{7:<12}\t{8:<6}'.format(
        'ID', '名称', '统率增益', '武力增益', '智力增益', '政治增益', '魅力增益', '所属势力', '所属英雄')
    )
    for t_id in gems.keys():
        print('{0:<4}\t{1:<12}\t{2:^8}\t{3:^8}\t{4:^8}\t{5:^8}\t{6:^8}\t{7:<12}\t{8:<6}'.format(
            t_id, gems.get(t_id).get('t_name'), gems.get(t_id).get('t_lead'), gems.get(t_id).get('t_force'),
            gems.get(t_id).get('t_brain'), gems.get(t_id).get('t_politics'), gems.get(t_id).get('t_charm'),
            groups.get(gems.get(t_id).get('t_group')).get('g_name') if groups.get(gems.get(t_id).get('t_group')) is not None else '无',
            heroes.get(gems.get(t_id).get('t_hero')).get('h_name') if heroes.get(gems.get(t_id).get('t_hero')) is not None else '无')
        )
            

def print_corps_info(level_ranker, ranker):
    print('{0:<4}\t{1:<12}\t{2:^8}\t{3:^8}'.format(
        'ID', '名称', '攻击力', '防御力')
    )
    for r_id in level_ranker:
        print('{0:<4}\t{1:<12}\t{2:^8}\t{3:^8}'.format(
            r_id, ranker.get(r_id).get('r_name'), ranker.get(r_id).get('r_force'), ranker.get(r_id).get('r_defense'))
        )


def print_choice_hero(h_candidate, c_num, heroes):
    print('请选择加入新势力的英雄ID(当前游戏难度最多可选择{}名英雄加入新势力，ID之间以空格隔开)：'.format(c_num))
    print('请选择执行英雄ID\n{0:<6}\t{1:<10}\t{2:<6}\t{3:<6}\t{4:<6}\t{5:<6}\t{6:<6}\t{7:<6}\t{8:<6}\t{9:<6}'.format(
        'ID', '姓名', '性别', '年龄', '身份', '统率', '武力', '智力', '政治', '魅力')
    )
    # 从候选英雄ID列表中循环获取c_num*2个英雄信息进行展示
    for h_id in h_candidate[:c_num * 2]:
        print('{0:<6}\t{1:<10}\t{2:<6}\t{3:<6}\t{4:<6}\t{5:<6}\t{6:<6}\t{7:<6}\t{8:<6}\t{9:<6}'.format(
            h_id, heroes.get(h_id).get('h_name'), heroes.get(h_id).get('h_gender'), heroes.get(h_id).get('h_age'),
            heroes.get(h_id).get('h_identity'), heroes.get(h_id).get('h_lead'), heroes.get(h_id).get('h_force'),
            heroes.get(h_id).get('h_brain'), heroes.get(h_id).get('h_politics'), heroes.get(h_id).get('h_charm'))
        )


def print_choice_gem(group_gem, gems, heroes):
    print('{0:<4}\t{1:<12}\t{2:^8}\t{3:^8}\t{4:^8}\t{5:^8}\t{6:^8}\t{7:<6}'.format(
        'ID', '名称', '统率增益', '武力增益', '智力增益', '政治增益', '魅力增益', '持有英雄')
    )
    for t_id in group_gem:
        print('{0:<4}\t{1:<12}\t{2:^8}\t{3:^8}\t{4:^8}\t{5:^8}\t{6:^8}\t{7:<6}'.format(
            t_id, gems.get(t_id).get('t_name'), gems.get(t_id).get('t_lead'), gems.get(t_id).get('t_force'),
            gems.get(t_id).get('t_brain'), gems.get(t_id).get('t_politics'), gems.get(t_id).get('t_charm'),
            heroes.get(gems.get(t_id).get('t_hero')).get('h_name') if heroes.get(gems.get(t_id).get('t_hero')) is not None else '无')
        )
