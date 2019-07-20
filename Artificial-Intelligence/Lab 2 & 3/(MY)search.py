# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:"""
    Path = []
    i = 1
    frontier = util.Stack()
    frontier.push(problem.getStartState())
    exploredList = []
    if problem.isGoalState(problem.getStartState()) is True:
        return
    else:
        while (i > 0):

            if (i==1):    #for start state to avoid "string index out of range" error
                path=frontier.pop()
                s = path[len(path) - 1]
            else:
              #for remaining states since now we have multiple tuples in a list
                temp = frontier.pop() #bcz we want some specific(2nd) tuple in path
        #returns the last element having 3 tuples as a single list of no tuples(except for start state bcz already no tuples)
                Path.append(temp[1])
                s = temp[0]
                    #for string 3rd tuple in s(current state)

            exploredList.append(s)
            if problem.isGoalState(s):
                return Path
            else:
                Successors = problem.getSuccessors(s)
                for a in Successors:
                    if a[0] not in exploredList:
                        successorPath = Path[:]

                        successorPath.append(Successors)
                   #will filter out the main tuple i.e. first tuple in frontier later(before its popped)
                        frontier.push((successorPath))
            i=i+1


    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    Path = []
    i = 1
    frontier = util.Queue()
    frontier.push(problem.getStartState())
    exploredList = []
    if problem.isGoalState(problem.getStartState()) is True:
        return
    else:
        while (i > 0):

            if (i == 1):  # for start state to avoid "string index out of range" error
                s = frontier.pop()
            else:
                # for remaining states since now we have multiple tuples in a list
                temp = frontier.pop()  # bcz we want some specific(2nd) tuple in path
                # returns the last element having 3 tuples as a single list of no tuples(except for start state bcz already no tuples)
                Path.append(temp[1])
                s = temp[0]
                # for string 3rd tuple in s(current state)

            exploredList.append(s)
            if problem.isGoalState(s):

                return Path
            else:
                Successors = problem.getSuccessors(s)
                for a in Successors:
                    if a[0] not in exploredList:
                        # will filter out the main tuple i.e. first tuple in frontier later(before its popped)
                        frontier.push((a[0], a[1], a[2]))
            i = i + 1
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    Path = []
    i = 1
    frontier = util.PriorityQueue()
    frontier.push(problem.getStartState(),0)   #0 cost since start state
    exploredList = []
    if problem.isGoalState(problem.getStartState()) is True:
        return
    else:
        while (i > 0):

            if (i == 1):  # for start state to avoid "string index out of range" error
                s = frontier.pop()
            else:
                # for remaining states since now we have multiple tuples in a list
                temp = frontier.pop()  # bcz we want some specific(2nd) tuple in path
                # returns the last element having 3 tuples as a single list of no tuples(except for start state bcz already no tuples)
               #will add only that child/element in frontier with minimum cost
                Path.append(temp[1])
                s = temp[0]
                # for string 3rd tuple in s(current state)

            exploredList.append(s)
            if problem.isGoalState(s):

                return Path
            else:
                Successors = problem.getSuccessors(s)
                costs=[]
                minimum=0
                for v in Successors:
                    costs.append(v[2])    #list of all children costs
                    minimum=min(costs)               #finds the minimum of all elements
                for a in Successors:
                    if a[0] not in exploredList:

                        # will filter out the main tuple i.e. first tuple in frontier later(before its popped)
                        frontier.push((a[0], a[1], a[2]),a[2])   #a[2] being cost of the child from current state

            i = i + 1
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
