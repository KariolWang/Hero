#! D:/Tools/Python35

from Hero_Era_Pro import GetConn

conn = GetConn.get_conn('hero_era')
group = GetConn.get_groups(conn).get(1)
ranker = GetConn.get_ranker(conn)
g_corps = group.get('g_corps')
gems = GetConn.get_gems(conn)

group_gem = GetConn.get_group_gem(conn, group.get('g_id'))
if len(group_gem) > 0:
    group_gem = [t_id for t_id in group_gem if gems.get(t_id).get('t_hero') != 0]
    print(len(group_gem) == 0)
