import gym
import math
import numpy as np
import matplotlib.pyplot as plt
import utils
from features import RBF

class Agent(object):
    def __init__(self,env):
        self.env = env
        self.num_action = self.env.action_space.n
        self.num_features = 12
        self.total_features = self.num_features*self.num_action+1
        self.sigma = 0.5 #0.5
        self.num_iterations = 30
        self.gamma = 0.995
        self.ep = 0.2        #0.2
        self.num_sampling = 200
        self.features = RBF(env,self.sigma,self.num_features)

    def epsilon_greedy(self, w, s, epsilon=0.3):
        if np.random.uniform() < epsilon:
            return self.env.action_space.sample()
        else:
            #return self.policy(w,s)
            return np.argmax(self.policy(w,s))

    def policy(self, w, s):
        Q = []
        for a in range(self.num_action):
            Q.append(np.dot(w.T,self.phi(s,a)))
        #return np.argmax(Q)
        return Q

    def phi(self,s,a):
        f = s
        z = np.zeros([self.num_features,1])
        bias = np.array([1])

        for action in range(self.num_action):
            if action == 0:
                phi = f if a == 0 else z
            elif action == a:
                phi = np.vstack((phi,f))
            else:
                phi = np.vstack((phi,z))
        phi = np.vstack((phi,np.array([1])))
        return phi

    def sampling(self, w, num_sampling=10):
        phi_sample = np.zeros([num_sampling,self.total_features])
        r_sample = np.zeros([num_sampling,1])

        s = self.env.reset()
        f = self.features.get_features(s)
        treward = []
        for step in range(num_sampling):
            #a = self.env.action_space.sample()
            a = self.epsilon_greedy(w,f,epsilon=self.ep)
            s2, r, done, info = self.env.step(a)
            f2 = self.features.get_features(s2)
            #phi_sample[step] = (self.phi(f,a)*(self.phi(f,a) - self.gamma*self.phi(f2,self.policy(w,f2)))).T
            aphi = np.matrix(np.zeros([self.total_features,1]))
            for action in range(self.num_action):
                aphi = aphi + np.matrix(self.phi(f2,action)) * np.asscalar(self.policy(w,f)[action])
            phi_sample[step] = (np.matrix(self.phi(f,a))-self.gamma*aphi).T
            r_sample[step] = 100 if done and sum(treward) > -199 else r 
            #r_sample[step] = 1/(1+(0.5-s2[0])**2)
            f = f2
            treward.append(r)
            if done:
                f = self.features.get_features(self.env.reset())

        X = np.matrix(phi_sample)
        r_sample = np.matrix(r_sample)
        return X, r_sample, sum(treward)/len(treward)

    def LSPI(self):
        old_w = np.zeros([self.total_features,1])
        error_list = []
        reward_list = []
        best_r = -1000
        II = np.eye(37)*0.01
        for i in range(self.num_iterations):
            print 'iteration ' + str(i+1)
            
            X, r_sample, rewardn = self.sampling(old_w,num_sampling=self.num_sampling)
            print X
            m = X.T*X
            if m.shape[0] == np.linalg.matrix_rank(m):
                w = np.linalg.inv(m)*X.T*r_sample
            else:
                raise False, 'rank not match'
           
            error = old_w - w
            error = np.asscalar(np.dot(error.T,error))
            error_list.append(error)
            reward_list.append(reward)
            old_w = w

        return w,error_list,reward_list

    def test(self, w, render=False, num_trials=100):
        total_reward = []
        for trial in range(num_trials):
            reward = 0
            s = env.reset()
            f = self.features.get_features(s)
            if render: print 'trial ' + str(trial)
            while True:
                if render: env.render()
                a = self.epsilon_greedy(w,f,epsilon=0.2) #QUICK
                s2, r, done, info = env.step(a)
                f = self.features.get_features(s2)
                reward += r
                if done:
                    break
            total_reward.append(reward)
        return sum(total_reward)/len(total_reward)

if __name__ == '__main__':
    env = gym.make('MountainCar-v0')
    agent = Agent(env)
    w,error_list,reward_list = agent.LSPI()
    try:
        print agent.test(w,render=True, num_trials=10)
    finally:
        pass
        print w
        utils.plot(error_list,reward_list)
    

