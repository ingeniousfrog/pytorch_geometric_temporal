import torch
import numpy as np

class StaticGraphDiscreteTemporalSignal(object):

    def __init__(self, edges, edge_weight, features, targets):
        self._edges = edges
        self._edge_weight = edge_weight
        self._features = features
        self._targets = targets


    def _get_edges(self):
        pass

    def _get_edge_weights(self):
        pass

    def _get_features(self)
        pass

    def _get_target(self):
        pass

    def __next__(self):
        self.t = t + 1
        if self.t <= len(self.features):
          
            feature = self.features[t]
            target = self.targets[t] 
            return (self.edges, self.edge_weight, feature, target)
        else:
            raise StopIteration

    def __iter__(self):
        self.t = 0
        return self



    
