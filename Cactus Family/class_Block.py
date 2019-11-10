from pico2d import *
import Cactus_Family

LEFT_COLLISION, TOP_COLLISION, RIGHT_COLLISION, BOTTOM_COLLISION = range(4)
ST_X_NONE, ST_X_FORWARD, ST_X_BAKWARD, ST_Y_NONE, ST_Y_UP, ST_Y_DOWN = range(6)


def is_player_collision_to_cac_group(group):
    for i in group:
        if Cactus_Family.cac[i].collision_to_cactus(Cactus_Family.player):
            return True


class Block:
    def __init__(self, pos = [400, 300]):
        self.x = pos[1] * 100
        self.y = pos[0] * 100
        self.rect = self.x - 50, self.y + 50, self.x + 50, self.y - 50
        self.collision_judgment = True

    def set_position(self, pos):
        self.x = pos[1] * 100
        self.y = pos[0] * 100

    # 플레이어랑 벽하고 충돌
    def collision_stone_to_block(self):
        if self.rect[0] + Cactus_Family.player.speed == Cactus_Family.player.rect[2] \
                and self.y == Cactus_Family.player.y:
            Cactus_Family.player.x_dir = ST_X_NONE
            Cactus_Family.player.x -= Cactus_Family.player.speed
        elif self.rect[2] - Cactus_Family.player.speed == Cactus_Family.player.rect[0] \
                and self.y == Cactus_Family.player.y:
            Cactus_Family.player.x_dir = ST_X_NONE
            Cactus_Family.player.x += Cactus_Family.player.speed
        elif self.rect[1] - Cactus_Family.player.speed == Cactus_Family.player.rect[3] \
                and self.x == Cactus_Family.player.x:
            Cactus_Family.player.y_dir = ST_Y_NONE
            Cactus_Family.player.y += Cactus_Family.player.speed
        elif self.rect[3] + Cactus_Family.player.speed == Cactus_Family.player.rect[1] \
                and self.x == Cactus_Family.player.x:
            Cactus_Family.player.y_dir = ST_Y_NONE
            Cactus_Family.player.y -= Cactus_Family.player.speed

    # 싱글 선인장이랑 벽하고 충돌
    def collision_single_cactus_to_block(self, ano):
        # if ano.collision_to_cactus(Cactus_Family.player):   # 돌하고 닿아있으면
        #     if self.rect[0] == ano.rect[2] and self.y == ano.y:
        #         # Cactus_Family.player.forward_access = False
        #         Cactus_Family.player.move_judge(ST_X_FORWARD)
        #         return False
        #     elif self.rect[2] == ano.rect[0] and self.y == ano.y:
        #         # Cactus_Family.player.bakward_access = False
        #         Cactus_Family.player.move_judge(ST_X_BAKWARD)
        #         return False
        #     if self.rect[1] == ano.rect[3] and self.x == ano.x:
        #         # Cactus_Family.player.down_access = False
        #         Cactus_Family.player.move_judge(ST_Y_DOWN)
        #         return False
        #     if self.rect[3] == ano.rect[1] and self.x == ano.x:
        #         # Cactus_Family.player.up_access = False
        #         Cactus_Family.player.move_judge(ST_Y_UP)
        #         return False
        # else:   # 돌하고 안닿아있으면 참
        #     return True
        if self.rect[0] + ano.speed == ano.rect[2] and self.y == ano.y:
            Cactus_Family.player.x_dir = ST_X_NONE
            Cactus_Family.player.x -= Cactus_Family.player.speed * 2
            ano.x_dir = ST_X_NONE
            ano.x -= ano.speed

        elif self.rect[2] - ano.speed == ano.rect[0] and self.y == ano.y:
            Cactus_Family.player.x_dir = ST_X_NONE
            Cactus_Family.player.x += Cactus_Family.player.speed * 2
            ano.x_dir = ST_X_NONE
            ano.x += ano.speed

        elif self.rect[1] - ano.speed == ano.rect[3] and self.x == ano.x:
            Cactus_Family.player.y_dir = ST_Y_NONE
            Cactus_Family.player.y += Cactus_Family.player.speed * 2
            ano.y_dir = ST_Y_NONE
            ano.y += ano.speed

        elif self.rect[3] + ano.speed == ano.rect[1] and self.x == ano.x:
            Cactus_Family.player.y_dir = ST_Y_NONE
            Cactus_Family.player.y -= Cactus_Family.player.speed * 2
            ano.y_dir = ST_Y_NONE
            ano.y -= ano.speed

    # 그룹 선인장이랑 벽하고 충돌
    def collision_group_cactus_to_block(self, group):
        if is_player_collision_to_cac_group(group):
            for i in group:
                if self.rect[0] == Cactus_Family.cac[i].rect[2] and self.y == Cactus_Family.cac[i].y:
                    Cactus_Family.player.move_judge(ST_X_FORWARD)
                    return False
                elif self.rect[2] == Cactus_Family.cac[i].rect[0] and self.y == Cactus_Family.cac[i].y:
                    Cactus_Family.player.move_judge(ST_X_BAKWARD)
                    return False
                elif self.rect[1] == Cactus_Family.cac[i].rect[3] and self.x == Cactus_Family.cac[i].x:
                    Cactus_Family.player.move_judge(ST_Y_DOWN)
                    return False
                elif self.rect[3] == Cactus_Family.cac[i].rect[1] and self.x == Cactus_Family.cac[i].x:
                    Cactus_Family.player.move_judge(ST_Y_UP)
                    print('dsds')
                    return False
        else:
            return True

    def update(self):
        self.rect = [self.x - 50, self.y + 50, self.x + 50, self.y - 50]
        self.collision_stone_to_block()

        for i in Cactus_Family.cactus_group.single_cactus:
            self.collision_single_cactus_to_block(Cactus_Family.cac[i])

        self.collision_judgment = True
        for i in range(len(Cactus_Family.cactus_group.merge_cactus_groups)):
            if self.collision_group_cactus_to_block(Cactus_Family.cactus_group.merge_cactus_groups[i]):
                self.collision_judgment = True
            else:
                self.collision_judgment = False
        if self.collision_judgment:  # 아무 충돌도없다는 거니까 아무대나 움직일수있게
            Cactus_Family.player.forward_access = True
            Cactus_Family.player.bakward_access = True
            Cactus_Family.player.up_access = True
            Cactus_Family.player.down_access = True

    def render(self):
        if Cactus_Family.debug_mode:
            draw_rectangle(self.rect[0], self.rect[1], self.rect[2], self.rect[3])
        pass
