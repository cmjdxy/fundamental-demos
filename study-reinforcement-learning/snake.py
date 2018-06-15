# -*- coding: utf-8 -*-
"""
A new file.
"""
import matplotlib.pyplot as plt
import numpy as np


plt.style.use('seaborn')
#np.random.seed(233)


class Snake:
    '''
    <名称>
        snake: 蛇棋
    <属性>
        states: 状态空间
        actions: 行为空间
    <方法>
        reward: 奖励函数
        get_transit_table: 状态转移表
    '''
    # 构造器
    def __init__(self, num_ladders, dice_ranges):
        self.num_ladders = num_ladders
        self.dice_ranges = dice_ranges
        self.ladders = self._get_ladders()
        self.states = list(range(100))
    # 主要方法
    def run(self, init_state, action, max_step=None):
        n_iter = 0
        trail = [init_state]
        if init_state == self.states[-1]:
            print('Terminal arrived! Iterations: {0}'.format(n_iter))
            print('Trail:', trail)
        else:
            while init_state != self.states[-1]:
                step = np.random.choice(self.dice_ranges[action]) # 选哪个骰子
                init_state = self._move_state(init_state, step)
                n_iter += 1
                trail.append(init_state)
            print('Terminal arrived! Iterations: {0}'.format(n_iter))
            print('Trail:', trail)
    def get_transit_table(self):
        transit_table = np.zeros([len(self.dice_ranges), 100, 100]).tolist()
        for i, dice in enumerate(self.dice_ranges):
            prob = 1 / dice
            for state in self.states:
                for step in range(1, dice + 1):
                    next_state = self._move_state(state, step)
                    transit_table[i][state][next_state] += prob
            transit_table[i][-1][-1] = [1] * len(self.dice_ranges)
        return transit_table
    def get_reward_table(self):
        reward_table = [-1] * 100
        reward_table[-1] = 100
        return reward_table
    # 辅助方法
    def _get_ladders(self):
        ladders = dict(np.random.choice(range(100),
                                        size=[self.num_ladders, 2],
                                        replace=False))
        reverse_ladders = {v : k for k, v in ladders.items()}
        ladders.update(reverse_ladders)
        return ladders
    def _move_state(self, state, step):
        state += step
        if state > self.states[-1]:
            state = 2 * self.states[-1] - state - step # 撞墙回头
        if state in self.ladders:
            state = self.ladders[state] # 爬梯子
        return state


class TableAgent:
    '''
    <名称>
        代理表
    <属性>
        状态转移表
        奖励表
        状态数
        行动数
        策略
        其它参数
    <方法>
    '''
    # 构造器
    def __init__(self, transit_table, reward_table):
        self.transit_table = transit_table
        self.reward_table = reward_table
        self.num_states = 100 # 共100个位置
        self.num_actions = 2 # 共2个骰子
        self.policy = [0] * 100 # 每个状态下使用的骰子
        self.value_pi = [0] * 100
        self.value_q =np.zeros([100, 2]).tolist()
        self.gamma = 0.8
    # 主接口
    def main():

        pass

    # 辅接口
    def sub():

        pass



if __name__ == '__main__':
    print('running...')
    env = Snake(10, [3, 6])
    env.run(10, 0)
