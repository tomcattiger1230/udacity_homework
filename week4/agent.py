import random
import math
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator

class LearningAgent(Agent):
    """ An agent that learns to drive in the Smartcab world.
        This is the object you will be modifying. """ 

    def __init__(self, env, learning=False, epsilon=1.0, alpha=0.5):
        super(LearningAgent, self).__init__(env)     # Set the agent in the evironment 
        self.planner = RoutePlanner(self.env, self)  # Create a route planner
        self.valid_actions = self.env.valid_actions  # The set of valid actions

        # Set parameters of the learning agent
        self.learning = learning # Whether the agent is expected to learn
        self.Q = dict()          # Create a Q-table which will be a dictionary of tuples
        self.epsilon = epsilon   # Random exploration factor
        self.alpha = alpha       # Learning factor

        ###########
        ## TO DO ##
        ###########
        # Set any additional class parameters as needed
        self.cnt = 1

    def reset(self, destination=None, testing=False):
        """ The reset function is called at the beginning of each trial.
            'testing' is set to True if testing trials are being used
            once training trials have completed. """

        # Select the destination as the new location to route to
        self.planner.route_to(destination)
        ########### 
        ## TO DO ##
        ###########
        # Update epsilon using a decay function of your choice
               
        # linear 
        # self.epsilon -= 0.05
        # e^t
        self.epsilon = math.exp(-.65*self.cnt) # .65 a, a+
        # 1/t^2
        # self.epsilon = math.pow((1/self.cnt), 2)  # b, f
        # a^t
        # self.epsilon = math.pow(.5, self.cnt) # a, a
        # Update additional class parameters as needed
        self.cnt += 1
        # If 'testing' is True, set epsilon and alpha to 0

        if testing:
            self.epsilon = 0
            self.alpha = 0

        return None

    def build_state(self):
        """ The build_state function is called when the agent requests data from the 
            environment. The next waypoint, the intersection inputs, and the deadline 
            are all features available to the agent. """

        # Collect data about the environment
        waypoint = self.planner.next_waypoint() # The next waypoint 
        inputs = self.env.sense(self)           # Visual input - intersection light and traffic
        deadline = self.env.get_deadline(self)  # Remaining deadline

        ########### 
        ## TO DO ##
        ###########
        # Set 'state' as a tuple of relevant data for the agent        
        state = None
        light_stop = False
        left_it = True
        right_it = True
        forward_it = True
        # all_pass = False
        if deadline>0:
            if inputs['light'] == 'green':
                light_stop = False
                if waypoint == 'left':
                    if inputs['oncoming']==None:
                        left_it = False
                if waypoint == 'right':
                        right_it = False
                if waypoint == 'forward':
                        forward_it = False

                # all_pass = (not light_stop) and (not (left_it or right_it or forward_it))
                # o_l = (not left_it) and right_it and forward_it
                # o_r = (not right_it) and left_it and forward_it
                # o_f = (not forward_it) and left_it and right_it
                # n_l = left_it and (not right_it) and (not forward_it)
                # n_r = right_it and (not left_it) and (not forward_it)
                # n_f = forward_it and (not right_it) and (not left_it)

            else:
                if waypoint != 'right':
                    light_stop = True
                else:
                    if inputs['left']!='forward':
                        right_it = False

                # o_l = False
                # o_r = False 
                # o_f = False
                # n_l = False
                # n_r = False
                # n_f = False
                
        # state = (light_stop, all_pass, o_l, o_r, o_f, n_l, n_r, n_f)
        state = (light_stop, left_it, right_it, forward_it)

        # if deadline>0:
        # state = (waypoint, inputs['light'], inputs['oncoming'], inputs['left'], inputs['right'])
        # else:
        #     pass
        #     state = (None, None, None, None)


        return state


    def get_maxQ(self, state):
        """ The get_max_Q function is called when the agent is asked to find the
            maximum Q-value of all actions based on the 'state' the smartcab is in. """

        ########### 
        ## TO DO ##
        ###########
        # Calculate the maximum Q-value of all actions for a given state

        maxQ = max(self.Q[state].values())

        return maxQ 


    def createQ(self, state):
        """ The createQ function is called when a state is generated by the agent. """

        ########### 
        ## TO DO ##
        ###########
        # When learning, check if the 'state' is not in the Q-table
        # If it is not, create a new dictionary for that state
        #   Then, for each action available, set the initial Q-value to 0.0
        if self.learning:
            if self.Q.has_key(state):
                pass
            else:
                self.Q[state] = {None:0., 'forward':0., 'left':0., 'right':0.}
        # actions = ['stop','forward', 'left', 'right']

        
        return


    def choose_action(self, state):
        """ The choose_action function is called when the agent is asked to choose
            which action to take, based on the 'state' the smartcab is in. """

        # Set the agent state and default action
        self.state = state
        self.next_waypoint = self.planner.next_waypoint()
        action = None

        ########### 
        ## TO DO ##
        ###########
        # When not learning, choose a random action
        # When learning, choose a random action with 'epsilon' probability
        #   Otherwise, choose an action with the highest Q-value for the current state

        #  learning 
        if self.learning:
            # state_action = self.Q[self.state]
            # if self.epsilon < 0.5:
                
            #     action = random.choice(self.valid_actions)
            # else:
            #     mQ = self.get_maxQ(state) 
            #     for k, v in self.Q[state].items():
            #         if v == mQ:
            #             action = k
            #     # max(self.Q[self.state].iterkeys(), key=lambda k: self.Q[self.state][k])
            
                
            action_list = [random.choice(self.valid_actions)]
            
            mQ = self.get_maxQ(state) 
            for k, v in self.Q[state].items():
                if v == mQ:
                    action_list.append(k)
            prob_list = [self.epsilon, 1-self.epsilon]
            cum = 0
            x_c = random.uniform(0, 1)
            for item, item_prob in zip(action_list, prob_list):
                cum += item_prob
                if x_c < cum:
                    action = item
        #  not learning 
        else:
            action = random.choice(self.valid_actions)

        return action


    def learn(self, state, action, reward):
        """ The learn function is called after the agent completes an action and
            receives an award. This function does not consider future rewards 
            when conducting learning. """

        ########### 
        ## TO DO ##
        ###########
        # When learning, implement the value iteration update rule
        #   Use only the learning rate 'alpha' (do not use the discount factor 'gamma')
        if self.learning:
            old_q = self.Q[state][action]
            pred_q = reward + self.epsilon*old_q
            self.Q[state][action] += self.alpha * (pred_q-old_q)

        return


    def update(self):
        """ The update function is called when a time step is completed in the 
            environment for a given trial. This function will build the agent
            state, choose an action, receive a reward, and learn if enabled. """

        state = self.build_state()          # Get current state
        self.createQ(state)                 # Create 'state' in Q-table
        action = self.choose_action(state)  # Choose an action
        reward = self.env.act(self, action) # Receive a reward
        self.learn(state, action, reward)   # Q-learn

        return
        

