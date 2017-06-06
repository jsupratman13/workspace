#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#filename: dqn.py                             
#brief: deep q-learning on neural network                  
#author: Joshua Supratman                    
#last modified: 2017.06.06 
#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv#
import numpy as np
import gym
import collections,random,sys
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

class Agent(object):
    def __init__(self,env):
        self.gamma = 0.99
        self.alpha = 0.01
        self.nepisodes = 1000
        self.epsilon = 1
        self.min_epsilon = 0.01
        self.epsilon_decay = 0.995
        self.batch_size = 32
        self.weights_name = 'check.hdf5'
        self.env = env
        self.nstates = env.observation_space.shape[0]
        self.nactions = env.action_space.n
        self.model = self.create_neural_network()
        self.memory = collections.deque(maxlen=500)

    def create_neural_network(self):
        model = Sequential()
        model.add(Dense(100,input_dim=self.nstates, activation='linear'))
        model.add(Dense(100,activation='relu'))
        model.add(Dense(self.nactions,activation='linear'))
        model.compile(loss='mse', optimizer=Adam(lr=self.alpha))
        return model

    def epsilon_greedy(self,state):
        if np.random.rand() < self.epsilon:
            return self.env.action_space.sample()
        else:
            Q = self.model.predict(state)
            return np.argmax(Q[0])

    def train(self):
        for episode in range(self.nepisodes):
            s = self.env.reset()
            s = np.reshape(s,[1,self.nstates]) #change shape from (2,) to (1,2)
            treward = 0
            while True:
                #if episode > self.nepisodes-5: self.env.render()
                a = self.epsilon_greedy(s)
                s2, r, done, info = self.env.step(a)
                s2 = np.reshape(s2, [1,self.nstates])
                r = 100 if done and treward > -199 else r
                self.memory.append((s,a,r,s2,done)) #store <s,a,r,s'> in replay memory
                s = s2
                treward += r
                if done:
                    break
            
            #save checkpoint
            if not episode%100 or treward > -199:
                self.model.save_weights('check'+str(episode)+'.hdf5')
            
            #replay experience
            if len(self.memory) > self.batch_size:
                loss = self.replay()
            
            print 'episode: ' + str(episode+1) + ' reward: ' + str(treward) + ' epsilon: ' + str(round(self.epsilon,2)) + ' loss: ' + str(round(loss,4))

            #shift from explore to exploit
            if self.epsilon > self.min_epsilon:
                self.epsilon *= self.epsilon_decay
            
        self.model.save_weights(self.weights_name)

    def replay(self):
        minibatch = random.sample(self.memory,self.batch_size)
        loss = 0.0
        for s,a,r,s2,done in minibatch:
            Q = r if done else r + self.gamma * np.max(self.model.predict(s2)[0])
            target = self.model.predict(s)
            target[0][a] = Q
            history = self.model.fit(s,target,epochs=1,verbose=0)
            #loss += self.model.train_on_batch(s,target)[0]
        #print 'loss: ' + str(history.history['loss'])
        #print 'loss: ' + str(loss)
        return history.history['loss'][0]

    def test(self,filename,ntrials=5):
        self.model.load_weights(filename)
        self.epsilon = 0.1
        for trial in range(ntrials):
            s = self.env.reset()
            s = np.reshape(s,[1,self.nstates])
            treward = 0
            while True:
                self.env.render()
                a = self.epsilon_greedy(s)
                s2, r, done, info = self.env.step(a)
                s = np.reshape(s2, [1,self.nstates])
                treward += r
                if done:
                    print 'trial: '+str(trial+1) + ' reward: ' + str(treward) + ' epsilon: ' + str(self.epsilon)
                    break

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        assert False, 'missing argument'
    env = gym.make('MountainCar-v0')
    agent = Agent(env)
    if str(sys.argv[1]) == 'train': 
        if len(sys.argv) > 2: agent.model.load_weights(str(sys.argv[2]))
        agent.train()
    if str(sys.argv[1]) == 'test':
        if len(sys.argv) == 2: assert False, 'missing .hdf5 weight'
        agent.test(str(sys.argv[2]))
