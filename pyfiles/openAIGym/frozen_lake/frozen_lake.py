import gym
import numpy as np
import matplotlib.pyplot as plt

class Agent(object):
    def __init__(self, env):
        self.env = env
        self.gamma = 0.99
        self.alpha = 0.1
        self.num_episodes = 100
        self.epsilon = 0.5
        self.Q = np.zeros([env.observation_space.n, env.action_space.n])
        self.Q_old = self.Q

    def set_RL(self, gamma, alpha, num_episodes):
        self.gamma = gamma
        self.alpha = alpha
        self.num_episodes = num_episodes

    def set_epsilon(self, eps):
        self.epsilon = eps

    def epsilon_greedy(self, Q, state):
        e = np.random.uniform()
        if e < self.epsilon:
            action = self.env.action_space.sample()
        else:
            action = np.argmax(Q[state,:])
        return action

    def SARSA(self):
        self.error_list = []
        self.reward_list = []
        for episode in range(self.num_episodes):
            s = self.env.reset()
            a = self.epsilon_greedy(self.Q,s) 
            reward = 0
            error_avg = []
            while True:
                s2 , r, done, info = self.env.step(a)
                a2 = self.epsilon_greedy(self.Q,s2)
                error = r + self.gamma * self.Q[s2,a2] - self.Q[s,a]
                self.Q[s,a] = self.Q[s,a] + self.alpha * error
                s = s2
                a = a2
                error_avg.append(error)
                reward += r
                if done: 
                    self.error_list.append(sum(error_avg)/len(error_avg))
                    self.reward_list.append(reward)
                    break
    
    def QLearning(self):
        self.error_list = []
        self.reward_list = []
        for episode in range(self.num_episodes):
            s = self.env.reset()
            reward = 0
            error_avg = []
            while True:
                a = self.epsilon_greedy(self.Q, s)
                s2, r, done, info = self.env.step(a)
                error = r + self.gamma * np.max(self.Q[s2,:]) - self.Q[s,a]
                self.Q[s,a] = self.Q[s,a] + self.alpha * error
                s = s2
                error_avg.append(error)
                reward += r
                if done: 
                    self.error_list.append(sum(error_avg)/len(error_avg))
                    self.reward_list.append(reward)
                    break

    def QLearningPassive(self):
        for episode in range(self.num_episodes):
            s = self.env.reset()
            while True:
                a = self.epsilon_greedy(self.Q_old, s)
                s2, r, done, info = self.env.step(a)
                self.Q[s,a] = self.Q[s,a] + self.alpha * (r + self.gamma * np.max(self.Q[s2,:]) - self.Q[s,a])
                s = s2
                if done: break
            self.Q_old = self.Q
    
    def train(self, algorithm='SARSA'):
        if algorithm == 'SARSA':
            self.SARSA()
        elif algorithm == 'QLearning':
            self.QLearning()
        else:
            self.QLearningPassive()

    def test(self):
        total_reward = 0
        for i in range(100):
            s = self.env.reset()
            reward = 0
            while True:
                a = np.argmax(self.Q[s,:])
                s2, r, done, info = self.env.step(a)
                s = s2
                reward += r
                if done:
                    break
            total_reward += reward
        print 'success rate: ' + str(total_reward/100)

    def plot(self):
        plt.figure(1)
        episode = np.arange(0,self.num_episodes,1)
        plt.subplot(211)
        plt.plot(episode,self.error_list)
        plt.xlabel('episode')
        plt.ylabel('error')

        plt.subplot(212)
        plt.plot(episode,self.reward_list)
        plt.xlabel('episode')
        plt.ylabel('reward')
        
        plt.show()

if __name__=='__main__':
    env = gym.make('FrozenLake-v0')
    agent = Agent(env)
    agent.set_RL(0.99, 0.01, 20000)
    agent.set_epsilon(0.3)
    agent.train(algorithm='QLearning')
    agent.plot()
    agent.test()