def run():
    """ Driving function for running the simulation. 
        Press ESC to close the simulation, or [SPACE] to pause the simulation. """

    ##############
    # Create the environment
    # Flags:
    #   verbose     - set to True to display additional output from the simulation
    #   num_dummies - discrete number of dummy agents in the environment, default is 100
    #   grid_size   - discrete number of intersections (columns, rows), default is (8, 6)
    env = Environment(verbose=False)
    
    ##############
    # Create the driving agent
    # Flags:
    #   learning   - set to True to force the driving agent to use Q-learning
    #    * epsilon - continuous value for the exploration factor, default is 1
    #    * alpha   - continuous value for the learning rate, default is 0.5
    agent = env.create_agent(LearningAgent, learning=True)
    
    ##############
    # Follow the driving agent
    # Flags:
    #   enforce_deadline - set to True to enforce a deadline metric
    env.set_primary_agent(agent, enforce_deadline=True)

    ##############
    # Create the simulation
    # Flags:
    #   update_delay - continuous time (in seconds) between actions, default is 2.0 seconds
    #   display      - set to False to disable the GUI if PyGame is enabled
    #   log_metrics  - set to True to log trial and simulation results to /logs
    #   optimized    - set to True to change the default log file name
    sim = Simulator(env, display=False, update_delay=.01, log_metrics=True, optimized=True)
    
    ##############
    # Run the simulator
    # Flags:
    #   tolerance  - epsilon tolerance before beginning testing, default is 0.05 
    #   n_test     - discrete number of testing trials to perform, default is 10
    sim.run(n_test=100, tolerance=0.05)


if __name__ == '__main__':
    run()