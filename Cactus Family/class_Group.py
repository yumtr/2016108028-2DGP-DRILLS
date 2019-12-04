import Cactus_Family
from pico2d import *


# 두 그룹 충돌 검사
def groups_collision_check(first_group, second_group):
    for i in first_group:
        for j in second_group:
            if Cactus_Family.cac[i].collision_to_cactus(Cactus_Family.cac[j]):
                return True


class Group:
    def __init__(self):
        self.all_cactus = []  # 합쳐진 선인장들의 그룹들
        self.merge_cactus_groups = []  # 충돌한 선인장들의 그룹
        self.single_cactus = []
        self.collision_sound = load_wav('sound_effect\\000029ab.wav')
        self.collision_sound.set_volume(100)

    # 싱글선인장에서 선인장끼리 붙어지면 그룹에 한번 넣음
    def make_cactus_group(self, coll_cac):
        self.single_cactus.remove(coll_cac)
        self.merge_cactus_groups.append([coll_cac])

        # 합쳐진 선인장그룹들 끼리 비교해서 병합함

    def group_checking(self):
        for i in range(len(self.merge_cactus_groups)):
            for j in range(len(self.merge_cactus_groups)):
                if not i == j:
                    if groups_collision_check(self.merge_cactus_groups[i], self.merge_cactus_groups[j]):
                        self.merge_cactus_groups[i].extend(self.merge_cactus_groups[j])
                        self.merge_cactus_groups[i].sort()
                        del self.merge_cactus_groups[j]
                        return

    def print_g(self):
        # print('모든 선인장', self.all_cactus)
        print('전체 그룹', self.merge_cactus_groups)
        print('그룹에 안속함', self.single_cactus)

    def update(self):
        for i in self.all_cactus:  # 충돌이 발생할때 한번만 부름
            if Cactus_Family.cac[i].is_collision:
                self.collision_sound.play()
                self.make_cactus_group(i)  # 그룹을 만든다
                self.all_cactus.remove(i)  # 충돌된 선인장을 전체 리스트에서 제거한다.
        self.group_checking()  # 항상 그룹끼리 체크해줌
