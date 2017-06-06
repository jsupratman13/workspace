#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#filename: qn.py                             
#brief: basic q-learning on neural network                  
#author: Joshua Supratman                    
#last modified: 2017.06.06 
#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv#
import numpy as np
import gym
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

class Agent(object):
    def __init__(self,env):
        self.gamma = 0.99
        self.alpha = 0.001
        self.nepisodes = 200
        self.epsilon = 0.17
        self.min_epsilon = 1
        self.epsilon_decay = 0.99
        self.ntrials = 5
        self.env = env
        self.nstates = env.observation_space.shape[0]
        self.nactions = env.action_space.n
        self.model = self.create_neural_network()

    def create_neural_network(self):
        model = Sequential()
        model.add(Dense(100,input_dim=self.nstates, activation='linear'))
        model.add(Dense(100,activation='relu'))
        model.add(Dense(self.nactions, activation='linear'))
        return model

    def epsilon_greedy(self,state):
        if np.random.rand() < self.epsilon:
            return self.env.action_space.sample()
            #return np.random.choice([0,2])
        else:
            Q = self.model.predict(state)
            return np.argmax(Q[0])

    def train(self):
        self.model.compile(loss='mse',optimizer=Adam(lr=self.alpha))
        for episode in range(self.nepisodes):
            s = self.env.reset()
            s = np.reshape(s,[1,self.nstates]) #change shape from (2,) to (1,2)
            treward = 0
            while True:
                if episode > self.nepisodes - 5: env.render()
                #get s,a,s2 and reshape s2
                a = self.epsilon_greedy(s)
                s2, r, done, info = self.env.step(a)
                s2 = np.reshape(s2, [1,self.nstates])
               
                #calculate Q
                Q = r if done else r + self.gamma * np.max(self.model.predict(s2)[0])
                target = self.model.predict(s)
                target[0][a] = Q
                self.model.fit(s,target,epochs=1,verbose=0)
                s = s2
                treward += r
                if done:
                    print 'episode: '+str(episode+1) + ' reward: ' + str(treward) + ' epsilon: ' + str(self.epsilon)
                    break
            if self.epsilon > self.min_epsilon:
                self.epsilon *= self.epsilon_decay
    

if __name__ == '__main__':
    env = gym.make('MountainCar-v0')
    np.random.seed(123) #to reproduce same random weight
    agent = Agent(env)
    agent.train()
