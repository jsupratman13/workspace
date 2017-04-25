import gym
import numpy as np
env = gym.make('FrozenLake-v0')

#initialize qTable
#left, down, right, up
Q = np.zeros([env.observation_space.n, env.action_space.n])
num_episode = 20000
gamma = 0.99 #discount ratio
alpha = 0.01 #learning factor best to start at 0.1
## passive is more stable

def epsilon_greedy(env, Q, state, epsilon=0.3):
    e = np.random.uniform()
    if e < epsilon:
        action = env.action_space.sample()
    else:
        action = np.argmax(Q[state,:])
    return action

def train_SARSA():
    #train
    for episode in range(num_episode):
        state = env.reset()
        action = epsilon_greedy(env,Q,state)
        while True:
            new_state, reward, done, info = env.step(action)
            new_action = epsilon_greedy(env,Q,new_state)
            Q[state,action] = Q[state,action] + alpha*(reward + gamma*Q[new_state,new_action] - Q[state,action])
            state = new_state
            action = new_action
            if done:
                break

def train_QLearning():
    #train
    for episode in range(num_episode):
        state = env.reset()
        while True:
            action = epsilon_greedy(env,Q,state)
            new_state, reward, done, info = env.step(action)
            Q[state,action] = Q[state,action] + alpha*(reward + gamma*np.max(Q[new_state,:]) - Q[state,action])
            state = new_state
            if done:
                break

def act():
    #use agent
    state = env.reset()
    run = 1
    success = 0
    rList = []
    rAll = 0
    while run is not 100:
        #env.render()
        action = np.argmax(Q[state,:])
        new_state,reward,done,info = env.step(action)
        state = new_state
        rAll += reward
        if done:
            #env.render()
            run+=1
            env.reset()
            rList.append(rAll)
            if reward:
                success += 1
                rAll = 0
    print 'success rate ' + str(success) + '%'
    if sum(rList) != 0:
        print 'average reward '+ str(sum(rList)/len(rList))

if __name__ == '__main__':
    act()
    train_SARSA()
    train_QLearning()
    act()
    print Q
