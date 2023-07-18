from unittest.mock import patch

from scripts.parser.parser import _parser_game_event_actions


def test_parser_integration_parser_game_event_actions():
    log_mock = [
        '  0:00 ------------------------------------------------------------\n',
        '  0:00 InitGame: \\sv_floodProtect\\1\\sv_maxPing\n',
        ' 15:00 Exit: Timelimit hit.\n',
        ' 20:37 ClientBegin: 2\n',
        ' 20:37 ShutdownGame:\n',
        ' 20:37 ------------------------------------------------------------\n',
        ' 12:13 InitGame: \\sv_floodProtect\\1\\sv_maxPing\\0\\\n',
        ' 12:14 ClientConnect: 2\n',
        ' 12:24 Kill: 3 4 6: Isgalamido killed Zeh by MOD_ROCKET\n',
        ' 12:26 Kill: 3 2 7: Isgalamido killed Dono da Bola by MOD_ROCKET_SPLASH\n',
        ' 13:26 ClientDisconnect: 2\n',
        ' 13:50 Item: 2 weapon_railgun\n',
        ' 14:02 Kill: 1022 5 22: <world> killed Assasinu Credi by MOD_TRIGGER_HURT\n',
        ' 14:15 Kill: 2 5 10: Zeh killed Assasinu Credi by MOD_RAILGUN\n',
        ' 14:29 Kill: 5 5 7: Assasinu Credi killed Assasinu Credi by MOD_ROCKET_SPLASH\n',
        ' 14:38 Kill: 1022 5 22: <world> killed Assasinu Credi by MOD_TRIGGER_HURT\n',
        ' 14:39 Item: 2 weapon_rocketlauncher\n',
        ' 15:06 Kill: 5 2 6: Assasinu Credi killed Zeh by MOD_ROCKET\n',
        ' 15:09 Item: 5 weapon_railgun\n',
        ' 15:18 Kill: 2 5 7: Zeh killed Assasinu Credi by MOD_ROCKET_SPLASH\n',
        ' 15:21 Item: 5 weapon_rocketlauncher\n',
        ' 15:27 Kill: 1022 5 22: <world> killed Assasinu Credi by MOD_TRIGGER_HURT\n',
        ' 15:36 Kill: 5 5 7: Assasinu Credi killed Assasinu Credi by MOD_ROCKET_SPLASH\n',
        ' 15:38 Kill: 1022 2 22: <world> killed Zeh by MOD_TRIGGER_HURT\n',
        ' 15:54 Kill: 5 2 6: Assasinu Credi killed Zeh by MOD_ROCKET\n',
        ' 16:46 Kill: 1022 5 22: <world> killed Assasinu Credi by MOD_TRIGGER_HURT\n',
        ' 16:47 ClientDisconnect: 5\n',
        ' 27:14 Exit: Timelimit hit.',
    ]
    with patch('scripts.parser.parser._save_games') as mock_save_games:
        mock_save_games.return_value = []

        result = _parser_game_event_actions(log_mock)

    assert result == [
        {'game_1': {'total_kills': 0, 'players': [], 'kills': {}}},
        {
            'game_2': {
                'total_kills': 13,
                'players': [
                    'Isgalamido',
                    'Zeh',
                    'Dono da Bola',
                    'Assasinu Credi',
                ],
                'kills': {
                    'Isgalamido': 2,
                    'Zeh': 1,
                    'Dono da Bola': 0,
                    'Assasinu Credi': -2,
                },
            }
        },
    ]
