import gym
import math
import numpy as np
import matplotlib.pyplot as plt
import utils
from features import RBF

def epsilon_greedy(w,s, epsilon=0.3):
    if np.random.uniform() < epsilon:
        return env.action_space.sample()
    else:
        return policy(w,s)

def policy(weights,state):
    Qt = []
    for action in range(num_action):
        Qt.append(Q(state,action,weights))
    return np.argmax(Qt)

def phi(s,a):
    #f = get_features(s,c,len(c),sigma)
    f = s #QUICK
    z = np.zeros([num_base_func,1])
    bias = np.array([1])

    for action in range(num_action):
        if action == 0:
            phi = f if a == 0 else z
        elif action == a:
            phi = np.vstack((phi,f))
        else:
            phi = np.vstack((phi,z))
    phi = np.vstack((phi,np.array([1])))
    return phi

def Q(s,a,w):
    return np.dot(w.T,phi(s,a))

def sampling(w, num_sampling=100):
    phi_sample = np.zeros([num_sampling,nb])
    r_sample = np.zeros([num_sampling,1])

    s = env.reset()
    f = features.get_features(s)
    for step in range(num_sampling):
        a = epsilon_greedy(w,f,epsilon=ep)
        s2, r, done, info = env.step(a)
        f2 = features.get_features(s2)
        phi_sample[step] = (phi(f,a)*(phi(f,a) - gamma*phi(f2,policy(w,f2)))).T
        r_sample[step] = r
        f = f2

    X = np.matrix(phi_sample)
    r_sample = np.matrix(r_sample)

    return X, r_sample

def LSPI(plot=False):
    w = np.zeros([nb,1])
    phi_sample = np.zeros([num_sampling,nb])
    r_sample = np.zeros([num_sampling,1])

    error_list = []
    reward_list = []
    best_r = -1000
    for i in range(num_iterations):
        print 'iteration ' + str(i+1)
        
        X, r_sample = sampling(w)
        w = np.linalg.inv(X.T*X)*X.T*r_sample

        #error = old_w - w
        #error = np.asscalar(np.dot(error.T,error))
        #error_list.append(error)
        #reward = test(w)
        #reward_list.append(reward)
        #if reward > best_r:
        #    best_w = w
        #    best_r = reward
    
    return w,error_list,reward_list
    #return best_w,error_list,reward_list

def test(weights, render=False):
    num_trials = 100
    total_reward = []
    for trial in range(num_trials):
        reward = 0
        s = env.reset()
        f = features.get_features(s)
        if render:
            print 'trial ' + str(trial)
        while True:
            if render:
                env.render()
            a = epsilon_greedy(weights,f,epsilon=0.2) #QUICK
            s2, r, done, info = env.step(a)
            r = -1 * (0.5 - s2[0])
            f = features.get_features(s2)
            #s = s2
            reward += r
            if done:
                break
        total_reward.append(reward)
    return sum(total_reward)/len(total_reward)

env = gym.make('MountainCar-v0')
num_action = env.action_space.n
num_base_func = 12
nb = num_base_func*num_action+1
sigma = 0.5 #2.5
num_iterations = 10
gamma = 0.999
ep = 0.2        #0.2
num_sampling = 100
features = RBF(env,sigma,num_base_func)

if __name__ == '__main__':
    w,error_list,reward_list = LSPI(plot=True)
    try:
        test(w,render=True)
    finally:
        print w
        utils.plot(error_list,reward_list)
    

