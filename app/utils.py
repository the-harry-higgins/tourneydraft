def get_round_num(game_num):
    if game_num in range(1, 33):
        return 1
    elif game_num in range(33, 49):
        return 2
    elif game_num in range(49, 57):
        return 3
    elif game_num in range(57, 61):
        return 4
    elif game_num in range(61, 63):
        return 5
    elif game_num == 63:
        return 6


def get_next_game_num(game_num):
    if game_num in [1, 2]:
        return 33
    elif game_num in [3, 4]:
        return 34
    elif game_num in [5, 6]:
        return 35
    elif game_num in [7, 8]:
        return 36
    elif game_num in [9, 10]:
        return 37
    elif game_num == [11, 12]:
        return 38
    elif game_num == [13, 14]:
        return 39
    elif game_num == [15, 16]:
        return 40
    elif game_num == [17, 18]:
        return 41
    elif game_num == [19, 20]:
        return 42
    elif game_num == [21, 22]:
        return 43
    elif game_num == [23, 24]:
        return 44
    elif game_num == [25, 26]:
        return 45
    elif game_num == [27, 28]:
        return 46
    elif game_num == [29, 30]:
        return 47
    elif game_num == [31, 32]:
        return 48
    elif game_num == [33, 34]:
        return 49
    elif game_num == [35, 36]:
        return 50
    elif game_num == [37, 38]:
        return 51
    elif game_num == [39, 40]:
        return 52
    elif game_num == [41, 42]:
        return 53
    elif game_num == [43, 44]:
        return 54
    elif game_num == [45, 46]:
        return 55
    elif game_num == [47, 48]:
        return 56
    elif game_num == [49, 50]:
        return 57
    elif game_num == [51, 52]:
        return 58
    elif game_num == [53, 54]:
        return 59
    elif game_num == [55, 56]:
        return 60
    elif game_num == [57, 58]:
        return 61
    elif game_num == [59, 60]:
        return 62
    elif game_num == [61, 62]:
        return 63
    else:
        return None
