import gym
import numpy as np

def RadialBasisFunction(state, center, sigma):
    diff = state - center
    diff = np.dot(diff,diff) #dot product of self = (euclidean dist)^2 since norm = root(dot product) = euclidean dist
    sigma = 0.5
    return np.exp(-0.5*diff/sigma**2)

def MakeCenters():
    #place centers for each states
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
    #length of centers must equal num_base_func
    phi_list = []
    for i in range(num_base_func-1):
        phi = np.array([RadialBasisFunction(state, centers[i],var)])
        phi_list.append(phi)
    #check if len of phi_list is equivalent to num_base_func
    phi_list.append(np.array([1]))
    return np.array(phi_list)

def epsilon_greedy(w,f, epsilon=0.3):
    if np.random.uniform() < epsilon:
        return env.action_space.sample()
    else:
        return policy(w,f)

def policy(weights,features):
    Q = []
    for a in range(num_action):
        Q.append(np.dot(weights[a].T,features))
    return np.argmax(Q)

def test(weights):
    num_trials = 100
    total_reward = []
    for trial in range(num_trials):
        reward = 0
        s = env.reset()
        f = get_features(s,c,num_base_func,sigma)
        while True:
            env.render()
            a = epsilon_greedy(weights,f,epsilon=0.2)
            #a = policy(weights,f)
            s2, r, done, info = env.step(a)
            f2 = get_features(s2,c,num_base_func,sigma)
            f = f2
            reward += r
            if done:
                break
        total_reward.append(reward)
    print 'average reward: ' + str(sum(total_reward)/len(total_reward))

def QLearning(Q,w):
    for i in range(num_episodes):
        s = env.reset()
        f = get_features(s,c,num_base_func,sigma)
        print 'episode ' + str(i+1)
        while True:
            Q2 = []
            a = epsilon_greedy(w,f,epsilon=ep)
            s2,r,done,info = env.step(a)
            f2 = get_features(s2,c,num_base_func,sigma)
            for action in range(num_action):
                Q2.append(np.dot(w[action].T,f2))

            error = r + gamma*np.max(Q2) - Q[a]
            
            Q[a] = Q[a] + alpha*error
            for action in range(num_action):
                w[action] = w[action] - alpha*error*f
                
            f = f2
            
            if done:
                break
    return w

def getQ(s,a):
    f = get_features(s,c,len(c),sigma)
    phi_list = []
    for action in range(num_action):
        pass

def QL():
    s = env.reset()
    Q = np.zeros([3,1])
    nb = len(c)*num_action + 1
    w = np.random.rand(nb,1)

    for i in range(num_episodes):
        s = env.reset()
        f = get_features(s,c,num_base_func,sigma)
        print 'episode ' + str(i+1)
        while True:
            Q2 = []
            a = epsilon_greedy(w,f,epsilon=ep)
            s2,r,done,info = env.step(a)
            f2 = get_features(s2,c,num_base_func,sigma)
            for action in range(num_action):
                Q2.append(np.dot(w[action].T,f2))

            error = r + gamma*np.max(Q2) - Q[a]
            
            Q[a] = Q[a] + alpha*error
            for action in range(num_action):
                w[action] = w[action] - alpha*error*f
                
            f = f2
            
            if done:
                break
    return w

env = gym.make('MountainCar-v0')
num_action = env.action_space.n
sigma = 0.5
c = MakeCenters()
num_base_func = len(c)+1
num_episodes = 400
gamma=0.01
alpha=0.01
ep = 0.2

if __name__ == '__main__':
    s = env.reset()
    Q = []
    w = []
    for a in range(num_action):
        w.append(np.random.rand(num_base_func,1))
        f = get_features(s,c,num_base_func,sigma)
        Q.append(np.dot(w[a].T,f))

    w = QLearning(Q,w)
    test(w)
    print w


