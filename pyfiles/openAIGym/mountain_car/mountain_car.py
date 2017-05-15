import gym
import numpy as np
import matplotlib.pyplot as plt

def RadialBasisFunction(state, center, sigma):
    diff = state - center
    diff = np.dot(diff,diff) #dot product of self = (euclidean dist)^2 since norm = root(dot product) = euclidean dist
    sigma = 0.5
    return np.exp(-0.5*diff/sigma**2)

def MakeCenters():
    s_max = env.observation_space.high
    s_min = env.observation_space.low
    s_pos = np.linspace(s_min[0],s_max[0],3)
    s_vel = np.linspace(s_min[1],s_max[1],4)
    
    return cartesian([s_pos,s_vel])

def cartesian(arrays, out=None):
    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype
    n = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([n,len(arrays)], dtype=dtype)
    m = n / arrays[0].size
    out[:,0] = np.repeat(arrays[0], m)
    if arrays[1:]:
        cartesian(arrays[1:], out=out[0:m,1:])
        for j in xrange(1,arrays[0].size):
            out[j*m:(j+1)*m, 1:] = out[0:m,1:]
    return out

def get_features(state, centers, num_base_func, var):
    phi_list = []
    for i in range(num_base_func):
        phi = np.array([RadialBasisFunction(state, centers[i],var)])
        phi_list.append(phi)
    return np.array(phi_list)

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

def test(weights, render=False):
    num_trials = 100
    total_reward = []
    for trial in range(num_trials):
        reward = 0
        s = env.reset()
        f = get_features(s,c,len(c),sigma) #QUICK
        print 'trial: ' + str(trial+1)
        while True:
            if render:
                env.render()
            #a = epsilon_greedy(weights,s,epsilon=0.2)
            a = epsilon_greedy(weights,f,epsilon=0.2) #QUICK
            s2, r, done, info = env.step(a)
            f = get_features(s2,c,len(c),sigma) #QUICK
            #s = s2
            reward += r
            if done:
                if r>= 0:
                    print 'success!!!'
                    break
                elif reward <= -500:
                    break
        total_reward.append(reward)
    print 'average reward: ' + str(sum(total_reward)/len(total_reward))

def phi(s,a):
    #f = get_features(s,c,len(c),sigma)
    f = s #QUICK
    z = np.zeros([len(c),1])
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

def QLearning():
    QTable = np.zeros([num_action,1])
    nb = len(c)*num_action + 1
    #w = np.random.rand(nb,1)
    w = np.zeros([nb,1])

    for i in range(num_episodes):
        s = env.reset()
        f = get_features(s,c,num_base_func,sigma) #QUICK
        print 'episode ' + str(i+1)
        while True:
            #a = epsilon_greedy(w,s,epsilon=ep)
            a = epsilon_greedy(w,f,epsilon=ep) #QUICK
            s2,r,done,info = env.step(a)
            f2 = get_features(s2,c,num_base_func,sigma) #QUICK

            for action in range(num_action):
                #QTable[action] = Q(s2,action,w)
                QTable[action] = Q(f2,action,w) #QUICK

            target = r + gamma*np.max(QTable)
            #error = target - Q(s,a,w)
            error = target - Q(f,a,w) #QUICK
           
            #w = w + alpha*error*phi(s,a)
            w = w + alpha*error*phi(f,a) # QUICK
            f = f2 #QUICK
            if done:
                break
    return w

def SARSA(plot=False):
    QTable = np.zeros([num_action,1])
    nb = len(c)*num_action + 1
    old_w = np.zeros([nb,1])
    w = old_w
    error_list = []
    reward_list = []
    for i in range(num_episodes):
        old_w = w
        s = env.reset()
        f = get_features(s,c,num_base_func,sigma) #QUICK
        a = epsilon_greedy(old_w,f,epsilon=ep)
        print 'episode ' + str(i+1)
        reward = []
        error_total = []
        while True:
            s2,r,done,info = env.step(a)
            f2 = get_features(s2,c,num_base_func,sigma) #QUICK
            a2 = epsilon_greedy(old_w,f2,epsilon=ep)

            target = r + gamma*Q(f2,a2,w)
            #error = target - Q(s,a,w)
            error = target - Q(f,a,w) #QUICK
           
            #w = w + alpha*error*phi(s,a)
            w = w + alpha*error*phi(f,a) # QUICK
            f = f2 #QUICK
            a = a2
            reward.append(r)
            error_total.append(np.asscalar(error))
            if done:
                error_list.append(sum(error_total)/len(error_total))
                reward_list.append(sum(reward)/len(reward))
                break
    
    return w,error_list,reward_list

def plot(error_list,reward_list):
    plt.figure(1)
    episode = np.arange(0,num_episodes,1)
    plt.xlabel('episode')
    plt.ylabel('error')
    plt.subplot(211)
    plt.plot(episode,error_list)
    plt.subplot(212)
    print reward_list
    plt.plot(episode,reward_list)
    plt.show()

env = gym.make('MountainCar-v0')
num_action = env.action_space.n
sigma = 7 #2.5
c = MakeCenters()
num_base_func = len(c)
num_episodes = 1500 #600
gamma=0.99     #0.99
alpha=0.001      #0.001
ep = 0.2        #0.2

if __name__ == '__main__':
    #w = QLearning()
    w, error_list, reward_list = SARSA(plot=True)
    try:
        test(w,render=True)
    finally:
        print w
        plot(error_list,reward_list)
